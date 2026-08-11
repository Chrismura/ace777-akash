#!/usr/bin/env python3
"""
Cortana × Thermo — questions + résumé horaire + URGENT voice (P3).
Lecture seule trading. Pas de GO.

Usage:
  python3 cortana_thermo.py status
  python3 cortana_thermo.py ask funding|mois|mois-dernier|climat|whales|dark|skip
  python3 cortana_thermo.py surveille
  python3 cortana_thermo.py resume [--say]
  python3 cortana_thermo.py horaire [--say]
  python3 cortana_thermo.py speak [--say]
  python3 cortana_thermo.py alert "message…"   # écrit .urgent_alert.json + speak
  python3 cortana_thermo.py urgent [--say]     # lit alerte si présente, speak, ack
  python3 cortana_thermo.py poll               # pour launchd 60s — silent si rien
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

WS = Path("/Users/christophe/ace777-test-day1/Index_Maison")
ROOT = WS.parent
THERMO = WS / "thermo"
LIVE = THERMO / "live.json"
VOCALE = WS / "A_Mon_Attention" / "ATTENTION_VOCALE.md"
FEED_JS = THERMO / "cortana_feed.js"
COCKPIT_FEED = WS / "cockpit" / "cortana_feed.js"
HORAIRE_LOG = THERMO / "cortana_horaire.log"
MISSION = WS / "cockpit" / "mission.json"
URGENT_PATH = Path(
    os.environ.get(
        "ACE777_URGENT_ALERT",
        "/tmp/ace777_swarm_pids/.urgent_alert.json",
    )
)
# Archive coffre (après conso) — le hot file /tmp est consommé
URGENT_LAST = THERMO / ".urgent_alert.last.json"


def alerts_day_path() -> Path:
    day = datetime.now(timezone.utc).strftime("%Y%m%d")
    return THERMO / f"cortana_alerts_{day}.json"


def append_day_alert(payload: dict) -> None:
    """Mémoire journée — même si l'alerte vocale est ratée / consommée."""
    path = alerts_day_path()
    THERMO.mkdir(parents=True, exist_ok=True)
    items = []
    if path.exists():
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(raw, list):
                items = raw
        except Exception:
            items = []
    row = dict(payload)
    row["logged_ts"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    items.append(row)
    # garde la journée (max 200)
    items = items[-200:]
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)
    # miroir cockpit + outbox
    for dest in (
        WS / "cockpit" / "alerts_day.json",
        WS / "OUTBOX_OBSIDIAN" / "cockpit" / "alerts_day.json",
    ):
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        except Exception:
            pass


def load_day_alerts() -> list:
    path = alerts_day_path()
    if not path.exists():
        return []
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        return raw if isinstance(raw, list) else []
    except Exception:
        return []



def load_live():
    if not LIVE.exists():
        return None
    return json.loads(LIVE.read_text(encoding="utf-8"))


def load_mission():
    if not MISSION.exists():
        return {}
    try:
        return json.loads(MISSION.read_text(encoding="utf-8"))
    except Exception:
        return {}


def ensure_fresh_hint(data):
    if not data:
        return "Pas de live.json — lance d'abord : python3 Index_Maison/scripts/thermo_quotidien_free.py"
    age = (datetime.now(timezone.utc).timestamp() - data.get("tsUnix", 0)) / 60
    if age > 90:
        return f"(snapshot un peu vieux : {data.get('ts')} — tu peux rafraîchir le thermo)"
    return ""


def fmt_num(x, d=4):
    if x is None:
        return "n/d"
    try:
        return f"{float(x):.{d}g}"
    except Exception:
        return str(x)


def _ff(x):
    try:
        return float(x) if x is not None else None
    except Exception:
        return None


def funding_spoken(f) -> str:
    """Funding en langage simple (évite 5.7e-05 à l'oral)."""
    v = _ff(f)
    if v is None:
        return "non disponible"
    # ordre de grandeur typique futures ~ 1e-5 … 1e-3
    if abs(v) < 1e-6:
        return "quasi zéro"
    # lire comme « zéro virgule … » via humanize côté voix ; ici forme décimale courte
    s = f"{v:.6f}".rstrip("0").rstrip(".")
    return s


