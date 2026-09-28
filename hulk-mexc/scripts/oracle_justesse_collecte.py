#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ORACLE DE JUSTESSE DE LA COLLECTE — vérifier les VALEURS, pas seulement leur forme (28/09/2026)
==============================================================================================

POURQUOI IL EXISTE (classe E11 : COHÉRENCE ≠ JUSTESSE)
-----------------------------------------------------
Le `gardien_collecte.py` vérifie la FORME de ce qu'on collecte : largeur du schéma, doublons,
ligne tronquée, trous. Il ne dit RIEN sur la VALEUR. Or « un prix écrit par le moteur est cohérent
avec le moteur » ne prouve pas qu'il est JUSTE : si la source se trompe, on se trompe avec elle
(E11, nommée par la FAMILLE le 23/09 : « mon invariant valide la formule DU MOTEUR »).
Le 27/09 on a mesuré que 95 % du corpus paper avait été collecté SANS ses colonnes de provenance —
et personne ne l'a vu. Cet oracle ferme la question jumelle : **le prix qu'on a écrit à l'instant T
est-il le même prix qu'une place INDÉPENDANTE, à la même minute ?**

CE QU'IL FAIT
-------------
  1. ÉCHANTILLONNE le journal VIVANT (celui du moteur, lu via `.hulk_resume_pointer`) : N lignes
     portant une provenance (`ts_prix_utc` + `price`), réparties dans le temps, paires variées.
  2. CONFRONTE chaque prix à la bougie 1 min d'une source **indépendante du moteur** :
       · Binance  → **JUSTESSE** (place différente) ;
       · MEXC    → **COHÉRENCE** (même place, autre point d'entrée) — étiqueté comme tel, jamais
                   présenté comme une indépendance qu'il n'a pas.
  3. CLASSE chaque ligne, sans jamais inventer :
       · `conforme`      — écart dans la barre ET dans l'amplitude de la minute elle-même ;
       · `hors_minute`   — le prix existe à l'identique dans une minute VOISINE (T±2) → c'est un
                           RETARD D'HORODATAGE, pas une valeur fausse (trouvaille du 23/09 :
                           13/13 « prix fautifs » existaient dans une minute antérieure) ;
       · `ecart_anormal` — écart au-delà de la barre ET de l'amplitude de la minute → à instruire ;
       · `non_verifiable`— source en panne, paire absente de la place, ou colonne absente (les
                           journaux d'avant le 23/09 n'ont pas de provenance) → DÉCLARÉ, jamais
                           compté comme conforme.
  4. AUTOTEST hors réseau : le contrôle prouve qu'il SAIT échouer (écart injecté → détecté)
     et qu'il ne ment pas quand la source est muette (→ non_verifiable, pas « OK »).

AUCUNE DONNÉE N'EST MODIFIÉE : lecture seule, et l'autotest se fait sur des fichiers synthétiques.

BORNES DÉCLARÉES (R8)
---------------------
  · La barre de justesse est un paramètre DÉCLARÉ, sourcé sur la mesure du 23/09 (audit MEXC×HULK :
    « prix Hulk vs MEXC fidèles à ±28 bps ») — ce n'est pas un seuil de décision du moteur (R17).
  · L'amplitude de la minute est respectée : un prix situé DANS le haut-bas de sa propre minute
    n'est pas une faute, même s'il s'écarte du close.
  · Une paire absente des places riches (petites capitalisations MEXC-only) n'est PAS vérifiable en
    justesse : elle est DÉCLARÉE comme telle, la cohérence MEXC est donnée à côté.
  · Réseau public requis (aucune clé). API en panne = ligne déclarée non vérifiable, jamais « OK ».

Usage :
  python3 oracle_justesse_collecte.py                 # N=12 lignes du journal vivant
  python3 oracle_justesse_collecte.py --n 20          # plus large
  python3 oracle_justesse_collecte.py --csv <chemin>  # un journal donné
Sorties : runs/ORACLE_JUSTESSE.json + Index_Maison/thermo/justesse_collecte.json (cockpit).
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent      # hulk-mexc/
RUNS = RACINE / "runs"
MAISON = RACINE.parent
THERMO = MAISON / "Index_Maison" / "thermo"
SORTIE = RUNS / "ORACLE_JUSTESSE.json"
ETAT_COCKPIT = THERMO / "justesse_collecte.json"

