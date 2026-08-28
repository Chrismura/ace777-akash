#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle : Détecteur de blocs privatisés / transactions fantômes (P0 + P1).
Contexte ACE777 : Utilise mempool.space (gratuit, sans clé), carnet d'historique 
glissant pour éliminer les faux positifs (tx normales entrées entre snapshot et bloc),
creusage sélectif respectant le free-tier (volume échantillonné, jamais N appels
pour N tx). Mode actif par défaut (décision 21/08).
"""

import os
import sys
import time
import json
import signal
import fcntl
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
LOCK_FILE = os.path.join(DATA_DIR, ".bloc_privatise.lock")

WINDOW_MINUTES = 60           # Fenêtre glissante pour l'historique des txids vus
MAX_HISTORY_AGE = WINDOW_MINUTES * 60
MIN_SNAPSHOTS = 6             # Compromis Gemini 24/08 : ≥ 6 snapshots (~12 min = 1 bloc
                              # complet de propagation) pour un taux fiable (leçon 1+2, 20/08 :
                              # à 3-5 snapshots le 24/08 → faux 100 % ; résorbé à snap 6)
FENETRE_BLOCS = 6             # Ancrage anti-veille (24/08) : fenêtre = 60 min OU dernier N blocs
ALERT_TX_THRESHOLD = 5        # Seuil de txs cachées pour creuser le détail (P1)
ALERT_TAUX_PCT = 10.0         # Seuil d'alerte ACTIF : taux fantôme ≥ 10 % (matrice du Juge, 21/08)
ALERT_VOLUME_BTC = 500.0      # + volume échantillon ≥ 500 BTC (matrice du Juge : taux>10% ET volume>500 BTC)
ECHANTILLON_MAX = 75          # Taille max d'échantillon de tx à creuser (24/08 : 50 → 75,
                              # compromis précision vs free-tier, zéro appel en régime normal)
HTTP_TIMEOUT = 10          # appels légers — fix 23/08 : timeouts COURTS prouvés
HTTP_TIMEOUT_LOURD = 15    # gros appels (mempool/txids, /tx/) — le 60 s ne se
                           # déclenchait JAMAIS (SYN black-hole réseau, vérifié
                           # 6 min bloqué) ; cpfp fonctionne avec 6 s → 15 s max
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

def verrou_anti_doublon():
    """Verrou exclusif non bloquant (fcntl) — compromis Gemini 24/08 : un seul
    process d'analyse à la fois. Si une 2e instance démarre (launchd + superviseur,
    cas du doublon vigie du 24/08), elle s'arrête net sans corrompre le carnet.
    Le verrou est libéré par l'OS à la sortie du process (run court)."""
    os.makedirs(DATA_DIR, exist_ok=True)
    fd = os.open(LOCK_FILE, os.O_CREAT | os.O_RDWR, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        os.close(fd)
        print("[DOUBLON] Une autre instance analyse déjà — arrêt (verrou anti-doublon 24/08).", file=sys.stderr)
        sys.exit(0)
    return fd

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
# Repli multi-source (fix 23/08) : mempool.space peut bannir/rate-limiter l'IP
# (le détecteur bombardait ~50 appels/2 min le 22/08 → timeouts en boucle 8h).
# → bascule automatique et PERSISTANTE sur blockstream.info (mêmes endpoints,
#   API publique gratuite) après 3 échecs consécutifs.

API_BASES = ["https://mempool.space/api", "https://blockstream.info/api"]
API_STATE_FILE = os.path.join(DATA_DIR, "mempool_api_base.json")
_api_idx = 0          # base actuellement utilisée (0 = mempool.space)

class _DelaiDepasse(Exception):
    """Déclenché par SIGALRM : interrompt une connexion qui ne répond jamais."""

# Garde-fou anti-blocage (constaté 23/08) : sur ce réseau, certaines IP sont
# "black-holées" (SYN_SENT sans réponse) et le timeout socket ne se déclenche
# PAS — le process restait coincé 8 h. SIGALRM force l'interruption, prouvé en
# test (5.0 s pile).
def _alarme_network(sig, frame):
    raise _DelaiDepasse("connexion bloquée (SYN black-hole)")

signal.signal(signal.SIGALRM, _alarme_network)

def _api_url(path):
    return f"{API_BASES[_api_idx]}/{path}"

def _charger_base():
    """Restaure la base choisie (persistance entre runs launchd — sinon le
    compteur repartirait à 0 à chaque cycle et la bascule n'arriverait jamais)."""
    global _api_idx
    try:
        with open(API_STATE_FILE, "r", encoding="utf-8") as f:
            d = json.load(f)
        if d.get("base") in (0, 1):
            _api_idx = int(d["base"])
    except Exception:
        pass

def _sauver_base():
    try:
        with open(API_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump({"base": _api_idx, "ts": int(time.time())}, f)
    except Exception:
        pass

def _bascule_api():
    """Bascule vers l'autre base (mempool.space ↔ blockstream.info) et fige le choix."""
    global _api_idx
    _api_idx = 1 - _api_idx
    _sauver_base()
    print(f"[INFO] Bascule API → {API_BASES[_api_idx]}", file=sys.stderr)

def _essayer(url, timeout, as_text):
    """2 tentatives courtes sur une URL, chacune protégée par SIGALRM (jamais
    de blocage long, même si le timeout socket ne se déclenche pas).
    Retourne (True, valeur) ou (False, None)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(2):
        check_kill_switch()
        signal.alarm(int(timeout) + 5)   # garde-fou : interrompt tout blocage
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if response.status == 200:
                    raw = response.read().decode('utf-8')
                    return (True, raw.strip() if as_text else json.loads(raw))
        except _DelaiDepasse:
            print(f"[ERREUR] {url} : connexion bloquée par le réseau — tentative abandonnée.", file=sys.stderr)
        except Exception as e:
            if attempt == 1:
                print(f"[ERREUR] Échec requête {url}: {e}", file=sys.stderr)
            else:
                time.sleep(1)
        finally:
            signal.alarm(0)
    return (False, None)

def _requete(path, timeout, as_text):
    """Essaie la base courante puis l'autre en repli immédiat ; fige le gagnant."""
    for _ in range(len(API_BASES)):
        ok, valeur = _essayer(_api_url(path), timeout, as_text)
        if ok:
            _sauver_base()
            return valeur
        _bascule_api()
    return None

def http_get_json(path, timeout=None):
    """GET JSON sur un chemin API (ex: 'mempool/txids'), avec repli multi-source.
    timeout=None -> HTTP_TIMEOUT_LOURD pour les gros payloads (mempool/txids, /tx/)."""
    if timeout is None:
        timeout = HTTP_TIMEOUT_LOURD if ("/txids" in path or path.startswith("tx/")) else HTTP_TIMEOUT
    return _requete(path, timeout, as_text=False)

_charger_base()

# --- GESTION DE L'HISTORIQUE GLISSANT (JSONL) ---

def _compter_lignes():
    """Compte les lignes du carnet (léger — sert au rythme des snapshots complets)."""
    if not os.path.exists(HISTORY_FILE):
        return 0
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0


def _union_txids_fichier():
    """Union des txids présents dans le carnet actuel (base de comparaison des deltas).
    La détection (load_history_index) n'utilise QUE cette union → stocker les deltas
    ne change RIEN au résultat tant que chaque txid persistant est dans ≥ 1 graine."""
    vus = set()
    if not os.path.exists(HISTORY_FILE):
        return vus
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                try:
                    vus.update(json.loads(ligne).get("txids", []))
                except json.JSONDecodeError:
                    continue
    except Exception:
        pass
    return vus


def snapshot_mempool():
    """Récupère les txids actuels de la mempool publique et les enregistre dans le carnet.
    Enregistre aussi la HAUTEUR du tip (ancrage anti-veille/dérive d'horloge,
    compromis Gemini 24/08) : la fenêtre glissante peut se caler sur les blocs
    plutôt que sur l'horloge système.

    FORMAT SEED+DELTA (28/08, GO Christophe — mémoire sans dénaturer la formule) :
    la détection n'utilise que l'UNION des txids vus sur la fenêtre glissante.
    → On écrit la liste COMPLÈTE (graine) toutes les ~10 lignes, et les NOUVEAUX
    txids (delta) entre les graines. Union identique, carnet ~20× plus léger
    (mempool congestée : 12 Mo → ~0,6 Mo par run).
    - Graine tous les 10 snapshots < fenêtre 60 min (30 snapshots) → toujours ≥ 2
      graines dans la fenêtre → un txid persistant est toujours dans une graine.
    - La clé reste "txids" → load_history_index/purge INCHANGÉS.
    - Liste vide/échec API → PAS de snapshot (évite carnet vide → faux 100 %)."""
    txids = http_get_json("mempool/txids")
    if not isinstance(txids, list) or not txids:
        return set()  # échec OU mempool vide = pas de snapshot (fiabilité préservée)

    now = int(time.time())
    txid_set = set(txids)

    hauteur = None
    h = http_get_text("blocks/tip/height")
    if h and h.strip().isdigit():
        hauteur = int(h.strip())

    os.makedirs(DATA_DIR, exist_ok=True)
    lignes = _compter_lignes()
    is_graine = (lignes == 0) or (lignes % 10 == 0)
    if is_graine:
        txids_a_ecrire = list(txid_set)
    else:
        vus = _union_txids_fichier()
        txids_a_ecrire = [t for t in txid_set if t not in vus]
    # Ajout append-only du snapshot courant (graine complète ou delta)
    entry = {"ts": now, "hauteur": hauteur, "txids": txids_a_ecrire}
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[ERREUR] Écriture historique mempool_vus.jsonl: {e}", file=sys.stderr)

    return txid_set

def load_history_index(max_age_sec=MAX_HISTORY_AGE, fenetre_blocs=FENETRE_BLOCS):
    """Charge l'historique jsonl, filtre par fenêtre glissante et retourne (set de txids vus, nb snapshots).

    Fenêtre = 60 min (horloge) OU dernier N blocs (hauteur du tip) — ancrage
    anti-veille/dérive d'horloge (compromis Gemini 24/08) : si l'horloge système
    saute (veille macOS, NTP), la hauteur de bloc reste le compteur fiable.

    Le nb de snapshots sert à exclure les artefacts de carnet vide (leçon 1+2 du
    20/08 + 24/08) : si on a moins de MIN_SNAPSHOTS snapshots dans la fenêtre
    (démarrage, purge, coupure réseau), le taux est marqué comme non fiable
    plutôt que de hurler 100 % de "fantômes"."""
    check_kill_switch()
    if not os.path.exists(HISTORY_FILE):
        return set(), 0
    
    now = int(time.time())
    cutoff = now - max_age_sec
    seen_txids = set()
    valid_lines = []
    n_snapshots = 0
    max_hauteur = None
    
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            raw = f.readlines()
        # Passe 1 : hauteur max du carnet (ancre indépendante de l'horloge)
        for line in raw:
            line = line.strip()
            if not line:
                continue
            try:
                h = json.loads(line).get("hauteur")
                if h is not None:
                    max_hauteur = h if max_hauteur is None else max(max_hauteur, h)
            except json.JSONDecodeError:
                continue
        # Passe 2 : garder les entrées dans la fenêtre temps OU le dernier N blocs
        for line in raw:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                ts = obj.get("ts", 0)
                h = obj.get("hauteur")
                dans_fenetre_temps = ts >= cutoff
                dans_fenetre_blocs = (max_hauteur is not None and h is not None
                                      and max_hauteur - h <= fenetre_blocs)
                if dans_fenetre_temps or dans_fenetre_blocs:
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

def purge_history(max_age_sec=MAX_HISTORY_AGE, fenetre_blocs=FENETRE_BLOCS):
    """Purge l'historique JSONL des entrées trop anciennes (même règle que
    load_history_index : 60 min OU dernier N blocs, pour rester cohérent)."""
    if not os.path.exists(HISTORY_FILE):
        return
    now = int(time.time())
    cutoff = now - max_age_sec
    max_hauteur = None
    
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            raw = f.readlines()
        for line in raw:
            line = line.strip()
            if not line:
                continue
            try:
                h = json.loads(line).get("hauteur")
                if h is not None:
                    max_hauteur = h if max_hauteur is None else max(max_hauteur, h)
            except json.JSONDecodeError:
                continue
        valid_lines = []
        for line in raw:
            line_str = line.strip()
            if not line_str:
                continue
            try:
                obj = json.loads(line_str)
                ts = obj.get("ts", 0)
                h = obj.get("hauteur")
                dans_fenetre_temps = ts >= cutoff
                dans_fenetre_blocs = (max_hauteur is not None and h is not None
                                      and max_hauteur - h <= fenetre_blocs)
                if dans_fenetre_temps or dans_fenetre_blocs:
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

def http_get_text(path, timeout=None):
    """GET HTTP texte brut (endpoints non-JSON, ex. blocks/tip/hash), avec repli multi-source."""
    if timeout is None:
        timeout = HTTP_TIMEOUT_LOURD if ("/txids" in path or path.startswith("tx/")) else HTTP_TIMEOUT
    return _requete(path, timeout, as_text=True)


def get_latest_block_info():
    """Récupère le hash du dernier bloc (texte brut) et ses txids (JSON)."""
    tip_hash = http_get_text("blocks/tip/hash")
    if not tip_hash:
        return None, []
    
    txids = http_get_json(f"block/{tip_hash}/txids")
    if not isinstance(txids, list):
        return tip_hash, []
        
    return tip_hash, txids

def analyze_block():
    """Exécute l'analyse du dernier bloc par rapport à l'historique de la mempool."""
    check_kill_switch()
    verrou_anti_doublon()   # un seul process d'analyse à la fois (24/08)
    
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

    # 5. Creusage sélectif (P1) : ne creuser le détail des tx que si le TAUX dépasse
    #    le seuil d'alerte (fix 23/08 + échantillon 75, compromis Gemini 24/08) :
    #    avant, ≥5 tx cachées suffisait à creuser 50 tx/régime normal (117 fantômes
    #    à ~2 %) → ~50 appels / 2 min = rate-limit mempool.space → pépite muette 8h.
    #    Le volume n'a de sens que pour les VRAIS événements (taux ≥ 10 %).
    #    Note 24/08 : l'API ne fournit PAS la valeur par tx dans le résumé du bloc
    #    (vérifié en direct : /api/block/{hash} = header seul) → volume = SOMME des
    #    outputs échantillonnés (borne inférieure honnête), PAS d'extrapolation
    #    médiane ×N (fausserait les queues lourdes = le cas baleine OTC).
    creuser = fiable and taux_fantome >= ALERT_TAUX_PCT and nb_tx_cachees >= ALERT_TX_THRESHOLD
    if creuser:
        print(f"[INFO] {nb_tx_cachees} txs fantômes (taux {taux_fantome:.1f}% >= {ALERT_TAUX_PCT}%). Récupération des détails (P1)...")
        for txid in fantomes[:ECHANTILLON_MAX]:  # Échantillon borné : précision vs free-tier (24/08)
            check_kill_switch()
            tx_data = http_get_json(f"tx/{txid}")
            if tx_data and isinstance(tx_data, dict):
                # Calcul du volume en BTC (somme des outputs en satoshis / 1e8)
                outs = tx_data.get("vout", [])
                val_sat = sum(out.get("value", 0) for out in outs)
                val_btc = val_sat / 1e8
                volume_btc += val_btc
                detailed_fantomes.append({"txid": txid, "volume_btc": val_btc})
            time.sleep(0.25)  # Respect rate-limit free-tier (24/08 : 0,2 → 0,25 s)
    else:
        # Volume estimé minimal ou non approfondi pour préserver l'API
        volume_btc = 0.0

    # --- Mode (actif par défaut depuis le 21/08, décision Christophe) ---
    mode = charger_mode()

    # --- Alerte ACTIVE : double condition matrice du Juge (21/08) ---
    # taux fantôme ≥ 10 % ET volume échantillon ≥ 500 BTC (pas l'un sans l'autre).
    alerte_emise = False
    alerte_raison = "Aucune anomalie (taux ou volume sous le seuil)"
    if mode == "actif" and fiable and taux_fantome is not None:
        if taux_fantome >= ALERT_TAUX_PCT and volume_btc >= ALERT_VOLUME_BTC:
            alerte_emise = True
            alerte_raison = (
                f"ALERTE BLOCS PRIVATISÉS : taux fantôme {taux_fantome}% ≥ {ALERT_TAUX_PCT:.0f}% "
                f"ET volume {round(volume_btc, 1)} BTC ≥ {ALERT_VOLUME_BTC:.0f} BTC "
                f"({nb_tx_cachees}/{total_txs} txs) — transaction(s) jamais vues dans la mempool "
                f"publique = OTC privée / CPFP masqué (matrice du Juge)."
            )
        else:
            alerte_raison = (
                f"Taux {taux_fantome}% (seuil {ALERT_TAUX_PCT:.0f}%) · "
                f"volume {round(volume_btc, 1)} BTC (seuil {ALERT_VOLUME_BTC:.0f}) — "
                f"double condition matrice du Juge non réunie"
            )

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