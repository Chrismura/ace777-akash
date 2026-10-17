# Hulk DIGEST — 2026-10-17T12:18:07Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 5.84 | 5.42 | -0.02 | 1313806.74 | 17.34 | skipped_fast |
| XRPUSDT | IDLE | 0.43 | 0.75 | 0.72 | -0.03 | 20919672.45 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.45 | 0.4 | -0.01 | 127432094.79 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.25 | 0.24 | -0.01 | 257777590.29 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.99 | 1.91 | 0.48 | -0.06 | 1354632.53 | 5.89 | skipped_fast |
| ZBCNUSDT | IDLE | 2.15 | 4.76 | 1.68 | -0.05 | 224834.66 | 18.27 | skipped_fast |
| KITEUSDT | IDLE | 2.57 | 4.54 | 3.98 | -0.02 | 60945.18 | 13.22 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.57 | 0.97 | -0.04 | 590546.2 | 5.4 | skipped_fast |
| CHIPUSDT | IDLE | 1.7 | 3.18 | 2.35 | -0.07 | 98462.81 | 13.13 | skipped_fast |
| CCUSDT | IDLE | 0.73 | 1.38 | 0.53 | 0.01 | 295552.75 | 9.62 | skipped_fast |
| EDELUSDT | IDLE | 1.2 | 2.11 | 1.9 | -0.05 | 156214.26 | 10.38 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 4.26 | 1.42 | -0.06 | 22835.14 | 5.32 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 1.96 | 1.65 | -0.07 | 70497.06 | 8.51 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.5 | 1.48 | -0.05 | 66502.06 | 4.06 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 1.3 | 0.42 | 0.01 | 44696.22 | 48.52 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.52 | 1.34 | -0.04 | 166870.32 | 4.82 | skipped_fast |
| RWAUSDT | IDLE | 1.21 | 2.35 | 0.4 | -0.01 | 52886.69 | 23.88 | skipped_fast |
| FLUIDUSDT | IDLE | 1.34 | 2.7 | 0.0 | 0.05 | 3788.43 | 21.51 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 1.48 | 0.99 | -0.06 | 86603.82 | 23.68 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.23 | 0.08 | -0.0 | 27622.9 | 5.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
