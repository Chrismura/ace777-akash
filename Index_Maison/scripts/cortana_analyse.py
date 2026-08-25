#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cortana_analyse.py — analyse LIVE d'un indice par Cortana (master analyste)
=============================================================================
Chantier 3 (06/08/2026) — spec validée Christophe :
  * Chaque bulle d'indice du cockpit aura un bouton Cortana -> ce script.
  * Il prend un indice (ex: funding), assemble les FAITS live + tendances
    24h/semaine depuis l'historique, et demande l'analyse à Gemini via le hub
    (routage task=cortana.analyse -> GEMINI prioritaire, repli Qwen local).
  * L'analyse est ENREGISTRÉE dans ~/ace777-test-day1/Index_Maison/analyses/
    (exigence Christophe : comparer plus tard avec le marché réel -> score de
    justesse de l'analyste).

Usage :
  python3 cortana_analyse.py funding            # analyse de l'indice funding
  python3 cortana_analyse.py funding --speak    # + lecture vocale (Vivienne)
  python3 cortana_analyse.py --list             # liste des indices dispo

Le prompt système vit dans le vault : PROMPT_MASTER_ANALYSTE.md.
Ce script ne passe JAMAIS d'ordre — lecture et opinion uniquement.
"""
import argparse
import csv
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime, timezone

SCRIPTS = os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts")
THERMO_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/thermo")
LIVE_JSON = os.path.join(THERMO_DIR, "live.json")
HISTORY = os.path.join(THERMO_DIR, "history.jsonl")
ANALYSES_DIR = os.path.join(THERMO_DIR, "analyses")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
MISSION_JSON = os.path.expanduser("~/ace777-test-day1/Index_Maison/cockpit/mission.json")
JUSTESSE = os.path.join(SCRIPTS, "justesse_cockpit.json")
DERIV_CORR_JSON = os.path.expanduser("~/ace777-test-day1/Index_Maison/data/deriv_corr.json")

# Lexique : id live.json -> (nom lisible, unité)
LEXIQUE = {
    "funding": ("Taux de financement", "taux par période de 8h"),
    "fundingAvg30": ("Funding moyenne 30j", "taux"),
    "oi": ("Open interest", "BTC (contrats)"),
    "longShort": ("Ratio long/short", "ratio"),
    "takerRatio": ("Ratio taker", "ratio"),
    "topTraderLS": ("Ratio L/S top traders", "ratio"),
    "fearGreed": ("Fear & Greed", "/100"),
    "marketCapUsd": ("Capitalisation totale", "USD"),
    "btcDominance": ("Dominance BTC", "%"),
    "altSeason": ("Saison altcoins", "label"),
    "altSeasonScore": ("Score saison altcoins", "/100"),
    "liq24Usd": ("Liquidations 24h", "USD"),
    "liqLongUsd": ("Liquidations longues 24h", "USD"),
    "liqShortUsd": ("Liquidations courtes 24h", "USD"),
    "gexPutCall": ("GEX proxy put/call OI", "ratio"),
    "gexCallWall": ("Mur de gamma calls", "strike"),
    "gexPutWall": ("Mur de gamma puts", "strike"),
    "etfBtcM": ("ETF BTC net inflow", "M$"),
    "etfEthM": ("ETF ETH net inflow", "M$"),
    "etfXrpM": ("ETF XRP net inflow", "M$"),
    "volumeCachedTaker": ("Taker buy ratio 24h", "ratio"),
    "volumeCachedPerpSpot": ("Ratio volume perp/spot", "ratio"),
    "chg24": ("Variation prix 24h", "%"),
    "chg1h": ("Variation prix 1h", "%"),
    "chg4h": ("Variation prix 4h", "%"),
    "panierDownPct": ("Panier en baisse", "%"),
    "whaleUsd": ("Flux baleines", "USD"),
    "whaleN": ("Baleines (≥50M$)", "compte"),
    "onchain": ("Flux onchain baleines (scan réel mempool — PAS le proxy aggTrades)", "synthèse"),
    "deriv_corr": ("Corrélations 30j dérivés (prix vs OI/funding/longShort/taker) + carte liquidité", "r 30j"),
    "liq_map": ("Carte liquidité : où sont les tas de liquidations par niveau de prix", "M$ par niveau"),
    "volQuote": ("Volume 24h", "USD"),
    "score": ("Score composite", "/100"),
    "climate": ("Climat", "label"),
    "mark": ("Prix mark BTC", "USD"),
    "radar": ("Radar climat (global)", "climat"),
    "bassine": ("Bassine / mur (score thermo)", "/100"),
    "verre": ("Verre d'eau (chaleur activite)", "%"),
}

# Indices toujours fournis comme contexte de mise en relation
CONTEXT_KEYS = ["mark", "chg24", "chg1h", "chg4h", "funding", "fundingAvg30",
                "oi", "longShort", "takerRatio", "topTraderLS", "fearGreed",
                "marketCapUsd", "btcDominance", "altSeason", "altSeasonScore",
                "panierDownPct", "whaleUsd", "whaleN", "volQuote", "score", "climate",
                "liq24Usd", "liqLongUsd", "liqShortUsd", "etfBtcM", "gexPutCall",
                "volumeCachedTaker", "volumeCachedPerpSpot"]


def lire_deriv_corr() -> dict:
    """Charge data/deriv_corr.json (corrélations 30j + carte liquidité).
    Renvoie {} si absent/illisible — jamais d'exception (les analyses continuent)."""
    try:
        with open(DERIV_CORR_JSON, encoding="utf-8") as f:
            return json.load(f) or {}
    except Exception:
        return {}

# Indices formes du cockpit : pas de cle live directe, valeur derivee
VIRTUAL = {
    "radar":   ("score", "Radar climat (global)", "climat global"),
    "bassine": ("score", "Bassine / mur (score thermo)", "/100"),
    "verre":   ("heat", "Verre d'eau (chaleur activite)", "%"),
}


def virtual_value(indice, live):
    """Valeur derivee pour les indices formes (bassine=score, verre=chaleur proxy)."""
    if indice == "verre":
        try:
            chg = abs(float(live.get("chg24") or 0))
            fund = abs(float(live.get("funding") or 0))
        except Exception:
            chg = fund = 0.0
        heat = min(100.0, round(chg * 8 + min(40.0, fund / 0.0003 * 30) + 20, 1))
        return heat, "chaleur locale (move 24h + stress funding) — proxy"
    if indice in ("radar", "bassine"):
        sc = live.get("score")
        clim = live.get("climate") or "climat inconnu"
        return sc, "climat " + str(clim)
    return None, None


def load_system_prompt():
    """Lit le prompt master analyste depuis le vault (canon).
    Y ajoute dynamiquement : (1) la conscience du système ACE777 (qui tourne,
    rôle chirurgical), (2) le score de justesse de l'analyste + ses derniers
    résultats (boucle d'apprentissage : elle voit ses erreurs et se recalibre).
    """
    candidates = [
        os.path.join(SCRIPTS, "prompts", "PROMPT_MASTER_ANALYSTE.md"),
        os.path.expanduser("~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md"),
    ]
    prompt = None
    for p in candidates:
        if os.path.exists(p):
            s = open(p).read()
            start = s.find("## SYSTEM PROMPT")
            end = s.find("---", start + 20)
            if start != -1 and end != -1:
                body = s[s.find("\n\n", start) + 2:end].strip()
                prompt = body
            else:
                prompt = s
            break
    if prompt is None:
        prompt = ("Tu es Cortana, master analyste crypto du cockpit ACE777. "
                  "Analyse l'indice reçu : faits, interpretation, mise en relation, "
                  "pattern, opinion. 8-12 phrases, chiffres exacts, vulgarise.")
    return prompt + "\n\n" + contexte_systeme()


def contexte_systeme() -> str:
    """Contexte vivant injecté : qui tourne dans ACE777 + boucle d'apprentissage."""
    lignes = ["### Contexte ACE777 (vivant, injecté à chaque analyse)"]

    # 1) Le système qui tourne (mission.json — lecture seule)
    try:
        m = json.load(open(MISSION_JSON))
        run = m.get("run") or "?"
        combo = m.get("comboPnl")
        a = m.get("alpha") or {}
        b = m.get("beta") or {}
        lignes.append(
            "- Système : run %s · duo ALPHA(sniper long x13)/BETA(éclaireur short x3) "
            "· combo %s $ · ALPHA %s fills (%s $) · BETA %s sondes (%s $)"
            % (run, "n/d" if combo is None else round(combo, 2),
               a.get("fills"), round(float(a.get("pnl") or 0), 2),
               b.get("fills"), round(float(b.get("pnl") or 0), 2))
        )
    except Exception:
        pass

    # 2) Ta place : analyste, jamais exécutante (rappel chirurgical)
    lignes.append(
        "- Ton rôle est CHIRURGICAL : tu es l'analyste, jamais dans la boucle d'ordre. "
        "Tes avis LONG/SHORT/NEUTRE informent l'humain (Christophe) et le superviseur, "
        "aucun d'eux ne déclenche un ordre. Le moteur ALPHA/BETA est 100% mécanique."
    )

    # 3) Boucle d'apprentissage : ton score de justesse + derniers résultats
    try:
        sc = json.load(open(JUSTESSE))
        pct = sc.get("pct")
        if pct is not None:
            lignes.append(
                "- Ton score de justesse global : %s%% (%s/%s avis notés). "
                "Ta note ne doit PAS te pousser vers NEUTRE : NEUTRE n'est pas un refuge, "
                "il est noté MISS dès que le marché bouge de ±0,3%% (il ne gagne que sur un "
                "marché réellement plat). Si tu es sous 60 pour cent, sois prudente sur tes "
                "CONFIANCES (préfère faible/moyenne) mais garde ta lecture : LONG/SHORT/NEUTRE "
                "selon les signaux, jamais par évitement. Au-dessus de 65 pour cent, tu peux "
                "être plus affirmée."
                % (pct, sc.get("total_hit"), sc.get("total_scored"))
            )
        par = sc.get("par_indice") or {}
        if par:
            lignes.append("- Ton bilan par indice (hit/n) : " + "; ".join(
                "%s %s/%s" % (k, v.get("hit"), v.get("n")) for k, v in sorted(par.items())))
    except Exception as _e:
        lignes.append("[contexte:justesse indisponible — %s]" % _e)

    # 4) Derniers résultats réels (HIT/MISS) — tu dois EN TIRER les leçons
    try:
        hist = load_history()
        analyses = []
        if os.path.isdir(ANALYSES_DIR):
            for fn in sorted(os.listdir(ANALYSES_DIR))[-3:]:
                try:
                    for line in open(os.path.join(ANALYSES_DIR, fn)):
                        line = line.strip()
                        if line:
                            analyses.append(json.loads(line))
                except Exception:
                    continue
        if analyses:
            recent = []
            for an in analyses[-6:]:
                avis_info = re.search(r"AVIS\s*STRICT\s*:\s*(\w+)", an.get("analyse") or "")
                if not avis_info:
                    continue
                t0 = None
                raw = an.get("faits_bruts") or {}
                if raw.get("ts"):
                    try:
                        t0 = datetime.fromisoformat(str(raw["ts"]).replace("Z", "+00:00")).timestamp()
                    except Exception:
                        pass
                p0 = None
                if t0:
                    for row in hist:
                        if row.get("tsUnix") and row.get("mark") and row.get("tsUnix") <= t0:
                            p0 = row["mark"]
                verdict = "en attente"
                if p0:
                    try:
                        p1 = None
                        for row in hist:
                            if row.get("tsUnix") and row.get("mark") and row.get("tsUnix") >= t0 + 24 * 3600:
                                p1 = row["mark"]
                                break
                        if p1:
                            move = (p1 - p0) / p0 * 100
                            avis = avis_info.group(1).upper()
                            if (avis == "LONG" and move > 0.05) or (avis == "SHORT" and move < -0.05):
                                verdict = "HIT"
                            elif (avis == "LONG" and move < -0.05) or (avis == "SHORT" and move > 0.05):
                                verdict = "MISS"
                            else:
                                verdict = "FLAT"
                    except Exception:
                        pass
                recent.append("%s sur %s -> %s" % (an.get("indice"), avis_info.group(1).upper(), verdict))
            if recent:
                lignes.append("- Tes derniers avis et ce que le marché a fait (24h) : " + " · ".join(recent[-5:]))
                lignes.append(
                    "- LEÇON : si tu répètes des MISS sur un indice, change de lecture sur CET indice "
                    "(ex. funding : funding positif ne veut pas toujours dire LONG)."
                )
    except Exception:
        pass

    # 4bis) VISION DES BOTS (18/08 — Christophe : « Cortana ne voit pas Hulk/ACE ») :
    #       Lecture SEULE des runs en cours pour que l'analyse porte aussi sur nos bots.
    try:
        ROOT_DIR = os.path.expanduser("~/ace777-test-day1")
        # --- ACE : dernier run (PnL, trades, raisons de sortie) ---
        ace_info = []
        for unit, csv_name in (("BETA", "MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"),
                               ("ALPHA", "MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv")):
            csv_path = os.path.join(ROOT_DIR, "runs", csv_name)
            if not os.path.exists(csv_path):
                continue
            last_day = None
            last_filled = []
            try:
                with open(csv_path) as f:
                    reader = csv.reader(f)
                    header = next(reader, None)
                    for row in reader:
                        if len(row) < 10:
                            continue
                        ts, _, _, status, _, _, _, _, pnl, reason = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]
                        if status == "FILLED":
                            last_filled.append((ts, float(pnl or 0), reason))
            except Exception:
                continue
            if not last_filled:
                continue
            # garder les FILLED du même jour UTC que le dernier trade
            last_day = last_filled[-1][0][:10]
            day_filled = [x for x in last_filled if x[0][:10] == last_day]
            total = sum(x[1] for x in day_filled)
            wins = sum(1 for x in day_filled if x[1] > 0)
            losses = sum(1 for x in day_filled if x[1] < 0)
            reasons = {}
            for _, _, r in day_filled:
                reasons[r] = reasons.get(r, 0) + 1
            top_reasons = ", ".join("%s x%s" % (k, v) for k, v in sorted(reasons.items(), key=lambda kv: -kv[1])[:4])
            ace_info.append(
                "%s (%s) : %d trades · PnL %+.2f$ · %d win/%d loss · sorties: %s"
                % (unit, last_day, len(day_filled), total, wins, losses, top_reasons or "n/a")
            )
        if ace_info:
            lignes.append("- ÉTAT ACE (dernier jour de run) : " + " | ".join(ace_info))
        # --- HULK : paper (positions, rip/stops, PnL) ---
        hulk_state = os.path.join(ROOT_DIR, "hulk-mexc", "runs", "PAPER_V1_20260816_214411_state.json")
        if os.path.exists(hulk_state):
            try:
                hs = json.load(open(hulk_state))
                pnl = hs.get("pnl_total")
                trades = hs.get("trades")
                pos = hs.get("positions") or {}
                pos_txt = ", ".join("%s(entrée %.4f)" % (k, float(v.get("entry") or 0)) for k, v in list(pos.items())[:6])
                lignes.append(
                    "- ÉTAT HULK (paper) : PnL %s$ · %s trades · positions: %s"
                    % ("n/d" if pnl is None else round(float(pnl), 2),
                       trades if trades is not None else "?", pos_txt or "aucune")
                )
            except Exception:
                pass
        hulk_csv = os.path.join(ROOT_DIR, "hulk-mexc", "runs", "PAPER_V1_20260816_214411.csv")
        if os.path.exists(hulk_csv):
            try:
                last_sells = []
                with open(hulk_csv) as f:
                    reader = csv.reader(f)
                    next(reader, None)
                    for row in reader:
                        if len(row) >= 11 and row[2] in ("SELL", "SELL_PARTIAL"):
                            last_sells.append((row[0], row[1], row[2], row[8], row[10]))
                if last_sells:
                    recent_sells = last_sells[-4:]
                    lignes.append("- HULK dernières sorties : " + " · ".join(
                        "%s %s %s (%s$ %s)" % (t, p, ev, pnl_v, reason_v)
                        for t, p, ev, pnl_v, reason_v in recent_sells))
            except Exception:
                pass
        # --- HULK : sonde aspiration (alerte en cours) ---
        hulk_alert = os.path.join(ROOT_DIR, "hulk-mexc", "runs", "VEILLE_ALERT.md")
        if os.path.exists(hulk_alert):
            try:
                alert_txt = open(hulk_alert).read().strip()
                if alert_txt:
                    lignes.append("- HULK SONDE (dernière alerte) : " + alert_txt[:300].replace(chr(10), " · "))
            except Exception:
                pass
    except Exception:
        pass

    # 5) Couche connaissance AUTO (option B — pilote contrôlé, garde-fous famille 15/08) :
    #    - injection SYNTHÉTIQUE pré-mâchée uniquement (jamais de chiffres bruts),
    #    - plafond 3 fiches par analyse (anti-infobésité à 44% de justesse),
    #    - filtre par sujet strict (mots-clés du nom/thèse), fallback rotation 1 fiche,
    #    - mode « observation » : on injecte, on mesure, si confusion → retour manuel.
    try:
        import injecter_connaissance as inj
        connaiss = inj.load_connaissance()
        projets = connaiss.get("projets", {}) or {}
        if projets:
            # Détection du sujet depuis l'indice demandé (le plus souvent un projet ou le marché)
            sujet = ""
            try:
                indice_courant = os.environ.get("INDICE_COURANT", "")
                if indice_courant:
                    sujet = indice_courant
            except Exception:
                pass
            selection = inj.selectionner_projets(projets, sujet=sujet)[:3]
            fiches = []
            for p in selection:
                p_data = projets.get(p, {})
                these = str(p_data.get("these", ""))[:200]
                statut = p_data.get("statut_verification", {}) or {}
                verdict = statut.get("verdict", "?") if isinstance(statut, dict) else "?"
                if these:
                    fiches.append(
                        "- Connaissance projet %s (%s) : %s [vérification : %s]"
                        % (p, p_data.get("nom", ""), these, verdict)
                    )
            if fiches:
                lignes.append("### Connaissance ACE777 (injectée — synthèse pré-mâchée)")
                lignes.extend(fiches[:3])
    except Exception:
        pass

    # 6) LEÇONS AGORA (boucle E4 — lecons_auto.py, famille 15/08) :
    #    axiomes issus de tes HIT/MISS, namespace cortana uniquement, TTL actif,
    #    max 3, synthèse pré-mâchée (jamais de chiffres bruts).
    try:
        agora_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "strategie", "CONNAISSANCE_PROJETS.json")
        if os.path.exists(agora_path):
            agora = json.load(open(agora_path, encoding="utf-8"))
            lecons = agora.get("lecons_agora", []) or []
            if isinstance(lecons, list):
                maintenant = datetime.now(timezone.utc)
                actives = []
                for l in lecons[:20]:
                    exp = l.get("ttl_expire")
                    if exp:
                        try:
                            if datetime.fromisoformat(str(exp).replace("Z", "+00:00")) < maintenant:
                                continue
                        except Exception:
                            pass
                    if l.get("namespace") == "cortana" and l.get("axiome"):
                        actives.append(l["axiome"])
                if actives:
                    lignes.append("### Leçons apprises (tes HIT/MISS — à appliquer)")
                    lignes.extend("- " + a for a in actives[:3])
    except Exception:
        pass

    return "\n".join(lignes)


