import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.request
import urllib.error
from typing import List, Dict, Any, Optional

# Chemins de base fixes selon le contexte
BASE_DIR = Path("/Users/christophe/test-freebuff")
VAULT_DIR = Path("/Users/christophe/Documents/Obsidian_ACE777")
SIGNETS_DIR = VAULT_DIR / "Signets_X/2026-08"
EVAL_DIR = VAULT_DIR / "Evaluations"
FICHE_EVAL_PATH = EVAL_DIR / "FICHE_EVALUATION_SIGNETS.md"
TABLEAU_PATH = EVAL_DIR / "TRI_SIGNETS_2026-08.md"
ATELIER_LIENS_SCRIPT = Path("/Users/christophe/ace777-test-day1/Index_Maison/scripts/atelier_liens.py")

HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"
TIMEOUT_SECONDES = 300


def nettoyer_frontmatter(contenu: str) -> str:
    """Retire le frontmatter YAML d'une note Markdown s'il existe."""
    if contenu.startswith("---"):
        parties = contenu.split("---", 2)
        if len(parties) >= 3:
            return parties[2].strip()
    return contenu.strip()


def charger_fichier_texte(chemin: Path) -> str:
    """Charge un fichier texte en UTF-8 avec gestion des erreurs de décodage."""
    if not chemin.exists():
        return ""
    try:
        with open(chemin, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception as e:
        print(f"[Avertissement] Impossible de lire {chemin} : {e}")
        return ""


def appeler_hub(task: str, messages: List[Dict[str, str]], max_tokens: int = 2000) -> Optional[Dict[str, Any]]:
    """Envoie une requête HTTP POST au Hub local avec gestion robuste du timeout."""
    payload = {
        "task": task,
        "messages": messages,
        "max_tokens": max_tokens
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        HUB_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDES) as reponse:
            reponse_texte = reponse.read().decode("utf-8", errors="replace")
            resultat_json = json.loads(reponse_texte)
            
            # Extraction standardisée selon les formats possibles du hub
            if "choices" in resultat_json and len(resultat_json["choices"]) > 0:
                contenu_reponse = resultat_json["choices"][0]["message"]["content"]
            elif "content" in resultat_json:
                contenu_reponse = resultat_json["content"]
            else:
                contenu_reponse = resultat_json

            if isinstance(contenu_reponse, str):
                # Nettoyage éventuel des blocs de code Markdown autour du JSON
                nettoye = re.sub(r"^```json\s*", "", contenu_reponse.strip())
                nettoye = re.sub(r"\s*```$", "", nettoye)
                return json.loads(nettoye)
            return contenu_reponse
            
    except urllib.error.URLError as e:
        print(f"[Erreur Hub] Échec de la requête réseau (task: {task}) : {e.reason}")
        return None
    except json.JSONDecodeError as e:
        print(f"[Erreur JSON] La réponse du Hub n'est pas un JSON valide (task: {task}) : {e}")
        return None
    except Exception as e:
        print(f"[Erreur Inattendue] (task: {task}) : {e}")
        return None


def verifier_json_valide(chemin: Path) -> bool:
    """Vérifie si un fichier existe et contient un JSON valide."""
    if not chemin.exists():
        return False
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            json.load(f)
        return True
    except Exception:
        return False


def traiter_lot(n_lot: int, dry_run: bool) -> bool:
    """Exécute le pipeline complet pour un lot spécifique."""
    prefixe_lot = f"[lot {n_lot}]"
    liste_path = BASE_DIR / f"LOT{n_lot}_LISTE.json"
    
    if not liste_path.exists():
        print(f"{prefixe_lot} Fichier liste introuvable ({liste_path}). Skip.")
        return False
        
    try:
        with open(liste_path, "r", encoding="utf-8") as f:
            noms_fichiers = json.load(f)
    except Exception as e:
        print(f"{prefixe_lot} Erreur de lecture du fichier liste : {e}. Skip.")
        return False

    if not isinstance(noms_fichiers, list):
        print(f"{prefixe_lot} Le contenu de la liste n'est pas une liste JSON valide. Skip.")
        return False

    # Préparation du contenu des posts
    posts_contenus = []
    for idx, nom_fichier in enumerate(noms_fichiers, 1):
        # S'assurer du bon nom de fichier .md
        nom_nettoye = nom_fichier if nom_fichier.endswith(".md") else f"{nom_fichier}.md"
        chemin_post = SIGNETS_DIR / nom_nettoye
        texte_brut = charger_fichier_texte(chemin_post)
        texte_propre = nettoyer_frontmatter(texte_brut)
        # Tronquer à ~1000 caractères max par post
        texte_tronque = texte_propre[:1000]
        
        posts_contenus.append({
            "n": idx,
            "nom_fichier": nom_nettoye,
            "contenu": texte_tronque
        })

    fiche_calibration = charger_fichier_texte(FICHE_EVAL_PATH)

    # Définition des chemins des fichiers de votes
    gemini_json_path = BASE_DIR / f"TRI_LOT{n_lot}_GEMINI.json"
    nim_json_path = BASE_DIR / f"TRI_LOT{n_lot}_NIM.json"
    juge_json_path = BASE_DIR / f"TRI_LOT{n_lot}_JUGE.json"

    if dry_run:
        print(f"{prefixe_lot} [DRY-RUN] {len(posts_contenus)} posts chargés.")
        print(f"{prefixe_lot} [DRY-RUN] Appels prévus : Gemini (audit.protocol), NIM (analyse.profonde), Juge (signets.juge).")
        print(f"{prefixe_lot} [DRY-RUN] Fichiers cibles : {gemini_json_path.name}, {nim_json_path.name}, {juge_json_path.name}")
        return True

    # Étape 2 : MAKERS (Gemini et NIM)
    prompt_posts_str = json.dumps(posts_contenus, ensure_ascii=False, indent=2)
    
    # 2.1 Gemini
    if verifier_json_valide(gemini_json_path):
        pass  # Idempotent : déjà présent et valide
    else:
        messages_gemini = [
            {"role": "system", "content": f"Fiche de calibration:\n{fiche_calibration}"},
            {"role": "user", "content": f"Analyse ces posts selon la grille (PERTINENT_INTEGRER, PERTINENT_VERIFIER, PERTINENT_IDEE, BRUIT, DOUBLON, DANGER). Réponds STRICTEMENT en JSON formaté ainsi: {{\"posts\":[{{\"n\":1,\"verdict\":\"...\",\"note\":\"...\",\"confiance\":0.85,\"action_concrete\":\"...\"}}]}}.\n\nPosts:\n{prompt_posts_str}"}
        ]
        res_gemini = appeler_hub("audit.protocol", messages_gemini)
        if res_gemini is not None:
            with open(gemini_json_path, "w", encoding="utf-8") as f:
                json.dump(res_gemini, f, ensure_ascii=False, indent=2)

    # 2.2 NIM
    if verifier_json_valide(nim_json_path):
        pass
    else:
        messages_nim = [
            {"role": "system", "content": f"Fiche de calibration:\n{fiche_calibration}"},
            {"role": "user", "content": f"Analyse ces posts selon la grille (PERTINENT_INTEGRER, PERTINENT_VERIFIER, PERTINENT_IDEE, BRUIT, DOUBLON, DANGER). Réponds STRICTEMENT en JSON formaté ainsi: {{\"posts\":[{{\"n\":1,\"verdict\":\"...\",\"note\":\"...\",\"confiance\":0.85,\"action_concrete\":\"...\"}}]}}.\n\nPosts:\n{prompt_posts_str}"}
        ]
        res_nim = appeler_hub("analyse.profonde", messages_nim)
        if res_nim is not None:
            with open(nim_json_path, "w", encoding="utf-8") as f:
                json.dump(res_nim, f, ensure_ascii=False, indent=2)

    # Étape 3 : JUGE (Utilise uniquement le contenu réel des posts)
    if verifier_json_valide(juge_json_path):
        pass
    else:
        messages_juge = [
            {"role": "system", "content": "Tu es le juge impartial des signets. Attribue une lettre de verdict parmi: I (Intégrer), V (Vérifier), D (Idée), B (Bruit), K (Doublon), X (Danger)."},
            {"role": "user", "content": f"Évalue ces posts et donne ton verdict en lettres (I, V, D, B, K, X). Réponds STRICTEMENT en JSON formaté ainsi: {{\"posts\":[{{\"n\":1,\"verdict\":\"I\",\"note\":\"...\",\"confiance\":0.9,\"action_concrete\":\"...\"}}]}}.\n\nPosts:\n{prompt_posts_str}"}
        ]
        res_juge = appeler_hub("signets.juge", messages_juge)
        if res_juge is not None:
            with open(juge_json_path, "w", encoding="utf-8") as f:
                json.dump(res_juge, f, ensure_ascii=False, indent=2)

    # Vérification que tous les votes nécessaires sont dispos pour la suite
    if not (verifier_json_valide(gemini_json_path) and verifier_json_valide(nim_json_path) and verifier_json_valide(juge_json_path)):
        print(f"{prefixe_lot} Erreur : Certains fichiers de votes sont absents ou invalides après les appels.")
        return False

    # Étape 6 : CHECK ADA (Agrégation et résumé console)
    votes_gemini = {}
    votes_nim = {}
    votes_juge = {}

    try:
        with open(gemini_json_path, "r", encoding="utf-8") as f:
            data_g = json.load(f)
            for p in data_g.get("posts", []):
                votes_gemini[p.get("n")] = p
        with open(nim_json_path, "r", encoding="utf-8") as f:
            data_n = json.load(f)
            for p in data_n.get("posts", []):
                votes_nim[p.get("n")] = p
        with open(juge_json_path, "r", encoding="utf-8") as f:
            data_j = json.load(f)
            for p in data_j.get("posts", []):
                votes_juge[p.get("n")] = p
    except Exception as e:
        print(f"{prefixe_lot} Erreur lors du chargement des votes pour l'agrégation Ada : {e}")
        return False

    # Normalisation basique des verdicts du Juge (lettres vers mots-clés ou conservation)
    correspondance_lettres = {
        "I": "PERTINENT_INTEGRER",
        "V": "PERTINENT_VERIFIER",
        "D": "PERTINENT_IDEE",
        "B": "BRUIT",
        "K": "DOUBLON",
        "X": "DANGER"
    }

    flammes_count = 0
    divergences_count = 0
    lignes_tableau = []

    for post_info in posts_contenus:
        num = post_info["n"]
        v_g = votes_gemini.get(num, {}).get("verdict", "INCONNU")
        v_n = votes_nim.get(num, {}).get("verdict", "INCONNU")
        
        brut_juge = votes_juge.get(num, {}).get("verdict", "INCONNU")
        v_j = correspondance_lettres.get(brut_juge, brut_juge)

        note_juge = votes_juge.get(num, {}).get("note", "Pas de note")
        
        # Détection Flammes (accord) vs Divergences
        # Accord simple si Gemini et NIM concordent
        if v_g == v_n:
            flammes_count += 1
        else:
            divergences_count += 1

        # Préparation ligne tableau : | Date | Auteur | Sujet | Verdict | Note |
        # Utilisation de métadonnées par défaut ou extraites du post si possible
        date_str = "2026-08-01"
        auteur_str = "Inconnu"
        sujet_str = post_info["nom_fichier"].replace(".md", "")
        verdict_final = v_j if v_j != "INCONNU" else v_g
        note_finale = note_juge.replace("|", "-") # Éviter de casser le markdown

        ligne_md = f"| {date_str} | {auteur_str} | {sujet_str} | {verdict_final} | {note_finale} |"
        lignes_tableau.append(ligne_md)

    print(f"[Ada - lot {n_lot}] Agrégation : {flammes_count} flammes (accords), {divergences_count} divergences.")

    # Étape 7 : TABLEAU (Append au fichier Markdown existant)
    try:
        TABLEAU_PATH.parent.mkdir(parents=True, exist_ok=True)
        mode_ouverture = "a" if TABLEAU_PATH.exists() else "w"
        with open(TABLEAU_PATH, mode_ouverture, encoding="utf-8") as f:
            if mode_ouverture == "w":
                f.write("# Tableau de Synthèse du Tri des Signets\n\n")
                f.write("| Date | Auteur | Sujet | Verdict | Note |\n")
                f.write("|---|---|---|---|---|\n")
            for ligne in lignes_tableau:
                f.write(ligne + "\n")
    except Exception as e:
        print(f"{prefixe_lot} Erreur lors de l'écriture du tableau final : {e}")
        return False

    print(f"{prefixe_lot} makers OK · juge OK · tableau OK")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Usine de tri des signets - Pipeline automatisé")
    parser.add_argument("--lot", type=int, help="Traiter un lot unique")
    parser.add_argument("--lots", type=int, nargs="+", help="Traiter plusieurs lots")
    parser.add_argument("--dry-run", action="store_true", help="Affiche les étapes sans exécuter les appels LLM")
    
    args = parser.parse_args()

    lots_a_traiter = []
    if args.lot is not None:
        lots_a_traiter.append(args.lot)
    if args.lots is not None:
        lots_a_traiter.extend(args.lots)

    if not lots_a_traiter:
        print("Aucun lot spécifié. Utilisez --lot N ou --lots N1 N2 ...")
        sys.exit(1)

    # Suppression des doublons potentiels tout en conservant l'ordre
    lots_uniques = []
    for l in lots_a_traiter:
        if l not in lots_uniques:
            lots_uniques.append(l)

    # Exécution du pipeline par lot (Time-out robuste intégré, continue en cas d'erreur)
    for lot_num in lots_uniques:
        try:
            traiter_lot(lot_num, args.dry_run)
        except Exception as e:
            print(f"[lot {lot_num}] Erreur critique inopinée : {e}. Continuation des autres lots.")

    # Étape 8 : À LA FIN de tous les lots, lancer l'atelier de liens
    if not args.dry_run and ATELIER_LIENS_SCRIPT.exists():
        print("[Atelier] Lancement de l'atelier de liens...")
        try:
            subprocess.run(
                ["python3", str(ATELIER_LIENS_SCRIPT), "--limit", "80"],
                check=True
            )
            print("[Atelier] Atelier de liens exécuté avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"[Atelier] Erreur lors de l'exécution de l'atelier de liens : {e}")
        except Exception as e:
            print(f"[Atelier] Erreur inattendue avec le sous-processus : {e}")
    elif args.dry_run:
        print("[DRY-RUN] Lancement simulé de l'atelier de liens.")
    else:
        print(f"[Atelier] Script atelier_liens.py introuvable à l'emplacement : {ATELIER_LIENS_SCRIPT}")


if __name__ == "__main__":
    main()
