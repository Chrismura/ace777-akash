# MÉTHODE DÉFINITIVE — LE HUB NE DOIT PLUS JAMAIS ÊTRE À SEC
*Rédigé par Buffy le 16/08 après lecture complète de `hub_prise_ia.py` (740 lignes) + historique des réparations. À passer au codeur + famille.*

---

## 1. Le schéma : comment le hub fonctionne (aujourd'hui)

**Rôle** : `prise-ia/hub_prise_ia.py` = **routeur LLM**, une seule porte (`:11435`).
Chaque **tâche** (`code.ia`, `analyste.strategie`, `cortana.analyse`…) est routée vers une **chaîne de providers** : `principal → fallback → secondary` (3 maillons max, lus dans `routing.json`).

**Les garde-fous déjà en place** (hérités des réparations 09-13/08) :
- **Budget cloud** : `cloud_daily_budget = 624` appels/jour → au-delà, bascule sur les gratuits.
- **Blacklist / backoff** : 3 échecs consécutifs → pause 15 min → 30 min → 1 h → 2 h → 4 h.
- **PATIENCE** : un provider *lent* n'est pas un échec (retry 1× avec timeout ×3).
- **Anti-fleau réseau** : DNS/connexion KO → bascule immédiate (pas de punition).
- **Filet de dernier recours** : si *tous* les providers étaient blacklistés → 1 tentative sans blacklist.

**L'inventaire réel** : **20 providers** configurés, dont **~15 gratuits et actifs** (gemini, nvidia, openrouter-free/juge/ultra, puter-grok, Qwen3-Coder, deepseek-coder, Devstral, 4× nemotron-nano, north-mini-code…).

---

## 2. Les 3 trous (pourquoi on retombe TOUJOURS à sec malgré les réparations)

### 🔴 Trou n°1 — La chaîne ne fait que 3 maillons, et rien ne la prolonge
Quand `gemini → openrouter-ultra → nvidia` échouent tous (429), le hub lève
`"Toutes les IA branchées ont échoué"` et **s'arrête** — sans jamais essayer les
~15 autres providers gratuits actifs. → **C'est exactement « à sec avec 10 offres
en file d'attente »** : les offres existent, mais le routeur ne les atteint jamais.
Le « filet de dernier recours » ne se déclenche QUE si les providers sont
*blacklistés* (`tried == 0`), jamais quand ils échouent simplement.

### 🟠 Trou n°2 — Le 429 est mal géré
`429 Too Many Requests` n'est PAS dans la liste « non retryable » (401/402/403/404).
Donc le hub fait une « PATIENCE » : retry après 3 s avec timeout ×3. Or un quota
ne se réinitialise **pas en 3 s** → le retry est inutile, et il bouffe le budget
temps au lieu de basculer vite sur le provider suivant. Le `Retry-After` n'est pas lu.

### 🟡 Trou n°3 — Le budget 180 s est mangé par le 1er provider lent
Le retry (`min(base*3, 900)`) n'est **pas borné** par le budget de requête (180 s).
Un provider lent peut donc manger 180 s + 540 s de retry → les maillons suivants
n'ont plus de temps et ne sont jamais tentés.

### 📌 Ce que l'historique montre
Les réparations (09/08 blacklist, 11/08 swaps, 13/08 campagne anti-fleau, 14/08
grok…) ont toutes été des **patchs sur la même architecture à 3 maillons**. Le
**filet universel** (« si la chaîne échoue → essayer TOUT le reste ») n'a **jamais
été ajouté**. C'est pour ça que ça retombe à chaque fois.

---

## 3. La méthode (refonte du failover, 4 règles — pas un patch de plus)

**Principe unique** : *le hub ne rend la main que quand TOUS les providers actifs ont
été tentés, pas seulement les 3 de la chaîne.*

### Règle 1 — Filet universel
Après la chaîne de la tâche, si tout a échoué → **essayer tous les providers actifs
restants** (triés par `order`), chacun avec une part du budget. (~15 lignes dans
`chat_completions`, juste après la boucle actuelle.)

### Règle 2 — 429 = bascule immédiate
Ajouter `429` à la catégorie non-retryable → **pas de retry**, bascule immédiate +
pause courte (60 s, ou `Retry-After` si présent). Le quota se réinitialise pendant
qu'on utilise les autres.

### Règle 3 — Budget PAR provider (au lieu d'un budget global mal réparti)
Chaque provider a droit à une part du budget : `180 s ÷ nb de providers restants`
(plancher 15 s). Un provider lent ne peut plus tout manger. Le retry est borné par
cette part, plus de `×3` illimité.

### Règle 4 — Anti-tempête par tâche (prévention)
Si une tâche (ex. `analyste.strategie`) échoue `429/502` N fois en X min → **mettre
cette tâche en pause 5 min** (throttling). C'est ce qui aurait empêché le
raz-de-marée des 13 vigies → analyste → 429 partout (aujourd'hui).

### Résultat attendu
Tant qu'il reste **1 provider gratuit actif qui répond**, le hub répond. Le
« roulement automatique » devient réel : il roule sur les ~15 gratuits, plus sur 3.

---

## 4. Ce qu'on NE touche PAS
- **`providers.json`** : les providers sont bons (les 2 codeurs intégrés aujourd'hui restent).
- **`routing.json`** : les chaînes restent telles quelles (elles expriment la *préférence*,
  pas la limite). Le filet universel s'ajoute EN DESSOUS.
- **Aucune nouvelle brique, aucun nouveau fichier** : tout se passe dans `hub_prise_ia.py`
  (fonctions `chat_completions` + `call_provider`, ~40 lignes au total).

---

## 5. Plan
| Étape | Qui |
|---|---|
| 1. Implémenter les 4 règles dans `hub_prise_ia.py` (backup + validation `py_compile`) | codeur (ou Buffy en codeur externe si hub KO) |
| 2. Test réel : couper les 3 providers de la chaîne → vérifier que le filet universel répond via un autre | codeur + Buffy |
| 3. Validation famille (maker ≠ checker) | famille |
| 4. GO Christophe → redémarrage hub | Christophe |

*Rien n'est modifié dans cette méthode — c'est une feuille de route, pas un correctif appliqué.*
