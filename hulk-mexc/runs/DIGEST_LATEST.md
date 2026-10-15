# Hulk DIGEST — 2026-10-15T16:03:08Z

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
| PYTHUSDT | IDLE | 3.95 | 25.14 | 3.95 | 0.2 | 3947161.7 | 13.42 | skipped_fast |
| WUSDT | IDLE | 2.42 | 7.48 | 0.78 | -0.01 | 2686062.0 | 7.37 | skipped_fast |
| ETHUSDT | IDLE | 2.66 | 5.29 | 0.23 | 0.0 | 341214538.82 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.41 | 4.76 | 0.43 | 0.01 | 54487775.0 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 1.76 | 3.48 | 0.24 | 0.01 | 498416693.69 | 0.0 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.6 | 9.55 | 1.05 | 0.01 | 1180503.68 | 6.72 | skipped_fast |
| REDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.0 | 12.67 | 0.0 | 0.08 | 72814.4 | 51.82 | skipped_fast |
| ZBCNUSDT | IDLE | 3.28 | 6.54 | 0.14 | 0.0 | 196407.6 | 16.48 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 4.95 | 0.35 | -0.06 | 450068.78 | 9.08 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 11.93 | 0.9 | -0.1 | 147182.82 | 10.61 | skipped_fast |
| BIOUSDT | IDLE | 2.4 | 6.71 | 0.0 | -0.02 | 88251.49 | 7.72 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 6.7 | 0.72 | -0.06 | 225570.72 | 31.62 | skipped_fast |
| KITEUSDT | IDLE | 2.37 | 7.56 | 0.55 | -0.02 | 68604.78 | 11.17 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 8.24 | 0.71 | 0.13 | 27163.4 | 4.75 | skipped_fast |
| HBARUSDT | IDLE | 2.16 | 4.27 | 0.35 | -0.01 | 370589.72 | 5.99 | skipped_fast |
| TELUSDT | IDLE | 2.72 | 6.61 | 0.68 | -0.01 | 96302.76 | 22.74 | skipped_fast |
| RIZEUSDT | IDLE | 1.41 | 5.51 | 2.03 | 0.02 | 64389.47 | 58.52 | skipped_fast |
| FLUIDUSDT | IDLE | 1.93 | 5.11 | 0.0 | 0.01 | 16798.95 | 21.45 | skipped_fast |
| MNSRYUSDT | IDLE | 1.46 | 2.77 | 1.02 | -0.0 | 31537.94 | 42.29 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.86 | 0.48 | -0.0 | 55190.95 | 7.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
