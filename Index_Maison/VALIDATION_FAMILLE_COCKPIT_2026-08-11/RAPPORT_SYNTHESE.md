# RAPPORT VALIDATION FAMILLE — COCKPIT (11/08/2026)

## VERDICTS (modèles réels vérifiés dans usage.jsonl — leçon 16:25)

| Famille | Modèle réel | Verdict | Confiance |
|---|---|---|---|
| GEMINI (audit.protocol) | gemini-flash-lite-latest | GARDER AVEC GARDE-FOUS RENFORCÉS | moyenne |
| DEEPSEEK (mission) | deepseek-v4-flash-0731 | GARDER AVEC GARDE-FOUS RENFORCÉS | moyenne |
| JUGE (signets.juge) | gemini-flash-lite-latest | GARDER AVEC GARDE-FOUS RENFORCÉS | moyenne |
| ULTRA (ultra.analyse) | gemini-flash-lite-latest | GARDER AVEC GARDE-FOUS RENFORCÉS | moyenne |

**4/4 : GARDER AVEC GARDE-FOUS RENFORCÉS** — l'architecture est la bonne, les garde-fous doivent être renforcés.

## FAILLES CONSENSUS (citées par 3-4 familles)

1. **[4/4] Pas de try/catch global JS** → une exception gèle l'onglet STRATÉGIE (page blanche).
2. **[4/4] Bridge down** → fetch échoue sans mode dégradé clair (« BRIDGE HORS LIGNE »).
3. **[4/4] Fichier veille corrompu/tronqué** → pas de validation de structure, pas de fallback.
4. **[3/4] Quota 429** → pas de gestion des erreurs de débit (retry / blacklist temporaire).
5. **[3/4] Pas de cache de secours** → si la veille du jour est absente, on perd la veille d'hier au lieu de l'afficher en « MODE CACHE J-1 ».

## ACTIONS PROPOSÉES (classées par la famille)

### INcASSABLE (quick wins, consensus)
- A1. try/catch global + par bloc de rendu dans le JS du cockpit (jamais de page blanche).
- A2. Wrapper chaque fetch : AbortController timeout 5s + pastille « BRIDGE HORS LIGNE ».
- A3. Bridge : temps max 3s par source, jamais bloquant (déjà 20-25s → resserrer sur le GET /offres).
- A4. DÉCOLLER : si échec hub, message clair + traçabilité dans un log.

### AUTO-RÉPARANT (mécanique)
- A5. KeepAlive launchd sur le bridge (auto-relance si crash).
- A6. Purge .tmp orphelins (>10 min) + rotation logs >10 Mo au démarrage du bridge.
- A7. Validation de structure du VEILLE_HUB avant parsing (fichier vide/tronqué → signaler + fallback).

### AUTO-ADAPTATIF
- A8. Fallback cache : si VEILLE_HUB du jour absent → afficher le dernier valide + badge « MODE CACHE J-1 ».
- A9. Gestion 429/403 : blacklist temporaire 1h des providers en erreur (cooldown).

### AUTO-INTELLIGENT (à plus forte valeur, validé par au moins 2 familles)
- A10. Health-check externe toutes les 5 min (ports 17777 + 17800 → relance auto si mort).
- A11. Score de fiabilité par source de veille sur 30 jours (détecter les sources menteuses).
- A12. Détection des doublons d'offres sur les 7 derniers rapports.

## RECOMMANDATION BUFFY
Appliquer immédiatement A1→A9 (incassable + auto-réparation + adaptatif, risque nul,
backups avant). A10→A12 (intelligent) : chantier séparé, à valider une fois les bases renforcées.
