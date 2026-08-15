#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
quant_desk.py — Quant desk v1 (Boucle Bull/Bear/Risque, mode OMBRE)
Confronte des thèses (Bull, Bear, Risque) et un arbitre sur l'état réel du portefeuille Hulk.
Sortie : Index_Maison/thermo/QUANT_DESK.md et Index_Maison/strategie/quant_desk.json.
Mode ombre pur : applique: false toujours. Aucun ordre n'est exécuté.
Stdlib uniquement. Fail-open.
Chantier 4 — signets N°25/N°68 @antpalkin + N°50 @gippp69 (15/08/2026).
"""

import os
import sys
import json
import glob
import time
import urllib.request
from datetime import datetime

# Chemins absolus ou relatifs robustes basés sur l'emplacement du script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

# Sous-dossiers et fichiers cibles
HULK_RUNS_DIR = os.path.join(ROOT_DIR, "hulk-mexc", "runs")
THERMO_DIR = os.path.join(ROOT_DIR, "Index_Maison", "thermo")
ANALYSES_DIR = os.path.join(THERMO_DIR, "analyses")
STRATEGIE_DIR = os.path.join(ROOT_DIR, "Index_Maison", "strategie")

JUSTESSE_PATH = os.path.join(SCRIPT_DIR, "justesse_v2.json")
DIGEST_PATH = os.path.join(HULK_RUNS_DIR, "DIGEST_LATEST.md")

QUANT_DESK_MD = os.path.join(THERMO_DIR, "QUANT_DESK.md")
QUANT_DESK_JSON = os.path.join(STRATEGIE_DIR, "quant_desk.json")

# URL du hub local (standard de l'écosystème ACE777)
HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"


def get_latest_hulk_state():
    """Trouve et lit le dernier fichier PAPER_V1_*_state.json par mtime."""
    pattern = os.path.join(HULK_RUNS_DIR, "PAPER_V1_*_state.json")
    files = glob.glob(pattern)
    if not files:
        return None, None
    latest_file = max(files, key=os.path.getmtime)
    try:
        with open(latest_file, "r", encoding="utf-8") as f:
            return json.load(f), latest_file
    except Exception:
        return None, None


def load_digest():
    """Charge le digest veille si présent."""
    if os.path.exists(DIGEST_PATH):
        try:
            with open(DIGEST_PATH, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            pass
    return "Aucun digest veille disponible."


def load_recent_cortana_analyses(limit=3):
    """Charge les N dernières lignes JSONL des analyses Cortana récentes."""
    all_lines = []
    if os.path.exists(ANALYSES_DIR):
        for path in glob.glob(os.path.join(ANALYSES_DIR, "*.jsonl")):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            try:
                                all_lines.append(json.loads(line))
                            except json.JSONDecodeError:
                                continue
            except Exception:
                continue
    all_lines.sort(key=lambda item: item.get("ts", ""), reverse=True)
    return all_lines[:limit]


def load_justesse():
    """Charge le taux de justesse v2."""
    if os.path.exists(JUSTESSE_PATH):
        try:
            with open(JUSTESSE_PATH, "r", encoding="utf-8") as f:
                return json.load(f).get("pct", "Inconnu")
        except Exception:
            pass
    return "Inconnu"


def call_hub(prompt, task_name="quant_desk", retries=2, delay=4):
    """Appelle le hub local (11435, format OpenAI-compatible) avec retry + fail-open."""
    payload = json.dumps({
        "task": task_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 900,
    }).encode("utf-8")
    req = urllib.request.Request(
        HUB_URL,
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=None) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                return res_data.get("choices", [{}])[0].get("message", {}).get("content")
        except Exception:
            if attempt < retries:
                time.sleep(delay)
    return None


def main():
    # 1. Chargement des données d'entrée (fail-open)
    state, state_path = get_latest_hulk_state()
    if not state:
        print("ERREUR: Données insuffisantes (aucun state Hulk trouvé).", file=sys.stderr)
        sys.exit(2)

    digest_content = load_digest()
    cortana_analyses = load_recent_cortana_analyses(limit=3)
    justesse_pct = load_justesse()

    # Extraction des métriques clés du state Hulk
    pnl_total = state.get("pnl_total", state.get("pnl", "N/A"))
    positions = state.get("positions", {})
    bags = state.get("bags", {})
    pair_cash = state.get("pair_cash", state.get("cash", "N/A"))
    notional_live = state.get("notional_live", "N/A")
    scores = state.get("scores", {})

    nb_pos = len(positions) if isinstance(positions, (dict, list)) else "N/A"
    nb_bags = len(bags) if isinstance(bags, (dict, list)) else "N/A"

    # Construction du contexte partagé pour les avocats
    contexte_str = f"""