def avis_funding(data: dict) -> str:
    f = _ff(data.get("funding"))
    a30 = _ff(data.get("fundingAvg30"))
    prev = _ff(data.get("fundingAvgPrevMonth"))
    bits = []
    if f is not None and a30 is not None:
        if f > a30 * 1.08:
            bits.append("un peu plus haut que la moyenne des trente jours")
        elif f < a30 * 0.92:
            bits.append("un peu plus bas que la moyenne des trente jours")
        else:
            bits.append("proche de la moyenne des trente jours")
    if f is not None and prev is not None:
        if f > prev * 1.05:
            bits.append("et au-dessus de la moyenne du mois précédent")
        elif f < prev * 0.95:
            bits.append("et sous la moyenne du mois précédent")
    if f is not None:
        if f > 0.00025:
            bits.append(
                "En clair : funding nettement positif — les positions longues paient cher le levier, "
                "souvent signe d’optimisme un peu chargé"
            )
        elif f > 0:
            bits.append(
                "En clair : funding positif soft — les longs paient encore les shorts, "
                "rien d’extrême"
            )
        elif f < -0.0001:
            bits.append(
                "En clair : funding négatif — les shorts paient les longs, "
                "souvent marché plus craintif ou short crowded"
            )
        else:
            bits.append("En clair : presque neutre — coût de levier faible")
    if not bits:
        return "Avis : je n’ai pas assez d’historique funding pour comparer."
    return "Avis : " + ", ".join(bits[:2]) + ". " + (bits[2] if len(bits) > 2 else "")


def avis_btc_moves(data: dict) -> str:
    c1, c4, c24 = _ff(data.get("chg1h")), _ff(data.get("chg4h")), _ff(data.get("chg24"))
    bits = []
    if c1 is not None:
        if abs(c1) < 0.3:
            bits.append("sur une heure, le bitcoin bouge peu — marché plutôt plat")
        elif c1 >= 1.5:
            bits.append("sur une heure, grosse poussée haussière — volatilité vive")
        elif c1 <= -1.5:
            bits.append("sur une heure, forte baisse — prudence sur les leviers")
        elif c1 > 0:
            bits.append("sur une heure, légère hausse")
        else:
            bits.append("sur une heure, légère baisse")
    if c24 is not None:
        if c24 >= 2:
            bits.append("sur vingt-quatre heures c’est clairement vert")
        elif c24 <= -2:
            bits.append("sur vingt-quatre heures c’est clairement rouge")
        elif abs(c24) < 0.5:
            bits.append("journée plutôt range")
    if c4 is not None and c1 is not None and (c4 * c1 < 0) and abs(c4) > 0.4 and abs(c1) > 0.3:
        bits.append("attention : une heure et quatre heures ne disent pas la même chose — possible retournement court")
    if not bits:
        return "Avis prix : lecture incomplète."
    return "Avis prix : " + " ; ".join(bits[:3]) + "."


def avis_ls_oi(data: dict) -> str:
    ls, oi, taker = _ff(data.get("longShort")), _ff(data.get("oi")), _ff(data.get("takerRatio"))
    bits = []
    if ls is not None:
        if ls > 1.4:
            bits.append("beaucoup plus de longs que de shorts — foule plutôt acheteuse, risque de squeeze baissier si ça casse")
        elif ls < 0.8:
            bits.append("plus de shorts que de longs — foule défensive, squeeze haussier possible")
        else:
            bits.append("équilibre long-court assez classique")
    if taker is not None:
        if taker > 1.2:
            bits.append("les acheteurs agressifs dominent un peu (taker)")
        elif taker < 0.85:
            bits.append("les vendeurs agressifs dominent un peu (taker)")
    if oi is not None:
        bits.append("l’intérêt ouvert donne la taille des paris ouverts — à croiser avec le prix, pas seul")
    return "Avis positionnement : " + " ; ".join(bits[:3]) + "."


