# Hulk DIGEST — 2026-08-22T02:28:29Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 9.6 | 0.1 | 0.15 | 7014450.85 | 21.07 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 10.52 | 0.13 | 0.17 | 154987347.03 | 1.98 | skipped_fast |
| HBARUSDT | IDLE | 2.35 | 5.29 | 0.0 | 0.09 | 966397.0 | 2.47 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 9.63 | 2.03 | 0.09 | 546285.65 | 47.49 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 6.33 | 0.03 | 0.15 | 652451.09 | 7.82 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 5.07 | 0.45 | -0.01 | 474482.92 | 6.02 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.13 | 8.18 | 0.76 | 0.1 | 193239.96 | 5.91 | skipped_fast |
| WUSDT | IDLE | 1.85 | 5.09 | 0.04 | 0.1 | 401929.89 | 14.02 | skipped_fast |
| EDELUSDT | IDLE | 2.48 | 5.02 | 3.04 | -0.03 | 79648.04 | 22.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.89 | 0.11 | 61344.09 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.26 | 0.18 | 157409.15 | 21.89 | skipped_fast |
| QNTUSDT | IDLE | 2.25 | 5.01 | 0.0 | 0.08 | 171083.24 | 1.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9345.09 | 32.54 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 4.09 | 0.89 | 0.11 | 61908.08 | 12.61 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.43 | 0.04 | 178548.78 | 72.65 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.75 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 2.08 | 0.0 | 0.04 | 54965.66 | 32.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