--- CONTEXTE RÉEL HULK ---
- Fichier state : {os.path.basename(state_path) if state_path else 'Inconnu'}
- PnL Total : {pnl_total}
- Positions actives (nb) : {nb_pos}
- Bags (nb) : {nb_bags}
- Pair Cash : {pair_cash}
- Notional Live : {notional_live}
- Scores / Régimes : {json.dumps(scores, ensure_ascii=False)}
- Justesse globale : {justesse_pct}

--- DERNIER DIGEST VEILLE ---
{digest_content[:1500]}

--- ANALYSES CORTANA RÉCENTES ---
{json.dumps(cortana_analyses, ensure_ascii=False, indent=2)}
"""

    # 2. Appels aux 3 avocats
    prompt_base = f"Voici le contexte du Quant Desk :\n{contexte_str}\n\n"

    prompt_bull = prompt_base + "Tu es l'avocat BULL. Défends la thèse haussière : quelles positions/entrées Hulk garder, quoi acheter sur le dip, quelles paires semblent prêtes à monter. Max 6 phrases."
    prompt_bear = prompt_base + "Tu es l'avocat BEAR. Défends la thèse baissière : quelles positions couper, quels risques de stop/dump, quoi NE PAS acheter. Max 6 phrases."
    prompt_risque = prompt_base + "Tu es l'avocat RISQUE. Tu ne prends parti ni pour ni contre : tu évalues le RISQUE de chaque thèse (sizing, volatilité, liquidité, concentration). Max 6 phrases."

    print("Interrogation de l'avocat BULL...")
    avis_bull = call_hub(prompt_bull, task_name="quant_desk")
    if not avis_bull:
        avis_bull = "AVOCAT BULL : indisponible (hub injoignable)."

    print("Interrogation de l'avocat BEAR...")
    avis_bear = call_hub(prompt_bear, task_name="quant_desk")
    if not avis_bear:
        avis_bear = "AVOCAT BEAR : indisponible (hub injoignable)."

    print("Interrogation de l'avocat RISQUE...")
    avis_risque = call_hub(prompt_risque, task_name="quant_desk")
    if not avis_risque:
        avis_risque = "AVOCAT RISQUE : indisponible (hub injoignable)."

    # Si le hub est totalement injoignable pour tous les avocats
    hub_injoignable = ("indisponible" in avis_bull and "indisponible" in avis_bear and "indisponible" in avis_risque)

    # 3. Appel de l'arbitre (4e appel hub)
    plaidoiries = f"""
PLAIDOIRIE BULL :
{avis_bull}

PLAIDOIRIE BEAR :
{avis_bear}

PLAIDOIRIE RISQUE :
{avis_risque}
"""

    prompt_arbitre = f"""
{contexte_str}

{plaidoiries}

En tant qu'arbitre superviseur, analyse ces trois plaidoiries et le contexte, puis rends ton verdict STRICTEMENT sous ce format exact :
VERDICT : BULL | BEAR | MIXTE | PRUDENT (choisir 1)
CONFIANCE : faible | moyenne | haute
POINTS FORTS (2 max) : ...
RISQUES RÉSIDUELS (2 max) : ...
ACTION CONSEILLÉE (1 ligne) : ex. « garder les positions, ne pas ouvrir sur les paires DEAD, préparer le cash pour un dip »
"""

    print("Interrogation de l'arbitre...")
    verdict_brut = call_hub(prompt_arbitre, task_name="quant_desk.arbitre")

    if not verdict_brut:
        verdict_brut = """VERDICT : PRUDENT