def load_live():
    if not os.path.exists(LIVE_JSON):
        return {}
    try:
        return json.load(open(LIVE_JSON))
    except Exception:
        return {}


def load_history():
    """Charge history.jsonl -> liste de dicts (plus ancien au plus récent)."""
    if not os.path.exists(HISTORY):
        return []
    out = []
    try:
        with open(HISTORY) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except Exception:
                    continue
    except Exception:
        return []
    return out


def fmt_val(v):
    if v is None:
        return "INDISPONIBLE (null)"
    if isinstance(v, float):
        if abs(v) < 1e-4 and v != 0:
            return f"{v:.2e}"
        return f"{v:,.4f}" if abs(v) < 10 else f"{v:,.2f}"
    return str(v)


def trend_pct(history, key, hours):
    """Tendance en % sur les N dernières heures à partir de history.jsonl."""
    if not history or key not in history[-1]:
        return None
    now = history[-1][key]
    if not isinstance(now, (int, float)) or now == 0:
        return None
    target_ts = history[-1].get("tsUnix", 0) - hours * 3600
    past = None
    for row in history:
        if row.get("tsUnix", 0) <= target_ts and row.get(key) is not None:
            past = row[key]
    if past is None or not isinstance(past, (int, float)) or past == 0:
        return None
    return (now - past) / abs(past) * 100.0