def avis_whales(data: dict) -> str:
    n = int(data.get("whaleN") or 0)
    usd = _ff(data.get("whaleUsd")) or 0
    if n <= 0 or usd < 1:
        return (
            "Avis baleines : pas de gros print proxy pour l’instant — "
            "silence ne veut pas dire calme absolu, juste rien d’énorme sur l’échantillon."
        )
    if usd >= 2_000_000:
        return (
            f"Avis baleines : {n} gros print(s), somme élevée — "
            "quelqu’un de gros a frappé ; je note, je ne traduis pas ça en ordre."
        )
    return (
        f"Avis baleines : {n} print(s) au-dessus du seuil — "
        "activité institutionnelle ou whale possible, à croiser avec le prix."
    )


def avis_climat(data: dict) -> str:
    climate = data.get("climate")
    score = _ff(data.get("score")) or 50
    words = {"ok": "calme", "warn": "attention", "hot": "chaud"}.get(climate, str(climate))
    if climate == "ok" and score >= 70:
        return (
            f"Avis climat : {words}, score {int(score)} — "
            "thermo plutôt clément ; bon pour observer, pas une invitation à monter le risque."
        )
    if climate == "hot" or score < 40:
        return (
            f"Avis climat : {words}, score {int(score)} — "
            "tension haute ; je privilégie sniffer et hygiène plutôt qu’élargir."
        )
    return (
        f"Avis climat : {words}, score {int(score)} — "
        "ni festin ni alarme ; on reste en mode lecture."
    )


def avis_ace_heat(data: dict, mission: dict) -> str:
    ace = data.get("ace") or {}
    heat = _ff(ace.get("heat"))
    sess = _ff(ace.get("sessionPnl")) or 0
    skip = ace.get("skip") or 0
    bits = []
    if heat is not None:
        if heat >= 7:
            bits.append("chaleur Ace élevée — beaucoup d’activité ou de stress moteur")
        elif heat <= 2:
            bits.append("chaleur Ace basse — moteur plutôt soft")
        else:
            bits.append("chaleur Ace dans une zone moyenne")
    if sess <= -3:
        bits.append("session Ace en recul — normal de ralentir les conclusions")
    elif sess >= 3:
        bits.append("session Ace positive — bien, sans crier victoire")
    if skip and int(skip) > 500:
        bits.append("beaucoup de SKIP : le filtre refuse souvent — sagesse ou marché trop sale")
    pf = mission.get("portfolio") or {}
    hulk = _ff(pf.get("hulk"))
    if hulk is not None and hulk <= -5:
        bits.append("Hulk aussi dans le rouge — les deux stacks demandent de l’œil")
    if not bits:
        return "Avis stacks : lecture Ace soft, rien de criant."
    return "Avis stacks : " + " ; ".join(bits[:3]) + "."


