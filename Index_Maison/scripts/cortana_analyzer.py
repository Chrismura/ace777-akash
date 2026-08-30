#!/usr/bin/env python3
"""
cortana_analyzer.py — ANALYSE AUTONOME DE CORTANA
Lit les signaux de sentinel.py, applique les fiches d'analyse,
génère des recommandations pour Hulk.

Architecture :
  sentinel.py → signals.json → cortana_analyzer.py → cortana_analysis.json → Hulk

Auteur : Ace (Index Maison)
Version : 1.0
Date : 2026-08-25
"""

import json
import time
from pathlib import Path
from datetime import datetime, timezone

DATA_DIR = Path(__file__).parent.parent / "data"
SIGNALS = DATA_DIR / "sentinel_signals.json"
FICHES_DIR = DATA_DIR / "fiches_analyse"
LIVE = Path(__file__).parent.parent / "thermo" / "live.json"
OUTPUT = DATA_DIR / "cortana_analysis.json"

# ─── Load fiches ──────────────────────────────────────────────

def load_fiches():
    """Charge toutes les fiches d'analyse"""
    fiches = {}
    if not FICHES_DIR.exists():
        return fiches
    for f in FICHES_DIR.glob("*.json"):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            fiches[data["type"]] = data
        except Exception as e:
            print(f"  [ANALYZER] Erreur fiche {f.name}: {e}")
    return fiches

# ─── Load live data ──────────────────────────────────────────

def load_live():
    """Charge les données live"""
    try:
        return json.loads(LIVE.read_text(encoding="utf-8"))
    except Exception:
        return {}

# ─── Load signals ────────────────────────────────────────────

def _to_epoch(ts):
    """Normalise un timestamp (float epoch ou chaîne ISO) en epoch float"""
    if ts is None:
        return 0
    if isinstance(ts, (int, float)):
        return float(ts)
    try:
        return datetime.fromisoformat(str(ts)).timestamp()
    except Exception:
        return 0

def load_signals():
    """Charge les signaux de sentinel (ts normalisé en epoch)"""
    try:
        data = json.loads(SIGNALS.read_text(encoding="utf-8"))
        signals = data.get("signals", [])
        for s in signals:
            s["ts"] = _to_epoch(s.get("ts"))
        return signals
    except Exception:
        return []

# ─── Match signal to fiche ──────────────────────────────────

def match_fiche(signal, fiches):
    """Trouve la fiche correspondant à un signal"""
    metric = signal.get("metric", "")
    
    # Mapping metric → fiche type
    mapping = {
        "cpfp": "blocs_privilises",
        "dust": "blocs_privilises",
        "rbf": "rbf_eleve",
        "sdi": "rbf_eleve",
        "ipt": "rbf_eleve",
        "volume": "rbf_eleve",
        "funding": "rbf_eleve",
    }
    
    fiche_type = mapping.get(metric, metric)
    return fiches.get(fiche_type)

# ─── Evaluate questions ─────────────────────────────────────

def evaluate_questions(fiche, live):
    """Évalue les questions de la fiche avec les données live"""
    results = {}
    oc = live.get("onchain", {})
    
    for q in fiche.get("questions", []):
        qid = q["id"]
        source = q.get("source", "")
        seuil = q.get("seuil", 0)
        
        # Extraire la valeur depuis live
        value = None
        if source == "live.json → chg1h":
            value = live.get("chg1h", 0)
        elif source == "live.json → sdi.sdi":
            value = live.get("sdi", {}).get("sdi", 0)
        elif source == "live.json → rbf.rbf_score":
            value = live.get("rbf", {}).get("rbf_score", 0)
        elif source == "live.json → funding":
            value = live.get("funding", 0)
        elif source == "live.json → whaleN":
            value = live.get("whaleN", 0)
        elif source == "bloc_privatise.json → volume_btc":
            value = oc.get("blocPrivatiseNbCachees", 0)
        elif "duree" in qid:
            value = 0  # TODO: calculer depuis l'historique
        elif "persistant" in qid:
            value = 0  # TODO: calculer depuis le timestamp
        
        if value is not None:
            if isinstance(seuil, (int, float)):
                results[qid] = {
                    "value": value,
                    "seuil": seuil,
                    "depasse": abs(value) > seuil if isinstance(value, (int, float)) else False
                }
            else:
                results[qid] = {"value": value, "seuil": seuil, "depasse": False}
        else:
            results[qid] = {"value": None, "seuil": seuil, "depasse": False}
    
    return results

# ─── Find matching interpretation ────────────────────────────

def find_interpretation(fiche, question_results):
    """Trouve l'interprétation qui correspond le mieux"""
    interpretations = fiche.get("interpretations", {})
    
    # Pour chaque interprétation, vérifier si les conditions sont remplies
    for key, interp in interpretations.items():
        condition = interp.get("condition", "")
        
        # Évaluation simplifiée des conditions
        if "duree < 5min" in condition:
            if question_results.get("duree", {}).get("value", 999) < 5:
                return interp
        elif "duree > 10min" in condition:
            if question_results.get("duree", {}).get("value", 0) > 10:
                return interp
        elif "prix < 2%" in condition:
            if abs(question_results.get("prix", {}).get("value", 0)) < 2:
                return interp
        elif "sdi > 0.3" in condition:
            if question_results.get("sdi", {}).get("value", 0) > 0.3:
                return interp
        elif "rbf > 0.6" in condition:
            if question_results.get("rbf", {}).get("value", 0) > 0.6:
                return interp
        elif "prix < -1%" in condition:
            if question_results.get("prix", {}).get("value", 0) < -1:
                return interp
        elif "prix > 1%" in condition:
            if question_results.get("prix", {}).get("value", 0) > 1:
                return interp
        elif "whales > 5" in condition:
            if question_results.get("whales", {}).get("value", 0) > 5:
                return interp
        elif "source == binance" in condition:
            # TODO: vérifier la source spécifique
            pass
        elif "source == deribit" in condition:
            pass
        elif "source == mempool" in condition:
            pass
    
    # Par défaut, retourner la première interprétation
    if interpretations:
        return list(interpretations.values())[0]
    
    return {"lecture": "Pas d'interprétation disponible", "niveau": "inconnu", "action": "Observer"}

