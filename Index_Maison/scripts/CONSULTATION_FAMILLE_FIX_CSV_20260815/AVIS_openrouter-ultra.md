# AVIS openrouter-ultra (provider OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte, 13.9s)

**1) Oui, pur logging.**  
La variable `$hold_done` est déjà calculée (ligne 2490) et affichée au terminal (ligne 2516). L'insertion ne touche aucune variable de décision, taille, prix, risque, ni flux d'ordres.

**2) Risque réel : consommateurs qui parsent par position et attendent 11 champs sur FILLED.**  
- `scripts/verifier_test.sh` : si il fait `cut -d, -f11` pour `holdSec`, il récupérera le message diagnostic → erreur silencieuse ou plantage.  
- `cockpit` / scripts d'analyse : idem s'ils indexent en dur `fields[10]` pour la durée.  
**Protection** : avant re-scellement, passer un one-liner de migration sur les CSV existants (insérer champ vide en 11e position sur les vieilles lignes FILLED) et valider que `verifier_test.sh` et le cockpit lisent correctement le nouveau format (12 champs, `holdSec` numérique, `msg` string).

**3) Corriger TOUTES les lignes (SKIP/OBSERVE/ENTRY_ERROR) à 12 colonnes.**  
- Écrire `holdSec` vide (`,,`) + message en 12e.  
- Raisons : cohérence schématique (même nombre de colonnes pour tout parseur), évite des `if line_type == FILLED` dans les consommateurs, et le genesis scellé impose une structure unique.

**4) Smoke test suffisant (pas de run testnet complet).**  
- 3–5 cycles réels (ou rejouer un log existant en mode dry-run) → vérifier :  
  a) CSV scellé a 12 colonnes sur **toutes** les lignes,  
  b) `holdSec` numérique sur FILLED, vide sur les autres,  
  c) `msg` présent en 12e,  
  d) `verifier_test.sh` et cockpit passent sans erreur.  
- Si OK → re-scellement (nouveau md5) + commit du correctif.