# ── PARAMÈTRES DÉCLARÉS (jamais cachés) ───────────────────────────────────────────
# Barre de justesse : MESURÉE le 23/09 (audit MEXC × HULK) — « prix Hulk vs MEXC fidèles à ±28 bps ».
# On ne juge donc pas la fidélité à 1 bps près : on cherche la VALEUR FAUSSE, pas le bruit de place.
BARRE_BPS = 40.0
# Fenêtre de recherche du retard d'horodatage : la minute T et ses voisines (T−2 … T+2).
VOISINES_MIN = 2
FORMATS_TS = ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%S+00:00")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}


def _journal_actif() -> Path | None:
    """Le journal du moteur, par son POINTEUR CANONIQUE (jamais par mtime : une réparation
    réécrit un vieux journal — cf. gardien_collecte)."""
    try:
        nom = (RUNS / ".hulk_resume_pointer").read_text(encoding="utf-8").strip()
        j = RUNS / nom.replace("_state.json", ".csv")
        if nom and j.exists():
            return j
    except Exception:
        pass
    js = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    return js[0] if js else None


def _ts(s: str) -> datetime | None:
    for f in FORMATS_TS:
        try:
            return datetime.strptime(s, f).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def _http_json(url: str, timeout: float = 8.0):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", errors="replace"))


