#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DÉCLARER + RE-SCELLER (chantier 23/09/2026) — « un écart n'est pas muet »
=========================================================================
RÈGLE MAISON R5/R13 : un scellé ne s'écrase JAMAIS sans le déclarer. Deux fichiers
scellés ont été modifiés aujourd'hui, donc la veilleuse et le drill crient (à raison) :
  « md5 différent : hulk-mexc/scripts/paper_diprip.py »
  « md5 différent : hulk-mexc/scripts/chiffrage_entree_sortie_replay.py »

Cet outil fait l'acte prévu par la maison : backup, mise à jour du md5, et — surtout —
une entrée de déclaration `_rescel_20260923` qui dit CE QUI a changé et POURQUOI, pour
que le re-scellement ne soit pas un silencieux « on écrase le contrôle ».
Lecture seule sur le moteur ; n'écrit que le registre (avec backup horodaté).
"""
import hashlib
import json
import os
import shutil
import time
from pathlib import Path

RACINE = Path.home() / "ace777-test-day1"
REG = RACINE / "Index_Maison" / "strategie" / "REGISTRE_SYNAPSES.json"

DECLARATIONS = {
    "hulk-mexc/scripts/paper_diprip.py": (
        "REFUS PARLANT 23/09 (GO Christophe « pourquoi RIZE a perdu le pump ? ») : le REFUS "
        "écrit désormais LE CHIFFRE QUI DÉCIDE — `ATTENTE:IMPULSE_WAIT dd6=2.50 seuil=21.70 "
        "manque=19.20pt m6=12.5` (l'achat le faisait déjà, le refus était muet). PORTÉE : 1 "
        "ligne de log + 30 lignes de commentaire ; `_detail` est calculé dans un try/except "
        "(un log ne casse jamais une boucle) ; le préfixe `ATTENTE:<régime>` reste INTACT "
        "(les instruments lisent `reason.split(':')[0]`). AUCUN seuil, AUCUNE porte, AUCUN "
        "ordre, AUCUNE décision modifiée. Effet immédiat MESURÉ : le seuil réel de RIZE est "
        "21,70 % (= 0,85 × 0,50 × cadence 51,1 %), pas les 5-12,75 % que mes documents "
        "annonçaient — l'erreur était dans MES instruments (classe F), le moteur avait "
        "raison. Vérifié : pnl 42,1679 $ / 9 positions / 175 trades identiques avant/après, "
        "0 traceback, veilleuse STABLE. Réversible en 1 ligne."
    ),
    "Index_Maison/scripts/gen_cockpit_vol.py": (
        "GARDIEN VISIBLE 23/09 (GO 1 — « un verdict qu'il faut aller chercher n'existe pas ») : "
        "la page « vol » gagne UN gardien — « Garde-fou seuil moteur » — qui lit "
        "`thermo/seuil_moteur.json` (état écrit par hulk-mexc/scripts/verif_seuil_moteur.py, "
        "appelé par git_push_auto.sh). Il dit COMBIEN de refus chiffrés ont été CONFRONTÉS au "
        "seuil recalculé, signale tout instrument qui recalcule un seuil sans la cadence, et "
        "refuse d'être un feu vert si l'état est figé (>8 h) ou si le refus parlant n'a pas "
        "encore produit 5 lignes (EN ATTENTE, normal < 1 h après une relance). LECTURE SEULE, "
        "ajout seul : aucun autre gardien touché, aucune donnée modifiée."
    ),
    # L'outil se déclare LUI-MÊME : le détecteur de la veilleuse l'a attrapé (modifié après
    # son premier scellement). C'est la preuve que le contrôle fonctionne, y compris sur son
    # propre outillage.
    "Index_Maison/scripts/declarer_rescel_20260923.py": (
        "Outil d'acte du 23/09 : déclare + re-scelle les fichiers modifiés (backup horodaté + "
        "entrée `_rescel_20260923` qui dit QUOI et POURQUOI). Modifié une 2e fois le même jour "
        "pour traiter les 3 fichiers touchés APRÈS leur scellement (batterie d'autotest, "
        "`--serie` de la sonde, `REPLAY_SLIP_BPS` du replay) — la veilleuse avait crié trois "
        "fois « INTRUSION : modification non déclarée », à juste titre. Leçon de processus : "
        "ON SCELLE APRÈS LA DERNIÈRE MODIFICATION."
    ),
    # --- 2e vague (même jour, après réponses de la FAMILLE) ---------------------------------
    # Leçon de processus, payée comptant : on scelle APRÈS la dernière modification. J'ai
    # scellé ces trois fichiers puis je les ai encore modifiés → la veilleuse a crié
    # (à juste titre) « INTRUSION : modification non déclarée » trois fois de suite.
    "hulk-mexc/scripts/verif_seuil_moteur.py": (
        "2e vague 23/09 (réponses de la FAMILLE : « aucune preuve de son taux de faux négatifs ») "
        "— l'autotest n'injecte plus UNE erreur mais CINQ troncatures différentes évaluées sur "
        "TROIS régimes (cadence dominante / plancher / m6 dominant) : 7/7 erreurs DISCRIMINANTES "
        "détectées (100 %), et un cas non discriminant au point testé cesse d'être compté comme "
        "un échec. Cet autotest m'a attrapé moi-même (il criait « cassé » à tort). Ajouts : "
        "empreintes md5 de `defaults.env` et `universe_profils.json` dans l'état, avec CRI de "
        "dérive de config et l'avertissement décisif (moteur non relancé ⇒ un désaccord serait "
        "LÉGITIME, ses décisions reposant sur les anciens paramètres)."
    ),
    "hulk-mexc/scripts/sonde_profondeur_carnet.py": (
        "2e vague 23/09 (objection de la FAMILLE : « une photo de carnet ne fait pas une règle ») "
        "— ajout de `--serie` (append d'un instantané en JSONL) et `--serie-analyse` (médianes "
        "par paire + test de stabilité min-max). C'est la seule forme sous laquelle un carnet "
        "périsable peut servir à décider quoi que ce soit (R17). 0 ordre, lecture seule."
    ),
    "hulk-mexc/scripts/chiffrage_entree_sortie_replay.py": (
        "SEUIL RÉEL 23/09 (classe F — l'instrument portait la même erreur que mes documents) : "
        "les TROIS calculs de seuil d'entrée ignoraient le terme `DIP_CADENCE_MULT × cadence` "
        "(ils ne lisaient que `dip_pct` → 5 % au lieu de 13,20 % sur EDEL). La cadence est "
        "désormais reproduite COMME LE MOTEUR (médiane des ranges de blocs de 24 h sur la "
        "fenêtre 15 j glissante, score_pair l.535-543). RÉSULTAT du rejeu hors ligne (klines "
        "locales, 90 j × 20 paires) : EDEL E0 −1,10 $ → +3,88 $ · E2 +18,58 $ (inchangé) → le "
        "gain du levier EDEL était GONFLÉ de 25 % (+19,68 → +14,70 $/90 j) ; rafales "
        "structurellement inaccessibles 66 % → 84 % ; E2+X2 test +62,50 → +59,42 $ (1re "
        "moitié +21,80 $, cohérent) ⇒ le flag `IMPULSE_SANS_REPLI_ON` d'EDEL tient, son motif "
        "est plus fort qu'annoncé. Corrigé, pas retiré. 2e vague 23/09 : le slippage devient un "
        "PARAMÈTRE (`REPLAY_SLIP_BPS`), objections Gemini/Grok/DeepSeek « vos gains sont "
        "mathématiquement surévalués sans mesure d'impact » : MESURÉ — E0+X4 −3,93 → −6,79 $ et "
        "E2+X2 +59,42 → +48,86 $ à 45 bps/côté (1re moitié +13,31 $, positive) ⇒ le levier tient "
        "au coût réel, la règle actuelle non (beaucoup de petits trades)."
    ),
}


# NOUVEAUX INSTRUMENTS (23/09) — le registre est le « fil logique » : un instrument qui
# n'y est pas n'existe pas pour la maison (il est invisible à la veilleuse, au drill, à la
# revue des organes). On les ajoute donc SCellés, avec leur rôle.
NOUVEAUX = {
    "hulk-mexc/scripts/verif_seuil_moteur.py": {
        "role": "GARDE-FOU DE MÉTHODE : confronte le seuil recalculé AUX CHIFFRES ÉCRITS PAR LE "
                "MOTEUR (refus parlants + cadence colonne 9 de son journal), nomme le terme qui "
                "décide (R15), détecte tout instrument qui recalcule un seuil d'entrée sans le "
                "terme `DIP_CADENCE_MULT × cadence` et s'autoteste (un chiffre faux injecté doit "
                "le faire sortir rc=3). rc=0 conforme · rc=3 désaccord · rc=2 pas assez de données.",
        "origine": "GO Christophe 23/09 (« c'est pas possible de faire encore ce type d'erreurs ») "
                   "après avoir publié 3 jours un seuil tronqué (5-12,75 % au lieu de 21,70 %)",
    },
    "hulk-mexc/scripts/chiffrage_sortie_paire.py": {
        "role": "GO 1 — décompose la SORTIE d'une paire sur les trades RÉELS : PnL encaissé, "
                "motif de sortie, giveback (pic atteint vs prix de sortie), ré-entrées plus "
                "hautes que la dernière vente, et « acheter et garder » sur la même fenêtre.",
        "origine": "GO Christophe 23/09 (« pourquoi RIZE, la seule qui monte, est la seule perdante ? »)",
    },
    "hulk-mexc/scripts/sonde_profondeur_carnet.py": {
        "role": "GO 3 — mesure la PROFONDEUR du carnet public par niveau de prix (dollars "
                "absorbables sous −0,5 / −1 / −2 %) pour remplacer le plafond arbitraire "
                "« 2 % du mur ». Révèle que le « mur » peut être un niveau AFFICHÉ (RIZE 801 k$ = "
                "1 234× la profondeur réelle de son carnet). LECTURE SEULE, 0 ordre.",
        "origine": "GO Christophe 23/09 (« la taille d'abord ») — chantier de la TAILLE",
    },
    "hulk-mexc/scripts/chiffrage_pump_manque.py": {
        "role": "Autopsie d'un épisode « pump manqué » sur les données du moteur (régimes, "
                "repli exigé vs offert), SCAN de toutes les paires (jambes ≥ 20 % prises/manquées "
                "+ cause + chiffrage au plafond réel) et `--cadences` (repli réellement exigé par "
                "paire + part de jambes structurellement inaccessibles). Lectures seule.",
        "origine": "Demande Christophe 22-23/09 (« explique-moi pourquoi RIZE a perdu le pump »)",
    },
    "hulk-mexc/scripts/cartographie_setups_paires.py": {
        "role": "SET-UP PAIRE PAR PAIRE (demande Christophe depuis le premier jour) : les 20 "
                "paires côte à côte — ENTRÉE (repli réellement exigé = max(dip_pct ; 0,50 × "
                "cadence moteur), jambes inaccessibles, porte qui refuse), SORTIE (stop ANNONCÉ "
                "vs stop RÉALISÉ, dust sweeps, motifs) et TAILLE (cap actuel vs profondeur "
                "mesurée). Aucun chiffre recalculé de mémoire : chaque valeur est lue dans le "
                "journal du moteur, mesurée, ou lue dans le profil. LECTURE SEULE, 0 ordre.",
        "origine": "Christophe 23/09 : « c'est ce que je te demande depuis le tout début, faire "
                   "le set-up sur chaque paire »",
    },
    "Index_Maison/scripts/consulter_famille_garde_fou_seuil_20260923.py": {
        "role": "Consultation de la FAMILLE (hub local, 4 modèles) sur la faute de méthode et "
                "le garde-fou : brief de CONTRADICTION (nommer l'angle mort, la classe "
                "d'erreur suivante, la priorité, l'erreur non vue), sorties AVIS_*.md + "
                "SYNTHESE.md. Un verdict qu'on ne peut pas contredire n'est pas un verdict.",
        "origine": "Christophe 23/09 : « consultation avec la famille (voyons si on peut éviter "
                   "que tu continues de faire des erreurs), prompt spécifique et contexte »",
    },
    "Index_Maison/scripts/declarer_rescel_20260923.py": {
        "role": "Outil d'ACTE : déclare et re-scelle les fichiers modifiés du 23/09 (backup "
                "horodaté du registre + entrée `_rescel_20260923` qui dit ce qui a changé et "
                "pourquoi). Règle maison R5/R13 : un scellé ne s'écrase jamais sans le déclarer.",
        "origine": "GO Christophe 23/09 — la veilleuse criait (à raison) sur 2 scellés modifiés",
    },
}


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def main():
    reg = json.load(open(REG, encoding="utf-8"))
    backup = REG.with_name(REG.name + ".bak_declare_20260923_%s" % time.strftime("%H%M%S"))
    shutil.copy2(REG, backup)
    print(f"backup : {backup.name}")
    faits = 0
    for nom, declaration in DECLARATIONS.items():
        cible = RACINE / nom
        if not cible.exists():
            print(f"  [SKIP] absent : {nom}")
            continue
        actuel = md5(cible)
        for it in reg["fichier"]:
            if str(it.get("nom")) == nom:
                avant = it.get("md5")
                if avant == actuel:
                    print(f"  [=] {nom} déjà conforme")
                    break
                it["md5"] = actuel
                it["date"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
                it["_rescel_20260923"] = declaration
                print(f"  [OK] {nom}\n       {avant} → {actuel}")
                faits += 1
                break
        else:
            print(f"  [ABSENT DU REGISTRE] {nom}")
    # 2) AJOUT des nouveaux instruments (seulement s'ils ne sont pas déjà au registre)
    noms = {str(i.get("nom")) for i in reg["fichier"]}
    for nom, meta in NOUVEAUX.items():
        cible = RACINE / nom
        if nom in noms:
            print(f"  [=] déjà au registre : {nom}")
            continue
        if not cible.exists():
            print(f"  [SKIP] absent : {nom}")
            continue
        reg["fichier"].append({"nom": nom, "role": meta["role"], "origine": meta["origine"],
                               "verif": "md5", "auto_modifiable": False,
                               "md5": md5(cible),
                               "date": time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime()),
                               "_ajout_20260923": "Instrument créé le 23/09/2026 (GO Christophe) "
                                                  "— ajouté au registre le jour même de sa création "
                                                  "pour qu'il soit VU (veilleuse, drill, revue)."})
        print(f"  [+] AJOUTÉ : {nom}")
    reg["updated"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    tmp = REG.with_suffix(".json.tmp")
    json.dump(reg, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    os.replace(tmp, REG)
    print(f"\n{faits} scellé(s) re-déclaré(s) · registre réécrit ({len(reg['fichier'])} entrées)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
