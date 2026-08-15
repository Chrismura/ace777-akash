#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle (ACE777) : PONT ONCHAIN — analyse les mouvements de baleines BTC (scan mempool
surveiller_whales.py) et injecte la section 'onchain' dans thermo/live.json.
Respecte les kill-switches ACE777, stdlib uniquement, écriture atomique, idempotent.

Structures réelles lues :
- data/whales_scan_latest.json : {"ts", "hauteur_tip", "gros_blocs": [{type, txid,
  hauteur, btc, sources, cibles, sources_label, sources_type}], "fragmentations":
  [{type, source, btc, sur_blocs}], "nb_surveilles"}
- data/whales_mouvements.jsonl : append-only, lignes {"ts", "type", "btc", ...}
- data/whales.json : {"_meta", "portefeuilles": [{address, label, entity, type}]}
"""

import os
import sys
import json
import tempfile
from pathlib import Path
from datetime import datetime, timezone, timedelta

INDEX_MAISON = Path(__file__).resolve().parent.parent

STOP_LOCAL = INDEX_MAISON / "strategie" / "STOP"
STOP_GLOBAL = Path.home() / "ace777-test-day1" / "Index_Maison" / "STOP_ALL"

DATA_DIR = INDEX_MAISON / "data"
THERMO_LIVE = INDEX_MAISON / "thermo" / "live.json"
WHALES_CFG = DATA_DIR / "whales.json"
WHALES_SCAN = DATA_DIR / "whales_scan_latest.json"
WHALES_LOGS = DATA_DIR / "whales_mouvements.jsonl"

SEUIL_GROS_BLOC_BTC = 1000.0
SEUIL_FRAG_BTC = 500.0


def verifier_kill_switch():
    if STOP_LOCAL.exists() or STOP_GLOBAL.exists():
        print("[KILL] Kill switch activé. Arrêt propre.", file=sys.stderr)
        sys.exit(0)


def charger_json(chemin, defaut):
    if not chemin.exists():
        return defaut
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[AVERTISSEMENT] Lecture {chemin}: {e}", file=sys.stderr)
        return defaut


def ecriture_atomique(chemin_cible, donnees):
    verifier_kill_switch()
    chemin_cible.parent.mkdir(parents=True, exist_ok=True)
    fd, chemin_tmp = tempfile.mkstemp(dir=str(chemin_cible.parent), prefix="tmp_ace_", text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        os.replace(chemin_tmp, chemin_cible)
    except Exception:
        if os.path.exists(chemin_tmp):
            try:
                os.remove(chemin_tmp)
            except Exception:
                pass
        raise


def lire_etiquettes(whales_meta):
    """whales.json → {adresse: label} pour qualifier la direction."""
    labels = {}
    for p in whales_meta.get("portefeuilles", []):
        addr = p.get("address")
        if addr:
            labels[addr] = p.get("label", "inconnu")
    return labels


def qualifier_direction(tx, labels):
    """inflow = vers exchange étiqueté · outflow = depuis exchange étiqueté · sinon neutral."""
    sources_label = tx.get("sources_label") or []
    cibles = tx.get("cibles") or []
    a_des_exchange = any("exchange" in str(s).lower() for s in sources_label)
    vers_exchange = any(
        labels.get(c.get("adresse")) and "exchange" in str(labels.get(c.get("adresse"))).lower()
        for c in cibles
    )
    if a_des_exchange and not vers_exchange:
        return "outflow"
    if vers_exchange and not a_des_exchange:
        return "inflow"
    return "neutral"


def lire_mouvements_24h():
    """Lit whales_mouvements.jsonl sur 24h glissantes → (cumul_btc, dernier_age_min)."""
    cumul = 0.0
    dernier_age_min = None
    maintenant = datetime.now(timezone.utc)
    limite = maintenant - timedelta(hours=24)
    if not WHALES_LOGS.exists():
        return cumul, dernier_age_min
    try:
        with open(WHALES_LOGS, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                try:
                    evt = json.loads(ligne)
                    ts_str = evt.get("ts")
                    if not ts_str:
                        continue
                    dt = datetime.fromisoformat(str(ts_str).replace("Z", "+00:00"))
                    if dt >= limite:
                        cumul += float(evt.get("btc", 0.0) or 0.0)
                        age = int((maintenant - dt).total_seconds() / 60)
                        if dernier_age_min is None or age < dernier_age_min:
                            dernier_age_min = age
                except Exception:
                    continue
    except Exception as e:
        print(f"[AVERTISSEMENT] Lecture {WHALES_LOGS}: {e}", file=sys.stderr)
    return cumul, dernier_age_min


def moyenne_mobile_7j():
    """Moyenne mobile 7j du cumul quotidien (approximation par fenêtres 24h sur le jsonl)."""
    if not WHALES_LOGS.exists():
        return 0.0
    maintenant = datetime.now(timezone.utc)
    cumuls_par_jour = {}
    try:
        with open(WHALES_LOGS, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                try:
                    evt = json.loads(ligne)
                    ts_str = evt.get("ts")
                    if not ts_str:
                        continue
                    dt = datetime.fromisoformat(str(ts_str).replace("Z", "+00:00"))
                    jour = dt.strftime("%Y-%m-%d")
                    cumuls_par_jour[jour] = cumuls_par_jour.get(jour, 0.0) + float(evt.get("btc", 0.0) or 0.0)
                except Exception:
                    continue
    except Exception:
        return 0.0
    jours = sorted(cumuls_par_jour.keys())[-7:]
    if not jours:
        return 0.0
    return round(sum(cumuls_par_jour[j] for j in jours) / len(jours), 2)


def main():
    verifier_kill_switch()

    scan_data = charger_json(WHALES_SCAN, {"gros_blocs": [], "fragmentations": []})
    whales_meta = charger_json(WHALES_CFG, {"portefeuilles": []})
    labels = lire_etiquettes(whales_meta)

    gros_blocs = scan_data.get("gros_blocs") or []
    fragmentations = scan_data.get("fragmentations") or []

    whale_blocs_n = len(gros_blocs)
    whale_blocs_btc = round(sum(float(g.get("btc", 0.0) or 0.0) for g in gros_blocs), 2)
    whale_frag_n = len(fragmentations)
    whale_frag_btc = round(sum(float(f.get("btc", 0.0) or 0.0) for f in fragmentations), 2)

    cumul_24h, dernier_age_min = lire_mouvements_24h()
    moy7j = moyenne_mobile_7j()

    # Direction dominante sur les gros blocs du scan récent
    dirs = [qualifier_direction(g, labels) for g in gros_blocs]
    n_in = dirs.count("inflow")
    n_out = dirs.count("outflow")
    if n_out > n_in:
        whale_dir = "outflow"
    elif n_in > n_out:
        whale_dir = "inflow"
    else:
        whale_dir = "neutral"

    sources = sorted({s for g in gros_blocs for s in (g.get("sources_label") or []) if s != "inconnu"})
    whale_source = ", ".join(sources) if sources else "inconnue"

    # Écart % au seuil de gros bloc (force du signal)
    whale_ecart_seuil = None
    if gros_blocs:
        whale_ecart_seuil = round((whale_blocs_btc / SEUIL_GROS_BLOC_BTC - 1.0) * 100.0, 1)

    alerte_bool = bool(gros_blocs) or bool(fragmentations)
    if alerte_bool:
        alerte_texte = (
            f"Activité baleines : {whale_blocs_n} gros bloc(s) ({whale_blocs_btc} BTC) "
            f"+ {whale_frag_n} fragmentation(s) ({whale_frag_btc} BTC). Source : {whale_source}."
        )
    else:
        alerte_texte = "Activité baleines nominale (aucun gros bloc ≥1000 BTC ni fragmentation ≥500 BTC)."

    synthese = (
        f"Direction onchain {whale_dir} | {whale_blocs_n} gros bloc(s) {whale_blocs_btc} BTC "
        f"sur le scan récent, cumul 24h {cumul_24h:.0f} BTC, source {whale_source}. {alerte_texte}"
    )

    # --- Onchain v2 : signal CPFP/dust (détecter_cpfp.py) — ENRICHIT la synthèse ---
    # Règles D2/D5/D6 : le pont n'enrichit QUE si mode ACTIF (validation 7 jours)
    # ET confirmation >= 2 (double condition déjà appliquée dans detecter_cpfp).
    cpfp_file = DATA_DIR / "cpfp_detect.json"
    cpfp_signal = None
    cpfp_score = 0.0
    if cpfp_file.exists():
        cpfp_data = charger_json(cpfp_file, {})
        mode = cpfp_data.get("mode", "observation")
        confirmation = int(cpfp_data.get("confirmation", 0) or 0)
        if mode == "actif" and confirmation >= 2 and cpfp_data.get("declenche_global"):
            cpfp_score = round(float(cpfp_data.get("zscores", 0.0) or 0.0) * 0.5, 2)  # D8 : ×0.5
            cpfp_signal = (
                "EXÉCUTION CPFP possible : mouvement de baleine camouflé détecté "
                "(arbre de poussière + transaction enfant à frais élevés). Prudence."
            )
            synthese += " | " + cpfp_signal

    section_onchain = {
        "whaleBlocsN": whale_blocs_n,
        "whaleBlocsBtc": whale_blocs_btc,
        "whaleFragN": whale_frag_n,
        "whaleFragBtc": whale_frag_btc,
        "whaleCumul24hBtc": round(cumul_24h, 2),
        "whaleMoy7jBtc": moy7j,
        "whaleDir": whale_dir,
        "whaleSource": whale_source,
        "whaleEcartSeuil": whale_ecart_seuil,
        "whaleAlerte": alerte_bool,
        "whaleAlerteTexte": alerte_texte,
        "dernierEvtMin": dernier_age_min if dernier_age_min is not None else -1,
        "synthèse": synthese,
        "cpfpSignal": cpfp_signal,
        "cpfpScore": cpfp_score,
    }

    verifier_kill_switch()
    live_data = charger_json(THERMO_LIVE, {})
    live_data["onchain"] = section_onchain
    ecriture_atomique(THERMO_LIVE, live_data)

    print(f"[OK] Pont onchain — blocs={whale_blocs_n} ({whale_blocs_btc} BTC) "
          f"frag={whale_frag_n} cumul24h={cumul_24h:.0f} BTC dir={whale_dir} "
          f"→ section onchain injectée dans live.json")


if __name__ == "__main__":
    main()
