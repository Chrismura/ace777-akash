#!/usr/bin/env python3
"""
ACE777 Cockpit — fenêtre dédiée.

Stack validée 31 juil. :
  1. LaunchAgents pont :17777 + HTTP :17800 (KeepAlive)
  2. pywebview = fenêtre native (préférence)
  3. Brave --app = filet si pywebview KO
  Jamais Safari / jamais file://

  bash Index_Maison/scripts/cockpit_up.sh
  # ou :
  bash Index_Maison/scripts/open_cockpit_app.sh
"""
from __future__ import annotations

import http.server
import signal
import socketserver
import subprocess
import sys
import threading
import time
import urllib.request
from functools import partial
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1")
INDEX = ROOT / "Index_Maison"
# Cache-buster : URL unique a chaque lancement -> WebKit ne peut pas servir l'ancien HTML
COCKPIT_REL = "/cockpit/index.html?v=" + str(int(time.time() * 1000))
BRIDGE = "http://127.0.0.1:17777/status"
HTTP_PORT = 17800
SCRIPTS = INDEX / "scripts"

CHROMIUM_APPS = [
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]


def _port_open(port: int = 17777) -> bool:
    """Quelqu’un écoute déjà sur le port ? (évite 2e pont → Address already in use)."""
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        return s.connect_ex(("127.0.0.1", port)) == 0
    finally:
        s.close()


def bridge_up() -> bool:
    """2 essais — le pont peut être lent pendant /mission."""
    for _ in range(2):
        try:
            with urllib.request.urlopen(BRIDGE, timeout=2.5) as r:
                if r.status == 200:
                    return True
        except Exception:
            time.sleep(0.35)
    return False


def ensure_bridge() -> None:
    if bridge_up():
        print("PONT=ON :17777")
        return
    # Port occupé mais /status flaky → NE PAS lancer un 2e pont
    if _port_open(17777):
        print("PONT=BUSY :17777 (déjà en écoute — pas de relance)", flush=True)
        return
    print("PONT=OFF — démarrage cortana_cockpit_bridge.py…")
    log = Path("/tmp/cortana_cockpit_bridge.log")
    subprocess.Popen(
        [sys.executable, str(SCRIPTS / "cortana_cockpit_bridge.py")],
        stdout=log.open("a"),
        stderr=subprocess.STDOUT,
        cwd=str(ROOT),
        start_new_session=True,
    )
    for _ in range(20):
        time.sleep(0.3)
        if bridge_up():
            print("PONT=ON")
            return
    print("PONT encore OFF — lecture partielle OK")


def keep_bridge_alive() -> None:
    """Relance seulement si vraiment mort (pas si port déjà pris). Anti-spam."""
    last_relaunch = 0.0

    def loop():
        nonlocal last_relaunch
        while True:
            time.sleep(12)
            try:
                if bridge_up():
                    continue
                if _port_open(17777):
                    # vivant mais /status a timeout — silence, pas de spam
                    continue
                now = time.time()
                if now - last_relaunch < 45:
                    continue
                last_relaunch = now
                print("PONT mort — relance…", flush=True)
                ensure_bridge()
            except Exception as e:
                print(f"watchdog pont: {e}", flush=True)

    threading.Thread(target=loop, daemon=True).start()


def wait_forever() -> None:
    """Boucle interruptible (Ctrl+C OK — sleep court + SIGINT)."""
    stop = threading.Event()

    def _stop(signum, frame):
        print("\nArrêt demandé — HTTP local peut rester si un autre process écoute.", flush=True)
        stop.set()

    signal.signal(signal.SIGINT, _stop)
    signal.signal(signal.SIGTERM, _stop)
    print("Watchdog actif. Ctrl+C pour quitter ce lanceur (ne tue pas ACE).", flush=True)
    print("Recharger le cockpit : ⌘R  (pas F5 = dictation micro macOS)", flush=True)
    while not stop.is_set():
        stop.wait(1.0)


def http_up() -> bool:
    try:
        with urllib.request.urlopen(
            f"http://127.0.0.1:{HTTP_PORT}{COCKPIT_REL}", timeout=1.0
        ) as r:
            return r.status == 200
    except Exception:
        return False


