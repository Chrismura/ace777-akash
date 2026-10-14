# Hulk DIGEST — 2026-10-14T20:24:25Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.53 | 8.82 | 0.27 | 0.1 | 1891739.2 | 8.21 | skipped_fast |
| WUSDT | IDLE | 1.0 | 4.46 | 1.56 | -0.1 | 2562404.16 | 5.21 | skipped_fast |
| XRPUSDT | IDLE | 0.82 | 1.49 | 1.06 | -0.03 | 44996275.75 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.33 | 0.84 | -0.03 | 203043862.46 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.68 | 0.15 | -0.01 | 434178251.16 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.35 | 4.53 | 1.14 | -0.05 | 1122337.45 | 4.8 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 5.26 | 3.45 | -0.03 | 195575.31 | 9.08 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 3.38 | 2.48 | -0.09 | 415605.77 | 8.58 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.72 | 11.33 | 5.84 | 0.08 | 18479.93 | 21.68 | skipped_fast |
| CHIPUSDT | IDLE | 1.98 | 5.83 | 3.93 | -0.08 | 104342.92 | 16.98 | skipped_fast |
| RWAINCUSDT | IDLE | 2.26 | 6.51 | 1.78 | -0.07 | 28860.29 | 20.76 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.61 | 2.75 | -0.04 | 166914.11 | 48.24 | skipped_fast |
| REDUSDT | IDLE | 2.23 | 4.43 | 0.15 | 0.02 | 61943.84 | 12.05 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 5.27 | 3.92 | -0.01 | 86388.48 | 12.55 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 2.29 | 0.92 | -0.04 | 526365.15 | 8.29 | skipped_fast |
| TELUSDT | IDLE | 2.87 | 5.3 | 2.9 | 0.01 | 103712.89 | 28.18 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 2.71 | 1.78 | -0.04 | 65963.08 | 3.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 2.68 | 0.96 | -0.0 | 49010.49 | 61.33 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.64 | 0.47 | -0.03 | 56359.62 | 23.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.61 | 0.22 | -0.01 | 36403.4 | 29.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
