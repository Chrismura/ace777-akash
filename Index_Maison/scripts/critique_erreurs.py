#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du module : critique_erreurs.py
Projet       : ACE777 — la 6ᵉ partie du cycle (« Fine-tune ») : LA MÉMOIRE DES ÉCHECS BRANCHÉE
Rôle         : Deux contrôles, aucun jugement, aucune invention :
   (A) BRANCHÉ (règle #15) — le registre `Index_Maison/REGISTRE_ECHECS_ET_ERREURS.md` n'existe
       que s'il est CONSULTÉ : on vérifie qu'il est cité par les points d'entrée qui font
       proposer des gardes (règles d'or, mémoire, règles d'agent). Non cité = un registre mort.
   (B) RÉCIDIVE — on relit les lignes de `MEMOIRE_COLLAB.md` POSTÉRIEURES à la dernière mise à
       jour du registre et on cherche les signatures des 9 classes d'erreur connues. Une
       récidive AVANT la correction est normal : c'est une récidive APRÈS qui est une faute.
Sortie       : `Index_Maison/CRITIQUE_ERREURS_DERNIER.md` + `.json` ; exit 1 si non branché
               OU si une classe récidive. Un registre non branché n'existe pas (R15).
AUCUN seuil inventé : les signatures sont écrites dans le registre lui-même (source unique).
0 €, lecture seule, aucun ordre.
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # Index_Maison
ROOT = os.path.dirname(BASE)
REGISTRE = os.path.join(BASE, "REGISTRE_ECHECS_ET_ERREURS.md")
MEMOIRE = os.path.join(BASE, "MEMOIRE_COLLAB.md")
SORTIE_MD = os.path.join(BASE, "CRITIQUE_ERREURS_DERNIER.md")
SORTIE_JSON = os.path.join(BASE, "CRITIQUE_ERREURS_DERNIER.json")

# Points d'entrée où le registre DOIT être cité pour être « branché » (R15).
# Chacun est un endroit réel d'où part une décision/proposition.
POINTS_ENTREE = {
    os.path.join(BASE, "REGLE_D_OR.md"): "les règles d'or (R17 renvoie au registre)",
    os.path.join(ROOT, ".cursorrules"): "les règles d'agent (Cursor) — là où on propose une garde",
}

# ── LES DEUX DÉTECTEURS DE RÉCIDIVE (et pourquoi il en faut deux) ─────────────────
#
# (1) MÉCANIQUE — `inventaire_seuils_fixes.py` (appelé par la discipline quotidienne) :
#     à chaque passage, toute clé de config qui DÉCIDE sans être mesurée ni rangée est
#     nommée. Un seuil « inventé » réapparaît donc TOUJOURS — impossible de le cacher
#     dans de la prose. C'est le détecteur fort.
#
# (2) PROSE — celui-ci : il relit la mémoire. Un texte qui PARLE d'une erreur n'est
#     pas une récidive (« on ne met pas de seuil fixe » cite la règle, il ne la viole
#     pas). Pour ne pas crier sur une simple mention — une alarme qui sonne pour un
#     comportement voulu tue la confiance dans l'alarme (R14, notre propre leçon) —
#     une récidive ne compte QUE si la ligne est un AVEU : elle dit qu'on l'a refaite.
#
# ⚠️ LIMITE DÉCLARÉE (E8) : un aveu tu est invisible à ce détecteur. Il ne remplace
#    pas le détecteur mécanique (1), il le complète. Les deux sont branchés.
# L'AVEU est nécessairement à la PREMIÈRE PERSONNE (ou « on », = nous) : c'est quelqu'un qui
# reconnaît avoir refait. Un texte qui PARLE de la récidive (ou qui cite « silencieux »,
# « seuil fixe »…) n'est pas un aveu — c'est la leçon. Le 22/09, ma propre ligne de mémoire
# citait le mot « RÉCIDIVE » et « SILENCIEUX » : sans ce durcissement, le détecteur criait au
# loup sur la ligne qui décrit la correction. Faux positif = alarme morte (R14).
AVEU = re.compile(
    r"j'ai (encore|de nouveau|recommenc|refait|recommis)"
    r"|on a (encore|de nouveau|recommenc|refait)"
    r"|nous avons (encore|de nouveau)"
    r"|me voilà encore|on y retourne"
    r"|même erreur (de|que)"
    r"|encore (la même|le même|une fois)",
    re.I)

# Signatures des classes d'erreur (E1..E9). Le registre en est la source ; ici, les motifs
# qui, UNIS À UN AVEU, trahissent une récidive. Étroits par construction.
SIGNATURES = {
    "E1_inventer_un_seuil": r"seuil fixe|timing fixe|en heures fixes|invent(é|e) un seuil|choisi au lieu",
    "E2_sans_verifier_a_la_source": r"sans vérifier à la source|à tort|faux positif retiré",
    "E3_mauvaise_source_instrument": r"écrite en dur|périmée|pointe la mauvaise source|lignes dupliquées",
    "E4_bloquer_au_lieu_de_mesurer": r"bloqu(é|ée|age) à vie|interdit .{0,20} à vie",
    "E5_deux_verites": r"deux comportements|non persisté|doublon de clé|double comptage",
    "E6_silence": r"muet|invisible \d+ ?h|silencieux",
    "E7_symptome_pas_cause": r"symptôme",
    "E8_limites_cachees": r"limite non (écrite|déclarée)",
    "E9_empiler_le_meme_jour": r"retiré le jour même|posé puis retiré|empil(é|er)",
}


def lire_ts_registre():
    """La date de dernière mise à jour du registre = la borne : avant = leçon, après = récidive."""
    try:
        txt = open(REGISTRE, encoding="utf-8").read()
    except Exception:
        return None, ""
    m = re.search(r"2026-\d{2}-\d{2}T\d{2}:\d{2}", txt)
    return (m.group(0) if m else None), txt


def main():
    ts_ref, txt_registre = lire_ts_registre()
    n_classes = len(re.findall(r"^\|\s*\*\*E\d", txt_registre, re.M))
    if not os.path.exists(REGISTRE):
        print("❌ registre absent — la 6ᵉ partie du cycle n'existe pas")
        return 1

    # (A) branché ?
    non_branche = []
    for chemin, raison in POINTS_ENTREE.items():
        try:
            contenu = open(chemin, encoding="utf-8", errors="ignore").read()
        except Exception:
            non_branche.append((chemin, raison + " [fichier absent]"))
            continue
        if "REGISTRE_ECHECS_ET_ERREURS" not in contenu:
            non_branche.append((chemin, raison))

    # (B) récidives après la dernière mise à jour du registre
    reprises = {}
    if ts_ref and os.path.exists(MEMOIRE):
        for ligne in open(MEMOIRE, encoding="utf-8", errors="ignore"):
            m = re.match(r"\|\s*(2026-\d{2}-\d{2}T\d{2}:\d{2})Z\s*\|", ligne)
            if not m or m.group(1) <= ts_ref:
                continue          # avant/égal à la correction : c'est la leçon, pas la récidive
            if not AVEU.search(ligne):
                continue          # une simple mention n'est pas une récidive (cf. limite déclarée)
            for classe, motif in SIGNATURES.items():
                if re.search(motif, ligne, re.I):
                    reprises.setdefault(classe, []).append(m.group(1))

    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    lignes = [
        "# Critique des erreurs récurrentes — le registre est-il BRANCHÉ, et se répète-t-on ?",
        "",
        f"> {maintenant} · `critique_erreurs.py` · référence (dernière mise à jour du registre) : "
        f"**{ts_ref or 'inconnue'}** · {n_classes} classes enregistrées.",
        "",
        "## (A) Le registre est-il consulté (R15 : un registre non lu n'existe pas) ?",
        "",
    ]
    if non_branche:
        for chemin, raison in non_branche:
            lignes.append(f"- ❌ **NON BRANCHÉ** — `{raison}` ne cite pas le registre → `{chemin}`")
    else:
        lignes.append("- ✅ cité par tous les points d'entrée contrôlés "
                      f"({len(POINTS_ENTREE)} points).")
    lignes += ["", "## (B) Récidives APRÈS la correction", ""]
    if reprises:
        for classe, ts in reprises.items():
            lignes.append(f"- 🔴 **{classe}** — {len(ts)} récidive(s) : {', '.join(ts)}")
    else:
        lignes.append("- ✅ aucune récidive depuis la dernière mise à jour du registre.")
    lignes += ["", "## Lecture", "",
               "Une récidive signalée ici n'est pas un reproche : c'est la classe d'erreur qui "
               "revient **malgré** la garde. C'est le signal que la garde est trop faible, pas "
               "que la personne a mal travaillé. Le registre est la seule mémoire de ces échecs.",
               "",
               "## Deux détecteurs, deux rôles (déclaré)", "",
               "- **Prose (ici)** : ne compte qu'un **AVEU à la première personne** (« j'ai encore… », "
               "« on a de nouveau… », « encore la même »). **Parler d'une erreur n'est pas la "
               "commettre** : citer « récidive » ou « silencieux » n'allume rien.",
               "- **Mécanique** (`inventaire_seuils_fixes.py`, branché sur la discipline "
               "quotidienne) : toute clé de config qui décide **sans être mesurée ni rangée** "
               "est nommée chaque passage. Un seuil inventé ne peut pas se cacher dans du texte.",
               "- ⚠️ **Limite déclarée** : un aveu tu échappe au détecteur de prose. C'est le "
               "détecteur mécanique qui ferme ce trou — pas la confiance."]

    open(SORTIE_MD, "w", encoding="utf-8").write("\n".join(lignes) + "\n")
    json.dump({"ts": maintenant, "ts_registre": ts_ref, "classes": n_classes,
               "non_branche": [c for c, _ in non_branche],
               "recidives": {k: len(v) for k, v in reprises.items()}},
              open(SORTIE_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"CRITIQUE ERREURS — registre : {n_classes} classes · non branché : {len(non_branche)} · "
          f"récidives : {len(reprises)}")
    for classe, ts in reprises.items():
        print(f"  🔴 récidive {classe} ({len(ts)})")
    for c, r in non_branche:
        print(f"  ❌ non branché : {r}")
    return 1 if (non_branche or reprises) else 0


if __name__ == "__main__":
    sys.exit(main())
