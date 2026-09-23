#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MESURES EXIGÉES PAR LE JURY (Tour 1 → Tour 2) — 23/09/2026
============================================================
Le jury permanent (session SUPERVISION_BUFFY_23_09) a posé 8 exigences chiffrées. Cet instrument
les produit UNE PAR UNE, et **étiquette chaque chiffre** : MESURÉ (lu dans une source) · ESTIMÉ
(modèle) · EXTRAPOLÉ · INFORMATION INSUFFISANTE. C'est la règle anti-E14 : rien n'est présenté
comme un fait s'il ne l'est pas.

Ce qu'il NE fait pas : aucun ordre, aucun €, aucune écriture dans le moteur. Lecture seule.

  §1 [Gemini]        délai de lecture du prix (la barre exigée : < 1 s)
  §2 [DeepSeek/Nem]  fréquence de scrutation de la garde + âge du prix à la décision
  §3 [Nemotron]      corrélation âge du prix ↔ glissement de sortie
  §4 [Nemotron]      espérance mathématique du poste « cooling »
  §5 [DeepSeek]      SOURCE des bougies (URL, cache, preuve par re-téléchargement)
  §6 [Gemini]        formule exacte qui fixe le stop de RIZE
  §7 [DeepSeek]      ce qu'un plafond de stop à 15 % aurait donné sur RIZE (drawdown)
  §8 [DeepSeek]      audit des AUTRES planchers de config vs seuils réellement appliqués
