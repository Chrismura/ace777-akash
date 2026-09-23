# SYNTHÈSE FAMILLE — 23/09/2026 — le garde-fou des seuils, jugé par 4 modèles

> Brief : la faute de méthode (seuil recalculé de mémoire : 5-12,75 % annoncés, 21,70 %
> réels), le garde-fou construit, ce qu'il a trouvé, les 3 mesures. Mission donnée :
> **CONTREDIRE, pas approuver** (nommer l'angle mort, la classe d'erreur suivante, la
> priorité, et l'erreur que je commets sans la voir).
> Avis complets : `AVIS_*.md` (même dossier). **Aucun avis n'a été appliqué sans mesure.**

## 1. Les quatre verdicts — UNANIMES : « insuffisant mais utile »

| modèle | verdict sur le garde-fou | confiance | priorité qu'il choisit |
|---|---|---|---|
| Google Gemini | insuffisant mais utile | **75 %** | **(C)** la taille (plafond sur un carnet fictif = risque systémique) |
| Nemotron-120b (le juge) | insuffisant mais utile | **80 %** | **(B)** le seuil — puis (A) si les pertes dépassent le risque annoncé |
| x-ai Grok | insuffisant mais utile | **70 %** | **(A)** le stop qui ne tient pas (« hémorragie directe ») |
| DeepSeek-V3 | insuffisant mais utile | **70 %** | **(C)** la taille |

**Aucun ne l'a jugé suffisant, aucun ne l'a jugé inutile. C'est le verdict le plus utile
qu'on pouvait recevoir** — et il est plus dur que le mien.

## 2. Les trous qu'ils nomment (et ce que j'en ai fait DANS LA JOURNÉE)

| # | objection | source | traitement |
|---|---|---|---|
| 1 | **Le gardien suppose la configuration STATIQUE** : si on change `DIP_CADENCE_MULT` ou un profil entre deux passages, il compare aux NOUVELLES valeurs et peut tout déclarer conforme. | Gemini · Nemotron | **FAIT** : l'état porte désormais les **empreintes md5** de `defaults.env` et `universe_profils.json`, et **crie une dérive de config** (avec l'avertissement décisif : si le moteur n'a pas été relancé, ses décisions reposent sur les ANCIENS paramètres → un désaccord serait alors légitime). |
| 2 | **Aucune preuve de son taux de faux négatifs.** « Confondre *détection d'une erreur connue* et *garantie d'aucune erreur non détectée*. » | Nemotron (n°5) | **FAIT** : l'autotest n'injecte plus UNE erreur mais **5 troncatures différentes sur 3 régimes** (cadence dominante / plancher / m6 dominant) → **7/7 erreurs discriminantes détectées (100 %)**, et il **refuse de compter comme échec un cas non discriminant**. Ce faisant, mon propre autotest m'a attrapé : il criait « cassé » sur des injections qui n'étaient pas des erreurs au point testé. |
| 3 | **Aucun slippage / mesure d'impact** : « vos gains sont mathématiquement surévalués sur des micro-caps ». | Gemini · Grok · DeepSeek | **MESURÉ, PAS PROMIS** : le slippage est devenu un paramètre du replay. Résultat (`REPLAY_SLIP_BPS`) : E0+X4 −3,93 $ → **−6,79 $** et E2+X2 +59,42 $ → **+48,86 $** à **45 bps/côté** (9× le coût supposé, au-dessus du spread mesuré de la plupart des paires), 1re moitié **+13,31 $ (positive)** ⇒ **le levier ne meurt pas au slippage réel** ; c'est la règle ACTUELLE qui est fragile au coût (beaucoup de petits trades). |
| 4 | **Biais de source unique** : « si le moteur applique une formule fausse et que le gardien duplique la MÊME logique, les deux mentent de concert ». | Grok | **NON TRAITÉ — et c'est le trou le plus juste.** Mon invariant prouve la **cohérence**, il ne prouve pas la **justesse**. Le seul remède propre : un **oracle indépendant** (rejouer la kline brute et vérifier le signal d'entrée enregistré, en court-circuitant la logique interne). C'est un chantier, à GO. |
| 5 | **Pas de test en marché baissier / flash crash** (nommé par **les quatre**). | tous | **NON TRAITÉ** : 90 j klines, 21 j de run, **un seul régime haussier** (BTC +12,3 %, 20/20 paires en hausse). Aucun des mes chiffres ne dit ce que la règle fait quand tous les « dips » sont des couteaux qui tombent. Chantier, à GO. |
| 6 | **L'écosystème n'est pas couvert** (notebooks, exports CSV, outils de reporting qui recalculent un seuil sans passer par le détecteur). | DeepSeek | **PARTIELLEMENT** : le détecteur balaie `hulk-mexc/scripts` + `Index_Maison/scripts`. Pas les notebooks/exports (il n'y en a pas dans le dépôt aujourd'hui, mais rien ne le garantit demain) → à déclarer. |
| 7 | **Contrôle par lot de 3 h** : un écart peut vivre 3 h. | Nemotron | **NON TRAITÉ** : cadence à renforcer (à GO — pose d'un agent). |

## 3. Ce qu'ils m'ordonnent de regarder en premier (désaccord, et il est instructif)

- **(C) la taille** (Gemini 75 %, DeepSeek) : « un plafond à 2 641 % de la profondeur réelle
  est un risque systémique ».
- **(B) le seuil** (Nemotron 80 %) : c'est la faute qui a produit la sur-exposition.
- **(A) le stop** (Grok 70 %) : « un stop qui glisse de 8 % à 39 % détruit l'asymétrie
  mathématique de la stratégie ; c'est une hémorragie directe ».

**Je ne tranche pas à leur place** : les trois sont chiffrées, et le désaccord dit surtout
qu'**aucune des trois n'est assez mesurée pour être priorisée objectivement** — ce qui est
en soi la conclusion (le prochain chiffrage doit porter sur (A), la seule qui **détruit du
capital** plutôt que d'en manquer ; Grok le dit et mes propres chiffres le confirment :
−4,19 $ d'exits dégradés contre +3,06 $ de gains sur RIZE).

## 4. Déclaration d'honnêteté sur la consultation

- Quatre modèles, mais **l'en-tête de l'avis Grok indique un provider « Google Gemini »** :
  les quatre opinions ne sont donc peut-être **pas quatre backends indépendants**. À traiter
  comme des avis motivés, pas comme un quorum.
- Ils ont répondu **sans accès au code** (brief en texte seul) : leurs objections sont de
  méthode, pas d'implémentation.
- Aucun avis n'a été appliqué sans être **transformé en mesure** (md5 de config, batterie
  d'injections, courbe de slippage).

## 5. Le mot que je retiens

> « Le garde-fou résout un problème de transcription humaine mais pas la justesse
> intrinsèque du modèle mathématique. » (Grok)

C'est exactement la distinction que je n'avais pas faite : **cohérence ≠ justesse**. Le
garde-fou ferme la classe d'erreur *« chiffre recalculé de mémoire »*. Il ne ferme **pas**
la classe *« le chiffre est fidèle et la règle est mauvaise »* — et cette seconde classe ne
se ferme qu'avec un **oracle indépendant** et un **marché qui descend**.