def build_facts(indice):
    """Assemble le JSON de faits pour l'analyste."""
    live = load_live()
    history = load_history()

    # Indices formes (radar/bassine/verre) : valeur derivee du live
    if indice == "onchain":
        # Synthèse textuelle pré-mâchée par le pont (jamais les chiffres bruts)
        oc = live.get("onchain", {})
        base_key = "onchain"
        name, unit = LEXIQUE.get(indice, (indice, ""))
        vval = oc.get("synthèse") or oc.get("synthese") or "Données onchain non disponibles"
        vnote = "source " + str(oc.get("whaleSource", "inconnue")) + " · direction " + str(oc.get("whaleDir", "neutral"))
    elif indice in ("deriv_corr", "liq_map"):
        # Corrélations 30j + carte liquidité (data/deriv_corr.json, gen_deriv_corr.py)
        dc = lire_deriv_corr()
        base_key = indice
        name, unit = LEXIQUE.get(indice, (indice, ""))
        if not dc:
            vval, vnote = "Données dérivés indisponibles", "fichier absent ou illisible"
        elif indice == "liq_map":
            liq = dc.get("liquidations") or {}
            vval = liq.get("lecture") or "Carte liquidité indisponible"
            vnote = (f"mark {dc.get('mark')} · longs dessous {liq.get('longs_below_usd')} $ · "
                     f"shorts dessus {liq.get('shorts_above_usd')} $")
        else:
            corr = dc.get("correlations") or {}
            lectures = " · ".join((v.get("lecture") or "") for v in corr.values() if v)
            vval = lectures or "Corrélations indisponibles"
            vnote = f"mark {dc.get('mark')} · ts {dc.get('ts')}"
    elif indice in VIRTUAL:
        base_key, name, unit = VIRTUAL[indice]
        vval, vnote = virtual_value(indice, live)
    else:
        base_key, vval, vnote = indice, live.get(indice), None
        name, unit = LEXIQUE.get(indice, (indice, ""))
    facts = {
        "indice_demande": {
            "id": indice,
            "nom": name,
            "unite": unit,
            "valeur_actuelle": ("n/d" if vval is None else fmt_val(vval)) + ("  (" + vnote + ")" if vnote else ""),
        },
        "tendances": {
            "tendance_24h_pct": trend_pct(history, base_key, 24),
            "tendance_semaine_pct": trend_pct(history, base_key, 24 * 7),
        },
        "autres_indices": {},
        "historique_recent": [],
        "serie_prix_recente": [],
    }

    for k in CONTEXT_KEYS:
        if k in live and k != indice:
            facts["autres_indices"][k] = fmt_val(live.get(k))

    # historique récent de l'indice (derniers 12 points horaires)
    for row in history[-12:]:
        if base_key in row:
            facts["historique_recent"].append({
                "ts": row.get("ts", "?"),
                "valeur": fmt_val(row.get(base_key)),
            })

    # série de prix (closes mark) : derniers 12 points pour lecture ondulatoire
    for row in history[-12:]:
        if "mark" in row:
            facts["serie_prix_recente"].append({
                "ts": row.get("ts", "?"),
                "mark": row.get("mark"),
            })

    # valeurs brutes (non formatées) pour la comparaison ultérieure
    raw = {k: live.get(k) for k in CONTEXT_KEYS + ([indice] if indice in live else []) if k in live}
    if vval is not None:
        raw[base_key] = vval
    raw["ts"] = live.get("ts")
    raw["tendances"] = {
        "tendance_24h_pct": trend_pct(history, base_key, 24),
        "tendance_semaine_pct": trend_pct(history, base_key, 24 * 7),
    }
    return facts, raw


