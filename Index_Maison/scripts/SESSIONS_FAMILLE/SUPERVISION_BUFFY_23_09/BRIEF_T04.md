# TOUR 4 — LE JURY EST RÉPARÉ, ET LA QUESTION « POURQUOI PAS LES DEUX ? » A UNE RÉPONSE MESURÉE

Trois choses ont changé depuis le tour 3, et deux d'entre elles viennent de Christophe, pas de moi.

## 1. VOUS N'ÉTIEZ PAS 3 VOIX, ET C'ÉTAIT UN DÉFAUT DE LA PLOMBERIE — CORRIGÉ

Christophe a dit : *« et oui pour le hub, ça me semble logique, vu que c'est toi qui t'en es
occupé, tu as encore une œuvre de merde qui ne marche pas »*. Il a raison, et voici ce qui se
passait, **mesuré** :

- Le hub (le routeur local qui vous appelle) a un « **filet universel** » : *« plus jamais à sec
  tant qu'UN fournisseur répond »*. Sur échec/lenteur, il **remplace** le modèle demandé par un
  autre et le signale (`substitue: true`).
- Effet mesuré : au tour 2, « DeepSeek » a été répondu par **Gemini** ; au tour 3, **les trois
  voix** ont été répondues par **Gemini** → vous n'étiez **qu'UNE voix**, trois fois.
- **Ce que fait le milieu** (ensembles d'évaluateurs, appels multi-fournisseurs) : on **épingle**
  le modèle, on **vérifie qui a répondu** (`response.model`), et une voix substituée est traitée
  comme un **échec d'appel**, jamais comme un avis. Sinon on additionne des erreurs corrélées en
  croyant moyenner des opinions indépendantes.

**Ce que j'ai câblé** : un mode `strict_model` dans le hub (aucun filet, échec franc si le modèle
n'est pas servi) + un test du jury **avant chaque tour**.

**Résultat du test à l'instant** (c'est vous, en direct) :

| demandé | réponse | fournisseur |
|---|---|---|
| `nvidia/nemotron-3-super-120b-a12b:free` | **lui-même** ✔ | OpenRouter Juge |
| `deepseek-ai/DeepSeek-V3-0324` | **lui-même** ✔ | HuggingFace |
| `x-ai/grok-4.3` | **échec 502 — voix indisponible** (plus de faux) | Puter Grok |
| `nex-agi/nex-n2.5-pro:free` | **lui-même** ✔ | Roulement nex-agi |

→ **3 voix indépendantes réelles, quorum atteint.** Détail qui compte : avec le filet, DeepSeek
**semblait** absent (servi par Gemini) alors que **son fournisseur répondait** — le filet masquait
une voix disponible. Autrement dit : la plomberie fabriquait la panne qu'elle prétendait couvrir.

## 2. « POURQUOI NE PAS FAIRE LES DEUX ? » — LA RÉPONSE EST MESURÉE

Christophe a refusé mon « arbitrage » : *« pourquoi ne pas faire les deux ??? »*. Il a raison, et
l'industrie fait exactement ça : **on ne lit pas le carnet, on l'écoute.**

J'ai ouvert un **flux WebSocket** MEXC (`wss://wbs-api.mexc.com/ws`,
`spot@public.aggre.bookTicker.v3.api.pb@10ms|100ms@<paire>`) et mesuré, deux fois :

| | REST (`/depth`, ce que fait le moteur) | **WebSocket (push)** |
|---|---|---|
| âge du prix, médiane | **1 058 ms** | **14–15 ms** |
| p90 | 2 020 ms | **81 ms** |
| part sous 1 s (la barre que vous avez fixée) | **22,7 %** | **100 %** (456/456 puis 610/610 échantillons) |
| cadence par paire | 1 lecture par cycle | **11 ms sur RIZE/TEL (10 ms), 100 ms sur ZBCN/BTC** |
| coût pour mesurer la chute | 2 lectures + **0,5 s d'attente voulue** | **la frise des messages, aucune attente** |

**Donc les deux, en même temps** : la fraîcheur (14 ms au lieu de 1 058 ms) **et** la mesure de la
chute par seconde (sur la frise des messages). Mon « arbitrage » était un faux dilemme — la limite
venait de **ma méthode de lecture**, pas de la barre que vous aviez fixée. **Je retire l'arbitrage.**

**Ce que je ne prétends pas** : les trames MEXC sont en **protobuf** et cette sonde ne décode que
le JSON → **la chute n'est pas mesurée ici**, seulement la frise qui la rendra mesurable. Le
câblage (snapshot REST + deltas du flux, méthode documentée par MEXC elle-même) **touche le
moteur** : il attend le GO de Christophe. Je ne l'ai pas fait, je ne le déclare pas fait.

## 3. E20 — MES CHIFFRES DU TOUR 1 ÉTAIENT FAUX ENVERS MOI-MÊME

Rappel du tour 3 : l'instrument qui a produit la boucle que vous avez validée jugeait les entrées
contre le **plancher du profil** au lieu du **seuil effectif** `max(plancher ; DIP_CADENCE_MULT ×
cadence)`. C'est **le gardien `verif_seuil_moteur.py` qui l'a crié**, pas moi.

| chiffre soumis au tour 1 | chiffre vrai |
|---|---|
| **28 %** d'entrées conformes | **5 % (3/60)** |
| `remploi de cash` 7/26 | **1/26** |
| `impulsion/pullback` 7/14 | **1/14** (seuil médian **13,20 %**) |
| `re-entrée après dump` 5/7 | **1/7** (seuil médian **8,44 %**) |
| `cooling` 0/13 | **0/13 — inchangé** |

**Vos reproches de conception sortent plus forts, pas plus faibles** : même les familles qui
annoncent une condition de baisse ne tiennent pas le seuil du moteur. Et je le redis pour que ce
soit au fil : les seuils dominés par la cadence sont **EDEL 13,20 % · RIZE 8,44 % · CHIP 6,69 % ·
QAIT 5,60 % · RED 5,01 %** ; ailleurs c'est la porte pullback (5 %) qui gouverne.

## 4. CE QUE JE VOUS DEMANDE (3 questions, courtes)

1. **Votre verdict du tour 1 tient-il**, sachant que « les défauts de conception » avaient été
   établis sur un compteur **5 fois trop indulgent** (corrigé contre moi) ?
2. **Validez-vous la direction WebSocket** comme réponse à votre exigence n°1 (latence < 1 s) —
   avec le chiffre que je viens de produire (14 ms médian, 100 % sous la barre) — ou exigez-vous
   autre chose avant de considérer ce point clos ?
3. **Le plafond de stop à 15 % sur RIZE** : le gain mesuré est **+0,87 $ sur 10 jours** et je
   propose de **ne pas toucher au moteur** pour 0,87 $ (R17/R18 : toute modification du risque se
   chiffre, et on ne modifie pas un moteur en service pour un gain marginal). **Contredisez-moi
   avec un chiffre si je me trompe** — c'est le seul endroit du dossier où je prends une position.

Répondez en 3 sections : VERDICT / CE QUE J'EXIGE AVANT LE PROCHAIN TOUR / CE QUI ME FERAIT
CHANGER D'AVIS. Étiquetez chaque chiffre MESURÉ / ESTIMÉ / INSUFFISANT. Vous êtes **3 voix
indépendantes vérifiées** (Nemotron, DeepSeek, nex-agi ; Grok est en panne 502 et **ne vote pas**).
