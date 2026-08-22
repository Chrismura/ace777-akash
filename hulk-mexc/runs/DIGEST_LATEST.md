# Hulk DIGEST — 2026-08-22T02:11:12Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 8.42 | 1.01 | 0.14 | 6907671.51 | 13.67 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 10.03 | 0.4 | 0.17 | 154258073.54 | 4.65 | skipped_fast |
| HBARUSDT | IDLE | 2.3 | 4.9 | 0.27 | 0.08 | 954156.03 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.5 | 9.63 | 3.13 | 0.08 | 545902.78 | 18.44 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 6.1 | 0.24 | 0.14 | 654247.18 | 10.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.79 | 4.13 | 0.0 | 0.01 | 513825.0 | 3.03 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 6.88 | 0.44 | 0.09 | 190540.18 | 5.96 | skipped_fast |
| WUSDT | IDLE | 1.74 | 4.41 | 0.53 | 0.08 | 399514.82 | 8.1 | skipped_fast |
| EDELUSDT | IDLE | 2.34 | 5.02 | 0.98 | -0.01 | 79571.28 | 32.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.77 | 0.11 | 61159.79 | 42.33 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.16 | 0.17 | 156797.49 | 12.15 | skipped_fast |
| QNTUSDT | IDLE | 2.3 | 4.89 | 1.16 | 0.07 | 171294.68 | 9.06 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.49 | 0.12 | 61366.72 | 11.7 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.01 | 9604.71 | 86.53 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.11 | 1.48 | 0.04 | 179032.83 | 82.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 19.77 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54752.91 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