def call_hub(facts, indice, correction=None):
    system = load_system_prompt()
    payload = {
        "task": "cortana.analyse",  # routage : Gemini prioritaire, repli Qwen
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": (
                f"Analyse l'indice suivant : {indice}.\n\n"
                f"Données :\n{json.dumps(facts, ensure_ascii=False, indent=1)}\n\n"
                "Donne ton analyse selon ta structure (FAITS, LECTURE PHYSIQUE, "
                "INTERPRÉTATION, MISE EN RELATION, PATTERN, OPINION)."
                + (correction or "")
            )},
        ],
        "temperature": 0.4,
        "max_tokens": 700,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=None) as resp:
        data = json.load(resp)
    content = data["choices"][0]["message"]["content"]
    return content, data.get("provider", "?")


def journalise(indice, facts, facts_bruts, content, provider, avis_ok=True):
    """Enregistre l'analyse (exigence Christophe : comparer avec le marché)."""
    os.makedirs(ANALYSES_DIR, exist_ok=True)
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(ANALYSES_DIR, f"{day}.jsonl")
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "indice": indice,
        "provider": provider,
        "faits": facts,           # valeurs formatées (lisibles)
        "faits_bruts": facts_bruts,  # valeurs brutes (pour comparer avec le marché réel)
        "analyse": content,
        "avis_ok": avis_ok,
    }
    with open(path, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return path


def speak_text(text, voice="fr-FR-VivienneMultilingualNeural", rate="-15%"):
    """Voix Vivienne via python3 -m edge_tts (même mécanisme que cortana_voice)."""
    # MUTE (E-11) : même règle que cortana_voice — silence si le fichier existe
    if os.path.exists("/tmp/ace777_swarm_pids/.cortana_mute"):
        print("  [voix:MUETTE] mute actif — saut", file=sys.stderr)
        return 1
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        path = f.name
    cmd = [
        "python3", "-m", "edge_tts",
        "--voice", voice,
        f"--rate={rate}",
        "--text", text,
        "--write-media", path,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
    if proc.returncode != 0 or not os.path.exists(path) or os.path.getsize(path) < 100:
        print("  ✘ generation voix echouee", file=sys.stderr)
        if os.path.exists(path):
            os.unlink(path)
        return 1
    subprocess.run(["killall", "say"], check=False, capture_output=True)  # une seule piste (règle maison)
    subprocess.run(["killall", "afplay"], check=False, capture_output=True)
    time.sleep(0.05)
    subprocess.run(["afplay", path], check=False, timeout=240)
    os.unlink(path)
    return 0


def main():
    ap = argparse.ArgumentParser(description="Analyse live d'un indice par Cortana (master analyste)")
    ap.add_argument("indice", nargs="?", default=None, help="id de l'indice (ex: funding, oi, fearGreed)")
    ap.add_argument("--speak", action="store_true", help="lire l'analyse à voix haute (Vivienne)")
    ap.add_argument("--list", action="store_true", help="lister les indices disponibles")
    a = ap.parse_args()

    if a.list:
        for k, (name, unit) in LEXIQUE.items():
            print(f"  {k:16} {name} ({unit})")
        return 0

    if not a.indice:
        print("Usage : python3 cortana_analyse.py <indice> [--speak]  (ou --list)")
        return 2

    indice = a.indice
    if indice not in LEXIQUE:
        print(f"Indice '{indice}' inconnu. Disponibles :")
        for k in LEXIQUE:
            print(f"  {k}")
        return 2

    facts, facts_bruts = build_facts(indice)
    print(f"[analyse] {LEXIQUE[indice][0]} — envoi au hub (cortana.analyse)...", file=sys.stderr)

    try:
        content, provider = call_hub(facts, indice)
        import re as _re
        def _has_avis(t):
            return _re.search(r"AVIS STRICT\s*:\s*(LONG|SHORT|NEUTRE)", t, _re.IGNORECASE) is not None
        if not _has_avis(content):
            print("[avis] AVIS STRICT absent - retry avec correction...", file=sys.stderr)
            correction = ("\n\nTa réponse précédente n'a PAS la section 7 obligatoire. "
                          "Rends l'analyse À NOUVEAU, terminée par EXACTEMENT :\n"
                          "AVIS STRICT : LONG|SHORT|NEUTRE\n"
                          "HORIZON : 24h|1 semaine\n"
                          "CONFIANCE : haute|moyenne|faible")
            try:
                content2, provider2 = call_hub(facts, indice, correction)
                if _has_avis(content2):
                    content, provider = content2, provider2
                else:
                    content = content2
            except Exception as e2:
                print(f"✘ retry échoué : {e2}", file=sys.stderr)
    except Exception as e:
        print(f"✘ hub injoignable ou réponse inattendue : {e}", file=sys.stderr)
        print("Repli : voici les faits bruts (pas d'analyse IA disponible) :")
        print(json.dumps(facts, ensure_ascii=False, indent=1))
        return 1

    journal = journalise(indice, facts, facts_bruts, content, provider, avis_ok=_has_avis(content))
    print(f"[provider: {provider}]", file=sys.stderr)
    print(f"[journal: {journal}]", file=sys.stderr)

    if a.speak:
        print("  ▶ lecture vocale (Vivienne)...", file=sys.stderr)
        return speak_text(content)
    print(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
