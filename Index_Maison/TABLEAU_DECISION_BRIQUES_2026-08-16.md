# TABLEAU DE DÉCISION — FINIR / JETER / OBSERVER (16/08)
*Rédigé par Buffy (superviseur) après vérification RÉELLE des fichiers, process et launchd. À soumettre à la famille pour verdict. Le constat de Christophe est confirmé : « on a presque tout, mais ça marche à moitié ». Cause racine : on spécifie vite, on finit lentement, le mode observation devient permanent.*

---

## RÈGLE PROPOSÉE (1 phrase)
**Un chantier à la fois, fini = ça décide ou ça agit (pas juste ça observe).** Toute brique en observation depuis > 7 jours sans date de décision est soit FINIE, soit JETÉE.

---

## LE TABLEAU (état vérifié le 16/08 20h)

| # | Brique | État RÉEL vérifié | Décision proposée | Justification |
|---|---|---|---|---|
| 1 | **Hub LLM** (prise-ia) | ✅ tourne, 4 règles + filet universel, testé réel (chaîne morte → réponse) | ✅ **FINI — garder** | Réparé aujourd'hui. La preuve : les 2 specs envoyées au codeur ont répondu via le filet (Gemini) pendant que la chaîne était saturée |
| 2 | **HULK paper** (15 positions) | ✅ tourne, process en vie, 15 seedées | ✅ **FINI — garder** | Vérifié : process 47852 en vie, 15 positions, EDEL réintégré |
| 3 | **Vigie temps réel** (vigie_live) | ✅ tourne (1 process — après kill des 13 doublons), timeout WS + pkill ajoutés | ✅ **FINI — garder** | Correctif appliqué aujourd'hui (moi en codeur externe) + spec envoyée au codeur pour le fix complet |
| 4 | **Pont gate** (:11439) | ✅ tourne, fail-closed 503 | ✅ **FINI — garder** | Vérifié process + log récent |
| 5 | **Cortana + pont cockpit** | ✅ tourne, bridge :17777 | ✅ **FINI — garder** | Vérifié process 66810 |
| 6 | **CPFP onchain** (detecter_cpfp) | ⚠️ tourne mais **MODE OBSERVATION** (silencieux, ne décide rien) | ⚠️ **OBSERVER — date butoir : 23/08** | Le mode observation sert à calibrer les seuils. Mais sans date, c'est éternel. Décision au 23/08 : passer ACTIF ou jeter |
| 7 | **Pépite vigie mempool** (tx fantômes / bloc privatisé) | ❌ **PAS BRANCHÉ** (aucun script ni plist ; spec envoyée au codeur aujourd'hui) | 🔧 **FINIR** | Spec + réponse codeur prêtes → brancher en vigie continue + Carte 4 CPFP |
| 8 | **Juge GLM-5.2 / disjoncteur −1,5 %** | ❌ **N'EXISTE PAS** (aucun script ; juste un prompt en commentaire + concept de Christophe) | 🔧 **FINIR** | C'est LA brique de sécurité manquante : coupe tous les bots à −1,5 % + réécriture d'ordre bridée. Dimensionner au capital (C7 = 8 %) |
| 9 | **Risk Guardian** (kill switch DD 8 %) | ❌ **ABSENT** (fichier n'existe pas ; documenté "prototype, pas en vol") | 🔧 **FINIR** (fusionner avec #8) | Le disjoncteur et le Risk Guardian font la même chose → UNE seule brique, pas deux |
| 10 | **ADA gardienne** | ⚠️ reflète + alerte, mais **ne peut rien bloquer** (voilure informative) | ⚠️ **OBSERVER — date butoir : 23/08** | Son rôle est d'informer, pas de bloquer — OK si on assume. À confirmer |
| 11 | **Règle de confiance pondérée** (score → exposition) | ⚠️ score_justesse + routeur_auto existent mais **pas branchés sur l'exposition** | 🔧 **FINIR** (étape 2, après #8) | Évolution "niveau expert" — après le disjoncteur |
| 12 | **Prompt formaté / FinOps** | ⚠️ contexte vivant injecté (6000 car) + indices pré-mâchés | ⚠️ **AMÉLIORER** (compresser les 6000 car) | Déjà bon esprit, mais on injecte encore trop → à réduire |
| 13 | **MiroFish** | ❌ PAUSE (décision 10/08) | ❌ **JETER** (ou garder en archive) | Tournait à vide, jamais utilisé depuis 10 jours |
| 14 | **qwen.elabore / qwen.btc** | ❌ PAUSE (décision 10/08) | ❌ **JETER** (ou archive) | Doublon du hub, jamais utilisé |
| 15 | **signets.lot2** | ❌ PAUSE | ❌ **JETER** (ou archive) | Jamais utilisé |

---

## CE QUE ÇA DONNE (résumé)
- **FINI et gardé (5)** : hub, HULK, vigie, pont gate, Cortana → **ça, c'est le socle qui marche.**
- **À FINIR (3, dans l'ordre)** : ① disjoncteur/Juge/Risk Guardian (LA sécurité), ② pépite mempool (branchée), ③ confiance pondérée (après ①).
- **OBSERVER avec date butoir (2)** : CPFP + ADA → décision au 23/08, sinon jeter.
- **JETER (3)** : MiroFish, qwen, signets.lot2 → en archive, plus de plists qui tournent à vide.

## DEMANDE À LA FAMILLE
Verdict par ligne : VALIDÉ / MODIFIÉ (dis-moi quoi) / REJETÉ. Surtout : le **disjoncteur −1,5 % dimensionné à C7 (8 % combiné)** — validez-vous le principe « le code bride l'IA, l'IA ne passe jamais d'ordre » (C2/C3) ?
