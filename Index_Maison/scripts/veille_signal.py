#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
veille_signal.py — ALARMES EXPLIQUÉES (24/08, GO Christophe)
=====================================================================
Problème : les sirènes sonnent mais Christophe ne sait jamais CE qu'elles
déclenchent. Ce script surveille les signaux onchain/dérivés et, quand un
signal SIGNIFICATIF passe, il déclenche une alerte qui s'EXPLIQUE :
  - ce qui a déclenché (chiffres exacts)
  - ce que ça veut dire (vulgarisé)
  - quoi surveiller / faire

Signaux surveillés (sources gratuites, 0 appel hub) :
  1. POUSSIÈRE + CPFP  : score poussière >= SEUIL_POUSS + signature CPFP
     (z-score >= 3 ou mode actif avec signal) = baleine camoufle un déplacement
  2. LIQUIDITÉ DÉRIVÉS : le prix passe SOUS le plus proche cluster de longs
     (carte liquidité deriv_corr.json) = risque de cascade baissière
  3. BALEINES          : net 24h <= SEUIL_DISTRIB (distribution massive)

Actions (le circuit des sirènes existant) :
  - écrit strategie/alarme.json (structuré, lu par vigie/analyste)
  - lance alerte_vocale.py --message "<explication>" (voix locale edge_tts,
    gratuite, boucle 30 s jusqu'à extinction manuelle)
  - journalise dans thermo/cortana_alerts_<jour>.json -> cockpit (niveau
    URGENT / WATCH, titre = l'explication courte)

Anti-spam : cooldown par signal (COOLDOWN_SEC, défaut 2 h), état dans
data/.veille_signal_state.json. Extinction vocale : touch STOP_ALERTE.
Stdlib uniquement. Plist : com.ace777.veille-signal (StartInterval, sans KeepAlive).
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent  # Index_Maison
THERMO = RACINE / "thermo"
DATA = RACINE / "data"
SCRIPTS = RACINE / "scripts"

LIVE = THERMO / "live.json"
DERIV = DATA / "deriv_corr.json"
VUE = DATA / "whales_vue_ensemble.json"
ALARME = RACINE / "strategie" / "alarme.json"
ETAT = DATA / ".veille_signal_state.json"

# --- Seuils (ajustables) ---
SEUIL_POUSS = 45.0          # score poussière (0-50) considéré HAUT
CPFP_Z_MIN = 3.0            # z-score CPFP considéré comme signature
COOLDOWN_SEC = 2 * 3600     # 2 h entre 2 alarmes du même type
MAX_ALERTES_JOUR = 200      # garde-fou du journal cockpit


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def lire_json(p):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def ecrire_json(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(p)


def load_etat():
    d = lire_json(ETAT)
    return d if isinstance(d, dict) else {}


def peut_declencher(etat, cle):
    last = etat.get(cle, 0)
    return (time.time() - last) >= COOLDOWN_SEC


def marquer(etat, cle):
    etat[cle] = time.time()
    ecrire_json(ETAT, etat)


def append_day_alert(level, title, detail=""):
    """Journalise dans cortana_alerts_<jour>.json (lu par le cockpit via /alerts)."""
    try:
        sys.path.insert(0, str(SCRIPTS))
        from cortana_thermo import append_day_alert as _append
        _append({"level": level, "title": title, "detail": detail[:300]})
    except Exception as e:
        print(f"[veille_signal] append_day_alert err: {e}", file=sys.stderr)


def declencher(cle, niveau, titre, explication, voix):
    """Écrit alarme.json + alerte vocale EXPLICATIVE + journal cockpit."""
    # 1. alarme.json structuré (le circuit des sirènes)
    al = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "type": cle,
        "symbole": "BTC",
        "ancienne": None, "nouvelle": None, "variation_pct": None,
        "raison": titre,
        "message": explication,
        "titre_news": None, "source_news": None, "lien_news": None,
    }
    ecrire_json(ALARME, al)

    # 2. Journal cockpit (niveau URGENT / WATCH)
    append_day_alert(niveau, titre, explication)

    # 3. VOIX : le message qui EXPLIQUE (pas juste une sirène)
    try:
        subprocess.Popen(
            ["python3", str(SCRIPTS / "alerte_vocale.py"),
             "--message", voix, "--id", cle],
            start_new_session=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    except Exception as e:
        print(f"[veille_signal] voix err: {e}", file=sys.stderr)

    print(f"⚡ ALARME [{niveau}] {titre}")
    print(f"   → {explication}")


# ---------------------------------------------------------------------------
# Signaux
# ---------------------------------------------------------------------------
def signal_poussiere():
    """Poussière haute + signature CPFP = baleine camoufle un déplacement.

    FIX 31/08 (GO Christophe, audit CPFP) : l'ancien déclencheur utilisait le
    score affiché (ratio sur un échantillon de 10 tx) → il oscillait 0/15/50 au
    hasard (en frais bas, 10/10 tx = poussière) → alarmes pour du bruit.
    Désormais le déclencheur = cpfpDustDeclenche (cumul 48h >= 1000, le VRAI
    signal soutenu, calculé par detecter_cpfp). Le score ratio reste affiché
    en INFO dans le message, plus jamais comme condition."""
    live = lire_json(LIVE)
    oc = live.get("onchain") or {}
    # Déclencheur = cumul 48h (signal soutenu, carte3.declenche). Le score ratio
    # (10 tx) n'est plus qu'une info d'affichage. AUCUNE alerte sur le bruit seul
    # (FIX 31/08, GO Christophe — l'ancien seuil 45 sur 10 tx faisait sonner
    # pour rien dès que l'échantillon tombait 9-10/10 poussière en frais bas).
    declenche = bool(oc.get("cpfpDustDeclenche"))
    if not declenche:
        return None
    score = oc.get("cpfpDustScore")
    score_f = float(score or 0.0)
    # FIX 31/08 (audit CPFP) : l'ancien test "z >= CPFP_Z_MIN" comparait le score
    # NORMALISÉ 0-100 (ex. 71.8 pour z=3.59) au seuil de z réel 3.0 → toujours
    # vrai → fausses alertes URGENT. La signature CPFP = carte2 (frais de creusage,
    # carte2.declenche) ou le signal global/confirmé — jamais le z normalisé.
    z_reel = oc.get("cpfpZReel")
    cpfp_mode = oc.get("cpfpMode") or ""
    cpfp_sig = oc.get("cpfpSignal")
    sig_cpfp = bool(oc.get("cpfpCarte2")) or bool(cpfp_sig) or (cpfp_mode == "actif" and oc.get("cpfpGlobal"))
    detail = oc.get("cpfpDustDetail") or ""
    z_aff = f"{z_reel}" if z_reel is not None else "?"
    if declenche and sig_cpfp:
        return {
            "cle": "poussiere_cpfp",
            "niveau": "URGENT",
            "titre": f"POUSSIÈRE {score_f:.0f}/50 (cumul 48h ≥ 1000) + CPFP — baleine camoufle un déplacement",
            "explication": (
                f"La poussière est soutenue : cumul 48h franchi ({detail[:100]}) AVEC une signature "
                f"CPFP (z réel {z_aff}σ). C'est la technique de camouflage des baleines : des milliers de "
                f"micro-transactions à frais nuls + une transaction enfant à frais astronomiques. "
                f"Lecture : une grosse entité prépare un déplacement massif INVISIBLE sur les seuils "
                f"classiques. Prudence — vérifier les supports et la liquidité avant tout."
            ),
            "voix": (
                f"Alerte onchain. La poussière est soutenue sur quarante-huit heures, "
                f"avec une signature CPFP détectée. C'est le camouflage des baleines : "
                f"elles préparent un déplacement massif invisible. Prudence sur le marché."
            ),
        }
    return {
            "cle": "poussiere_haute",
            "niveau": "WATCH",
            "titre": f"POUSSIÈRE soutenue (cumul 48h ≥ 1000, {detail[:80]}) — sans CPFP",
            "explication": (
                f"La poussière est soutenue sur 48h ({detail[:100]}), SANS signature "
                f"CPFP pour l'instant. La mempool se remplit de micro-transactions à frais minimaux : "
                f"activité qui s'anime, mais aucun gros acteur ne prépare encore de déplacement camouflé. "
                f"Surveiller : si une signature CPFP (z-score ≥ {CPFP_Z_MIN:.0f}) apparaît, l'alerte passe "
                f"en URGENT."
            ),
            "voix": (
                f"Alerte onchain. La poussière est soutenue sur quarante-huit heures, "
                f"sans signature CPFP pour l'instant. On surveille : si le CPFP apparaît, "
                f"l'alerte passe en urgent."
            ),
        }


def signal_liquidite():
    """Le prix passe SOUS le plus proche cluster de longs = risque de cascade."""
    d = lire_json(DERIV)
    if not d:
        return None
    liq = d.get("liquidations") or {}
    clusters = liq.get("clusters_2000usd") or {}
    mark = d.get("mark") or 0
    longs_below = liq.get("longs_below_usd") or 0
    if not clusters or not mark:
        return None
    # cluster de longs le plus proche SOUS le prix
    niveaux = sorted(int(b) for b in clusters if int(b) < mark)
    if not niveaux:
        return None
    plus_proche = niveaux[-1]
    longs_cluster = (clusters.get(str(plus_proche)) or {}).get("long") or 0
    # le prix est passé SOUS le cluster de longs (marge 0,5 %)
    if mark < plus_proche * 0.995 and longs_cluster > 0:
        return {
            "cle": "cascade_long",
            "niveau": "URGENT",
            "titre": f"PRIX SOUS LE CLUSTER DE LONGS {plus_proche:,} $ — risque de cascade",
            "explication": (
                f"Le prix ({mark:,.0f} $) est passé sous le plus proche cluster de longs "
                f"({plus_proche:,} $, {longs_cluster:,.0f} $ de positions long liquidées là). "
                f"Lecture : les longs sont liquidés quand le prix baisse jusqu'à leur niveau — "
                f"la zone {plus_proche:,} $ a déjà balayé {longs_below/1e6:.1f} M$ de longs en dessous. "
                f"Si le prix continue de tomber, les liquidations forcées s'auto-alimentent (cascade). "
                f"Surveiller le retour au-dessus de {plus_proche:,} $ pour invalider."
            ),
            "voix": (
                f"Alerte dérivés. Le prix est passé sous le cluster de liquidations de longs "
                f"à {plus_proche:,} dollars. Les positions long sont en danger, "
                f"risque de cascade baissière. Surveille le retour au-dessus de {plus_proche:,} dollars."
            ),
        }
    return None


def signal_baleines():
    """Distribution massive : net 24h très négatif."""
    v = lire_json(VUE)
    if not v:
        return None
    t = v.get("total") or {}
    net = t.get("net_btc")
    if net is None or net > -1000:  # seuil : -1000 BTC net sur 24h
        return None
    lecture = t.get("lecture") or "DISTRIBUTION"
    return {
        "cle": "distribution_whales",
        "niveau": "WATCH",
        "titre": f"BALEINES : {lecture} — net {net:+,.0f} BTC/24h",
        "explication": (
            f"Les portefeuilles surveillés relâchent massivement : net {net:+,.0f} BTC sur 24h "
            f"(reçus {t.get('in_btc',0):,.0f} / envoyés {t.get('out_btc',0):,.0f}). "
            f"Lecture : les gros porteurs mettent du BTC sur le marché (possible pression vendeuse). "
            f"À confronter au prix et à la poussière — si les deux confirment, prudence renforcée."
        ),
        "voix": (
            f"Alerte baleines. Les gros portefeuilles relâchent : "
            f"net de {abs(net):,.0f} bitcoins sur vingt-quatre heures. "
            f"Possible pression vendeuse sur le marché."
        ),
    }


def main():
    etat = load_etat()
    declenche = False
    for sig_fn in (signal_poussiere, signal_liquidite, signal_baleines):
        try:
            sig = sig_fn()
        except Exception as e:
            print(f"[veille_signal] err {sig_fn.__name__}: {e}", file=sys.stderr)
            continue
        if not sig:
            continue
        if peut_declencher(etat, sig["cle"]):
            declencher(sig["cle"], sig["niveau"], sig["titre"],
                       sig["explication"], sig["voix"])
            marquer(etat, sig["cle"])
            declenche = True
        else:
            print(f"[veille_signal] {sig['cle']} en cooldown (déjà déclenché < 2h)")
    if not declenche:
        # état nominal : rien à crier
        print(f"[veille_signal] {now_iso()} — aucun signal significatif (ou en cooldown)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
