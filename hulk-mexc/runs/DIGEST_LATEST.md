# Hulk DIGEST — 2026-08-22T05:07:42Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 3.27 | 15.45 | 4.75 | 0.15 | 14108832.32 | 33.85 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 19.3 | 1.21 | 0.28 | 183636847.62 | 2.38 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.59 | 10.33 | 0.79 | 0.15 | 1127819.49 | 1.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.15 | 0.2 | 749654.42 | 7.37 | skipped_fast |
| CHIPUSDT | IDLE | 2.9 | 5.36 | 2.94 | 0.0 | 446636.25 | 12.12 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 8.22 | 1.22 | 0.15 | 450298.46 | 10.61 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.04 | 9.0 | 0.49 | 0.09 | 203409.8 | 5.8 | skipped_fast |
| ZBCNUSDT | IDLE | 1.6 | 4.29 | 2.6 | 0.09 | 538607.6 | 40.43 | skipped_fast |
| QNTUSDT | IDLE | 2.74 | 9.16 | 4.34 | 0.1 | 186987.04 | 4.42 | skipped_fast |
| RWAINCUSDT | IDLE | 2.36 | 4.48 | 1.57 | 0.01 | 10345.47 | 21.38 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 7.96 | 6.32 | 0.19 | 158273.49 | 12.17 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 6.62 | 0.44 | 0.15 | 68336.92 | 11.41 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.28 | 1.31 | -0.02 | 80959.24 | 33.2 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.49 | 0.1 | 184013.72 | 24.82 | skipped_fast |
| RIZEUSDT | IDLE | 1.11 | 4.41 | 4.22 | 0.09 | 58692.28 | 44.52 | skipped_fast |
| RWAUSDT | IDLE | 1.71 | 3.38 | 0.24 | 0.07 | 56864.23 | 15.96 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 34.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
