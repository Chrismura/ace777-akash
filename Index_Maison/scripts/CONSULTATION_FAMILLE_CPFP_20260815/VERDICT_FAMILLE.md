# VERDICT FAMILLE — Onchain v2 : camouflage UTXO/CPFP + seuils statistiques (15/08/2026)

**Avis reçus** : gemini (75%), nvidia (68%) = 2/4 (openrouter 502 réseau, habituel).

## Verdict : GO-AVEC-RÉSERVE (convergent)

## Les 3 cartes — TOUTES GARDÉES (convergent)
| Carte | Seuil v1 gemini | Seuil v1 nvidia | Arbitrage Buffy |
|---|---|---|---|
| **1. Z-score adaptatif** (cible mobile — la baleine ne peut pas s'adapter) | z > 3.5σ, moyenne mobile 7j | z ≥ 3σ, fenêtre 24h, **secours absolu ≥500 BTC** tant que <7j d'historique | **z ≥ 3σ + secours absolu** |
| **2. Signature CPFP par frais** (inaltérable — le frais astronomique EST le mécanisme) | enfant >25× médiane + parent <1.1 sat/vB | enfant ≥20× médiane + parent ≤1 sat/vB + **total arbre ≥100 BTC** | **≥20× + parent ≤1 sat/vB + total ≥100 BTC** |
| **3. Accumulation dust** (anticipation — la poussière se dépose avant) | 48h, ≥500 adresses dust (≤546 sats) | **mode passif**, ≥1000 adresses/48h + ≥50 BTC, heuristique par script | **passif, ≥1000 adresses/48h** |

## Anti-faux-positifs (convergent, renforcé)
1. **Double condition OBLIGATOIRE** : alerte seulement si z-score ≥3σ **ET** signature CPFP simultanées (un seul signal → rien) — nvidia.
2. **Critère topologique** : camouflage = arbre profond/large (centaines de branches à frais nuls vers un nœud final) vs CPFP d'urgence = un seul parent — gemini.
3. **2 confirmations** avant d'alerter (évite les CPFP avortés) — nvidia.
4. **Seuil de montant** : total arbre <100 BTC → filtré — nvidia + gemini (>50 BTC change).

## Coût API mempool.space (contrainte free tier — CRITIQUE)
- **~3 appels/scan** (frais médians + tx récentes + dust) = 864/jour — **sous la limite gratuite** — nvidia.
- ⚠️ **Pré-filtre IMPÉRATIF** : ne requêter parents/enfants QUE si le pré-filtre (frais >20×) détecte une anomalie — sinon ban IP 429 — gemini.
- **Backoff exponentiel + cache local 5 min + profondeur d'exploration max 2** — gemini + nvidia.

## Intégration — même pont, pondération différente (divergent → arbitrage)
- Oui : pont → live.json → synthèse Cortana + modulateur Ada (±10%).
- gemini : v2 = 40% du mix onchain (plus furtif/imminent).
- nvidia : v2 = ×0.5-0.8 (indirect, moins fiable que gros blocs).
- **Arbitrage Buffy** : signal v2 = **confirmation** (×0.5) tant qu'on n'a pas validé en réel ;
  il force le score onchain vers négatif si manipulation détectée. Neutre forcé <60% conservé.

## Améliorations captées (les 2)
1. **Mode SILENCIEUX 7 jours** avant activation des alertes : log uniquement, validation des
   seuils en conditions réelles — nvidia.
2. **Test rétroactif 30j** si données dispo + **backoff + cache** pour l'API — nvidia + gemini.

## Décision Buffy (supervision)
- Les 3 cartes de Christophe + supervision sont validées : **seuils adaptatifs** (elles ne
  peuvent pas s'adapter à une ligne mobile) + **signature frais inaltérable** + **anticipation
  dust**.
- **v1 = mode OBSERVATION silencieux 7j** (log + rapport, zéro alerte) → on calibre les seuils
  sur le réel avant de brancher les alertes. C'est le pilote.
- Pré-filtre + backoff + cache obligatoires (free tier).
- Chantier = extension de surveiller_whales.py + pont, zéro touche moteur Hulk → réversible.
