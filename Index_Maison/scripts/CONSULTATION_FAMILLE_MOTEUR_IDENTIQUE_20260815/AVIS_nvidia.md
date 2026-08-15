# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 323.0s)

**ANALYSE FACTUELLE — RÉPONSES AUX 5 QUESTIONS**

---

## 1) CONFIRMATION MOTEUR : MÊME MOTEUR EXACT

**OUI, confirmé sans ambiguïté.** Preuves :

- **Genesis identique** : `genesis_md5=8d9ee8d6997eeadabf3da642f326d3d7` sur les 4 CSV scellés → même code source, même config.
- **Preuve CSV décisive** : les 17 333 premières lignes du fichier du 15/08 sont **octet pour octet identiques** au fichier complet du 14/08. C'est la preuve formelle d'un moteur unique append-only.
- **Séquences cohérentes** : les patterns de cycles (ex: Run 4h #1 cyc=504→515→524 avec qty=0.249→0.249→0.201) montrent une logique de sizing cohérente avec le design (revenge 1.5x = 0.249, strong_conf_full = 0.083-0.133).

**Aucun élément dans les séquences ne suggère un comportement différent d'un run à l'autre.** Les variations de PNL s'expliquent par les conditions de marché (hausse vs baisse), pas par un changement de moteur.

---

## 2) LE PATTERN REVENGE : ANORMAL ET EXPLIQUÉ PAR LE HEARTBEAT

**Le taux de 68-91% est ANORMAL** par rapport au design (revenge ponctuel après perte SCOUT, TTL 20s). 

**Votre hypothèse heartbeat est PLAUSIBLE et probablement correcte.** Mécanisme :

```
duo_touch_heartbeat() → met à jour ts_ms à CHAQUE cycle SCOUT
→ l'état "perte SCOUT" (status=CLOSED, pnl<0) reste "frais" (ts_ms récent)
→ le TTL de 20s n'expire JAMAIS
→ ALPHA lit un état toujours valide → reste armé en revenge en continu
```

**Preuve indirecte** : la corrélation revenge ALPHA ↔ perte BETA n'est que de 14% à ≤30s (le TTL nominal). Si le TTL fonctionnait, on attendrait ≥80% de corrélation à ≤20s. Le fait que 59% des revenge suivent une perte BETA à ≤5min suggère que l'état reste "frais" bien au-delà de 20s.

**Autre explication possible** : le `duo_hunter_decide()` pourrait avoir une logique de "revenge persistant" non documentée (ex: un flag `revenge_armed` qui ne se reset qu'après un trade gagnant). Mais le heartbeat est l'explication la plus simple et la plus cohérente avec le code.

---

## 3) BETA "INUTILE" : RÔLE SCOUT NORMAL MAIS DÉSÉQUILIBRÉ

**C'est le rôle SCOUT normal** : BETA teste, subit les pertes, ALPHA frappe. Le ratio PNL (ALPHA/BETA = 70x / 8x / 3.4x) est cohérent avec le design.

**MAIS le déséquilibre est préoccupant** :
- BETA fait 155-204 trades pour 0.40-2.51$ → **frais de transaction non couverts** (sur testnet, pas de frais réels, mais en production ce serait une hémorragie).
- BETA a 0% de trades en revenge → il ne profite jamais de ses propres signaux.

**Recommandation** : vérifier si le SCOUT devrait avoir un mode "confirmation" qui réduit sa fréquence quand ALPHA est en position, pour éviter le gaspillage de capital.

---

## 4) LES FLAT (25-39%) : FILTRE DE QUALITÉ OU CAPITAL IMMOBILISÉ ?

**C'est le filtre de qualité qui travaille, mais avec un coût.**

- **Preuve** : les flat ont `exit=shock_inversion_stop` ou `fluid_exit_brake` → le moteur détecte une inversion et sort au même prix pour éviter une perte. C'est le comportement attendu d'un filtre.
- **Coût** : chaque flat immobilise du capital pendant `hold_sec` (non tracé dans le CSV, mais probablement 30-120s). Sur 65 trades ALPHA, 16-25 flat → **capital immobilisé 25-39% du temps sans rendement**.

**Verdict** : filtre correct, mais le taux de 39% (Run Nuit) suggère que le filtre pourrait être trop sensible en marché calme. À surveiller.

---

## 5) CSV : ANOMALIE DE TRACAGE CONFIRMÉE

**OUI, anomalie confirmée.** La colonne `holdSec` contient le message détaillé (radar=..., size_note=..., soft=..., tension=...) au lieu de la durée de détention. La colonne `msg` est vide.

**Impact** : impossible de calculer la durée moyenne de détention, le temps de capital immobilisé, ou de corréler hold_sec avec le PNL. C'est un **défaut de traçage critique** pour l'analyse post-mortem.

**Cause probable** : un bug dans le code de logging qui écrit le message dans le mauvais champ (swap de colonnes).

---

## CONCLUSION GLOBALE

| Question | Verdict | Confiance |
|----------|---------|-----------|
| 1. Même moteur | OUI | 100% (preuve octet par octet) |
| 2. Revenge anormal + heartbeat | OUI, heartbeat plausible | 85% (manque preuve directe du code) |
| 3. BETA déséquilibré | Rôle normal, mais coût élevé | 90% |
| 4. Flat = filtre | OUI, mais taux élevé à surveiller | 80% |
| 5. CSV anomalie | OUI, bug de traçage | 100% |

**Action prioritaire** : 
1. **Corriger le heartbeat** (ligne 1545) pour qu'il ne rafraîchisse PAS `ts_ms` quand l'état est CLOSED avec pnl<0 — ou ajouter un flag `revenge_consumed` qui se reset après un trade ALPHA.
2. **Corriger le logging CSV** (swap holdSec/msg).
3. **Ajouter un compteur de revenge** dans duo_state.json pour tracer le nombre de revenge consécutifs.

Le système est **fonctionnel et rentable** (PNL positif sur les 3 runs), mais le heartbeat neutralise le TTL et crée un état de revenge permanent non prévu par le design. C'est un **bug de conception** qui doit être corrigé avant la mise en production.
