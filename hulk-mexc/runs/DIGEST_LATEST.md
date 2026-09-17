# Hulk DIGEST — 2026-09-17T00:03:31Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.83 | 3.44 | 1.5 | 0.01 | 58152785.1 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.94 | 1.86 | 0.18 | 0.01 | 367831305.28 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.53 | 0.23 | 0.01 | 504042973.68 | 0.03 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.53 | 8.94 | 0.0 | 0.12 | 505521.34 | 24.53 | skipped_fast |
| RWAINCUSDT | IDLE | 4.14 | 7.81 | 3.2 | -0.02 | 20542.68 | 5.82 | skipped_fast |
| WUSDT | IDLE | 2.79 | 5.55 | 0.25 | 0.01 | 208877.26 | 10.86 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 2.99 | 0.26 | 0.0 | 413780.23 | 1.89 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 5.13 | 1.41 | -0.02 | 80372.12 | 16.53 | skipped_fast |
| KITEUSDT | IDLE | 1.99 | 7.47 | 0.05 | 0.08 | 67755.11 | 10.18 | skipped_fast |
| BIOUSDT | IDLE | 1.9 | 3.79 | 0.12 | -0.0 | 79513.34 | 15.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 2.17 | 0.91 | 0.02 | 182149.11 | 13.81 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 3.24 | 0.34 | -0.01 | 65338.29 | 2.31 | skipped_fast |
| EDELUSDT | IDLE | 0.52 | 3.15 | 1.97 | 0.12 | 299606.1 | 30.33 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.15 | 0.51 | -0.01 | 275846.05 | 1.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 9.65 | 5.91 | 0.26 | 60548.21 | 96.41 | skipped_fast |
| RWAUSDT | IDLE | 1.96 | 3.87 | 0.3 | 0.02 | 55021.37 | 29.92 | skipped_fast |
| QNTUSDT | IDLE | 1.51 | 2.99 | 0.2 | -0.0 | 37112.95 | 4.9 | skipped_fast |
| TELUSDT | IDLE | 1.29 | 2.38 | 1.3 | -0.03 | 114744.01 | 48.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.07 | 0.0 | -0.02 | 1573.23 | 21.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.48 | 0.24 | -0.01 | 31578.79 | 25.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
