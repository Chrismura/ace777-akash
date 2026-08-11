#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genere par Google Gemini via hub (loi 1quinquies : Ada specifie, le hub ecrit) — 09/08 conditions famille
# Fichier : verif_conditions.py
import os
sys = __import__('sys')
json = __import__('json')
re = __import__('re')
subprocess = __import__('subprocess')
hashlib = __import__('hashlib')
datetime = __import__('datetime')
time = __import__('time')
pathlib = __import__('pathlib')

MAISON = pathlib.Path("/Users/christophe/ace777-test-day1")
INDEX_MAISON = MAISON / "Index_Maison"
WORM_LOG = INDEX_MAISON / "WORM_JOURNAL.log"
FICHIERS_CRITIQUES = INDEX_MAISON / "FICHIERS_CRITIQUES.txt"
PAUSE_FILE = INDEX_MAISON / "PAUSE_ORCHESTRATRICE"
PROBATOIRE_FILE = INDEX_MAISON / "PROBATOIRE.json"

def ecrire_worm(niveau, categorie, message):
    ts = datetime.datetime.now().isoformat()
    msg_propre = str(message).replace("\n", " ").replace("|", "/")
    ligne = f"| {ts} | {niveau} | {categorie} | {msg_propre} |\n"
    # macOS : append direct sous flag uappnd (corrige checker 09/08).
    with open(WORM_LOG, "a", encoding="utf-8") as f:
        f.write(ligne)

def verifier_conditions():
    c1_etat = "NON APPLIQUEE"
    c1_preuve = "Repertoire Maison absent"
    if MAISON.exists():
        c1_etat = "APPLIQUEE"
        c1_preuve = f"Repertoire {MAISON} present"

    c2_etat = "NON APPLIQUEE"
    c2_preuve = "WORM absent"
    if WORM_LOG.exists():
        res = subprocess.run(["ls", "-lO", str(WORM_LOG)], capture_output=True, text=True)
        if "uappnd" in res.stdout:
            c2_etat = "APPLIQUEE"
            c2_preuve = "WORM present avec flag uappnd actif"
        else:
            c2_etat = "PARTIELLE"
            c2_preuve = "WORM present mais flag uappnd inactif"

    c3_etat = "NON APPLIQUEE"
    c3_preuve = "Fichiers critiques absents"
    if FICHIERS_CRITIQUES.exists():
        with open(FICHIERS_CRITIQUES, "r", encoding="utf-8") as f:
            lignes = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]
        existants = sum(1 for l in lignes if pathlib.Path(l).exists())
        if existants == len(lignes) and len(lignes) > 0:
            c3_etat = "APPLIQUEE"
            c3_preuve = f"{existants}/{len(lignes)} fichiers critiques presents"
        elif existants > 0:
            c3_etat = "PARTIELLE"
            c3_preuve = f"{existants}/{len(lignes)} fichiers critiques presents"
        else:
            c3_etat = "NON APPLIQUEE"
            c3_preuve = "Aucun fichier critique trouve"

    c4_etat = "NON APPLIQUEE"
    c4_preuve = "HUB non joignable"
    try:
        import urllib.request
        req = urllib.request.urlopen("http://127.0.0.1:11435/health", timeout=3)
        if req.status < 500:
            c4_etat = "APPLIQUEE"
            c4_preuve = "HUB /health repond"
    except Exception:
        c4_etat = "NON APPLIQUEE"
        c4_preuve = "Echec connexion HUB /health"

    c5_etat = "APPLIQUEE"
    c5_preuve = "Aucune sanction active"
    if PAUSE_FILE.exists():
        c5_etat = "NON APPLIQUEE"
        c5_preuve = "Fichier PAUSE_ORCHESTRATRICE present (sanction active)"

    c6_etat = "NON APPLIQUEE"
    c6_preuve = "Mode probatoire non configure"
    if PROBATOIRE_FILE.exists():
        c6_etat = "APPLIQUEE"
        c6_preuve = "Fichier PROBATOIRE.json actif"

    print("+-------------+---------------------+------------------------------------------+")
    print("| CONDITION   | ETAT                | PREUVE                                   |")
    print("+-------------+---------------------+------------------------------------------+")
    print(f"| C1 (Maison) | {c1_etat:<19} | {c1_preuve:<40} |")
    print(f"| C2 (WORM)   | {c2_etat:<19} | {c2_preuve:<40} |")
    print(f"| C3 (Crit.)  | {c3_etat:<19} | {c3_preuve:<40} |")
    print(f"| C4 (HUB)    | {c4_etat:<19} | {c4_preuve:<40} |")
    print(f"| C5 (Sanct.) | {c5_etat:<19} | {c5_preuve:<40} |")
    print(f"| C6 (Prob.)  | {c6_etat:<19} | {c6_preuve:<40} |")
    print("+-------------+---------------------+------------------------------------------+")