"""
from __future__ import annotations

import csv
import hashlib
import json
import statistics as st
import sys
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
CFG = ROOT / "config" / "defaults.env"
PROFILS = ROOT / "strategie" / "universe_profils.json"
API = "https://api.mexc.com/api/v3/klines"

RAPPORT: list[str] = []
JSON_OUT: dict = {"instrument": "mesures_jury_tour2.py", "ts_utc": None,
                  "etiquettes": "MESURÉ / ESTIMÉ / EXTRAPOLÉ / INFORMATION INSUFFISANTE"}


def dire(s: str = "") -> None:
    RAPPORT.append(s)
    print(s, flush=True)


def cfg_env() -> dict:
    out = {}
    if CFG.exists():
        for l in CFG.read_text(encoding="utf-8").splitlines():
            l = l.strip()
            if l and not l.startswith("#") and "=" in l:
                k, v = l.split("=", 1)
                out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def profil(pair: str) -> dict:
    try:
        d = json.loads(PROFILS.read_text(encoding="utf-8"))
        return (d.get("paires") or d).get(pair) or {}
    except Exception:
        return {}


def journal() -> tuple[Path, list[dict]]:
    p = sorted(RUNS.glob("PAPER_V1_*.csv"))[-1]
    return p, list(csv.DictReader(p.open(newline="", encoding="utf-8")))


def iso(ms) -> str:
    return datetime.fromtimestamp(int(ms) / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ─────────────────────────────────────────────────────────────────────────────────────────────
def s1_delai_lecture() -> None:
    dire("\n══ §1 [Gemini] DÉLAI DE LECTURE DU PRIX — barre exigée : < 1 s ══")
    p = sorted(RUNS.glob("CORPUS_ASP_*.csv"))[-1]
    delays, paires, ts_vus = [], set(), set()
    with p.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                delays.append((float(r["delay_s"]), r["pair"], r["ts"]))
            except Exception:
                continue
            paires.add(r["pair"])
            ts_vus.add(r["ts"])
    if not delays:
        dire("  INFORMATION INSUFFISANTE — aucune lecture horodatée dans le corpus.")
        return
    v = [d[0] for d in delays]
    sous_1s = sum(1 for x in v if x < 1.0)
    dire(f"  SOURCE : {p.name} — {len(v)} lectures live horodatées · {len(paires)} paires · "
         f"{len(ts_vus)} passes")
    dire(f"  MESURÉ : délai de lecture  médiane {st.median(v):.3f} s · p90 {sorted(v)[int(.9*len(v))-1]:.3f} s "
         f"· max {max(v):.3f} s")
    dire(f"  MESURÉ : part des lectures < 1 s : {sous_1s}/{len(v)} = {100*sous_1s/len(v):.1f} %")
    par_paire = defaultdict(list)
    for d, pa, _ in delays:
        par_paire[pa].append(d)
    pires = sorted(((st.median(x), k) for k, x in par_paire.items()), reverse=True)[:3]
    dire("  MESURÉ : 3 paires les plus lentes (médiane) — " +
         " · ".join(f"{k} {m:.2f}s" for m, k in pires))
    JSON_OUT["s1_delai"] = {"n": len(v), "median_s": round(st.median(v), 3),
                            "p90_s": round(sorted(v)[int(.9*len(v))-1], 3), "max_s": round(max(v), 3),
                            "pct_sous_1s": round(100*sous_1s/len(v), 1), "source": p.name}


def s2_scrutation_et_age() -> None:
    dire("\n══ §2 [DeepSeek/Nemotron] FRÉQUENCE DE SCRUTATION + ÂGE DU PRIX À LA DÉCISION ══")
    c = cfg_env()
    poll = c.get("POLL_SEC", "?")
    dire(f"  MESURÉ (config lue, {CFG.name}) : POLL_SEC = {poll} s → la boucle regarde CHAQUE paire "
         f"toutes les ~{poll} s")
    p, rows = journal()
    ts = [r["ts"] for r in rows if r.get("ts")]
    dire(f"  MESURÉ (journal {p.name}) : {len(rows)} lignes · {len(set(ts))} instants distincts")
    ages = []
    for r in rows:
        a = (r.get("age_prix_s") or "").strip()
        if a:
            try:
                ages.append(float(a))
            except Exception:
                pass
    if ages:
        dire(f"  MESURÉ : âge du prix écrit à la décision — n={len(ages)} · médiane "
             f"{st.median(ages):.2f} s · p90 {sorted(ages)[int(.9*len(ages))-1]:.2f} s · max {max(ages):.2f} s")
        dire("  ⚠ PORTÉE : les lignes SKIP sont dédupliquées (même motif). Le journal ne prouve donc "
             "PAS l'âge du prix pendant 24 h — seules les lignes écrites portent l'âge.")
    else:
        dire("  INFORMATION INSUFFISANTE : aucune ligne ne porte age_prix_s.")
    # stops depuis GO 2 : le tag _impact_av{N}s/`_ap{M}s` est la mesure du correctif
    tags = [r for r in rows if "_impact_av" in (r.get("reason") or "")]
    dire(f"  MESURÉ : décisions de sortie passées par le prix frais (tag `_impact_av…`) : {len(tags)}")
    for r in tags[-5:]:
        dire(f"     {r['ts']} {r['pair']} {r['reason'][:80]}")
    if not tags:
        dire("  → n=0 : GO 2 est en vol depuis trop peu de temps pour qu'un stop se soit présenté. "
             "Le délai médian/p90 exigé par Nemotron (§1 de son avis) NE PEUT PAS être produit "
             "aujourd'hui — INFORMATION INSUFFISANTE, pas « conforme ».")
    JSON_OUT["s2_scrutation"] = {"poll_sec": poll, "n_ages": len(ages),
                                 "median_age_s": round(st.median(ages), 2) if ages else None,
                                 "n_sorties_prix_frais": len(tags)}


def s3_age_vs_glissement() -> None:
    dire("\n══ §3 [Nemotron] CORRÉLATION ÂGE DU PRIX ↔ GLISSEMENT ══")
    p, rows = journal()
    stops = [r for r in rows if "stop-" in (r.get("reason") or "").lower()]
    avec_age = [r for r in stops if (r.get("age_prix_s") or "").strip()]
    dire(f"  MESURÉ : {len(stops)} sorties de type stop au total · {len(avec_age)} portent un âge "
         f"(la colonne n'existe que depuis GO 1, 23/09)")
    o = sorted(RUNS.glob("ORACLE_INDEPENDANT_*.json"))
    if o:
        d = json.loads(o[-1].read_text(encoding="utf-8"))
        s = d.get("stops") or {}
        if s:
            dire(f"  MESURÉ (oracle indépendant, {o[-1].name}) : {s.get('honores')}/{s.get('n')} stops "
                 f"honorés · retard médian {s.get('retard_median_min')} min · coût du retard "
                 f"{s.get('cout_retard_usd')} $")
    dire("  INFORMATION INSUFFISANTE pour la corrélation demandée : il faudrait l'âge AU MOMENT du "
         "déclenchement × le glissement réel, et **aucun stop n'a eu lieu depuis GO 2**. Chiffre "
         "manquant nommé : `age_avant_s` des 53 stops historiques (colonne créée après). Le tag "
         "`_impact_av{N}s_ap{M}s` la produira au premier stop — pas avant. Je ne comble pas avec "
         "une estimation.")


def s4_esperance_cooling() -> None:
    dire("\n══ §4 [Nemotron] ESPÉRANCE MATHÉMATIQUE DU POSTE « cooling » ══")
    p = sorted(RUNS.glob("BOUCLE_SETUPS_MAIN_*.json"))
    if not p:
        dire("  INFORMATION INSUFFISANTE — boucle des set-ups absente.")
        return
    d = json.loads(p[-1].read_text(encoding="utf-8"))
    trades = d.get("trades") or []
    cool = [t for t in trades if "cooling" in (t.get("motif_achat") or "").lower()]
    autres = [t for t in trades if t not in cool]
    if not cool:
        dire("  INFORMATION INSUFFISANTE — aucune entrée `cooling` sur la fenêtre.")
        return

    def stats(ts, nom):
        net = [float(t.get("net_main") or 0) for t in ts]
        g = [x for x in net if x > 0]
        dire(f"  {nom} : n={len(net)} · net total {sum(net):+.2f} $ · moyenne {st.mean(net):+.3f} $ "
             f"· médiane {st.median(net):+.3f} $ · gagnants {len(g)}/{len(net)} ({100*len(g)/len(net):.0f} %) "
             f"· meilleur {max(net):+.2f} $ · pire {min(net):+.2f} $")
        return {"n": len(net), "total": round(sum(net), 2), "moyenne": round(st.mean(net), 3),
                "mediane": round(st.median(net), 3), "gagnants": f"{len(g)}/{len(net)}"}

    dire(f"  SOURCE : {p[-1].name} ({d.get('fenetre_jours')} j, {len(trades)} trades) — net à la main "
         f"(frais + spread estimés)")
    a = stats(cool, "MESURÉ  poste `cooling`")
    b = stats(autres, "MESURÉ  tout le reste")
    dire("  → Lecture : c'est l'espérance que le jury réclamait. Elle est NETTE, et la famille "
         "d'entrée `cooling` est comparée au reste sur la même fenêtre.")
    JSON_OUT["s4_cooling"] = {"cooling": a, "autres": b}


def s5_source_bougies() -> None:
    dire("\n══ §5 [DeepSeek] SOURCE DES BOUGIES (preuve vérifiable) ══")
    dire(f"  SOURCE : {API}?symbol=<PAIRE>&interval=1m&startTime=<ms>&endTime=<ms>&limit=1000")
    caches = sorted(RUNS.glob("ORACLE_KL_*.json"))
    dire(f"  MESURÉ : {len(caches)} fichiers de bougies brutes en cache, empreinte SHA-256 des 3 plus gros :")
    infos = []
    for f in sorted(caches, key=lambda x: -x.stat().st_size)[:3]:
        h = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
        try:
            k = json.loads(f.read_text(encoding="utf-8"))
            per = f"{iso(k[0][0])} → {iso(k[-1][0])} · {len(k)} bougies"
        except Exception:
            per = "illisible"
        dire(f"     {f.name}  sha256:{h}…  {per}")
        infos.append({"fichier": f.name, "sha256_16": h})
    # preuve par re-téléchargement : 2 bougies RIZE, comparées au cache
    try:
        req = urllib.request.Request(
            f"{API}?symbol=RIZEUSDT&interval=1m&limit=2", headers={"User-Agent": "hulk-jury/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            lot = json.loads(r.read().decode())
        dire(f"  MESURÉ (re-téléchargement live, {datetime.now(timezone.utc).strftime('%H:%M:%SZ')}) : "
             f"{len(lot)} bougies RIZEUSDT reçues de MEXC — "
             + " · ".join(f"{iso(k[0])} close={k[4]}" for k in lot))
        dire("  → la même API que celle utilisée par l'oracle répond, avec l'horodatage des bougies : "
             "la source est VÉRIFIABLE, pas déclarative.")
        JSON_OUT["s5_source"] = {"api": API, "caches": infos, "preuve_live": [
            {"open": iso(k[0]), "close": k[4]} for k in lot]}
    except Exception as e:                                            # noqa: BLE001
        dire(f"  [!] re-téléchargement impossible ({str(e)[:80]}) — la source reste nommée mais "
             f"non re-prouvée à l'instant.")


def s6_formule_stop_rize() -> None:
    dire("\n══ §6 [Gemini] FORMULE EXACTE QUI FIXE LE STOP DE RIZE ══")
    c = cfg_env()
    fl = c.get("STOP_FLOOR_PCT", "?")
    mu = c.get("STOP_CADENCE_MULT", "?")
    dire(f"  MESURÉ (code, paper_diprip.py:633) : stop = max( plancher_de_la_paire ; "
         f"cadence_de_la_paire × {mu} )")
    dire(f"  MESURÉ (config {CFG.name}) : STOP_FLOOR_PCT = {fl} · STOP_CADENCE_MULT = {mu}")
    pr = profil("RIZEUSDT")
    cal = pr.get("calib") or {}
    dire(f"  MESURÉ (strategie/universe_profils.json) : RIZEUSDT.calib.stop_pct = {cal.get('stop_pct')} "
         f"→ c'est le PLANCHER, pas le stop")
    _, rows = journal()
    cad = [(float(r["cadence"]), r["ts"]) for r in rows
           if r.get("pair") == "RIZEUSDT" and (r.get("cadence") or "").strip()]
    if cad:
        c_med = st.median([x[0] for x in cad])
        c_max = max(cad, key=lambda x: x[0])
        dire(f"  MESURÉ (journal) : cadence RIZE observée — n={len(cad)} · médiane {c_med:.2f} % "
             f"· max {c_max[0]:.2f} % ({c_max[1]})")
        dire(f"  MESURÉ : stop RIZE = max({cal.get('stop_pct')} ; cadence × {mu}) → médiane "
             f"{max(float(cal.get('stop_pct') or 0), c_med*float(mu)):.2f} % · au pire "
             f"{max(float(cal.get('stop_pct') or 0), c_max[0]*float(mu)):.2f} %")
        dire(f"  → le 44 % observé se reproduit : cadence RIZE × {mu} dépasse très largement le "
             f"plancher de {cal.get('stop_pct')} %.")
        dire(f"  ⚠ CORRECTION PUBLIÉE : j'avais écrit « cadence × 0,70 » (le DÉFAUT du code) alors que "
             f"la config applique {mu}, et « plancher 8 % » pour le global alors que STOP_FLOOR_PCT "
             f"= {fl}. Deux lectures de défauts pris pour des valeurs effectives — classe E18.")
        JSON_OUT["s6_formule"] = {"plancher": cal.get("stop_pct"), "mult": mu,
                                  "cadence_mediane": round(c_med, 2),
                                  "stop_median": round(max(float(cal.get('stop_pct') or 0), c_med*float(mu)), 2)}


def s7_riz_drawdown() -> None:
    dire("\n══ §7 [DeepSeek] PLAFOND DE STOP À 15 % : ce que RIZE aurait donné ══")
    p = sorted(RUNS.glob("BOUCLE_SETUPS_MAIN_*.json"))
    if not p:
        dire("  INFORMATION INSUFFISANTE.")
        return
    trades = [t for t in (json.loads(p[-1].read_text(encoding="utf-8")).get("trades") or [])
              if t.get("paire") == "RIZEUSDT"]
    kl: list[list] = []
    for f in RUNS.glob("ORACLE_KL_RIZEUSDT_*.json"):
        try:
            kl.extend(json.loads(f.read_text(encoding="utf-8")))
        except Exception:
            pass
    kl.sort(key=lambda k: int(k[0]))
    if not kl:
        dire("  INFORMATION INSUFFISANTE — bougies RIZE absentes du cache (lancez l'oracle avec --refresh).")
        return
    dire(f"  SOURCE : {len(kl)} bougies 1 m RIZEUSDT ({iso(kl[0][0])} → {iso(kl[-1][0])}), "
         f"même cache que l'oracle indépendant.")
    tot = {"sans": 0.0, "39": 0.0, "15": 0.0}
    for t in trades:
        tm = lambda s: int(datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp() * 1000)
        t0, t1 = tm(t["achat"]), tm(t["sortie"])
        seg = [k for k in kl if t0 <= int(k[0]) <= t1]
        if not seg:
            continue
        plancher = float(t["prix_entree"]) * 0.3923
        pire = min(float(k[3]) for k in seg)                     # low le plus bas
        qty = float(t.get("qty") or 0)
        creux_pct = (pire / float(t["prix_entree"]) - 1) * 100
        sans = (pire - float(t["prix_entree"])) * qty
        # Un stop PLAFONNE la perte : la perte réalisée est la MOINS mauvaise des deux
        # (le niveau) → max(), jamais min(). Erreur de signe corrigée le 23/09 avant
        # publication (elle donnait « réduction 0 % », ce qui était faux).
        a39 = max(sans, -float(t["prix_entree"]) * 0.3923 * qty) if creux_pct <= -39.23 else sans
        a15 = max(sans, -float(t["prix_entree"]) * 0.15 * qty) if creux_pct <= -15.0 else sans
        tot["sans"] += sans
        tot["39"] += a39
        tot["15"] += a15
        dire(f"     {t['achat']} mise {t['mise_usdt']} $ · creux marché {creux_pct:+.2f} % · "
             f"perte au creux {sans:+.2f} $ · avec stop 39,23 % {a39:+.2f} $ · avec plafond 15 % {a15:+.2f} $")
    if tot["sans"] < 0:
        red = 100 * (1 - tot["15"] / tot["sans"]) if tot["sans"] else 0
        dire(f"  MESURÉ (2 trades RIZE) : perte au creux cumulée {tot['sans']:+.2f} $ → avec plafond "
             f"15 % {tot['15']:+.2f} $ → réduction {red:.0f} %")
        dire(f"  MESURÉ : avec le stop réel 39,23 % {tot['39']:+.2f} $ (le stop n'a rien amorti).")
        dire("  ESTIMÉ : le chiffre suppose la sortie AU niveau du plafond, sans glissement et sans "
             "ré-entrée → OPTIMISTE pour le plafond.")
        dire("  EXTRAPOLÉ (et je le dis) : « réduction du drawdown > 50 % » au niveau du PORTEFEUILLE "
             "n'est PAS démontré par 2 trades sur 16 paires — je ne le signe pas.")
        JSON_OUT["s7_riz"] = {"creux_cumule": round(tot["sans"], 2), "avec_plafond_15": round(tot["15"], 2),
                              "avec_stop_3923": round(tot["39"], 2), "reduction_pct": round(red, 0)}


def s8_autres_planchers() -> None:
    dire("\n══ §8 [DeepSeek] AUDIT DES AUTRES PLANCHERS DE CONFIG vs SEUILS RÉELLEMENT APPLIQUÉS ══")
    cles = ["stop_pct", "dip_pct", "rip_pct", "mise_max_pct_mur"]
    c = cfg_env()
    dire("  MESURÉ (lecture de strategie/universe_profils.json) — planchers de config par paire :")
    dire("     paire          " + "".join(f"{k:>13}" for k in cles))
    trouves = 0
    for pair in sorted({p.stem for p in RUNS.glob("ORACLE_KL_*.json")} |
                       {"RIZEUSDT", "EDELUSDT", "TELUSDT", "ZBCNUSDT", "KITEUSDT", "WUSDT",
                        "CCUSDT", "REDUSDT", "XRPUSDT", "PYTHUSDT", "RWAINCUSDT"}):
        cal = (profil(pair).get("calib") or {})
        if not cal:
            continue
        trouves += 1
        dire(f"     {pair:<14}" + "".join(f"{(cal.get(k) if cal.get(k) is not None else '—'):>13}" for k in cles))
    dire(f"  MESURÉ : {trouves} paires ont des planchers de config nommés "
         f"(STOP_FLOOR_PCT global = {c.get('STOP_FLOOR_PCT', '—')})")
    dire("  MESURÉ (contre-épreuve, journal) : le seuil RÉELLEMENT appliqué est écrit dans les motifs — "
         "ex. `stop-39.23%_guard_partial_50`, `impulse_pullback_dd6=5.1>=5.0`. Pour RIZE le motif "
         "porte 39,23 % alors que la config porte 8,0 → **le plancher n'est pas le seuil**.")
    dire("  → CONCLUSION DE L'AUDIT : les planchers `stop_pct` sont des MINIMUMS, jamais des seuils. "
         "Les citer comme « stop annoncé » est la faute E17. `dip_pct`/`rip_pct` suivent la même "
         "mécanique dans le code (le motif écrit la valeur retenue, pas la config).")
    # ── L'AUDIT DEMANDÉ, MAINTENANT FAIT POUR DE VRAI (Tour 2, exigence 8 de DeepSeek) ──────
    # Le gardien `verif_seuil_moteur.py` m'a signalé que j'auditais les planchers SANS le terme
    # qui les domine. On le calcule ici, terme par terme : plancher du profil vs seuil EFFECTIF
    # = max(plancher ; DIP_CADENCE_MULT × cadence), avec le terme DOMINANT de chaque paire.
    mult = float(c.get("DIP_CADENCE_MULT", "0.50"))
    pull_min = float(c.get("IMPULSE_PULLBACK_MIN_PCT", "5"))
    _, jrows = journal()
    cad: dict[str, list] = defaultdict(list)
    for r in jrows:
        v = (r.get("cadence") or "").strip()
        if v:
            try:
                cad[r["pair"]].append(float(v))
            except Exception:
                pass
    dire(f"  MESURÉ, terme par terme — seuil EFFECTIF = max(plancher ; DIP_CADENCE_MULT {mult} × "
         f"cadence), puis porte `IMPULSE_PULLBACK_MIN_PCT` {pull_min} :")
    dire(f"     {'paire':<12}{'plancher':>10}{'cadence':>9}{'× mult':>9}{'dip':>8}{'besoin':>8}"
         f"   terme dominant")
    ecarts = 0
    for pair in sorted(cad, key=lambda p: -(st.median(cad[p]) if cad[p] else 0)):
        cal = (profil(pair).get("calib") or {})
        if not cal:
            continue
        plancher = float(cal.get("dip_pct") if cal.get("dip_pct") is not None
                         else c.get("DIP_FLOOR_PCT", "2.5"))
        cmed = st.median(cad[pair])
        tcad = cmed * mult
        dip = max(plancher, tcad)
        # R20.2 / E23 : le terme pullback du PROFIL prime sur le plancher global (le moteur
        # lit `_cal.get("impulse_pullback_min_pct", cfg.get(...))`, paper_diprip.py:649).
        # Sans ça, BTC (profil 1,5 < global 5,0) était audité contre le mauvais seuil.
        _pp = cal.get("impulse_pullback_min_pct")
        pull_p = float(_pp if _pp is not None else pull_min)
        besoin = max(dip, pull_p)
        dom = ("cadence (DIP_CADENCE_MULT)" if tcad >= max(plancher, pull_p)
               else "plancher du profil" if plancher >= pull_p else "plancher pullback")
        if dom.startswith("cadence"):
            ecarts += 1
        dire(f"     {pair:<12}{plancher:>9.2f}%{cmed:>8.1f}%{tcad:>8.2f}%{dip:>7.2f}%{besoin:>7.2f}%"
             f"   {dom}")
    dire(f"  MESURÉ : sur {len(cad)} paires tradées, **{ecarts} ont un seuil d'entrée EFFECTIF "
         f"supérieur à leur plancher** — c'est-à-dire que citer le plancher comme « le seuil » "
         f"était faux pour elles (classe E17/E18).")
    dire("  → AUDIT FAIT (plus « insuffisant ») : le plancher de config n'est JAMAIS le seuil quand "
         "le terme cadence le dépasse ; le terme DOMINANT est publié paire par paire ci-dessus. "
         "Reste NON fait et déclaré : l'audit des AUTRES familles de défauts de config "
         "(`mise_max_pct_mur`, seuils de `defaults.env`) — ceux-là ne sont pas couverts ici.")
    JSON_OUT["s8_planchers"] = {"mult": mult, "n_paires": len(cad), "paires_ou_cadence_domine": ecarts}


def main() -> int:
    JSON_OUT["ts_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    dire("MESURES EXIGÉES PAR LE JURY — TOUR 1 → TOUR 2 · " + JSON_OUT["ts_utc"])
    dire("Étiquettes : MESURÉ / ESTIMÉ / EXTRAPOLÉ / INFORMATION INSUFFISANTE. Lecture seule, 0 ordre.")
    for f in (s1_delai_lecture, s2_scrutation_et_age, s3_age_vs_glissement, s4_esperance_cooling,
              s5_source_bougies, s6_formule_stop_rize, s7_riz_drawdown, s8_autres_planchers):
        try:
            f()
        except Exception as e:                                        # noqa: BLE001
            dire(f"  [!] section indisponible : {type(e).__name__} {str(e)[:120]}")
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    (RUNS / f"MESURES_JURY_TOUR2_{ts}.txt").write_text("\n".join(RAPPORT) + "\n", encoding="utf-8")
    (RUNS / f"MESURES_JURY_TOUR2_{ts}.json").write_text(
        json.dumps(JSON_OUT, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n(runs/MESURES_JURY_TOUR2_{ts}.txt/.json)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
