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
        "0 traceback, veilleuse STABLE. Réversible en 1 ligne. "
        "-- 2e MODIFICATION DU MÊME JOUR (GO 1 + GO 2, 23/09, exigence de la FAMILLE) : le journal "
        "écrit 5 colonnes de plus — `ts_prix_utc` (quand le PRIX a été lu chez MEXC), `age_prix_s` "
        "(son âge à l'écriture : l'audit a trouvé des remplissages à 1-5 min de retard), "
        "`spread_bps`, `spread_source` (asp = vue live, profil = repli figé) et `cout_estime_usdt` "
        "(frais 5 bps/côté ESTIMÉS + spread). ADDITIF ET SANS EFFET SUR LES DÉCISIONS : aucune "
        "colonne retirée, aucun seuil, aucune porte, aucun ordre modifié ; `_PRICE_TS` est "
        "renseigné à la LECTURE du prix (batch + fallback unitaire) et tout est calculé dans un "
        "try/except (un log ne casse jamais une boucle). Le PnL inscrit reste BRUT : le net est "
        "un calcul de reporting séparé, pour ne pas toucher au disjoncteur. "
        "-- 3e MODIFICATION DU MÊME JOUR (classe E15, 23/09) : les 5 colonnes NE SUIVAIENT PAS LE "
        "RESUME, qui recopiait l'ANCIEN fichier (`shutil.copy2`) PAR-DESSUS le nouveau → journal "
        "vivant à en-tête 11 colonnes et lignes à 16 (mesuré : 76 162 lignes à 11 + 12 à 16). "
        "CORRIGÉ À LA RACINE : `CSV_SCHEMA` devient la SOURCE UNIQUE du schéma, le resume "
        "RÉÉCRIT l'en-tête courant en jetant l'ancien, et une garde à l'écriture hurle "
        "`SCHEMA_ECART` au lieu d'écrire une ligne bancale. ADDITIF : aucune colonne retirée, "
        "aucun seuil, aucune porte, aucun ordre. Vérifié après relance par le watchdog de la "
        "maison : en-tête 16, `verif_schema_journal` CONFORME rc=0, état repris à l'identique "
        "(pnl 42,1679 $ / 175 trades / 10 positions). "
        "-- 4e MODIFICATION DU MÊME JOUR (GO 2, ordre Christophe « le stop vérifié à l'instant de "
        "l'impact ») : le stop se décidait sur le prix du cycle (âge jusqu'à 120 s). Désormais, "
        "au déclenchement, un GET ciblé frais remplace ce prix AVANT la vente (`last_price_frais`, "
        "≈ 0,3 s) et l'âge des deux prix est éCRIT dans le motif (`_impact_avNs_apNs`) — le "
        "déclenchement, les seuils et les portes restent IDENTIQUES, seul le prix utilisé est plus "
        "récent. Les motifs historiques gardent leur préfixe exact (aucun lecteur cassé) ; le "
        "motif de balayage de poussière nomme maintenant son niveau (`dust_sweep_stop_guard_PAIRE_stopX%`) "
        "pour que le niveau de stop soit lisible partout. Échec réseau → prix du cycle conservé et "
        "tag `_impact_NA` : aucune valeur inventée. Vérifié par `verif_stop_impact.py` (5/5, dont "
        "4 cas d'échec rejetés). Réversible en 4 lignes. "
        "-- CORRECTION DE COMPRÉHENSION QUE CETTE MODIF ACCOMPAGNE (classe E17) : j'ai publié "
        "« stop annoncé 8 % » pour RIZE en lisant `calib.stop_pct` — un PLANCHER ; le stop réel de "
        "la machine est `max(plancher ; cadence × 0.70)` = 39,23 % (44 % aujourd'hui), écrit dans "
        "ses propres motifs. Le stop TIENT au point de base ; c'est son NIVEAU qui est énorme."
    ),
    "Index_Maison/scripts/verifier_regles_or.py": (
        "R18 AJOUTÉE LE 23/09 (ordre Christophe : « ouvre un round avec la famille et garde la "
        "fenêtre ouverte, tu n'es plus digne de diriger seule » · « sinon c'est radiation à vie, "
        "règle d'or ») : **R18 — LE JURY PERMANENT**. Elle est MESURÉE, pas promise : il faut une "
        "session de famille OUVERTE, consultée dans les 24 h, dont le fil est COHÉRENT (chaque "
        "tour posé a ses avis) et avec au moins 3 voix INDÉPENDANTES (une substitution modèle "
        "demandé ≠ servi ne compte pas — faute E16). Ajout purement additif : aucune règle "
        "existante modifiée, 12 règles mesurées au lieu de 11."
    ),
    # Clés factices supprimées le 23/09/2026 : une édition trop rapide avait coupé la
    # déclaration de paper_diprip.py EN DEUX (clés « _marker_inutile », « _suite »,
    # « __trou_inchange__ »). Son texte — 3e modification (E15, schéma du journal) incluse —
    # est remis dans SA déclaration, ci-dessus. Leçon de processus, écrite ici pour qu'elle
    # serve : après toute édition de CE fichier, relire la déclaration de bout en bout AVANT
    # de lancer le re-scellement (une déclaration coupée passe le py_compile et scelle les
    # mauvais md5).
    "hulk-mexc/scripts/satellite_aspiration.py": (
        "GO 3 (23/09/2026, GO Christophe après l'audit MEXC × HULK) — COUVERTURE DES 20 PAIRES. "
        "L'audit a mesuré que 13 paires sur 20 n'avaient AUCUNE vue live : le satellite ne sondait "
        "que les paires en régime COOLING/IMPULSE (5 max) + les 6 forcées, soit 7-8 en pratique. "
        "Pour ces paires, le moteur plafonnait la mise sur le `mur_bid_med` du PROFIL — chiffre figé, "
        "faux de 8 à 82 % (RIZE : cap 4,88 $ pour un carnet mesuré à 364,74 $). "
        "CHANGEMENT : la sélection sonde TOUTES les paires du moteur (ordre : forcées → actives → "
        "autres) et MAX_PAIRS passe à 20, surchargeable par ASPIRATION_MAX_PAIRS. "
        "COÛT MESURÉ : une passe complète = 35,8 s pour 40 lectures /depth (≈ 80-100 appels/min, "
        "sous le plafond observé ~200/min) ; launchd StartInterval=20 s ⇒ une passe sur deux est "
        "sautée (pas de chevauchement) ⇒ âge d'une vue ≈ 40-55 s, sous le `wall_stale_sec` de 120 s. "
        "ADDITIF : `n_paires_univers`, `couverture_pct`, `max_pairs` sont désormais écrits dans le "
        "JSON pour que la couverture soit VERIFIABLE au lieu d'être supposée. RÉVERSIBLE en 1 ligne."
    ),
    "Index_Maison/scripts/gen_cockpit_vol.py": (
        "GARDIEN VISIBLE 23/09 (GO 1 — « un verdict qu'il faut aller chercher n'existe pas ») : "
        "la page « vol » gagne DES gardiens qui lisent des états ÉCRITS par des contrôles "
        "appelés par git_push_auto.sh — d'abord « Garde-fou seuil moteur » "
        "(`thermo/seuil_moteur.json` : combien de refus chiffrés ont été CONFRONTÉS au seuil "
        "recalculé, instrument qui recalcule sans la cadence, refus d'être un feu vert si "
        "l'état est figé >8 h) ; puis, même jour, « Horodatage mémoire (E13) » "
        "(`thermo/memoire_horodatage.json` : lignes horodatées, heure future interdite, "
        "remontées de temps signalées mais NON re-datées). MODIFIÉ UNE 2e FOIS le 23/09 pour "
        "ce 2e gardien (le scellement est refait ici, après la DERNIÈRE modification — leçon "
        "E12). **3e modification le 23/09** : un 15ᵉ gardien, « Schéma du journal (E15) » "
        "(`hulk-mexc/runs/VERIF_SCHEMA_JOURNAL.json`) — largeur de schéma, nombre "
        "d'incohérences, journal vivant conforme, refus d'être un feu vert si l'état est figé "
        ">8 h. LECTURE SEULE, ajout seul : aucun autre gardien touché, aucune donnée modifiée."
    ),
    # L'outil se déclare LUI-MÊME : le détecteur de la veilleuse l'a attrapé (modifié après
    # son premier scellement). C'est la preuve que le contrôle fonctionne, y compris sur son
    # propre outillage.
    "hulk-mexc/scripts/verif_schema_journal.py": (
        "GARDIEN E15 (23/09/2026) — journal de données écrit en DEUX largeurs (en-tête 11, lignes 16). "
        "Refinement APRÈS le 1er scellement, et la raison écrite pour qu'elle ne soit pas "
        "redécidée par oubli : (1) un journal incoherent mais DÉJÀ SUPERSEDED par un journal plus "
        "récent est **signalé, non bloquant** — une alarme qui ne s'éteint jamais tue la confiance "
        "dans l'alarme (R14) ; (2) la règle « âge < 1 h = bloquant » a été ESSAYÉE puis REJETÉE "
        "(elle allumait un rouge sur une faute déjà corrigée et déjà remplacée) ; (3) le schéma est "
        "lu À LA SOURCE en retirant les commentaires (le 1er essai comptait « asp » et « profil » "
        "comme des colonnes — 18 au lieu de 16). BLOQUANT = le journal le plus récent seulement. "
        "LECTURE SEULE : n'écrit dans aucun journal."
    ),
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
    "hulk-mexc/scripts/verif_schema_journal.py": {
        "role": "GARDIEN DE LA CLASSE E15 (journal écrit en DEUX largeurs : en-tête 11, lignes 16) : "
                "lit le schéma À LA SOURCE (`paper_diprip.CSV_SCHEMA`, jamais recopié), vérifie "
                "R1/R2 (en-tête = largeur des lignes) sur 20 journaux, R3 (le journal du moteur "
                "VIVANT doit être au schéma courant), R4 autotest 4/4 (conforme · en-tête court "
                "reconnu cohérent · ligne large détectée · ligne vide tolérée). LECTURE SEULE. "
                "rc=0 conforme · rc=1 écart dans le journal courant.",
        "origine": "Faute trouvée le 23/09 en vérifiant le GO 1 de Christophe (traçabilité du "
                   "prix) : le resume écrasait l'en-tête neuf par l'ancien — silencieux donc grave",
    },
    "hulk-mexc/scripts/chiffrage_pnl_net.py": {
        "role": "GO 2 (23/09, exigence de la FAMILLE) : calcule le PnL NET à côté du BRUT — "
                "frais (5 bps/côté, DÉCLARÉS estimés) + spread de sortie mesuré. Le `pnl_total` du "
                "moteur reste BRUT : ce n'est PAS un changement de décision, c'est un reporting.",
        "origine": "Audit MEXC × HULK : 39,70 $ brut → 36,19 $ net (−8,8 %) ; la famille a exigé "
                   "d'arrêter de piloter avec un chiffre brut faux de 8,8 %",
    },
    "Index_Maison/scripts/auto_evaluation_buffy.py": {
        "role": "AUTO-ÉVALUATION de mes 14 jours, chiffrée par instrument : lignes de mémoire "
                "dont je suis l'auteur, livrables cités nommément, progression du PnL journal par "
                "journal, classes d'erreurs. Écrit un AVERTISSEMENT D'ATTRIBUTION : les "
                "compteurs de fichiers créés ne sont PAS mon œuvre (leçon E14). LECTURE SEULE.",
        "origine": "Ordre Christophe 23/09 « tu vas évaluer ton ouvrage des deux dernières "
                   "semaines »",
    },
    "Index_Maison/scripts/consulter_famille_jugement_buffy_20260923.py": {
        "role": "CONSULTATION DE JUGEMENT : soumet à la famille mes livrables, MES ERREURS "
                "(16 classes) et l'évolution de HULK, et exige un verdict fermé + un CRITÈRE "
                "MESURABLE + le fait qui invaliderait l'avis. Écrit l'en-tête de chaque avis avec "
                "le modèle QUI A RÉPONDU (+ bandeau SUBSTITUTION et `META_*.json`) — corrigé le "
                "jour même (classe E16 : le hub avait substitué grok → gemini et je l'ignorais).",
        "origine": "Ordre Christophe 23/09 « le demander à la famille de t'évaluer… et leur "
                   "demander si tout ceci est acceptable »",
    },
    "Index_Maison/scripts/consulter_famille_garde_fou_seuil_20260923.py": {
        "role": "Consultation de la FAMILLE (hub local, 4 modèles) sur la faute de méthode et "
                "le garde-fou : brief de CONTRADICTION (nommer l'angle mort, la classe "
                "d'erreur suivante, la priorité, l'erreur non vue), sorties AVIS_*.md + "
                "SYNTHESE.md. Un verdict qu'on ne peut pas contredire n'est pas un verdict.",
        "origine": "Christophe 23/09 : « consultation avec la famille (voyons si on peut éviter "
                   "que tu continues de faire des erreurs), prompt spécifique et contexte »",
    },
    # Fichier PRÉ-EXISTANT mais ABSENT DU REGISTRE (trou détecté le 23/09 en déclarant sa
    # modification) : le satellite qui alimente la vue live n'était invisible ni du drill, ni de
    # la veilleuse, ni de la revue des organes. On le scelle en même temps qu'on le corrige.
    "hulk-mexc/scripts/satellite_aspiration.py": {
        "role": "SATELLITE D'OBSERVATION : sonde le carnet MEXC (/depth) par paire et écrit "
                "`runs/aspiration_live.json` (spread, mur bid/ask, chute du mur, délai) — c'est LA "
                "source du cap de mise et du gate de murs du moteur. Lancé par launchd "
                "(com.ace777.satellite-aspiration, StartInterval 20 s, mode --once). "
                "23/09 (GO 3) : sonde désormais TOUTES les paires du moteur (avant : 5 actives + "
                "6 forcées ⇒ 13 paires aveugles), écrit sa couverture et son âge dans le JSON, et "
                "reste sous le plafond de requêtes mesuré (≈ 80-100/min pour ~200/min).",
        "origine": "Audit MEXC × HULK (23/09) — les 13 paires sans vue live plafonnaient leur mise "
                   "sur un profil figé faux de 8 à 82 %",
    },
    "hulk-mexc/scripts/audit_mexc_vs_hulk.py": {
        "role": "AUDIT GO 1 (23/09, demande Christophe « compare les données de MEXC une par une "
                "avec celles de Hulk ») : pour les 20 paires, rejoue les MÊMES endpoints et les "
                "MÊMES formules que le moteur (ticker/price, depth?limit=20 avec mur = MAX niveau "
                "unitaire, profondeur cumulée sous −0,5/−1/−2 %) et mesure les écarts prix / spread "
                "/ mur, l'âge de la vue live, et les trous (paires sans profil, sans vue live). "
                "LECTURE SEULE, 0 ordre.",
        "origine": "Demande Christophe 23/09 (audit MEXC × Hulk, GO 1)",
    },
    "hulk-mexc/scripts/audit_sequences_trades.py": {
        "role": "AUDIT GO 2 : reconstruit CHAQUE séquence par conservation des quantités (BUY / "
                "SELL_PARTIAL / SELL), la confronte aux klines 1 min MEXC (le prix inscrit tombe-t-il "
                "dans le [low, high] de sa minute ?), mesure la justesse (MFE/MAE 60 min, giveback, "
                "laissé sur la table) et recalcule le **net de coûts** (le journal inscrit le BRUT : "
                "`pnl = (price − entry) × sell_qty`). Budget de temps déclaré ; les séquences non "
                "traitées sont NOMMÉES, jamais comblées. LECTURE SEULE, 0 ordre.",
        "origine": "Demande Christophe 23/09 (audit séquences, mises, justesse — GO 2)",
    },
    "hulk-mexc/scripts/audit_horodatage_prix.py": {
        "role": "Sous-analyse ciblée : pour chaque prix du journal qui ne tombe PAS dans sa minute, "
                "cherche dans ±6 min la minute qui le contient → tranche entre « retard d'horodatage » "
                "(le prix est vrai, l'heure est fausse) et « prix périmé » (on a paper-tradé un prix "
                "qui n'existait plus). 13/13 → retard d'horodatage, aucun prix fantôme.",
        "origine": "GO 2 — question « les données sont-elles correctement enregistrées ? »",
    },
    "hulk-mexc/scripts/audit_memoire_donnees.py": {
        "role": "AUDIT GO 3 : couverture (profil / vue live / obs murs / état / journal / set-up par "
                "paire), complétude colonne par colonne, colonnes MANQUANTES nommées, cohérence "
                "interne (horodatages, continuité de pnl_total, doublons) et **re-injection des "
                "set-up** (stop annoncé vs réalisé en $, mise vs cap, mise vs profondeur mesurée) "
                "avec ses limites déclarées (extrêmes mesurés, cap d'aujourd'hui). LECTURE SEULE.",
        "origine": "Demande Christophe 23/09 (« vérifie les données qu'on mémorise, si il en manque, "
                   "ensuite tu rejoues tout ça avec les derniers set-up »)",
    },
    "hulk-mexc/scripts/probe_prix_mexc_fraicheur.py": {
        "role": "LE TEST EXIGÉ PAR LA FAMILLE : l'écart d'horloge (en-tête HTTP `Date` de MEXC vs "
                "notre horloge), l'ÂGE DU DERNIER TRADE réel par paire et l'écart entre le « dernier "
                "prix » et le MILIEU DU CARNET. Résultat : horloge à 0,6 s, 16/20 paires ont échangé "
                "dans la dernière minute (donc le retard de 1-5 min EST notre chaîne pour elles), et "
                "l'écart ticker/mid atteint −90,9 bps sur RIZE. Verdict rendu PAR PAIRE (l'ancien "
                "verdict global « H2 dominante » était plus large que la mesure — corrigé le jour même).",
        "origine": "Réponses de la FAMILLE (Gemini/Grok/Nemotron : « mesure l'écart d'horloge avant "
                   "de conclure ») — classe E14 (conclusions au-delà de la mesure)",
    },
    "Index_Maison/scripts/consulter_famille_audit_mexc_20260923.py": {
        "role": "Consultation de la FAMILLE sur l'audit : brief construit À PARTIR DES JSON des "
                "instruments (aucun chiffre retapé), mes erreurs E10/E12/E13 listées, mission de "
                "CONTREDIRE. 4 avis + SYNTHESE.md (verdict unanime « utile mais incomplet », ordre "
                "imposé : horodatage d'abord, net de coûts ensuite).",
        "origine": "Christophe 23/09 : « remets tout ça à la famille, conteste avec tes erreurs »",
    },
    "Index_Maison/scripts/verif_memoire_horodatage.py": {
        "role": "GARDIEN DE LA CLASSE E13 (heure de mémoire ESTIMÉE au lieu d'être LUE) : "
                "R1 = aucune ligne de la date la plus récente ne peut être datée dans le FUTUR "
                "(> +5 min) — aurait attrapé les 4 lignes du 23/09 écrites de tête (10:40Z pour "
                "un artefact de 09:47Z) ; R2 = ordre décroissant dans la date ; autotest 5/5 "
                "rejoué à heure FIXE (un test qui passe à 14 h et échoue à 9 h ne prouve rien) ; "
                "limites déclarées (heure SOUS-estimée indétectable ; les lignes anciennes hors "
                "ordre sont SIGNALÉES, jamais re-datées — on n'invente pas une seconde fois). "
                "LECTURE SEULE : n'écrit jamais dans la mémoire, seulement son verdict "
                "(runs/ + thermo/ pour le cockpit). rc=0 conforme · rc=1 anomalie.",
        "origine": "GO Christophe 23/09 (« c'est pas possible de faire encore ce type "
                   "d'erreurs ») — mes propres horodatages de mémoire étaient faux de +53 min",
    },
    "Index_Maison/scripts/declarer_rescel_20260923.py": {
        "role": "Outil d'ACTE : déclare et re-scelle les fichiers modifiés du 23/09 (backup "
                "horodaté du registre + entrée `_rescel_20260923` qui dit ce qui a changé et "
                "pourquoi). Règle maison R5/R13 : un scellé ne s'écrase jamais sans le déclarer.",
        "origine": "GO Christophe 23/09 — la veilleuse criait (à raison) sur 2 scellés modifiés",
    },
    "hulk-mexc/scripts/oracle_independant.py": {
        "role": "ORACLE INDÉPENDANT (classe E11, GO 1 du 23/09) : juge CHAQUE trade sur les bougies "
                "1 min MEXC BRUTES — aucun indicateur du moteur n'est relu. Il dit (A) si la baisse "
                "était réellement là avant l'achat, (B) le meilleur et le pire point atteints, "
                "(C) si le stop RÉEL (niveau LU dans le motif de sortie du moteur, jamais deviné) a "
                "été touché et avec quel retard, (D) ce que le marché a fait après la vente, "
                "(E) le PnL recalculé (quantité × écart) et net estimé. C'est la seule voix qui "
                "puisse contredire la machine autrement qu'avec ses propres chiffres.",
        "origine": "Christophe : « tu n'es plus digne de diriger seule » → GO 1 = fermer E11 par un "
                   "juge extérieur au moteur",
    },
    "hulk-mexc/scripts/boucle_setups_main.py": {
        "role": "LA BOUCLE DES SET-UPS REFaite À LA MAIN (10 jours, toutes les paires) : reprend les "
                "faits horodatés du journal (heure, prix, quantité) et recalcule TOUT le reste — "
                "prix vérifié dans sa bougie, motif d'entrée par FAMILLE (une condition de baisse "
                "ne s'applique qu'aux familles qui l'annoncent), part de chaque sortie, verdict de "
                "marché après la vente, niveau et honneur du stop, PnL net à la main.",
        "origine": "Ordre Christophe 23/09 : « reprends toute la boucle des set-ups avec données à "
                   "la main sur les 10 derniers jours et soumets-la à la famille pour qu'elle valide »",
    },
    "hulk-mexc/scripts/chiffrage_stop_serre.py": {
        "role": "CONTRE-FACTUEL DU STOP (exigence de la famille, tour 1) : chiffre ce qu'aurait donné "
                "un PLAFOND de stop (10/15/20/25 %) sur les 10 jours, en cherchant À LA MAIN la "
                "première minute où le marché touche le niveau. Publie aussi la formule exacte du "
                "stop : `max(calib.stop_pct ; cadence de la paire × 0.70)`. Limites déclarées : "
                "aucune ré-entrée simulée, sortie supposée AU niveau (optimiste).",
        "origine": "Famille (Gemini « justification de la formule RIZE 44 % », DeepSeek « backtest "
                   "stop ≤ 15 % »)",
    },
    "hulk-mexc/scripts/verif_stop_impact.py": {
        "role": "GARDE-FOU DU GO 2 : prouve que le stop se décide sur un prix FRAIS — R1 lecture "
                "horodatée (< 2 s), R2 les DEUX âges (celui qui décidait vs celui qui décide), "
                "R3 échec réseau = aucun prix inventé, R4 compatibilité des motifs historiques, "
                "R5 AUTOTEST qui sait échouer (4 cas périmés rejetés). LECTURE SEULE.",
        "origine": "GO 2 Christophe : « le stop vérifié à l'instant de l'impact »",
    },
    "Index_Maison/scripts/session_famille.py": {
        "role": "LA FENÊTRE OUVERTE SUR LA FAMILLE (R18) : session persistante avec MÉMOIRE DU FIL "
                "— chaque tour est renvoyé au jury AVEC l'historique, la mémoire de session est "
                "écrite depuis les AVIS BRUTS (je ne réécris pas les verdicts), le transcript est "
                "append-only, et l'étiquette d'un avis nomme le modèle QUI A RÉPONDU (substitution "
                "déclarée, non comptée comme voix indépendante — classe E16).",
        "origine": "Ordre Christophe 23/09 : « ouvre un round avec la famille et garde la fenêtre "
                   "ouverte, qu'elle ait la mémoire du chat »",
    },
    "Index_Maison/scripts/git_push_auto.sh": {
        "role": "POINT D'ENTRÉE DES CONTRÔLES (toutes les 3 h) : y sont appelés le garde-fou des "
                "seuils (E10), le gardien d'horodatage de la mémoire (E13) et — ajouté le "
                "23/09 — le gardien de schéma du journal (E15, `hulk-mexc/scripts/"
                "verif_schema_journal.py --json hulk-mexc/runs/VERIF_SCHEMA_JOURNAL.json`). "
                "C'est ce fichier qui fait que mes contrôles PASSENT au lieu d'exister.",
        "origine": "Un contrôle qui n'est appelé par personne n'existe pas (R15) — le pont "
                   "entre le gardien et la veilleuse de la maison",
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