# ─── Generate analysis ──────────────────────────────────────

def analyze_signal(signal, fiches, live):
    """Analyse un signal et retourne une recommandation"""
    fiche = match_fiche(signal, fiches)
    if not fiche:
        return {
            "signal": signal,
            "fiche": None,
            "interpretation": {"lecture": "Pas de fiche disponible", "niveau": "inconnu"},
            "action": "Observer"
        }
    
    # Évaluer les questions
    question_results = evaluate_questions(fiche, live)
    
    # Trouver l'interprétation
    interpretation = find_interpretation(fiche, question_results)
    
    return {
        "signal": signal,
        "fiche": fiche["type"],
        "questions": question_results,
        "interpretation": interpretation,
        "action": interpretation.get("action", "Observer"),
        "niveau": interpretation.get("niveau", "inconnu")
    }

# ─── Main ───────────────────────────────────────────────────

def run_analysis():
    """Exécute l'analyse complète"""
    print("[ANALYZER] Début d'analyse...")
    
    # 1. Charger les données
    fiches = load_fiches()
    live = load_live()
    signals = load_signals()
    
    print(f"  Fiches: {len(fiches)}")
    print(f"  Signaux: {len(signals)}")
    
    # 2. Analyser chaque signal récent (dernières 30 min)
    now = time.time()
    recent_signals = [s for s in signals if now - s.get("ts", 0) < 1800]
    
    analyses = []
    for signal in recent_signals:
        analysis = analyze_signal(signal, fiches, live)
        analyses.append(analysis)
        
        # Log
        niveau = analysis.get("niveau", "inconnu")
        emoji = {"neutre": "🔵", "surveiller": "🟡", "dangereux": "🔴", "critique": "🚨", "haussier": "🟢"}.get(niveau, "⚪")
        print(f"  {emoji} {signal.get('metric', '?')}: {analysis.get('interpretation', {}).get('lecture', '?')[:60]}")
    
    # 3. Assemblage du résultat
    result = {
        "timestamp": int(time.time()),
        "date": datetime.now(timezone.utc).isoformat(),
        "n_analyses": len(analyses),
        "analyses": analyses,
        "resume": generate_resume(analyses)
    }
    
    # 4. Annonce vocale si nécessaire
    annoncer_analyse(analyses)
    
    # 5. Sauvegarde
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"  Résultat: {OUTPUT}")
    return result

def generate_resume(analyses):
    """Génère un résumé des analyses"""
    if not analyses:
        return "Aucune analyse en cours"
    
    niveaux = [a.get("niveau", "inconnu") for a in analyses]
    
    if "critique" in niveaux:
        return "🚨 ALERTE CRITIQUE — des actions immédiates sont nécessaires"
    elif "dangereux" in niveaux:
        return "🔴 DANGER détecté — réduire les expositions"
    elif "surveiller" in niveaux:
        return "🟡 SURVEILLANCE — des signaux sont à observer"
    elif "haussier" in niveaux:
        return "🟢 SIGNAL HAUSSIER — le momentum est favorable"
    else:
        return "🔵 CALME — pas de signal alarmant"


def annoncer_analyse(analyses):
    """Annonce l'analyse à voix haute si niveau critique ou dangereux"""
    if not analyses:
        return
    
    # Vérifier si une analyse mérite une annonce vocale
    niveaux_requierts = ["critique", "dangereux", "haussier"]
    analyses_importantes = [a for a in analyses if a.get("niveau") in niveaux_requierts]
    
    if not analyses_importantes:
        return  # Pas d'annonce pour neutre/surveiller
    
    # Construire le message vocal
    messages = []
    for a in analyses_importantes[:2]:  # Max 2 analyses
        niveau = a.get("niveau", "")
        metric = a.get("signal", {}).get("metric", "")
        lecture = a.get("interpretation", {}).get("lecture", "")
        action = a.get("action", "")
        
        emoji = {"critique": "Alerte", "dangereux": "Attention", "haussier": "Signal positif"}.get(niveau, "Info")
        messages.append(f"{emoji}. {metric}. {lecture[:80]}. {action}")
    
    msg_final = " ".join(messages)
    
    # Lancer l'alerte vocale (une seule fois, pas en boucle)
    try:
        import subprocess
        from datetime import datetime, timezone
        ts = int(time.time())
        alerte_script = Path(__file__).parent / "alerte_vocale.py"
        subprocess.Popen(
            ["python3", str(alerte_script), "--message", msg_final, "--id", f"cortana_{ts}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        print(f"  🔊 Alerte vocale lancée: {msg_final[:60]}...")
    except Exception as e:
        print(f"  ⚠️ Erreur alerte vocale: {e}")

if __name__ == "__main__":
    run_analysis()
