# Hulk DIGEST — 2026-08-22T02:33:51Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 10.52 | 1.23 | 0.15 | 7101220.06 | 3.84 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 11.93 | 0.08 | 0.18 | 155912698.21 | 9.77 | skipped_fast |
| HBARUSDT | IDLE | 2.39 | 5.43 | 0.23 | 0.09 | 968867.06 | 1.23 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 9.63 | 1.72 | 0.1 | 544119.65 | 27.76 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 6.75 | 0.27 | 0.15 | 652996.27 | 9.55 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 5.1 | 0.0 | -0.0 | 458880.0 | 11.96 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.12 | 8.18 | 0.56 | 0.1 | 193135.66 | 20.63 | skipped_fast |
| WUSDT | IDLE | 1.95 | 5.62 | 0.23 | 0.1 | 403283.32 | 8.99 | skipped_fast |
| EDELUSDT | IDLE | 2.46 | 5.02 | 2.82 | -0.03 | 79623.03 | 22.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.07 | 0.1 | 61473.16 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.22 | 0.17 | 157773.26 | 19.45 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.31 | 0.08 | 172646.27 | 11.9 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9324.96 | 37.95 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.05 | 177119.97 | 10.34 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.2 | 0.12 | 62373.31 | 13.46 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.77 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.17 | 0.0 | 0.04 | 55110.64 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
