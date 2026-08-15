# VERDICT FAMILLE — Veilleuse / Synapse + alerte vocale en boucle (15/08/2026)

**Avis reçus** : gemini (92%), nvidia (78%) = 2/4 (openrouter 502 réseau, habituel).

## Verdict : GO-AVEC-RÉSERVE (convergent)

## 1. REGISTRE DES SYNAPSES — noyau critique uniquement
- **Indexer uniquement la PROD critique** : scripts exécutés par launchd, plists actives,
  configs sensibles, moteur core. **Cible 30-50 entrées max** (sinon bruit) — nvidia.
- **Exclure** : logs, caches, fichiers temporaires, scripts de dev — gemini.
- **Faux positifs** : le `RELEASE_RECEIPT` (ou le script de déploiement) **doit mettre à jour
  le registre en même temps**. Tout écart sans mise à jour = non déclaré = alerte — les deux.
- **Champ `maj_attendue`** (dernière modif légitime) + **`auto_modifiable: true`** pour les
  fichiers qui se modifient eux-mêmes — nvidia.
- **Fichiers de DONNÉES (live.json, whales) : PAS de md5** (ils changent en continu) →
  vérifier la **fraîcheur** (timestamp < 10 min) au lieu de l'intégrité — nvidia.

## 2. VEILLEUSE — cadence 10 min, 4 vérifs hiérarchisées
1. **Intégrité md5** des fichiers indexés → intrusion/modification non déclarée
2. **Process attendus vivants** (launchctl list) → panne/crash
3. **Fraîcheur des données critiques** (live.json, whales, alarmes) → blocage silencieux
4. **Présence des kill-switches** (STOP, STOP_ALL) → sécurité en place
- **Cadence 10 min** (compromis réactivité/charge) — les deux.
- **Distinguer panne vs intrusion** dans le message vocal :
  - « ALERTE INTRUSION : modification non déclarée de [fichier] » (md5 ≠ + pas de reçu)
  - « ALERTE PANNE : [process] inactif depuis [durée] » (process mort OU données périmées)
- **Auto-intégrité** : la veilleuse vérifie son propre md5 (compromission de la veilleuse) — nvidia.

## 3. ALERTE VOCALE EN BOUCLE — volonté Christophe respectée + garde-fous
- **Boucle infinie stricte PENDANT LES HEURES DE VEILLE (07h-23h)** — volonté de Christophe — gemini.
- **Atténuation NOCTURNE (23h-07h)** — condition du GO famille (nvidia) :
  répétition toutes les 10 min + volume réduit (alerte active mais non assourdissante).
- **Limite de sécurité absolue** : après **24h** de boucle → mode « log uniquement » +
  notification push si dispo (si personne n'a réagi en 24h, le problème est ailleurs) — nvidia.
- **Fréquence** : message complet toutes les **30 s** + pause 5 s — les deux.
- **Identifiant unique d'alerte** (ex. `ALERTE_VEILLEUSE_20260815_1430`) → le kill-switch
  `STOP_ALERTE` est précis et ne tue pas une autre alerte — nvidia.

## 4. PRIORITÉ VOCALE — OUI, l'alerte bloque (convergent)
- Une alerte critique **doit écraser et monopoliser le canal audio** (`killall say`,
  règle maison respectée). La sécurité prime sur les synthèses informatives secondaires.

## Améliorations captées
1. **Raccourci unique** `arret_alerte` (ou `stop`) : `touch STOP_ALERTE` + nettoyage en un geste — gemini.
2. **Journal d'alerte structuré** : chaque alerte écrit `ALERTE_[ts].json` (message, cause, heure) — nvidia.
3. **`MAINTENANCE_PREVUE`** : suspend les alertes pendant une maintenance planifiée — nvidia.

## ⚠️ Point à trancher PAR CHRISTOPHE (condition du GO nvidia)
L'**atténuation nocturne** (23h-07h : fréquence espacée + volume réduit) :
- **OUI** (recommandé famille) : volonté respectée le jour, pas de nuisance la nuit.
- **NON** (boucle infinie stricte 24h/24) : nvidia basculerait vers NO-GO (nuisance permanente).

## Décision Buffy (supervision)
- Design validé : registre prod-only (30-50) + veilleuse 10 min (4 vérifs, panne≠intrusion)
  + alerte vocale boucle 30s avec identifiant unique + priorité absolue.
- **Soumission à Christophe** : atténuation nocturne OUI/NON (seul point bloquant famille).
- Chantier = veille/observation + alerte, zéro touche moteur Hulk → réversible.
