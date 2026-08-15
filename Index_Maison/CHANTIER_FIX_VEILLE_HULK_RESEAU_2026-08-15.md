# CHANTIER — Veille Hulk robuste au réseau (fix anti-pend) — 15/08/2026

**Statut : APPLIQUÉ + VÉRIFIÉ** · hors genesis (outil paper) · réversible.

## Contexte
La veille Hulk (`hulk-mexc/scripts/digest_watch.py`) se pendait sur le réseau WiFi/alpage (contrainte PERMANENTE) → plus de digest depuis 2,5 jours → positions Hulk gelées en WATCH. Famille (2/4 : gemini 90%, nvidia 78%) + Cortana ont validé le chantier.

## Cause racine
`http_json` = `timeout=40s × 3 retries` (sleep linéaire) par appel, ~18 paires × 4 appels → un seul scan pouvait durer des heures sous réseau dégradé, sans aucune borne. Aucun circuit-breaker.

## Fix appliqué (4 mécanismes)
1. **Timeout strict** : 40s → 12s par appel HTTP.
2. **Back-off exponentiel** : sleep linéaire 1s/2s → exponentiel 1→2→4s (plafonné 8s).
3. **Circuit-breaker par host** : 3 échecs réseau consécutifs (api.mexc.com / api.llama.fi) → ouverture 60s (fast-fail). Un 4xx/5xx HTTP (serveur répond) ne compte PAS comme panne.
4. **Deadline de scan globale** : `SCAN_DEADLINE_SEC=90` → si dépassée, paires restantes = `scan_deadline` + digest marqué `degraded: true` (bandeau d'alerte).

## Fichiers modifiés
- `hulk-mexc/scripts/digest_watch.py` : imports + `http_json` + helpers circuit-breaker + `build_digest` (deadline/degraded) + `run_once` (lecture cfg + log) + `to_markdown` (bandeau).
- `hulk-mexc/config/defaults.env` : + `SCAN_DEADLINE_SEC=90` (seule valeur lue depuis cfg).

## Vérifications (toutes vertes)
1. `python3 -m py_compile scripts/digest_watch.py` → OK.
2. **Test circuit-breaker isolé** : host mort → 1er appel échoue ~7s (3 retries + back-off), 2e appel = circuit-open en 0.00s (fast-fail). ✅
3. **Smoke test one-shot** : scan borné à **91s** (au lieu de pendre indéfiniment), digest FRESH (17:28 au lieu du 13/08 03:37 = 2,5 jours). **15/15 paires core scannées**, 3 paires watch (QNT/FLUID/RWA, en fin de liste) en `scan_deadline` (réseau lent pendant le scan). Bandeau dégradé OK. ✅
4. DefiLlama probe : répond 0.3-1.6s → le goulot = réseau INTERMITTENT (alpage), pas un endpoint précis. Le fix borne exactement ce cas.

## Retour arrière (réversible)
- **digest_watch.py** (suivi git, dernier commit 77cad5da) : `git checkout -- hulk-mexc/scripts/digest_watch.py`
  ou : ré-appliquer en inverse les 6 blocs OLD du `SPEC_FIX_VEILLE_HULK_RESEAU_2026-08-15.md`.
- **defaults.env** (non suivi git) : supprimer les 2 lignes ajoutées (`SCAN_DEADLINE_SEC=90` + commentaire).

## Décision Buffy (supervision)
Le codeur (code.ia) a validé le diff sans hallucination (contexte exact injecté). Deadline 90s = bon équilibre : les 15 paires CORE (tradées) passent toujours en premier, les 3 watch (supplémentaires) sont sacrifiées en cas de lenteur — priorité correcte. Sur un cycle réseau rapide, les 18 passent en <60s.

## Suite logique (prochain chantier, validé famille)
2. **Kill-switch déterministe global** (veille muette > X heures → STANDBY) — nvidia.
3. **Brancher Cortana** en pilote de paramètres (contrat JSON Cortana↔moteur).
