# AVIS CODEUR (task code.ia) — AVANT FUSION

provider: NVIDIA build.nvidia.com (100+ modeles)

Parfait. On a un état réel mesuré, une spec validée, et une étape de fusion qui arrive. Avant de casser quoi que ce soit, on va **simplifier et préparer le terrain**. Voici mon analyse technique, concrète et actionnable.

---

### 1. Améliorations à faire MAINTENANT (avant la fusion)

Oui, il y a **3 actions immédiates** qui simplifieront drastiquement la fusion :

**A. Supprimer `com.ace777.verif-setup` (mort)**
- C'était un service de vérification initiale. Il a fait son travail. Le `state.json` et le superviseur le remplacent.
- **Action :** `launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.ace777.verif-setup.plist` puis `rm` le plist.
- **Pourquoi :** Un service de moins à analyser, fusionner, ou désactiver.

**B. Fusionner `com.ace777.heartbeat` + `com.ace777.pulse-sous-loeil` + `com.ace777.vigie` en UN SEUL service `com.ace777.superviseur`**
- Ce sont les 3 services de monitoring de base. Ils se marchent dessus.
- **Action :** Créer un script unique `superviseur_core.sh` qui fait les 3 checks (présence, heartbeat, alerte). Désactiver les 3 anciens, charger le nouveau.
- **Pourquoi :** C'est la **colonne vertébrale** de la fusion. On la construit AVANT de tout casser.

**C. Préparer le terrain pour `com.ace777.analyste-cadence` et `com.ace777.observatoire`**
- Ce sont des services de "tri/analyse" qui seront absorbés par le superviseur.
- **Action :** Ne pas les désactiver maintenant, mais **documenter dans un fichier `FUSION_MAP.md`** ce qu'ils font, et ce que le superviseur doit reprendre d'eux.
- **Pourquoi :** On sait exactement quoi absorber, sans avoir à relire le code de chaque service pendant la fusion.

---

### 2. Comment SIMPLIFIER la fusion ? (Ordre et colonne vertébrale)

**Ordre de désactivation (du plus simple au plus complexe) :**

1. **Phase 0 (Préparation) :** Supprimer `verif-setup`. Créer le `superviseur_core.sh`. Tester manuellement.
2. **Phase 1 (Monitoring) :** Désactiver `heartbeat`, `pulse-sous-loeil`, `vigie`. Activer `superviseur` (qui les remplace).
3. **Phase 2 (Tri/Analyse) :** Désactiver `analyste-cadence`, `observatoire`, `analyse-usage`. Le superviseur absorbe leurs fonctions (via des hooks dans `superviseur_core.sh`).
4. **Phase 3 (Redondants) :** Désactiver `surveillance-quotas` (absorbé par le superviseur), `propose-ameliorations` (absorbé par le superviseur), `eval-offres` (absorbé par le superviseur).
5. **Phase 4 (Nettoyage) :** Désactiver les services qui ne sont plus nécessaires après absorption (ex: `graph-cerveau` si le superviseur gère le graphe, `rotation-logs` si le superviseur gère les logs).

**Colonne vertébrale à garder :**
- `com.ace777.state-generator` (source de vérité)
- `com.ace777.backup-check` (contrôle backup)
- `com.ace777.cockpit-http` et `com.ace777.cockpit-pont` (interface)
- `com.ace777.cortana.horaire` et `com.ace777.cortana.urgent` (vocal, protégé)
- `com.ace777.superviseur` (NOUVEAU, le chef d'orchestre)

---

### 3. Les 3 RISQUES principaux de la fusion

**Risque 1 : Le superviseur unique devient un goulot d'étranglement**
- **Problème :** Si le superviseur tombe, tout tombe.
- **Solution :** Le superviseur doit être **léger** (un script bash simple, pas un monstre Python). Il doit écrire dans `state.json` en continu. S'il tombe, `launchd` le relance automatiquement (KeepAlive). Et le `state.json` reste la source de vérité, donc les autres services peuvent continuer à fonctionner en mode dégradé.

**Risque 2 : Perte de fonctionnalités lors de l'absorption**
- **Problème :** On fusionne des services, mais on oublie une fonctionnalité critique.
- **Solution :** Avant de désactiver un service, **lire son plist et son script**. Noter dans `FUSION_MAP.md` ce qu'il fait. Le superviseur doit avoir des **hooks** (fonctions) pour chaque fonctionnalité absorbée. Tester chaque hook individuellement.

**Risque 3 : Conflit de timing avec `launchd`**
- **Problème :** Deux services qui se chevauchent (ex: `state-generator` toutes les 120s et `superviseur` qui lit `state.json` toutes les 60s).
- **Solution :** Le superviseur doit **lire** `state.json` (pas le modifier). Le `state-generator` est le SEUL à écrire. Le superviseur doit avoir un intervalle **plus long** que le `state-generator` (ex: 300s). Éviter les courses.

---

### 4. Le superviseur unique doit absorber en priorité

**Priorité 1 (Critique) :**
- `com.ace777.heartbeat` (monitoring de base)
- `com.ace777.pulse-sous-loeil` (surveillance)
- `com.ace777.vigie` (alerte)

**Priorité 2 (Important) :**
- `com.ace777.analyste-cadence` (analyse de rythme)
- `com.ace777.observatoire` (observation)
- `com.ace777.analyse-usage` (analyse d'usage)

**Priorité 3 (Secondaire) :**
- `com.ace777.surveillance-quotas` (surveillance des quotas)
- `com.ace777.propose-ameliorations` (propositions)
- `com.ace777.eval-offres` (évaluation des offres)

**À NE PAS ABSORBER (garder séparés) :**
- `com.ace777.cortana.horaire` et `com.ace777.cortana.urgent` (vocal, protégé par la loi)
- `com.ace777.cockpit-http` et `com.ace777.cockpit-pont` (interface)
- `com.ace777.state-generator` (source de vérité)
- `com.ace777.backup-check` (contrôle backup)

---

### 5. Verdict : AMELIORER D'ABORD

**La fusion n'est PAS prête à être conçue.** Il faut d'abord :

1. **Supprimer `verif-setup`** (mort).
2. **Créer le `superviseur_core.sh`** (la colonne vertébrale) et le tester manuellement.
3. **Créer `FUSION_MAP.md`** pour documenter ce que chaque service fait, et ce que le superviseur doit absorber.

Une fois ces 3 actions faites, la fusion sera **simple et mécanique** : on désactive les services un par un, on vérifie que le superviseur fonctionne, et on passe au suivant.

**En résumé :** On ne fusionne pas pour fusionner. On **prépare le terrain** pour que la fusion soit un simple "copier-coller" de fonctionnalités dans un script unique, sans risque de perte.

---

**Prochaine action concrète :** Je te propose de créer le `superviseur_core.sh` (avec les hooks pour heartbeat, pulse, vigie, et les analyses de base). Dis-moi si tu veux que je te le code, ou si tu préfères d'abord faire le nettoyage de `verif-setup`.
