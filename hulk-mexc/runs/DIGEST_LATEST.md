# Hulk DIGEST — 2026-08-22T04:05:14Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.76 | 11.91 | 0.17 | 0.19 | 9709089.29 | 22.21 | skipped_fast |
| XRPUSDT | IDLE | 2.17 | 12.22 | 2.54 | 0.18 | 166605903.69 | 3.21 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 10.63 | 0.67 | 0.2 | 711015.6 | 19.67 | skipped_fast |
| HBARUSDT | IDLE | 2.12 | 6.03 | 0.77 | 0.1 | 1011152.85 | 3.62 | skipped_fast |
| CHIPUSDT | IDLE | 2.9 | 5.36 | 2.88 | -0.03 | 458513.31 | 3.03 | skipped_fast |
| BIOUSDT | IDLE | 3.05 | 7.36 | 3.02 | 0.07 | 199547.51 | 3.02 | skipped_fast |
| WUSDT | IDLE | 1.99 | 7.18 | 1.15 | 0.13 | 428554.89 | 10.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 4.29 | 1.96 | 0.12 | 537134.77 | 22.94 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80562.43 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.1 | 59142.97 | 44.52 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.36 | 0.13 | 67563.5 | 12.38 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.81 | 0.21 | 157778.19 | 26.89 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 3.8 | 0.83 | 0.09 | 178553.33 | 7.43 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56326.49 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.4 | 0.41 | 0.07 | 174312.7 | 30.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
