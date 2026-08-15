# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 149.2s)

AVIS CONSULTATIF — DESIGN « VEILLEUSE / SYNAPSE » ACE777

---

## 1. REGISTRE DES SYNAPSES

**Quels fichiers indexer :** Uniquement les composants critiques de production (scripts exécutés par launchd, plists, configs actives, données de sortie attendues, moteur). Pas les scripts de développement, pas les journaux, pas les fichiers temporaires. Cible : 30-50 entrées max, sinon le registre devient du bruit.

**Éviter les faux positifs :** Le registre doit avoir un champ `"maj_attendue"` (date/heure de dernière modification légitime). Toute modification après cette date sans RELEASE_RECEIPT = alerte. Mais il faut un **mécanisme de grâce** : si un script modifie son propre fichier (ex. log interne), il doit être exclu du registre ou avoir un champ `"auto_modifiable": true`. Les fichiers de données (live.json, whales) ne doivent PAS être dans le registre md5 — ils changent en continu. Pour eux, vérifier la **fraîcheur** (timestamp < 10 min) et non l'intégrité.

**Recommandation :** Le RELEASE_RECEIPT doit être **obligatoire** pour toute modification de fichier indexé. Sinon, la veilleuse hurlera à chaque mise à jour légitime non déclarée.

---

## 2. VEILLEUSE

**Vérifications essentielles (par ordre de priorité) :**
1. Intégrité des fichiers indexés (md5) — détecte intrusion/modification non déclarée
2. Process attendus vivants (launchctl list) — détecte panne/crash
3. Fraîcheur des données critiques (live.json, whales, alarmes) — détecte blocage silencieux
4. Présence des kill-switches (STOP, STOP_ALL) — vérifie que la sécurité est en place

**Cadence :** 10 minutes est raisonnable. Pas plus fréquent (bruit CPU, faux positifs), pas plus rare (délai de détection trop long).

**Distinguer panne vs intrusion :**
- **Intrusion** : md5 différent + pas de RELEASE_RECEIPT → « INTRUSION détectée sur [fichier] »
- **Panne** : process mort OU données périmées → « PANNE détectée : [process] inactif depuis [durée] »
- **Les deux** : message vocal distinct pour chaque cas. Ne pas mélanger.

---

## 3. ALERTE VOCALE EN BOUCLE

**Le risque de nuisance est réel.** La volonté de Christophe est claire : boucle infinie jusqu'à extinction manuelle. Mais une boucle infinie stricte la nuit, sans personne, = nuisance permanente + usure matérielle.

**Compromis raisonnable :**
- Boucle infinie **pendant les heures de veille** (07h00-23h00) — volonté de Christophe respectée
- **Nuit (23h00-07h00)** : répétition toutes les 10 minutes au lieu de continue, avec volume réduit — l'alerte reste active mais non assourdissante
- **Limite de sécurité absolue** : après 24h de boucle continue, l'alerte passe en mode « log uniquement » + notification push (si disponible) — car si personne n'a réagi en 24h, le problème est ailleurs

**Fréquence de répétition :** Message complet toutes les 30 secondes, pause de 5 secondes entre répétitions. Assez fréquent pour être entendu, pas assez pour devenir un mur de son.

---

## 4. PRIORITÉ VOCALE

**Oui, l'alerte doit bloquer les autres voix.** C'est le comportement correct. Une alerte = urgence absolue. `killall say` est la règle maison, elle doit être respectée. MAIS : l'alerte vocale doit avoir un **identifiant unique** (ex. `ALERTE_VEILLEUSE_20260815_1430`) pour que le kill-switch `STOP_ALERTE` soit précis et ne tue pas une autre alerte en cours.

---

## VERDICT : **GO-AVEC-RÉSERVE**

Le design est solide et répond à l'exigence de Christophe. Les réserves portent sur :
1. La gestion de la nuit (limite de sécurité nécessaire)
2. Le registre doit être strictement limité aux fichiers de production
3. Le RELEASE_RECEIPT doit être rendu obligatoire pour éviter les faux positifs

## CONFIANCE : **78 %**

## HYPOTHÈSES :
1. Christophe accepte une atténuation nocturne de l'alerte vocale (volume réduit, fréquence espacée) — sinon, boucle infinie stricte 24h/24
2. Les scripts de production sont stables et ne se modifient pas eux-mêmes (sinon, faux positifs systématiques)
3. Le système launchd est fiable et les plists sont correctement configurées

## CE QUI CHANGERAIT L'AVIS :
- **Basculerait vers NO-GO** : si Christophe refuse toute atténuation nocturne ET que le système doit tourner 24h/24 sans surveillance humaine — nuisance permanente inacceptable
- **Basculerait vers GO** : si Christophe confirme explicitement l'acceptation de l'atténuation nocturne + engagement à maintenir le RELEASE_RECEIPT à jour

## AMÉLIORATIONS PROPOSÉES :
1. **Journal d'alerte structuré** : chaque alerte vocale écrit un fichier `ALERTE_[horodatage].json` avec le message, la cause, l'heure — pour traçabilité après coup
2. **Test d'auto-vérification** : la veilleuse vérifie elle-même son propre md5 (auto-intégrité) pour détecter une compromission de la veilleuse
3. **Mode silencieux programmé** : si une maintenance est planifiée (ex. mise à jour), un fichier `MAINTENANCE_PREVUE` suspend les alertes pour une durée définie — évite les fausses alertes pendant les interventions légitimes

---

## SYNTHÈSE (5 lignes max)

Registre des synapses limité aux fichiers de production (30-50 entrées) avec RELEASE_RECEIPT obligatoire pour toute modification. Veilleuse à 10 min vérifiant md5, process, fraîcheur des données — distinguant clairement intrusion vs panne. Alerte vocale en boucle avec atténuation nocturne (volume réduit, fréquence espacée) et limite de sécurité à 24h. Priorité vocale absolue avec identifiant unique pour kill-switch précis. GO-AVEC-RÉSERVE, confiance 78 %, conditionné à l'acceptation de l'atténuation nocturne par Christophe.