CONFIANCE : faible
POINTS FORTS (2 max) : Aucun (hub injoignable)
RISQUES RÉSIDUELS (2 max) : Impossibilité de contacter le hub LLM
ACTION CONSEILLÉE (1 ligne) : maintenir l'état actuel en mode ombre, vérifier la connexion du hub."""

    # Parsing basique ou conservation brute structurée pour le json/rapport
    verdict_final = "PRUDENT"
    confiance_final = "faible"
    action_conseillee = "maintenir l'état actuel en mode ombre."

    for line in verdict_brut.splitlines():
        line_upper = line.upper()
        if line_upper.startswith("VERDICT :"):
            verdict_final = line.split(":", 1)[1].strip()
        elif line_upper.startswith("CONFIANCE :"):
            confiance_final = line.split(":", 1)[1].strip()
        elif line_upper.startswith("ACTION CONSEILLÉE :") or line_upper.startswith("ACTION CONSEILLEE :"):
            action_conseillee = line.split(":", 1)[1].strip()

    # 4. Écriture des sorties
    os.makedirs(THERMO_DIR, exist_ok=True)
    os.makedirs(STRATEGIE_DIR, exist_ok=True)

    timestamp_iso = datetime.now().isoformat()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Rapport Markdown : Index_Maison/thermo/QUANT_DESK.md
    md_content = f"""# Quant desk — {date_str}

## Contexte réel Hulk
- **PnL Total** : `{pnl_total}`
- **Positions actives** : `{nb_pos}`
- **Bags** : `{nb_bags}`
- **Pair Cash** : `{pair_cash}`
- **Notional Live** : `{notional_live}`
- **Justesse globale** : `{justesse_pct}`

---

## Plaidories des Avocats

### 🐂 Avocat BULL
{avis_bull}

### 🐻 Avocat BEAR
{avis_bear}

### ⚖️ Avocat RISQUE
{avis_risque}

---

## Verdict Arbitre & Croisement Cortana

- **VERDICT** : `{verdict_final}`
- **CONFIANCE** : `{confiance_final}`
- **ACTION CONSEILLÉE** : `{action_conseillee}`

### Avis stricts Cortana récents (références)
```json
{json.dumps(cortana_analyses, ensure_ascii=False, indent=2)}
```

---

> **ENCADRÉ** : mode ombre — conseil différé, rien d'appliqué.
"""

    with open(QUANT_DESK_MD, "w", encoding="utf-8") as f:
        f.write(md_content)

    # JSON structuré : Index_Maison/strategie/quant_desk.json
    json_data = {
        "ts": timestamp_iso,
        "contexte": {
            "pnl_total": pnl_total,
            "positions_nb": nb_pos,
            "bags_nb": nb_bags,
            "pair_cash": pair_cash,
            "notional_live": notional_live,
            "justesse_pct": justesse_pct
        },
        "verdict": verdict_final,
        "confiance": confiance_final,
        "action_conseillee": action_conseillee,
        "brut_arbitre": verdict_brut,
        "applique": False
    }

    with open(QUANT_DESK_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print(f"Rapport généré avec succès : {QUANT_DESK_MD}")
    print(f"JSON stratégique mis à jour : {QUANT_DESK_JSON}")

    # Exit code
    sys.exit(1 if hub_injoignable else 0)


# -----------------------------------------------------------------------------
# BRANCHEMENT (OPTIONNEL, à laisser OFF par défaut)
# Pour l'activer dans la discipline quotidienne : décommenter l'appel ci-dessous
# dans discipline_quotidienne.py (ou appeler ce script via cron/manuel).
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