def answer(cmd: str, data: dict) -> str:
    f = data.get("funding")
    a30 = data.get("fundingAvg30")
    prev = data.get("fundingAvgPrevMonth")
    climate = data.get("climate")
    score = data.get("score")
    words = {"ok": "calme", "warn": "attention", "hot": "chaud"}.get(climate, climate)

    if cmd in ("funding", "fonding", "now"):
        return (
            f"Funding maintenant : {funding_spoken(f)}. "
            f"C’est le coût du levier sur les futures bitcoin. "
            f"Moyenne trente jours : {funding_spoken(a30)}. "
            f"Mois précédent : {funding_spoken(prev)}. "
            f"{avis_funding(data)}"
        )
    if cmd in ("mois", "30j", "moyenne", "avg"):
        return (
            f"Moyenne funding environ trente jours : {funding_spoken(a30)} "
            f"(sur {data.get('fundingSamples30')} points). "
            f"Actuel : {funding_spoken(f)}. {avis_funding(data)}"
        )
    if cmd in ("mois-dernier", "prev", "precedent", "précédent"):
        return (
            f"Moyenne funding du mois précédent : {funding_spoken(prev)} "
            f"(sur {data.get('fundingSamplesPrev')} points). "
            f"Actuel : {funding_spoken(f)}. {avis_funding(data)}"
        )
    if cmd in ("climat", "status", "thermo", "score"):
        return (
            f"Climat thermo : {words} — score {score} sur 100. "
            f"Bitcoin vingt-quatre heures {data.get('chg24')} pour cent. "
            f"Long court {data.get('longShort')}. {avis_climat(data)}"
        )
    if cmd in ("whale", "whales", "baleine"):
        return (
            f"Baleines proxy : {data.get('whaleN')} gros print(s) au-dessus de cinq cent mille dollars, "
            f"somme environ {fmt_num(data.get('whaleUsd'), 0)} dollars. "
            f"Source Binance, pas Whale Alert. {avis_whales(data)}"
        )
    if cmd in ("dark", "otc", "pool"):
        return (
            f"Proxy dark : intérêt ouvert {fmt_num(data.get('oi'), 0)}, "
            f"ratio acheteur {fmt_num(data.get('takerRatio'), 2)}. "
            f"Pas de dark pool américain gratuit en temps réel. {avis_ls_oi(data)}"
        )
    if cmd in ("skip", "sagesse"):
        ace = data.get("ace") or {}
        return (
            f"SKIP en queue du live : {ace.get('skip')} "
            f"(fichier {ace.get('live')}). "
            f"{avis_ace_heat(data, {})}"
        )
    if cmd in ("prix", "btc", "bitcoin", "move"):
        return (
            f"Bitcoin : une heure {data.get('chg1h')} pour cent, "
            f"quatre heures {data.get('chg4h')}, "
            f"vingt-quatre heures {data.get('chg24')}. "
            f"{avis_btc_moves(data)}"
        )
    if cmd in ("surveille", "watch"):
        bullets = data.get("lecture") or []
        return "Surveillance : " + " · ".join(bullets[:3]) + " " + avis_climat(data)
    return (
        f"Je peux dire : funding, moyenne 30j, mois dernier, climat, whales, dark, skip, "
        f"prix, surveillance, resume. Maintenant funding={funding_spoken(f)}, climat={words}."
    )


def sentiment_avis(data: dict, mission: dict) -> tuple[str, str]:
    """Retourne (label, phrase). label ∈ BULLISH|NEUTRE|CAUTIOUS|BEARISH"""
    score = float(data.get("score") or 50)
    climate = data.get("climate") or "ok"
    chg24 = data.get("chg24")
    try:
        chg24 = float(chg24) if chg24 is not None else 0.0
    except Exception:
        chg24 = 0.0
    funding = data.get("funding")
    try:
        funding = float(funding) if funding is not None else None
    except Exception:
        funding = None
    ace = data.get("ace") or {}
    sess = ace.get("sessionPnl")
    try:
        sess = float(sess) if sess is not None else 0.0
    except Exception:
        sess = 0.0
    hulk = (mission.get("hulk") or {}).get("pnl")
    try:
        hulk = float(hulk) if hulk is not None else 0.0
    except Exception:
        hulk = 0.0

    pts = 0
    if climate == "ok":
        pts += 1
    elif climate == "hot":
        pts -= 2
    elif climate == "warn":
        pts -= 1
    if score >= 75:
        pts += 2
    elif score >= 55:
        pts += 1
    elif score < 40:
        pts -= 2
    if chg24 > 1.5:
        pts += 1
    elif chg24 < -1.5:
        pts -= 1
    if funding is not None:
        if funding > 0.0003:
            pts -= 1
        elif funding < -0.0001:
            pts += 1
    if sess < -5:
        pts -= 1
    if hulk < -5:
        pts -= 1

    if pts >= 3:
        label = "BULLISH"
        phrase = (
            "Synthèse : sentiment plutôt constructif — thermo calme, pas de feu rouge. "
            "Je reste vigilante sur le funding et le duo ; pas de GO implicite."
        )
    elif pts >= 1:
        label = "NEUTRE"
        phrase = (
            "Synthèse : sentiment neutre à légèrement positif. "
            "On laisse tourner le setup ; je sniffe, je ne décide pas à ta place."
        )
    elif pts >= -1:
        label = "CAUTIOUS"
        phrase = (
            "Synthèse : prudence. Indices mitigés ou session un peu rouge — "
            "surveille skips et recul Hulk plus Ace, garde le doigt sur arrêt."
        )
    else:
        label = "BEARISH"
        phrase = (
            "Synthèse : sentiment défensif. Climat ou portefeuilles sous pression — "
            "préfère hygiène ou pause plutôt qu’élargir le risque."
        )
    return label, phrase