def compter_violations():
    if not WORM_LOG.exists():
        return 0
    maintenant = datetime.datetime.now()
    limite = maintenant - datetime.timedelta(days=7)
    count = 0
    with open(WORM_LOG, "r", encoding="utf-8") as f:
        for ligne in f:
            if "VIOLATION" in ligne:
                parties = ligne.split("|")
                if len(parties) > 1:
                    ts_str = parties[1].strip()
                    try:
                        ts = datetime.datetime.fromisoformat(ts_str)
                        if ts >= limite:
                            count += 1
                    except ValueError:
                        pass
    return count

def verifier_sanctions():
    v_count = compter_violations()
    print(f"Nombre de violations dans les 7 derniers jours : {v_count}")
    if v_count >= 3:
        if not PAUSE_FILE.exists():
            with open(PAUSE_FILE, "w", encoding="utf-8") as f:
                f.write(f"PAUSE ORCHESTRATRICE - {datetime.datetime.now().isoformat()} - Violations: {v_count}\n")
            ecrire_worm("ALERTE", "SANCTION", f"Sanction appliquee : {v_count} violations detectees sur 7 jours.")
            print("SANCTION APPLIQUEE : Fichier PAUSE_ORCHESTRATRICE cree.")
        else:
            print("Sanction requise mais PAUSE_ORCHESTRATRICE deja existant.")
    else:
        print("Aucune sanction necessaire.")

def gerer_probatoire():
    if not PROBATOIRE_FILE.exists():
        print("Fichier PROBATOIRE.json absent.")
        return
    try:
        with open(PROBATOIRE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        debut_str = data.get("debut")
        actions = data.get("actions_autonomes", 0)
        debut = datetime.datetime.strptime(debut_str, "%Y-%m-%d")
        jours_ecoules = (datetime.datetime.now() - debut).days
        if jours_ecoules < 0:
            jours_ecoules = 0
        
        if jours_ecoules < 7:
            quota = 1
            periode = "7 premiers jours"
        else:
            quota = 3
            periode = "Apres les 7 premiers jours"
            
        print(f"Mode probatoire - Debut : {debut_str}")
        print(f"Jours ecoules : {jours_ecoules} ({periode})")
        print(f"Actions autonomes enregistrees : {actions}")
        print(f"Quota autorise : max {quota} action(s) par jour")
    except Exception as e:
        print(f"Erreur lecture PROBATOIRE.json : {e}")

def reset_pause():
    if PAUSE_FILE.exists():
        PAUSE_FILE.unlink()
        ecrire_worm("INFO", "SANCTION", "Suppression de PAUSE_ORCHESTRATRICE demandee par Christophe.")
        print("Fichier PAUSE_ORCHESTRATRICE supprime avec succes.")
    else:
        print("Aucun fichier PAUSE_ORCHESTRATRICE trouve.")

def main():
    args = sys.argv[1:]
    if "--reset-pause" in args:
        reset_pause()
    elif "sanction" in args:
        verifier_sanctions()
    else:
        verifier_conditions()
        print("")
        verifier_sanctions()
        print("")
        gerer_probatoire()

if __name__ == "__main__":
    main()

