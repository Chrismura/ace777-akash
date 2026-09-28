# Hulk DIGEST — 2026-09-28T18:29:21Z

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
| WUSDT | IDLE | 1.74 | 8.22 | 5.97 | -0.1 | 2607587.06 | 11.74 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 3.98 | 1.5 | -0.02 | 66850769.6 | 1.99 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 18.61 | 7.84 | 0.31 | 22237773.54 | 11.73 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 13.26 | 2.07 | 0.35 | 10606022.67 | 3.9 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.55 | 0.89 | 0.0 | 395265254.1 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 1.11 | 2.14 | 0.5 | -0.01 | 821869458.17 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.12 | 5.44 | 3.53 | -0.08 | 1299571.55 | 3.79 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 5.9 | 0.96 | -0.04 | 1340874.8 | 3.02 | skipped_fast |
| CHIPUSDT | IDLE | 2.74 | 6.46 | 4.13 | -0.07 | 68446.31 | 15.89 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.45 | 9.21 | 5.35 | 0.07 | 14633.81 | 131.8 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.1 | 9.69 | 0.61 | 0.05 | 153348.85 | 5.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.75 | 2.23 | -0.05 | 238660.35 | 27.6 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 4.83 | 1.92 | -0.07 | 114377.17 | 3.38 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 6.35 | 2.21 | -0.09 | 101021.94 | 15.91 | skipped_fast |
| REDUSDT | IDLE | 1.76 | 4.06 | 1.91 | -0.06 | 62083.28 | 14.89 | skipped_fast |
| EDELUSDT | IDLE | 0.72 | 4.59 | 2.28 | 0.13 | 178581.25 | 27.37 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 3.36 | 0.18 | -0.12 | 67072.92 | 58.74 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 3.66 | 0.0 | -0.05 | 3178.67 | 21.85 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.67 | 0.5 | -0.01 | 60547.53 | 14.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 0.96 | 0.6 | -0.02 | 34785.68 | 14.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
