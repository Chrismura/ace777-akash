# BRIEF SPEC V2.1 soumis a la famille (re-validation) — 10/08

SPEC V2.1 — SETUP DES 3 ETAGES ACE777 (RE-VALIDATION — 10/08/2026)

CONTEXTE : Mac 8 Go, hub local 11435 (9 providers gratuits), 29 services
launchd. Objectif : 13 services en 3 étages, superviseur unique, mode
probatoire C6, 6 conditions famille C1-C6, loi 1quinquies.

La famille a juge la spec V2 : GO AVEC RESERVES (8 reserves). Grok a produit la
SPEC V2.1 qui les integre toutes. Voici ce qui a change (DELTA vs V2) :

## A. LES 8 RESERVES FAMILLE — INTEGREES AVEC SOLUTION DE CODE

P1 - FIABILITE STATE.JSON :
1. Champ "status" : HEALTHY | STALE | DEGRADED a la racine de state.json.
   Seuils : live.json age > 15 s -> STALE ; autres feeds > 2 min -> STALE ;
   feed absent/corrompu/hash invalide -> DEGRADED.
2. "feed_hash" : SHA-256 des 4 feeds agreges dans l'ordre fixe
   (mission.json + cortana_feed.json + live.json + routing.json).
3. Fallback feeds bruts : dans le superviseur, si state.json absent OU hash
   invalide -> lecture directe des feeds bruts + log avertissement.
4. Tolerance pannes generateur : load_json_safe() par feed — un feed corrompu
   est ignore (log), la mise a jour globale continue.

P2 - LATENCE :
5. Cadence state.json : 2 minutes (StartInterval 120). Impact disque mesure :
   ~4 Ko/ecriture x 30 = 120 Ko/heure — acceptable Mac 8 Go.

P3 - MIROFISH REVERSIBILITE :
6. Fichier obligatoire DESACTIVES_2026-08-10/README_MIROFISH.md avec procedure
   exacte de re-activation (restaurer plists, retirer skip_check, launchctl
   load, verifier HEALTHY dans state.json).

P4 - VOCAL COMPATIBILITE :
7. cortana_cockpit_bridge.py lit crypto-voice-assistant-core/VERSION et
   alerte si version != attendue (ou fichier manquant).

P5 - CONTROLE BACKUP LEGER :
8. Presence par metadonnees (os.path.exists + stat) toutes les 30 min, SANS
   lecture recursive. Taille totale (du -sk) toutes les 6 h. Manifeste leger
   par dossier : name, size, hash (SHA-256 des 500 premiers octets).

## B. LOI DU BRUT — PRINCIPE DIRECTEUR (decouverte nuit 09->10/08)

"c'est dans le brut que se cache la verite" : la machine ECRIT le brut, l'IA
LIT le brut, PERSONNE n'interprete entre les deux.

Application :
- state.json ne contient JAMAIS de prose/resume/interpretation — uniquement
  mesures brutes, timestamps, hashes, compteurs, statuts.
- mission.json / cortana_feed.json / live.json restent bruts aussi. Toute
  transformation (scoring, synthese) va dans une couche analysis/ separee.
- system_state_generator.py est INTERDIT de produire du texte narratif.

## C. REALITE MIROFISH — DECISION ASSUMEE

Mirofish = MEMBRE DE L'EQUIPE (simulation sociale multi-agents, recherche-
grade, jamais d'execution). Desactive le 10/08 (tournait a vide 14 h, budget).
- Option (c) confirmee MAIS formulee comme decision assumee : membre d'equipe
  en pause budgetaire, re-activable a la demande (README).
- Principe anti-invisibilite : tout service qui tourne sans etre visible dans
  state.json = anomalie. state.json/cockpit = remede a la maladie de
  l'invisibilite.

## D. 3 PREMIERES ETAPES (loi 1quinquies, re-validation JUGE entre chacune)

E1. Implémentation status + feed_hash + fallback -> system_state_generator.py
    v2.1 + tests unitaires.
E2. Cadence 2 min + controles backup legers -> plist StartInterval 120 +
    backup_light_check.sh.
E3. README_MIROFISH.md + verification version Rust dans
    cortana_cockpit_bridge.py.


QUESTIONS A LA FAMILLE (RE-VALIDATION de la SPEC V2.1) :
1. Les 8 reserves que vous avez formulees sont-elles TOUTES correctement
   integrees dans la V2.1 (verifiez chacune : status, feed_hash, fallback,
   tolerance pannes, cadence 2 min, README Mirofish, version Rust, controle
   backup leger) ?
2. La LOI DU BRUT (state.json sans prose, generateur interdit de narratif,
   transformation reportee en couche analysis/) est-elle correctement gravee ?
3. La formulation Mirofish (membre d'equipe en pause budgetaire, procedure de
   re-activation documentee) est-elle satisfaisante ?
4. Verdict final sur la SPEC V2.1 : GO / GO AVEC RESERVES / NON
   (avec 1 phrase de justification + les reserves restantes, s'il y en a).
   La loi 1quinquies : votre verdict decide du passage au code.