def build_resume(data: dict, mission: dict | None = None) -> tuple[str, str, str]:
    mission = mission or {}
    climate = data.get("climate")
    words = {"ok": "calme", "warn": "attention", "hot": "chaud"}.get(climate, str(climate))
    ace = data.get("ace") or {}
    label, avis = sentiment_avis(data, mission)
    pf = mission.get("portfolio") or {}

    def pct(x):
        try:
            return f"{float(x):.2f}%"
        except Exception:
            return "n/d"

    def money(x):
        try:
            return f"{float(x):.2f}$"
        except Exception:
            return "n/d"

    mark = data.get("mark")
    try:
        mark_s = f"{float(mark):.0f}"
    except Exception:
        mark_s = "n/d"

    lines = [
        "Résumé Cortana, mode pédagogique.",
        f"Climat {words}, score {data.get('score')} sur cent. {avis_climat(data)}",
        f"Bitcoin cours {mark_s} dollars, "
        f"une heure {pct(data.get('chg1h'))}, "
        f"quatre heures {pct(data.get('chg4h'))}, "
        f"vingt-quatre heures {pct(data.get('chg24'))}. "
        f"{avis_btc_moves(data)}",
        f"Taux de financement actuel {funding_spoken(data.get('funding'))}, "
        f"moyenne trente jours {funding_spoken(data.get('fundingAvg30'))}, "
        f"mois précédent {funding_spoken(data.get('fundingAvgPrevMonth'))}. "
        f"{avis_funding(data)}",
        f"Ratio long court {fmt_num(data.get('longShort'), 3)}, "
        f"intérêt ouvert {fmt_num(data.get('oi'), 0)}, "
        f"ratio acheteur {fmt_num(data.get('takerRatio'), 2)}. "
        f"{avis_ls_oi(data)}",
        f"Baleines : {data.get('whaleN') or 0} grosses transactions, "
        f"environ {fmt_num(data.get('whaleUsd'), 0)} dollars. "
        f"{avis_whales(data)}",
        f"Ace en direct, {ace.get('skip') or 0} passés, "
        f"bénéfice session {money(ace.get('sessionPnl'))}, "
        f"chaleur {fmt_num(ace.get('heat'), 1)}. "
        f"{avis_ace_heat(data, mission)}",
    ]
    if pf:
        lines.append(
            f"Portefeuille : Ace {money(pf.get('ace'))}, "
            f"Hulk {money(pf.get('hulk'))}, "
            f"total {money(pf.get('total'))}."
        )
    lines.append(avis)
    text = " ".join(lines)
    return text, label, avis


def write_vocale(resume: str, pertinence: str = "SOFT", sentiment: str | None = None):
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    sent = f"\n- sentiment: {sentiment}" if sentiment else ""
    body = f"""# Attention vocale — Cortana

## Dernier résumé
> {resume}

## Meta
- statut: READY
- ts: {ts}
- pertinence: {pertinence}{sent}
- compte: thermo-free
- lien Index: S22b C14 · résumé horaire

## Règle
Cortana / `speak_attention` peut lire le résumé, puis repasser IDLE.
"""
    VOCALE.write_text(body, encoding="utf-8")
    out = WS / "OUTBOX_OBSIDIAN" / "Swarm_Bus"
    out.mkdir(parents=True, exist_ok=True)
    (out / "10_ATTENTION_VOCALE.md").write_text(body, encoding="utf-8")
    (WS / "OUTBOX_OBSIDIAN" / "A_Mon_Attention").mkdir(parents=True, exist_ok=True)
    (WS / "OUTBOX_OBSIDIAN" / "A_Mon_Attention" / "ATTENTION_VOCALE.md").write_text(body, encoding="utf-8")


