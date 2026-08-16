# AVIS GEMINI (task gemini.analyse, provider NVIDIA build.nvidia.com (100+ modeles), 119.7s)

**VERDICT : GO-AVEC-RÉSERVES**

**CONFIANCE : 78 %**

---

**1. VERDICT DÉTAILLÉ**

Le pré-vol est solide sur le principe : vérifier la **traversée** (maillon par maillon) plutôt que la seule existence des fichiers est LA bonne réponse au problème posé. La plist 5 min est un bon compromis entre réactivité et bruit. Le cockpit 🩺 est l'interface « un coup d'œil » demandée.

**Réserves :**
- **Seuil d'âge** : « fichier frais » — quel âge max ? Si c'est 5 min (aligné plist), un marché calme (append-only vide) peut déclencher un faux positif. Si c'est 15-30 min, on rate une vraie panne pendant 3 cycles. **Information insuffisante** sur les seuils exacts par chaîne.
- **Process label** : « process vivant » — si le process est relancé par launchd avec un PID différent mais un label identique, `pgrep` par nom peut rater (ex. `python3` vs `python3.11`). Vérifier que le matching est par **label launchd** ou **chemin absolu**, pas par nom de process générique.

---

**2. LES 6 CHAÎNES — MANQUES**

| Chaîne | Verdict | Commentaire |
|--------|---------|-------------|
| BALEINES | ✅ | Bien définie (scan→pont→live.json→consommateurs). |
| HULK | ✅ | Sonde→CSV aspiration : correct. |
| LIVE | ✅ | Thermo→mission→cockpit : correct. |
| CPFP | ⚠️ | « Observation 7j » — seuil d'âge ? Si le fichier est mis à jour 1×/jour, 5 min de fraîcheur = faux positif permanent. **Information insuffisante**. |
| SÉCURITÉ | ✅ | Veilleuse : correct. |
| SAISON | ✅ | 6 indices : correct. |

**Chaînes manquantes :**
1. **HUB LLM** (si Ada/Cortana passent par un hub central) — si le hub tombe, toutes les chaînes en aval deviennent rouges en cascade → bruit. À isoler comme chaîne dédiée.
2. **GIT PUSH AUTO** — si le push échoue silencieusement, les sauvegardes sont fausses. C'est un maillon « sortie » critique.
3. **SCAN BALEINES SEUL** — le problème initial était « scan tourne mais pont mort ». La chaîne BALEINES couvre ça, mais vérifier que le scan est bien un maillon **distinct** (pas fusionné avec le pont dans le code).

---

**3. FAUX POSITIFS / FAUX NÉGATIFS**

**Faux positifs (crier à tort) :**
- Fichier append-only vide sur marché calme (CPFP, SAISON) → chaîne rouge alors que tout va bien.
- Process relancé avec PID différent mais même label → détecté comme « mort » si matching par PID.
- Latence réseau transitoire (1-2 s) entre écriture fichier et lecture consommateur → rouge si le check est trop strict.

**Faux négatifs (rater) :**
- Fichier **présent et frais mais vide** (0 octet) — le check « donnée présente » doit vérifier **taille > 0** ET **contenu non vide** (ex. JSON `{}`).
- Process vivant mais **bloqué** (deadlock, attente I/O) — le process est là, le fichier est frais, mais rien ne traverse. **C'est LE faux négatif le plus dangereux** : il reproduit exactement le problème initial (scan tournait, pont mort).

---

**4. ALERTE VOCALE — PERTINENCE ET ESCALADE**

**Pertinente : oui**, mais avec escalade progressive pour éviter la sur-alerte :

1. **Log** (immédiat) : transition rouge → append-only + timestamp.
2. **Carte rouge cockpit** (1er cycle, 5 min) : visible mais silencieux.
3. **Voix** (2e cycle consécutif, 10 min) : seulement si la chaîne est **toujours rouge** après un cycle de recheck.
4. **Escalade humaine** (3e cycle, 15 min) : notification push/SMS si la chaîne est critique (BALEINES, SÉCURITÉ).

**Règle anti-bruit** : une chaîne qui passe rouge puis verte dans le même cycle (transitoire) ne déclenche **jamais** la voix. Seuil : 2 cycles consécutifs.

---

**5. AMÉLIORATION PROPOSÉE (clause permanente)**

**Idée principale : « MAILLON TÉMOIN » — un test de bout en bout synthétique.**

Injecter un **fichier factice signé** (ex. `sante_test.json` avec un payload connu) dans la chaîne BALEINES toutes les 5 min, et vérifier qu'il **ressort chez Ada/Cortana** avec le bon contenu. Si le témoin ne traverse pas, la chaîne est rouge — même si tous les fichiers « réels » semblent frais.

**Pourquoi ça change tout** : ça détecte le **faux négatif n°1** (process vivant mais bloqué, fichier frais mais non consommé). C'est le seul moyen de prouver que la donnée **traverse réellement**, pas juste qu'elle existe.

**Idées secondaires :**
- **Seuil d'âge dynamique** par chaîne (CPFP : 24 h, LIVE : 5 min, etc.) — configurable, pas un seuil global.
- **Check « taille > 0 ET contenu non vide »** pour tous les fichiers JSON (évite le faux positif « fichier vide »).

---

**HYPOTHÈSES**
1. Les seuils d'âge sont **configurables par chaîne** (pas un global) — sinon CPFP/SAISON seront en faux positif permanent.
2. Le matching process se fait par **label launchd ou chemin absolu**, pas par nom générique.
3. Le cockpit est accessible **sans authentification** (lecture seule) pour un coup d'œil rapide.

---

**CE QUI CHANGERAIT L'AVIS**
- **Preuve que le maillon témoin est implémenté** (ou au moins prévu) → GO sans réserve.
- **Seuils d'âge documentés par chaîne** (pas de global) → lève la réserve principale.
- **Détection de fichier vide (0 octet) comme rouge** → élimine le faux négatif critique.

---

**SYNTHÈSE (5 lignes)**
Le pré-vol est bien conçu : vérifier la traversée plutôt que l'existence est la bonne réponse. Réserves : seuils d'
