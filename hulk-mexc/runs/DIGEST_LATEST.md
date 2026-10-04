# Hulk DIGEST — 2026-10-04T23:58:42Z

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
| QNTUSDT | IDLE | 2.19 | 8.34 | 2.85 | -0.02 | 3311520.79 | 11.89 | skipped_fast |
| XRPUSDT | IDLE | 0.95 | 1.84 | 0.46 | 0.02 | 20465438.9 | 0.66 | skipped_fast |
| BTCUSDT | IDLE | 0.89 | 1.73 | 0.35 | 0.02 | 350171143.22 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.43 | 0.42 | 0.01 | 134590085.61 | 0.66 | skipped_fast |
| EDELUSDT | IDLE | 2.8 | 6.67 | 2.44 | 0.04 | 535326.19 | 14.14 | skipped_fast |
| WUSDT | IDLE | 0.71 | 1.97 | 0.77 | 0.05 | 1026117.94 | 10.31 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.55 | 8.15 | 1.97 | 0.06 | 220181.62 | 18.68 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 7.97 | 5.93 | -0.06 | 5958.55 | 41.75 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.0 | 13.25 | 1.86 | 0.12 | 44701.26 | 44.08 | skipped_fast |
| CCUSDT | IDLE | 1.0 | 1.98 | 0.12 | 0.04 | 354068.93 | 8.51 | skipped_fast |
| PYTHUSDT | IDLE | 0.58 | 1.12 | 0.28 | -0.0 | 345334.7 | 2.56 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.33 | 0.34 | 0.02 | 479746.64 | 5.76 | skipped_fast |
| REDUSDT | IDLE | 1.64 | 3.25 | 0.25 | -0.02 | 71317.59 | 13.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.42 | 4.69 | 2.28 | 0.11 | 66590.46 | 12.28 | skipped_fast |
| KITEUSDT | IDLE | 0.87 | 1.82 | 0.77 | -0.03 | 83095.82 | 7.49 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 1.78 | 0.06 | -0.01 | 74051.48 | 6.5 | skipped_fast |
| TELUSDT | IDLE | 1.52 | 2.99 | 0.36 | -0.01 | 132123.51 | 20.44 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.52 | 0.24 | 0.04 | 4172.02 | 21.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 0.92 | 0.62 | -0.0 | 44390.02 | 31.1 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.51 | 0.07 | 0.0 | 52240.67 | 14.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