def klines_binance(pair: str, t: datetime, n_minutes: int = 1):
    """Bougies 1 min Binance autour de t. Retourne {minute_iso: (open, high, low, close)} ou None."""
    pas = (VOISINES_MIN * 2 + n_minutes) * 60000
    debut = int(t.timestamp() * 1000) - VOISINES_MIN * 60000
    url = (f"https://api.binance.com/api/v3/klines?symbol={pair}&interval=1m"
           f"&startTime={debut}&endTime={debut + pas}&limit={VOISINES_MIN * 2 + n_minutes}")
    try:
        d = _http_json(url)
    except Exception:
        return None
    out = {}
    for k in d or []:
        try:
            m = datetime.fromtimestamp(int(k[0]) / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M")
            out[m] = (float(k[1]), float(k[2]), float(k[3]), float(k[4]))
        except Exception:
            continue
    return out


def klines_mexc(pair: str, t: datetime, n_minutes: int = 1):
    """Même chose sur MEXC — COHÉRENCE (même place que le moteur), pas justesse indépendante."""
    pas = (VOISINES_MIN * 2 + n_minutes) * 60000
    debut = int(t.timestamp() * 1000) - VOISINES_MIN * 60000
    url = (f"https://api.mexc.com/api/v3/klines?symbol={pair}&interval=1m"
           f"&startTime={debut}&endTime={debut + pas}&limit={VOISINES_MIN * 2 + n_minutes}")
    try:
        d = _http_json(url)
    except Exception:
        return None
    out = {}
    for k in d or []:
        try:
            m = datetime.fromtimestamp(int(k[0]) / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M")
            out[m] = (float(k[1]), float(k[2]), float(k[3]), float(k[4]))
        except Exception:
            continue
    return out


def juger(prix: float, t: datetime, bougies: dict | None) -> dict:
    """Classe UNE ligne. Ne renvoie jamais 'conforme' par défaut : sans donnée → non_verifiable."""
    if not bougies:
        return {"verdict": "non_verifiable", "motif": "source muette (réseau/paire absente)",
                "ecart_bps": None}
    cle = t.strftime("%Y-%m-%dT%H:%M")
    if cle in bougies:
        _o, haut, bas, close = bougies[cle]
        ecart = (prix / close - 1) * 10000 if close else None
        amp = (haut - bas) / bas * 10000 if bas else 0.0
        if ecart is None:
            return {"verdict": "non_verifiable", "motif": "close nul", "ecart_bps": None}
        # dans l'amplitude de SA propre minute → pas une faute, même loin du close
        if abs(ecart) <= max(BARRE_BPS, amp):
            return {"verdict": "conforme", "ecart_bps": round(ecart, 1),
                    "amplitude_bps": round(amp, 1), "reference": "close de la minute"}
        # sinon : le prix existe-t-il à l'identique dans une minute VOISINE ? (retard, pas valeur fausse)
        for m, (_o2, _h2, _b2, c2) in bougies.items():
            if m == cle or not c2:
                continue
            if abs((prix / c2 - 1) * 10000) <= BARRE_BPS:
                retard = (t.strftime("%Y-%m-%dT%H:%M") != m)
                return {"verdict": "hors_minute" if retard else "conforme",
                        "ecart_bps": round(ecart, 1), "minute_trouvee": m,
                        "motif": "le prix correspond à une minute VOISINE → retard d'horodatage, "
                                 "pas une valeur fausse"}
        return {"verdict": "ecart_anormal", "ecart_bps": round(ecart, 1),
                "amplitude_bps": round(amp, 1),
                "motif": f"écart {ecart:+.1f} bps > max(barre {BARRE_BPS:g} ; amplitude {amp:.1f}) "
                         f"et le prix n'existe dans aucune minute voisine"}
    return {"verdict": "non_verifiable", "motif": "aucune bougie à cette minute", "ecart_bps": None}


def echantillonner(chemin: Path, n: int) -> tuple[list[dict], dict]:
    """N lignes avec provenance, réparties dans le temps (et non les N dernières : on veut
    couvrir la collecte, pas un seul instant). Retourne (échantillon, stats_journal)."""
    rows: list[dict] = []
    avec = 0
    with chemin.open(newline="", encoding="utf-8", errors="replace") as f:
        for r in csv.reader(f):
            # Une ligne sans provenance (journal d'avant le 23/09, ou ligne sans prix) n'est PAS
            # une faute : elle est simplement HORS du champ de cet oracle — et elle ne sera jamais
            # comptée comme conforme (on ne suppose pas).
            if len(r) < 16 or not r[11] or not r[4]:
                continue
            t = _ts(r[11])
            try:
                prix = float(r[4])
            except ValueError:
                continue
            if t is None or prix <= 0:
                continue
            avec += 1
            rows.append({"ts_journal": r[0], "pair": r[1], "event": r[2], "prix": prix,
                         "ts_prix_utc": r[11], "age_prix_s": r[12], "spread_bps": r[13],
                         "spread_source": r[14], "_t": t})
    random.Random(20260928).shuffle(rows)                 # tirage REPRODUCTIBLE
    return rows[:n], {"lignes_avec_provenance": avec}


def autotest() -> list[tuple[str, bool, str]]:
    """Le contrôle SAIT-il échouer, et SAIT-il se taire ? Aucun réseau."""
    res = []
    t = datetime(2026, 9, 28, 9, 0, tzinfo=timezone.utc)
    cle = "2026-09-28T09:00"
    bon = {cle: (100.0, 100.5, 99.5, 100.0)}
    r1 = juger(100.0, t, bon)
    res.append(("prix exact → conforme", r1["verdict"] == "conforme", f"{r1['verdict']} {r1['ecart_bps']} bps"))
    r2 = juger(100.0 * 1.05, t, bon)                       # +500 bps : valeur fausse
    res.append(("valeur fausse (+500 bps) → DÉTECTÉE",
                r2["verdict"] == "ecart_anormal", f"{r2['verdict']} {r2['ecart_bps']} bps"))
    r3 = juger(100.0, t, {cle: (100.0, 103.0, 97.0, 100.0)})   # amplitude 600 bps
    res.append(("écart DANS l'amplitude de la minute → conforme",
                r3["verdict"] == "conforme", f"{r3['verdict']} · amplitude {r3.get('amplitude_bps')} bps"))
    voisin = {"2026-09-27T23:59": (100.0, 100.0, 100.0, 100.0), cle: (101.0, 101.0, 101.0, 101.0)}
    r4 = juger(100.0, t, voisin)                           # notre prix = la minute PRÉCÉDENTE
    res.append(("RETARD d'horodatage → 'hors_minute' (pas 'fausse valeur')",
                r4["verdict"] == "hors_minute", f"{r4['verdict']} → {r4.get('minute_trouvee')}"))
    r5 = juger(100.0, t, None)
    res.append(("source MUETTE → non_verifiable (jamais 'OK' en silence)",
                r5["verdict"] == "non_verifiable", r5["motif"]))
    r6 = juger(100.0, t, {})                               # place sans cette paire
    res.append(("paire absente de la place → non_verifiable",
                r6["verdict"] == "non_verifiable", r6["motif"]))
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description="Oracle de justesse des valeurs collectées (journal paper).")
    ap.add_argument("--csv", default=None)
    ap.add_argument("--n", type=int, default=12, help="nb de lignes échantillonnées (défaut 12)")
    args = ap.parse_args()

    chemin = Path(args.csv) if args.csv else _journal_actif()
    if not chemin or not chemin.exists():
        print("AUCUN journal trouvé", file=sys.stderr)
        return 2

    ech, stats = echantillonner(chemin, args.n)
    res_auto = autotest()
    auto_ok = all(ok for _, ok, _ in res_auto)

    resultats = []
    for e in ech:
        b_bin = klines_binance(e["pair"], e["_t"])
        b_mex = klines_mexc(e["pair"], e["_t"])
        j_bin = juger(e["prix"], e["_t"], b_bin)
        j_mex = juger(e["prix"], e["_t"], b_mex)
        resultats.append({
            "pair": e["pair"], "event": e["event"], "ts_journal": e["ts_journal"],
            "ts_prix_utc": e["ts_prix_utc"], "prix_moteur": e["prix"],
            "age_prix_s": e["age_prix_s"], "spread_bps": e["spread_bps"],
            "justesse_binance": j_bin, "coherence_mexc": j_mex,
        })

    def compte(champ, verdict):
        return sum(1 for r in resultats if r[champ]["verdict"] == verdict)

    ecarts_bin = [r["justesse_binance"]["ecart_bps"] for r in resultats
                  if r["justesse_binance"]["ecart_bps"] is not None]
    ecarts_bin.sort()
    mediane = round(ecarts_bin[len(ecarts_bin) // 2], 1) if ecarts_bin else None
    n_anormaux = compte("justesse_binance", "ecart_anormal")
    n_hors_min = compte("justesse_binance", "hors_minute")
    n_nv = compte("justesse_binance", "non_verifiable")
    n_conf = compte("justesse_binance", "conforme")

    verdict = {
        "instrument": "oracle_justesse_collecte.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "journal": chemin.name,
        "barre_bps": BARRE_BPS,
        "n_echantillon": len(resultats),
        "lignes_avec_provenance": stats["lignes_avec_provenance"],
        "justesse_binance": {"conforme": n_conf, "hors_minute": n_hors_min,
                             "ecart_anormal": n_anormaux, "non_verifiable": n_nv,
                             "ecart_median_bps": mediane},
        "coherence_mexc": {"conforme": compte("coherence_mexc", "conforme"),
                           "hors_minute": compte("coherence_mexc", "hors_minute"),
                           "ecart_anormal": compte("coherence_mexc", "ecart_anormal"),
                           "non_verifiable": compte("coherence_mexc", "non_verifiable")},
        "detail": resultats,
        "autotest_fiable": auto_ok,
        "autotest": [{"cas": n, "ok": ok, "detail": d} for n, ok, d in res_auto],
        "conforme": bool(auto_ok and n_anormaux == 0),
        "note": ("JUSTESSE = place INDÉPENDANTE (Binance) · COHÉRENCE = même place (MEXC). "
                 "Un 'non_verifiable' n'est jamais compté comme conforme : on ne suppose pas.")
    }
    SORTIE.write_text(json.dumps(verdict, indent=2, ensure_ascii=False), encoding="utf-8")
    try:
        THERMO.mkdir(parents=True, exist_ok=True)
        ETAT_COCKPIT.write_text(json.dumps({
            "instrument": "oracle_justesse_collecte.py", "ts_utc": verdict["ts_utc"],
            "journal": chemin.name, "n_echantillon": len(resultats),
            "conforme": verdict["conforme"], "barre_bps": BARRE_BPS,
            "ecart_median_bps": mediane, "ecart_anormal": n_anormaux,
            "hors_minute": n_hors_min, "non_verifiable": n_nv, "conforme_n": n_conf,
            "autotest_fiable": auto_ok,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception:
        pass

    print(f"ORACLE DE JUSTESSE — journal {chemin.name} · {len(resultats)} ligne(s) échantillonnée(s)"
          f" (barre {BARRE_BPS:g} bps)")
    print(f"  JUSTESSE (Binance, place indépendante) : {n_conf} conforme(s) · {n_hors_min} hors-minute"
          f" · {n_anormaux} ÉCART(S) ANORMAL(AUX) · {n_nv} non vérifiable(s)")
    print(f"  écart médian |bps| : {mediane}   ·   COHÉRENCE (MEXC) : "
          f"{verdict['coherence_mexc']['conforme']} conforme(s) · "
          f"{verdict['coherence_mexc']['ecart_anormal']} anormal(aux)")
    for r in resultats[:8]:
        j = r["justesse_binance"]
        print(f"    {r['ts_journal']} {r['pair']:12} {r['prix_moteur']:<14} "
              f"→ {j['verdict']:14} {str(j.get('ecart_bps')):>8} bps"
              + (f"  [{j.get('motif','')[:50]}]" if j.get("motif") else ""))
    print("\nAUTOTEST :")
    for n, ok, d in res_auto:
        print(f"   [{'OK ' if ok else 'RATE'}] {n} — {d}")
    print(f"\nVERDICT : {'CONFORME' if verdict['conforme'] else 'À INSTRUIRE'}"
          f" · autotest {'FIABLE' if auto_ok else 'NON FIABLE'}")
    print("Lecture seule : aucune donnée du journal n'est modifiée.")
    return 0 if verdict["conforme"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
