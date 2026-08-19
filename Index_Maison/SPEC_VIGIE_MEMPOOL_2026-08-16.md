# SPEC — DÉTECTEUR « BLOC PRIVATISÉ » (pépite vigie mempool) — 2026-08-16

> **Contexte** : pépite de Christophe `hulk-mexc/scripts/vigie_mempool_pepite_christophe.py`.
> **Portée de CETTE spec** : UNIQUEMENT le détecteur (P0 + P1 du chantier). Le **Juge** (matrice) et la **distribution Ada/Cortana** sont des specs SÉPARÉES à venir.
> **Doctrine** : stdlib uniquement, écriture atomique, kill-switch, idempotent, 100 % gratuit (mempool.space sans clé), MODE OBSERVATION par défaut.

---

## Objectif

Détecter les blocs « privatisés » : une transaction incluse dans un bloc miné mais **absente de la mempool publique** = OTC privée / CPFP masqué. Sortie : `taux_fantôme`, `volume_btc`, `nb_tx_cachees`.

## Le bug à corriger (P0 — IMPÉRATIF)

La pépite compare un **snapshot de mempool pris à T0** avec le bloc miné à **T0+2 s**. Or la mempool change en continu → toute tx normale entrée entre T0 et le bloc est faussement « fantôme ». La détection est inutilisable telle quelle.

**Correctif imposé** : historique local persistant des txids vus dans nos snapshots de mempool. Une tx n'est « fantôme » que si elle n'a **jamais** été vue dans nos snapshots sur une fenêtre glissante (≥ 10 min). Pas de comparaison « 1 snapshot ↔ 1 bloc ».

---

## Livrables (codeur)

### 1. `Index_Maison/scripts/detecter_bloc_privatise.py` (NOUVEAU)

- **Sources API mempool.space** (URLs déjà corrigées, à réutiliser) :
  - tip : `https://mempool.space/api/blocks/tip/hash`
  - txids d'un bloc : `https://mempool.space/api/block/{hash}/txids`
  - mempool publique : `https://mempool.space/api/mempool/txids`
- **Historique** : maintenir `data/mempool_vus.jsonl` (append-only) des txids vus à chaque snapshot, avec ts. Purger au-delà de la fenêtre (ex. 60 min).
- **Détection** : pour chaque tx du dernier bloc, « fantôme » = jamais présente dans l'historique sur la fenêtre. Ne PAS re-fetcher le détail de TOUTES les tx : pré-filtre API (voir P1).
- **Pré-filtre API (P1 — IMPÉRATIF, doctrine free tier)** : ne creuser le détail (`/api/tx/{txid}`) que si `nb_tx_cachees` dépasse un seuil OU si le volume est significatif. Backoff + cache + quota. On ne fait JAMAIS N appels pour N tx d'un bloc entier.
- **Sortie** : `data/bloc_privatise.json` — `{ts, bloc, taux_fantome, volume_btc, nb_tx_cachees, mode, alerte_potentielle}`. `mode = "observation"` par défaut → `alerte_potentielle.emise = false` TOUJOURS (silencieux).
- **Options** : `--once` (pour launchd), `--bilan` (génère `data/BLOC_PRIVATISE_BILAN.md`).
- **Kill-switch** : vérifier `Index_Maison/strategie/STOP` et `Index_Maison/STOP_ALL` avant toute écriture.

### 2. NE PAS toucher
- `detecter_cpfp.py`, `surveiller_whales.py`, `pont_onchain.py`, `paper_diprip.py` (moteur Hulk). Le branchement (« Carte 4 » / pont / Ada-Cortana) viendra dans une spec SÉPARÉE, après validation famille.

---

## Format de réponse exigé

- Bloc ```python complet pour le fichier.
- Une section « NOTES » finale : choix faits, points d'attention, fenêtre d'historique retenue, comportement du pré-filtre.
- Réponds en français, factuel.