def ensure_http() -> str:
    url = f"http://127.0.0.1:{HTTP_PORT}{COCKPIT_REL}"
    if http_up():
        print(f"HTTP=ON :{HTTP_PORT}")
        return url

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, fmt, *args):
            pass

        def end_headers(self):
            path = (self.path or "").split("?", 1)[0].lower()
            if path.endswith((".html", ".js", ".json", ".css")) or "/cockpit/" in path:
                self.send_header(
                    "Cache-Control", "no-store, no-cache, must-revalidate, max-age=0"
                )
                self.send_header("Pragma", "no-cache")
                self.send_header("Expires", "0")
            super().end_headers()

    handler = partial(Quiet, directory=str(INDEX))
    # allow reuse
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", HTTP_PORT), handler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    for _ in range(20):
        time.sleep(0.1)
        if http_up():
            print(f"HTTP=ON :{HTTP_PORT} (serveur local Index_Maison)")
            return url
    print("HTTP fail — repli file://", file=sys.stderr)
    return (INDEX / "cockpit" / "index.html").resolve().as_uri()


def open_webview(url: str) -> bool:
    try:
        import webview  # type: ignore
    except ImportError:
        print("pywebview absent — repli Brave --app", flush=True)
        return False
    print("MODE=pywebview (fenêtre native · anti-cache user_agent)", flush=True)
    print("Ferme la fenêtre pour quitter. Recharger : ⌘R (ferme+relance si page stale)", flush=True)
    try:
        # UNE SEULE fenêtre (surtout pas deux create_window avant start :
        # pywebview/Cocoa crée alors 2 fenêtres et la visible peut être une
        # ancienne — bug qui faisait « toujours pareil »).
        ua = "ACE777-cockpit-{}".format(int(time.time()))
        webview.create_window(
            "ACE777 COCKPIT",
            url,
            width=1280,
            height=860,
            min_size=(900, 600),
            background_color="#050804",
        )
        # Anti-cache fiable (Buffy 29/08) : pywebview 3.4 n'implémente PAS
        # private_mode (le TypeError faisait TOUJOURS un fallback SANS anti-
        # cache → WebKit gardait l'ancien HTML, le cockpit ne se mettait jamais
        # à jour). La solution fiable en 3.4 : un user_agent UNIQUE à chaque
        # lancement → WebKit ne retrouve pas la page en cache et re-télécharge
        # le HTML neuf (l'URL porte déjà ?v=timestamp).
        try:
            webview.start(debug=False, user_agent=ua)
        except TypeError:
            # vieille version sans user_agent : fallback simple
            webview.start(debug=False)
        return True
    except Exception as e:
        print(f"pywebview FAIL ({e}) — repli Brave --app", flush=True)
        return False


def open_chromium_app(url: str) -> bool:
    for bin_path in CHROMIUM_APPS:
        if not Path(bin_path).exists():
            continue
        print(f"MODE=chromium-app ({Path(bin_path).name}) — filet", flush=True)
        subprocess.Popen(
            [bin_path, f"--app={url}", "--new-window"],
            start_new_session=True,
        )
        return True
    return False


def main() -> int:
    cockpit = INDEX / "cockpit" / "index.html"
    if not cockpit.exists():
        print(f"FAIL: {cockpit}", file=sys.stderr)
        return 1
    # feed frais
    try:
        subprocess.run(
            [sys.executable, str(SCRIPTS / "cockpit_mission_feed.py")],
            cwd=str(ROOT),
            timeout=45,
            check=False,
            capture_output=True,
        )
    except Exception:
        pass
    # Daemons LaunchAgents préférés ; ensure_* = filet si absents
    ensure_bridge()
    keep_bridge_alive()
    url = ensure_http()
    # cache-bust
    if url.startswith("http://"):
        url = url + ("&" if "?" in url else "?") + "v=" + str(int(time.time()))
    print(f"COCKPIT {url}")
    print("TIP: recharger = ⌘R  |  F5 Mac = dictation (pas refresh)")

    # Validé : pywebview d'abord · Brave --app en secours · jamais Safari
    if open_webview(url):
        return 0
    if open_chromium_app(url):
        wait_forever()
        return 0

    print("MODE=open-repli")
    subprocess.run(["open", url if url.startswith("http") else str(cockpit)], check=False)
    wait_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
