#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle : Détecteur de blocs privatisés / transactions fantômes (P0 + P1).
Contexte ACE777 : Utilise mempool.space (gratuit, sans clé), carnet d'historique 
glissant pour éliminer les faux positifs (tx normales entrées entre snapshot et bloc),
et pré-filtre strict respectant le free-tier. Mode observation par défaut.
"""

import os
import sys
import time
import json
import urllib.request
import urllib.error
import tempfile
from datetime import datetime, timezone

# --- CONFIGURATION & CONSTANTES ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
INDEX_MAISON = os.path.join(BASE_DIR, "Index_Maison")
STRATEGIE_DIR = os.path.join(INDEX_MAISON, "strategie")
DATA_DIR = os.path.join(INDEX_MAISON, "data")

STOP_FILE = os.path.join(STRATEGIE_DIR, "STOP")
STOP_ALL_FILE = os.path.join(INDEX_MAISON, "STOP_ALL")
GLOBAL_STOP_ALL = os.path.expanduser("~/ace777-test-day1/Index_Maison/STOP_ALL")

HISTORY_FILE = os.path.join(DATA_DIR, "mempool_vus.jsonl")
OUTPUT_JSON = os.path.join(DATA_DIR, "bloc_privatise.json")
HIST_JSONL = os.path.join(DATA_DIR, "bloc_privatise_hist.jsonl")
BILAN_MD = os.path.join(DATA_DIR, "BLOC_PRIVATISE_BILAN.md")
MODE_FILE = os.path.join(DATA_DIR, "bloc_privatise_mode.json")

WINDOW_MINUTES = 60           # Fenêtre glissante pour l'historique des txids vus
MAX_HISTORY_AGE = WINDOW_MINUTES * 60
MIN_SNAPSHOTS = 3             # Minimum de snapshots dans la fenêtre pour un taux fiable (leçon 1+2, 20/08)
ALERT_TX_THRESHOLD = 5        # Seuil de txs cachées pour creuser le détail (P1)
ALERT_TAUX_PCT = 10.0         # Seuil d'alerte ACTIF : taux fantôme ≥ 10 % (matrice du Juge, 21/08)
HTTP_TIMEOUT = 10
USER_AGENT = "ACE777-VigieMempool/1.0"

# Décision 21/08 (Christophe, GO direct — famille mise de côté pour la pépite) :
# la pépite sort du mode observation silencieux et passe en ACTIF. On peut la
# repasser en observation avec : python3 detecter_bloc_privatise.py --observation

# --- UTILITAIRES DE SÉCURITÉ ---

def check_kill_switch():
    """Vérifie l'existence des fichiers de stop. Quitte proprement si actifs."""
    stops = [STOP_FILE, STOP_ALL_FILE, GLOBAL_STOP_ALL]
    for s in stops:
        if os.path.exists(s):
            print(f"[KILL-SWITCH] Arrêt d'urgence activé par : {s}", file=sys.stderr)
            sys.exit(0)

