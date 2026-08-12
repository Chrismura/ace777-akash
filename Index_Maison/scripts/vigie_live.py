#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""vigie_live.py — VIGIE MARCHÉ TEMPS RÉEL (brique 1, ACE777).

Écoute BTCUSDT + ETHUSDT via WebSocket Binance public (client RFC 6455 brut,
stdlib) + les news RSS (cointelegraph + google news macro).
Filtre le bruit, et sur événement significatif : écrit strategie/alarme.json
puis déclenche analyste.py en sous-processus détaché.

Code initial : codeur du hub (code.ia). Corrections d'intégration (Buffy) :
- BUG 1 : variation 60 s comparée au prix d'ouverture de fenêtre (était ~0)
- BUG 2 : snapshot prix 5 min réel (était comparé au prix courant)
- BUG 3 : volume x3 non testé tant que < 3 fenêtres d'historique
- BUG 4 : import sys manquant

Tout en stdlib. Zéro dépendance. Zéro API payante.
"""

import socket
import ssl
import base64
import os
import struct
import json
import time
import sys
import threading
import urllib.request
import subprocess
from datetime import datetime
from collections import deque

# --- Configuration ---------------------------------------------------------
BINANCE_HOST = "stream.binance.com"
BINANCE_PATH = "/stream?streams=btcusdt@aggTrade/ethusdt@aggTrade"
RSS_URLS = {
    "cointelegraph": "https://cointelegraph.com/rss",
    "google_news": ("https://news.google.com/rss/search?q=bitcoin+OR+crypto+"
                    "OR+fed+interest+rate+OR+carry+trade+OR+recession"
                    "&hl=en-US&gl=US&ceid=US:en"),
}
KEYWORDS = ["fed", "interest rate", "carry trade", "cpi", "recession",
            "crash", "war", "assassination", "bank", "default", "emergency",
            "nikkei", "liquidation", "fed now"]
OUTPUT_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie")
ALERT_FILE = os.path.join(OUTPUT_DIR, "alarme.json")
LOG_FILE = os.path.join(OUTPUT_DIR, "journal_radar.log")
ANALYSTE = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/scripts/analyste.py")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- État par symbole ------------------------------------------------------
class SymbolData:
    def __init__(self):
        self.last_price = 0.0
        self.window_start = time.time()
        self.price_at_window_start = 0.0    # BUG 1 : prix au début de fenêtre
        self.price_at_5min = 0.0            # BUG 2 : snapshot prix 5 min
        self.time_at_5min = 0.0             # BUG 2 : quand le snapshot a été pris
        self.window_volume = 0.0
        self.volume_history = deque(maxlen=10)
        self.cooldown_until = 0

symbols = {"BTCUSDT": SymbolData(), "ETHUSDT": SymbolData()}
news_cooldown = 0.0
last_news_titles = {source: deque(maxlen=5) for source in RSS_URLS}


# --- WebSocket brut (client RFC 6455, stdlib — testé le 11/08) -------------
def ws_connect(host, path):
    ctx = ssl.create_default_context()
    s = socket.create_connection((host, 443), timeout=10)
    ws = ctx.wrap_socket(s, server_hostname=host)
    key = base64.b64encode(os.urandom(16)).decode()
    req = (f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\n"
           f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\n"
           f"Sec-WebSocket-Version: 13\r\n\r\n")
    ws.sendall(req.encode())
    resp = b""
    while b"\r\n\r\n" not in resp:
        resp += ws.recv(4096)
    return ws


def ws_recv(ws):
    hdr = ws.recv(2)
    if len(hdr) < 2:
        return None
    ln = hdr[1] & 0x7F
    if ln == 126:
        ln = struct.unpack(">H", ws.recv(2))[0]
    elif ln == 127:
        ln = struct.unpack(">Q", ws.recv(8))[0]
    data = b""
    while len(data) < ln:
        chunk = ws.recv(ln - len(data))
        if not chunk:
            return None
        data += chunk
    return data.decode(errors="replace")


# --- Traitement des trades (le cœur : seuils) ------------------------------
def process_trade(symbol, price, quantity):
    now = time.time()
    data = symbols[symbol]
    data.last_price = price
    data.window_volume += quantity

    # Ouverture d'une nouvelle fenêtre de 60 s
    if now - data.window_start >= 60:
        data.volume_history.append(data.window_volume)
        data.window_volume = 0.0
        data.window_start = now
        data.price_at_window_start = price          # BUG 1 : figer la référence

    # Premier prix de référence (démarrage à froid)
    if data.price_at_window_start == 0.0:
        data.price_at_window_start = price

    # Snapshot 5 min : pris une seule fois après 5 min de fonctionnement
    if data.time_at_5min == 0.0 and now - data.window_start >= 300:
        data.price_at_5min = price
        data.time_at_5min = now

    # --- Calcul des indicateurs (contre les VRAIES références) ---
    base60 = data.price_at_window_start
    var_60s = (abs(price - base60) / base60) if base60 else 0.0

    base5 = data.price_at_5min
    var_5min = (abs(price - base5) / base5) if data.time_at_5min and base5 else 0.0

    n_hist = len(data.volume_history)
    avg_volume = (sum(data.volume_history) / n_hist) if n_hist else 0.0
    # BUG 3 : ne tester le volume que si ≥ 3 fenêtres d'historique
    volume_x3 = (data.window_volume >= 3 * avg_volume) if (n_hist >= 3 and avg_volume > 0) else False

    declenche = False
    raison = ""
    if var_60s >= 0.005:
        declenche, raison = True, "0.5% en 60s"
    elif var_5min >= 0.02:
        declenche, raison = True, "2% en 5 min"
    elif volume_x3:
        declenche, raison = True, "volume x3"

    if declenche and now > data.cooldown_until:
        data.cooldown_until = now + 300  # cooldown 5 min par symbole
        alert = {
            "ts": datetime.utcnow().isoformat() + "Z",
            "type": "prix",
            "symbole": symbol,
            "ancienne": round(base60, 2),
            "nouvelle": round(price, 2),
            "variation_pct": round((price - base60) / base60 * 100, 2) if base60 else 0.0,
            "raison": raison,
            "titre_news": None,
            "source_news": None,
            "lien_news": None,
        }
        try:
            with open(ALERT_FILE, "w", encoding="utf-8") as f:
                json.dump(alert, f, ensure_ascii=False, indent=2)
            subprocess.Popen(
                ["python3", ANALYSTE, "--alerte", ALERT_FILE, "--speak"],
                start_new_session=True)
            print(f"⚡ ALERTE {symbol} : {raison} ({alert['variation_pct']}%) + VOIX")
        except Exception as e:
            print(f"Erreur déclenchement analyste : {e}", file=sys.stderr)

    # Journalisation (1 ligne par événement, même bruit)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.utcnow().isoformat()}Z {symbol} {price} "
                    f"{var_60s:.4f} {data.window_volume:.1f} "
                    f"declenche={'oui' if declenche else 'non'}\n")
    except Exception:
        pass


# --- News RSS --------------------------------------------------------------
def fetch_rss(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"Erreur RSS {url}: {e}", file=sys.stderr)
        return None


def parse_rss(xml):
    import xml.etree.ElementTree as ET
    try:
        root = ET.fromstring(xml)
        items = []
        for item in root.findall(".//item"):
            title = item.findtext("title") or ""
            link = item.findtext("link") or ""
            items.append({"title": title, "link": link})
        return items
    except Exception as e:
        print(f"Erreur parsing RSS: {e}", file=sys.stderr)
        return []


def check_news():
    global news_cooldown
    now = time.time()
    if now < news_cooldown:
        return

    for source, url in RSS_URLS.items():
        xml = fetch_rss(url)
        if not xml:
            continue
        for item in parse_rss(xml):
            title_low = item["title"].lower()
            kw = next((k for k in KEYWORDS if k in title_low), None)
            if kw and title_low not in last_news_titles[source]:
                last_news_titles[source].append(title_low)
                alert = {
                    "ts": datetime.utcnow().isoformat() + "Z",
                    "type": "news",
                    "symbole": None,
                    "ancienne": None,
                    "nouvelle": None,
                    "variation_pct": None,
                    "raison": f"mot-cle: {kw}",
                    "titre_news": item["title"],
                    "source_news": source,
                    "lien_news": item["link"],
                }
                try:
                    with open(ALERT_FILE, "w", encoding="utf-8") as f:
                        json.dump(alert, f, ensure_ascii=False, indent=2)
                    subprocess.Popen(
                        ["python3", ANALYSTE, "--alerte", ALERT_FILE, "--speak"],
                        start_new_session=True)
                    print(f"⚡ ALERTE NEWS [{source}] {item['title'][:80]} + VOIX")
                except Exception as e:
                    print(f"Erreur alerte news : {e}", file=sys.stderr)
                news_cooldown = now + 1800  # cooldown news 30 min
                return


# --- Threads ---------------------------------------------------------------
def websocket_thread():
    while True:
        try:
            ws = ws_connect(BINANCE_HOST, BINANCE_PATH)
            print("Connecté au WebSocket Binance (BTC+ETH)")
            while True:
                data = ws_recv(ws)
                if not data:
                    break
                try:
                    msg = json.loads(data)
                    d = msg.get("data")
                    # Défense : messages non conformes (ping, event, …) ignorés
                    if not isinstance(d, dict):
                        continue
                    s, p, q = d.get("s"), d.get("p"), d.get("q")
                    if s in symbols and p is not None and q is not None:
                        process_trade(s, float(p), float(q))
                except (json.JSONDecodeError, KeyError, ValueError, TypeError):
                    continue
        except Exception as e:
            print(f"Erreur WebSocket: {e} — reconnexion dans 5 s", file=sys.stderr)
            time.sleep(5)


def news_thread():
    while True:
        check_news()
        time.sleep(60)


def main():
    threading.Thread(target=websocket_thread, daemon=True).start()
    threading.Thread(target=news_thread, daemon=True).start()
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
