# SPEC — Quant desk v1 (boucle Bull/Bear/Risque, mode OMBRE) — 15/08/2026

**Chantier 4** (ordre famille validé : gemini rang 2 « hulk_quant_loop », nvidia mentionne la structure quant desk @antpalkin).
**Origine** : signet N°25 @antpalkin (300 agents en 40 min) + N°68 @antpalkin (trader top 0,04% WorldQuant qui **réécrit ses stratégies perdantes** pendant son sommeil) + N°50 @gippp69 (les 3 schémas de workflow Anthropic : séquentiel / parallèle / boucle d'évaluateur).
**Décision de supervision** : **v1 = conseil différé en mode OMBRE** (la famille l'a posé pour Cortana : « conseil différé à la reconnexion »). Le quant desk CONFRONTE des thèses et ÉCRIT un avis — le moteur `paper_diprip.py` n'est PAS modifié, rien n'est appliqué.

**Ce que fait la v1 (périmètre borné)** : 3 avocats (Bull, Bear, Risque) débattent sur l'état RÉEL du portefeuille Hulk + le contexte de marché, puis un arbitre (Buffy/superviseur assisté) tranche. Sortie = rapport lisible + JSON. Objectif : **exercer la logique de débat AVANT de brancher quoi que ce soit** (même philosophie que la dérive mémoire et le Kelly : ombre d'abord, preuve ensuite).

---

## Fichier à créer : `Index_Maison/scripts/quant_desk.py`

Python 3, stdlib uniquement (le hub est appelé via urllib — pas de lib externe). Lancé à la demande : `python3 quant_desk.py` (et optionnellement par la discipline quotidienne, voir plus bas).

### Données d'entrée (lecture seule, fail-open)
1. **État Hulk réel** : dernier `hulk-mexc/runs/PAPER_V1_*_state.json` (le plus récent par mtime). Extraire : `pnl_total`, `positions` (nb, paires), `bags` (nb), `pair_cash`, `notional_live`, `scores` (régimes par paire).
2. **Dernier digest veille** : `hulk-mexc/runs/DIGEST_LATEST.md` (si présent — contexte marché des paires).
3. **Analyses Cortana récentes** : les 3 dernières lignes de `Index_Maison/thermo/analyses/*.jsonl` (tous fichiers, triées par ts, les plus récentes) — surtout `radar`, `funding`, `fearGreed`, `btc`. Extraire pour chacune : indice, avis strict, confiance.
4. **Justesse** : `Index_Maison/scripts/justesse_v2.json` → `pct` (pour pondérer le poids des avis).

### Les 3 avocats (appels hub — task distincte par rôle)
Pour CHAQUE avocat, un appel hub (`task: "quant_desk"`), avec le même contexte mais un rôle différent :
- **BULL** : « Tu es l'avocat BULL. Défends la thèse haussière : quelles positions/entrées Hulk garder, quoi acheter sur le dip, quelles paires semblent prêtes à monter. Max 6 phrases. »
- **BEAR** : « Tu es l'avocat BEAR. Défends la thèse baissière : quelles positions couper, quels risques de stop/dump, quoi NE PAS acheter. Max 6 phrases. »
- **RISQUE** : « Tu es l'avocat RISQUE. Tu ne prends parti ni pour ni contre : tu évalues le RISQUE de chaque thèse (sizing, volatilité, liquidité, concentration). Max 6 phrases. »

Chaque avocat reçoit le même CONTEXTE réel (état Hulk + digest + analyses + justesse). Sortie attendue : `AVOCAT BULL : <texte>` (etc.).

### L'arbitre (4e appel hub — task `quant_desk.arbitre`)
- Reçoit les 3 plaidoiries + le contexte.
- Rendu EXACT (format strict) :
  ```
  VERDICT : BULL | BEAR | MIXTE | PRUDENT (choisir 1)
  CONFIANCE : faible | moyenne | haute
  POINTS FORTS (2 max) : ...
  RISQUES RÉSIDUELS (2 max) : ...
  ACTION CONSEILLÉE (1 ligne) : ex. « garder les positions, ne pas ouvrir sur les paires DEAD, préparer le cash pour un dip »
  ```
- NB : l'arbitre ne donne JAMAIS d'ordre — c'est un conseil différé.

### Sortie
1. **Rapport** : `Index_Maison/thermo/QUANT_DESK.md` :
   - `# Quant desk — <date>` · contexte (pnl, positions, bags, cash, justesse).
   - Les 3 plaidoiries (BULL/BEAR/RISQUE) verbatim.
   - Le verdict arbitre + les AVIS STRICT de Cortana récents (pour recroiser).
   - **ENCADRÉ** : « mode ombre — conseil différé, rien d'appliqué. »
2. **JSON** : `Index_Maison/strategie/quant_desk.json` : `{ts, contexte: {...}, verdict, confiance, action_conseillee, applique: false}`.
3. **Exit code** : `0` = verdict rendu · `1` = hub injoignable (fail-open, on n'écrit que le contexte) · `2` = données insuffisantes (pas de state Hulk).

### Robustesse (règle d'or réseau alpage)
- Chaque appel hub : timeout None (comme les autres scripts), 2 tentatives, sleep 4 entre.
- Si un avocat échoue : on continue avec les autres (l'arbitre voit « AVOCAT X : indisponible »).
- Si le hub est injoignable partout : exit 1, on écrit quand même un mini-rapport avec juste le contexte (utile pour l'humain).

### Branchement (OPTIONNEL, à laisser OFF par défaut)
- Ne PAS l'ajouter au launchd quotidien par défaut (3-4 appels hub/jour = coût réseau ; c'est un outil à la demande).
- Laisser un commentaire dans le script : « pour l'activer dans la discipline : décommenter l'appel dans discipline_quotidienne.py ».

### Contraintes
- Stdlib, français, commenté, fail-open partout, `applique: false` TOUJOURS.
- Ne modifie JAMAIS : state, CSV, moteur, genesis, analyses.
- Réversible : suppression du script = retour à l'état d'avant.

### Format de sortie attendu du codeur
Le code EXACT de `Index_Maison/scripts/quant_desk.py`. Zéro modification d'autre fichier (le branchement discipline est DÉSACTIVÉ par défaut).