def atomic_write_json(filepath, data):
    """Écriture atomique d'un fichier JSON (mkstemp + os.replace)."""
    check_kill_switch()
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    dir_name = os.path.dirname(filepath)
    fd, temp_path = tempfile.mkstemp(dir=dir_name, text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(temp_path, filepath)
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise e

# --- REQUÊTES HTTP ROBUSTES ---

def http_get_json(url):
    """Effectue une requête GET HTTP et retourne le JSON parsé avec retries."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        check_kill_switch()
        try:
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as response:
                if response.status == 200:
                    return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            if attempt == 2:
                print(f"[ERREUR] Échec requête {url}: {e}", file=sys.stderr)
                return None
            time.sleep(2 * (attempt + 1))
    return None

# --- GESTION DE L'HISTORIQUE GLISSANT (JSONL) ---

def snapshot_mempool():
    """Récupère les txids actuels de la mempool publique et les enregistre dans le carnet."""
    url = "https://mempool.space/api/mempool/txids"
    txids = http_get_json(url)
    if not isinstance(txids, list):
        return set()
    
    now = int(time.time())
    txid_set = set(txids)
    
    os.makedirs(DATA_DIR, exist_ok=True)
    # Ajout append-only du snapshot courant
    entry = {"ts": now, "txids": list(txid_set)}
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[ERREUR] Écriture historique mempool_vus.jsonl: {e}", file=sys.stderr)
        
    return txid_set

def load_history_index(max_age_sec=MAX_HISTORY_AGE):
    """Charge l'historique jsonl, filtre par fenêtre glissante et retourne (set de txids vus, nb snapshots).

    Le nb de snapshots sert à exclure les artefacts de carnet vide (leçon 1+2 du
    20/08) : si on a moins de MIN_SNAPSHOTS snapshots dans la fenêtre (démarrage,
    purge, coupure réseau), le taux est marqué comme non fiable plutôt que de
    hurler 100 % de "fantômes"."""
    check_kill_switch()
    if not os.path.exists(HISTORY_FILE):
        return set(), 0
    
    now = int(time.time())
    cutoff = now - max_age_sec
    seen_txids = set()
    valid_lines = []
    n_snapshots = 0
    
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    ts = obj.get("ts", 0)
                    if ts >= cutoff:
                        valid_lines.append(line)
                        n_snapshots += 1
                        for tx in obj.get("txids", []):
                            seen_txids.add(tx)
                except json.JSONDecodeError:
                    continue
                    
        # Réécriture optionnelle/allègement si le fichier devient trop gros (garder uniquement les valides)
        # Pour rester idempotent et simple, on ne réécrit pas à chaque fois, mais on peut purger périodiquement.
    except Exception as e:
        print(f"[ERREUR] Lecture historique: {e}", file=sys.stderr)
        
    return seen_txids, n_snapshots

def purge_history(max_age_sec=MAX_HISTORY_AGE):
    """Purge l'historique JSONL des entrées trop anciennes."""
    if not os.path.exists(HISTORY_FILE):
        return
    now = int(time.time())
    cutoff = now - max_age_sec
    valid_lines = []
    
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line_str = line.strip()
                if not line_str:
                    continue
                try:
                    obj = json.loads(line_str)
                    if obj.get("ts", 0) >= cutoff:
                        valid_lines.append(line_str)
                except json.JSONDecodeError:
                    continue
        atomic_write_json_lines(HISTORY_FILE, valid_lines)
    except Exception as e:
        print(f"[ERREUR] Purge historique: {e}", file=sys.stderr)

def atomic_write_json_lines(filepath, lines):
    """Écriture atomique d'un fichier JSONL."""
    check_kill_switch()
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    dir_name = os.path.dirname(filepath)
    fd, temp_path = tempfile.mkstemp(dir=dir_name, text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            for l in lines:
                f.write(l + "\n")
        os.replace(temp_path, filepath)
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise e

def append_jsonl(filepath, data):
    """Append atomique d'une ligne JSONL (historique des taux)."""
    check_kill_switch()
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"[ERREUR] Append {filepath}: {e}", file=sys.stderr)

def charger_mode():
    """Retourne le mode : 'actif' par défaut (décision 21/08) sauf si --observation."""
    if os.path.exists(MODE_FILE):
        try:
            with open(MODE_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("mode", "actif")
        except Exception:
            pass
    return "actif"

def set_mode(mode):
    """Écrit le mode dans MODE_FILE (atomique)."""
    data = {"mode": mode, "ts": datetime.now(timezone.utc).isoformat()}
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(MODE_FILE), text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp, MODE_FILE)
    except Exception as e:
        if os.path.exists(tmp):
            os.remove(tmp)
        print(f"[ERREUR] set_mode: {e}", file=sys.stderr)
        os.replace(temp_path, filepath)
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise e

# --- LOGIQUE DE DÉTECTION ---

def http_get_text(url):
    """GET HTTP et retourne le texte brut (pour endpoints non-JSON, ex. blocks/tip/hash)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        check_kill_switch()
        try:
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as response:
                if response.status == 200:
                    return response.read().decode('utf-8').strip()
        except Exception as e:
            if attempt == 2:
                print(f"[ERREUR] Échec requête {url}: {e}", file=sys.stderr)
                return None
            time.sleep(2 * (attempt + 1))
    return None


def get_latest_block_info():
    """Récupère le hash du dernier bloc (texte brut) et ses txids (JSON)."""
    tip_hash = http_get_text("https://mempool.space/api/blocks/tip/hash")
    if not tip_hash:
        return None, []
    
    txids = http_get_json(f"https://mempool.space/api/block/{tip_hash}/txids")
    if not isinstance(txids, list):
        return tip_hash, []
        
    return tip_hash, txids

def analyze_block():
    """Exécute l'analyse du dernier bloc par rapport à l'historique de la mempool."""
    check_kill_switch()
    
    # 1. Snapshot de la mempool courante et enrichissement de l'historique
    snapshot_mempool()
    purge_history()
    
    # 2. Charger l'historique des txids vus sur la fenêtre glissante
    seen_history, n_snapshots = load_history_index()
    
    # 3. Récupérer le dernier bloc miné
    block_hash, block_txids = get_latest_block_info()
    if not block_hash or not block_txids:
        print("[ERREUR] Impossible de récupérer les informations du dernier bloc.", file=sys.stderr)
        return None
        
    total_txs = len(block_txids)
    if total_txs == 0:
        return None

    # 4. Identification des fantômes (jamais vus dans notre historique glissant)
    fantomes = [tx for tx in block_txids if tx not in seen_history]
    nb_tx_cachees = len(fantomes)
    taux_fantome = round((nb_tx_cachees / total_txs) * 100, 4) if total_txs > 0 else 0.0

    # Leçon 1+2 (20/08) : carnet trop vide = mesure non fiable (artefact de
    # démarrage/purge qui donnait 100 %). On le marque, on ne crie pas dessus.
    fiable = n_snapshots >= MIN_SNAPSHOTS
    if not fiable:
        print(f"[INFO] Historique insuffisant ({n_snapshots} snapshots < {MIN_SNAPSHOTS}) — taux non fiable, marqué null.", file=sys.stderr)
    
    volume_btc = 0.0
    detailed_fantomes = []

    # 5. Pré-filtre API (P1) : ne creuser le détail des tx que si le seuil est dépassé
    if nb_tx_cachees >= ALERT_TX_THRESHOLD:
        print(f"[INFO] {nb_tx_cachees} txs fantômes détectées (seuil >= {ALERT_TX_THRESHOLD}). Récupération des détails (P1)...")
        for txid in fantomes[:50]: # Limite de sécurité pour le free-tier
            check_kill_switch()
            tx_data = http_get_json(f"https://mempool.space/api/tx/{txid}")
            if tx_data and isinstance(tx_data, dict):
                # Calcul du volume en BTC (somme des outputs en satoshis / 1e8)
                outs = tx_data.get("vout", [])
                val_sat = sum(out.get("value", 0) for out in outs)
                val_btc = val_sat / 1e8
                volume_btc += val_btc
                detailed_fantomes.append({"txid": txid, "volume_btc": val_btc})
            time.sleep(0.2) # Respect rate-limit free-tier
    else:
        # Volume estimé minimal ou non approfondi pour préserver l'API
        volume_btc = 0.0

    # --- Mode (actif par défaut depuis le 21/08, décision Christophe) ---
    mode = charger_mode()

    # --- Alerte ACTIVE si taux fiable ≥ seuil (décision 21/08, matrice du Juge) ---
    alerte_emise = False
    alerte_raison = "Aucune anomalie (taux sous le seuil)"
    if mode == "actif" and fiable and taux_fantome is not None:
        if taux_fantome >= ALERT_TAUX_PCT:
            alerte_emise = True
            alerte_raison = (
                f"ALERTE BLOCS PRIVATISÉS : taux fantôme {taux_fantome}% ≥ seuil "
                f"{ALERT_TAUX_PCT:.0f}% ({nb_tx_cachees}/{total_txs} txs) — "
                f"transaction(s) jamais vues dans la mempool publique = OTC privée / CPFP masqué. "
                f"Volume échantillon {round(volume_btc, 4)} BTC."
            )
        else:
            alerte_raison = f"Taux {taux_fantome}% sous le seuil {ALERT_TAUX_PCT:.0f}%"

    result = {
        "ts": int(time.time()),
        "utc": datetime.now(timezone.utc).isoformat(),
        "bloc": block_hash,
        "total_tx_bloc": total_txs,
        "nb_tx_cachees": nb_tx_cachees,
        "taux_fantome": taux_fantome if fiable else None,
        "taux_non_fiable": not fiable,
        "n_snapshots": n_snapshots,
        "volume_btc": round(volume_btc, 4),
        "mode": mode,
        "alerte_potentielle": {
            "emise": alerte_emise,
            "raison": alerte_raison
        },
        "fantomes_echantillon": detailed_fantomes[:10]
    }

    # Enregistrement atomique du résultat (état courant, lu par le pont)
    atomic_write_json(OUTPUT_JSON, result)

    # Historique des taux en append (pour corrélation avec les prix — décision 21/08)
    hist_entry = {
        "ts": int(time.time()),
        "utc": datetime.now(timezone.utc).isoformat(),
        "bloc": block_hash,
        "taux_fantome": taux_fantome if fiable else None,
        "taux_non_fiable": not fiable,
        "n_snapshots": n_snapshots,
        "nb_tx_cachees": nb_tx_cachees,
        "total_tx_bloc": total_txs,
        "volume_btc": round(volume_btc, 4),
        "mode": mode,
        "alerte": alerte_emise
    }
    append_jsonl(HIST_JSONL, hist_entry)

    mode_txt = "ACTIF" if mode == "actif" else "observation"
    alerte_txt = " 🚨 ALERTE" if alerte_emise else ""
    print(f"[SUCCÈS] Analyse bloc {block_hash[:10]}... Taux fantôme: {taux_fantome}% ({nb_tx_cachees}/{total_txs} txs). Mode {mode_txt}.{alerte_txt}")
    return result

def generer_bilan():
    """Génère un fichier Markdown récapitulatif (data/BLOC_PRIVATISE_BILAN.md)."""
    check_kill_switch()
    if not os.path.exists(OUTPUT_JSON):
        print("[BILAN] Aucun fichier de résultat trouvé.", file=sys.stderr)
        return
        
    try:
        with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[BILAN] Erreur lecture {OUTPUT_JSON}: {e}", file=sys.stderr)
        return
        
    md_content = f"""# Bilan Vigie Mempool - Détecteur Bloc Privatisé
*Généré le : {data.get('utc', 'N/A')}*

## Dernier Bloc Analysé
- **Hash du bloc** : `{data.get('bloc', 'N/A')}`
- **Total Transactions** : `{data.get('total_tx_bloc', 0)}`
- **Transactions Fantômes** : `{data.get('nb_tx_cachees', 0)}`
- **Taux Fantôme** : `{data.get('taux_fantome', 0.0)} %`
- **Volume estimé (BTC)** : `{data.get('volume_btc', 0.0)} BTC`
- **Mode** : `{data.get('mode', 'observation')}`
- **Alerte Émise** : `{data.get('alerte_potentielle', {}).get('emise', False)}`

## Doctrine & Paramètres
- Fenêtre d'historique glissant : `{WINDOW_MINUTES} minutes`
- Seuil de déclenchement d'approfondissement (P1) : `{ALERT_TX_THRESHOLD} txs`
- Source : `mempool.space` (Free tier, sans clé)
"""
    atomic_write_json_lines(BILAN_MD, [md_content])
    print(f"[BILAN] Rapport généré : {BILAN_MD}")

# --- MAIN ---

def main():
    check_kill_switch()

    if "--actif" in sys.argv:
        set_mode("actif")
        print("[MODE] Pépite BLOCS PRIVATISÉS basculée en ACTIF — alertes taux ≥ "
              f"{ALERT_TAUX_PCT:.0f}% actives. (décision Christophe 21/08)")
        return
    if "--observation" in sys.argv:
        set_mode("observation")
        print("[MODE] Pépite BLOCS PRIVATISÉS repassée en OBSERVATION (silencieuse).")
        return
    if "--bilan" in sys.argv:
        generer_bilan()
        return

    analyze_block()

if __name__ == "__main__":
    main()