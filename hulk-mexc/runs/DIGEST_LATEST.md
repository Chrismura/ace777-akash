# Hulk DIGEST — 2026-10-05T22:38:10Z

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
| QNTUSDT | IDLE | 2.22 | 4.16 | 1.91 | 0.02 | 2607357.03 | 1.56 | skipped_fast |
| XRPUSDT | IDLE | 0.98 | 1.91 | 0.38 | -0.01 | 34639704.54 | 0.66 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.06 | 0.23 | -0.01 | 375933310.24 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.96 | 0.1 | -0.01 | 674336894.7 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.05 | 5.96 | 0.88 | 0.02 | 677815.78 | 2.53 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.88 | 9.35 | 1.33 | 0.05 | 142467.55 | 7.7 | skipped_fast |
| WUSDT | IDLE | 2.96 | 5.83 | 0.57 | 0.02 | 396464.12 | 15.65 | skipped_fast |
| RIZEUSDT | IDLE | 2.03 | 23.96 | 11.56 | 0.32 | 73573.82 | 28.3 | skipped_fast |
| EDELUSDT | IDLE | 2.34 | 4.51 | 1.09 | 0.01 | 297693.92 | 7.9 | skipped_fast |
| BIOUSDT | IDLE | 2.68 | 7.54 | 4.32 | 0.06 | 107475.39 | 3.09 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.73 | 1.27 | -0.02 | 414751.23 | 3.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.71 | 0.23 | 0.02 | 279497.18 | 20.55 | skipped_fast |
| REDUSDT | IDLE | 1.78 | 3.58 | 0.86 | -0.01 | 83539.69 | 6.41 | skipped_fast |
| MNSRYUSDT | IDLE | 3.22 | 5.85 | 3.92 | 0.01 | 46495.96 | 30.67 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 2.36 | 0.46 | -0.01 | 477318.78 | 7.83 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.83 | 0.69 | -0.04 | 68669.22 | 7.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.19 | 2.91 | 1.51 | 0.01 | 18193.78 | 37.34 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 5.16 | 4.21 | 0.2 | 68034.15 | 19.96 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 1.46 | 1.13 | -0.0 | 135970.06 | 36.39 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.29 | -0.01 | 51448.25 | 14.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
