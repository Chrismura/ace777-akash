# 🧭 POINT DE REPRISE — 2026-08-15 ~10:45Z (coupure Freebuff)

## État du correctif CSV (le travail en cours)

**FAIT :**
- Durées récupérées rétroactivement 100% (675/675) → `Index_Maison/durees_restituees_3_runs_2026-08-15.csv` + `SYNTHESE_DUREES_3_RUNS_2026-08-15.md`. Moteur = scalper (hold 2-13s, médiane 5-6s).
- Famille 4/4 (gemini, nvidia, juge, ultra) a validé le correctif CSV (logging-only, corriger les 16 lignes echo).
- Codeur (code.ia) a HALLUCINÉ → diff exact généré depuis le fichier réel : `Index_Maison/DIFF_EXACT_FIX_CSV_2026-08-15.md`.
- **Correctif APPLIQUÉ au genesis** : 16 lignes 11→12 champs. `bash -n` OK.
- md5 genesis : `8d9ee8d6…` → **`fe2a7bcc9dc1f31bd524ffc433f9186d`**
- Backup : `genesis_manifest.txt.BAK_avant_fix_csv_20260815-103358`
- Références md5 mises à jour : `GO_VORTEX_V2.sh` (EXPECT_MD5_PREFIX=fe2a7bcc), `scripts/preflight_ace777.sh`, `scripts/verif_pre_run_3x.sh`, `scripts/verif_setup_champion.sh`.

**À FAIRE (prochain Buffy) :**
1. **Smoke test** (vérifier CSV 12 colonnes en conditions réelles) :
   ```bash
   cd ~/ace777-test-day1
   source scripts/load_config.sh vortex_v2_collab
   TEST_TAG_OVERRIDE=SMOKE_FIX_CSV_20260815 ./launch_test_master_base_v8_6_fortress.sh --duration 120
   # puis : awk -F, '{print NF}' runs/SMOKE_FIX_CSV_*.csv | sort | uniq  → doit donner 12
   ```
   ⚠️ Attention : ce lancement réinitialise duo_state.json et touche runs/.
2. Si smoke OK → finaliser le **re-scellement** (md5 déjà = fe2a7bcc) + vérifier qu'aucune autre référence à 8d9ee8d6 ne bloque (grep 8d9ee8d6 hors fichiers historiques/BAK/SCELLE).
3. Mettre à jour les docs (INDEX_COMMANDES §commandes) si besoin.

**AMÉLIORATIONS PROPOSÉES (à prioriser avec Christophe) :**
1. Famille : standardiser « verdict + confiance 0-100% + hypothèses + ce qui changerait l'avis » (proto #5).
2. Juge : avis tronqué → max_tokens 2200→3200 + vérifier finish_reason.
3. Codeur : contrainte « si info absente → réponds insuffisant, n'invente rien » (proto #6).
4. Scellement : enregistrer md5 config dans le champ `config=` de la signature (actuellement vide).
5. Hub : traiter 402 comme signal de retrait immédiat dans routeur_auto.py (mission pointe sur puter-grok mort).

## Règle d'or retenue
- Toujours DEMANDER avant d'agir (lire/analyser par défaut).
- Champion intouchable sans GO humain explicite.
- Je propose, Christophe tranche.
- À chaque travail : chercher une amélioration à proposer (stacking functions).
- Prompts famille = proto #9 Multi-Perspective + #5 Confidence-Weighted. Codeur = #8 Constraint-First + #6 Context Injection.