def refresh_feed(data: dict, extra: str | None = None, sentiment: str | None = None):
    feed = {
        "ts": data.get("ts"),
        "climate": data.get("climate"),
        "score": data.get("score"),
        "headline": extra or ((data.get("lecture") or ["Thermo"])[0]),
        "bullets": (data.get("lecture") or [])[:4],
        "funding": data.get("funding"),
        "fundingAvg30": data.get("fundingAvg30"),
        "fundingAvgPrevMonth": data.get("fundingAvgPrevMonth"),
        "deltas": data.get("deltas") or {},
        "sentiment": sentiment,
        "askHints": [
            "Funding maintenant ?",
            "Moyenne funding ~30j ?",
            "Résumé horaire ?",
            "Climat ?",
        ],
    }
    (THERMO / "cortana_feed.json").write_text(json.dumps(feed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    js = (
        "window.__CORTANA_FEED__ = "
        + json.dumps(feed, ensure_ascii=False)
        + ";\nwindow.__CORTANA__ = window.__CORTANA_FEED__;\n"
    )
    FEED_JS.write_text(js, encoding="utf-8")
    if COCKPIT_FEED.parent.exists():
        COCKPIT_FEED.write_text(js, encoding="utf-8")


def append_horaire_log(text: str, sentiment: str):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    with HORAIRE_LOG.open("a", encoding="utf-8") as f:
        f.write(f"{ts}\t{sentiment}\t{text}\n")


def say_text(text: str, *, urgent: bool | None = None):
    """Voix humanisée FR only (edge Vivienne). urgent=None → déduit du texte."""
    try:
        from cortana_voice import speak as cv_speak
        if urgent is None:
            u = "URGENT" in text.upper() or text.upper().startswith("ALERTE")
        else:
            u = urgent
        spoken = cv_speak(text, urgent=u)
        print(f"[voix:ok] {spoken[:200]}{'…' if len(spoken) > 200 else ''}")
        return
    except Exception as e:
        print(f"[voix-ERR] {e} — silence (pas de repli Amélie)", file=sys.stderr)


def write_urgent_alert(
    msg: str,
    source: str = "manual",
    level: str = "URGENT",
    title: str | None = None,
) -> Path:
    """Écrit alerte atomique sous /tmp/ace777_swarm_pids/ (contrat swarm)."""
    URGENT_PATH.parent.mkdir(parents=True, exist_ok=True)
    THERMO.mkdir(parents=True, exist_ok=True)
    payload = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "level": level,
        "title": title or "ALERTE",
        "msg": msg,
        "source": source,
        "ack": False,
        "max_global_dd_pct": float(os.environ.get("MAX_GLOBAL_DD_PCT", "8")),
    }
    tmp = URGENT_PATH.with_suffix(URGENT_PATH.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(URGENT_PATH)
    # Mémoire journée : pas les micro-fills (spam) — garder dual/whale/move/attention/urgent
    src = str(payload.get("source") or "")
    if src not in ("cortana_watch_fill", "cortana_watch_hulk"):
        try:
            append_day_alert(payload)
        except Exception:
            pass
    return URGENT_PATH


def load_urgent() -> dict | None:
    if not URGENT_PATH.exists():
        return None
    try:
        data = json.loads(URGENT_PATH.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return None
        if data.get("ack"):
            return None
        return data
    except Exception:
        return None


def ack_urgent(data: dict) -> None:
    """Consomme le fichier /tmp (remove) + archive Index thermo."""
    data = dict(data)
    data["ack"] = True
    data["acked_ts"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    THERMO.mkdir(parents=True, exist_ok=True)
    URGENT_LAST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        URGENT_PATH.unlink(missing_ok=True)
    except Exception:
        pass


def handle_urgent(do_say: bool = True) -> int:
    """Lit alerte, parle (subprocess say — pas os.system), consomme. Exit 0 traité, 2 rien."""
    data = load_urgent()
    if not data:
        return 2
    title = data.get("title") or "ALERTE"
    msg = data.get("msg") or data.get("message") or "Alerte urgente sans message."
    level = str(data.get("level") or "URGENT").upper()
    source = data.get("source") or "?"
    is_hard = level == "URGENT"
    text = f"{'Alerte' if is_hard else 'Info'} {title}. {msg}. Provenance {source}."
    print(text)
    write_vocale(text, "PERTINENT" if is_hard else "SOFT", sentiment="URGENT" if is_hard else "INFO")
    live = load_live() or {"ts": data.get("ts"), "climate": "hot", "score": 0, "lecture": [text]}
    refresh_feed(live, extra=text, sentiment="URGENT" if is_hard else "INFO")
    if do_say:
        # SOFT respecte mute ; URGENT peut parler (CORTANA_MUTE_ALLOW_URGENT)
        say_text("Cortana. " + text, urgent=is_hard)
        if VOCALE.exists():
            t = VOCALE.read_text(encoding="utf-8")
            VOCALE.write_text(t.replace("statut: READY", "statut: IDLE"), encoding="utf-8")
    ack_urgent(data)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Cortana × Thermo")
    ap.add_argument(
        "cmd",
        nargs="?",
        default="status",
        help="status|ask|surveille|resume|horaire|speak|alert|urgent|poll",
    )
    ap.add_argument("topic", nargs="?", default="climat", help="funding|mois|… ou message alert")
    ap.add_argument("--say", action="store_true", help="lire à voix haute (say)")
    ap.add_argument("--refresh-thermo", action="store_true", help="rafraîchir live.json avant résumé")
    # message multi-mots pour alert
    ap.add_argument("rest", nargs="*", help=argparse.SUPPRESS)
    args = ap.parse_args()

    cmd = args.cmd.lower()

    # --- P3 urgent path (pas besoin de live.json) ---
    if cmd == "alert":
        parts = [args.topic] + list(args.rest or [])
        msg = " ".join(p for p in parts if p and p != "climat").strip()
        if not msg:
            print("Usage: cortana_thermo.py alert \"message\"", file=sys.stderr)
            return 1
        write_urgent_alert(msg, source="manual")
        return handle_urgent(do_say=True)

    if cmd in ("urgent", "poll"):
        # poll = silencieux si rien ; urgent force say si alerte
        do_say = True if cmd == "urgent" else True
        rc = handle_urgent(do_say=do_say)
        if cmd == "poll" and rc == 2:
            return 0  # rien à faire — OK pour launchd
        return 0 if rc in (0, 2) else rc

    # avant résumé horaire : vider une urgence en attente
    if cmd in ("resume", "horaire"):
        handle_urgent(do_say=True)

    if args.refresh_thermo or cmd in ("resume", "horaire"):
        script = WS / "scripts" / "thermo_quotidien_free.py"
        if script.exists():
            subprocess.run([sys.executable, str(script)], check=False, cwd=str(ROOT))

    miss_script = WS / "scripts" / "cockpit_mission_feed.py"
    if cmd in ("resume", "horaire") and miss_script.exists():
        subprocess.run([sys.executable, str(miss_script)], check=False, cwd=str(ROOT))

    data = load_live()
    if not data:
        print("NO_LIVE — lance d'abord thermo_quotidien_free.py", file=sys.stderr)
        return 1

    topic = (args.topic or "climat").lower()
    sentiment = None

    if cmd in ("resume", "horaire"):
        text, sentiment, _avis = build_resume(data, load_mission())
        pertinence = "PERTINENT" if sentiment in ("CAUTIOUS", "BEARISH") or data.get("climate") == "hot" else "SOFT"
    elif cmd == "ask":
        text = answer(topic, data)
        pertinence = "SOFT"
    elif cmd == "surveille":
        text = answer("surveille", data)
        pertinence = "SOFT"
    elif cmd == "speak":
        text = answer("climat", data)
        pertinence = "SOFT"
    else:
        text = answer("climat", data)
        pertinence = "SOFT"

    hint = ensure_fresh_hint(data)
    if hint and cmd not in ("resume", "horaire"):
        text = text + " " + hint

    print(text)
    if sentiment:
        print(f"[sentiment={sentiment}]")

    write_vocale(text, pertinence, sentiment=sentiment)
    refresh_feed(data, extra=text, sentiment=sentiment)

    if cmd in ("resume", "horaire"):
        append_horaire_log(text, sentiment or "?")

    if args.say or cmd == "speak":
        say_text("Cortana. " + text)
        t = VOCALE.read_text(encoding="utf-8")
        VOCALE.write_text(t.replace("statut: READY", "statut: IDLE"), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
