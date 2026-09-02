# Hulk DIGEST — 2026-09-02T08:35:25Z

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
| XRPUSDT | IDLE | 0.91 | 1.59 | 1.53 | -0.02 | 37486123.74 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 0.98 | 0.91 | -0.02 | 359416833.39 | 0.21 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.91 | 0.89 | -0.01 | 505749901.03 | 0.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 7.58 | 0.61 | 0.15 | 949596.15 | 6.49 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 7.01 | 2.66 | 0.12 | 817321.87 | 1.82 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 16.28 | 5.77 | 0.05 | 173599.04 | 32.55 | skipped_fast |
| CCUSDT | IDLE | 2.26 | 4.27 | 3.71 | -0.07 | 339105.98 | 10.71 | skipped_fast |
| WUSDT | IDLE | 2.07 | 3.84 | 2.06 | 0.02 | 407106.43 | 15.57 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.41 | 10.57 | 1.64 | 0.1 | 10357.02 | 42.85 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 9.77 | 0.49 | 0.15 | 75064.48 | 8.81 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 2.67 | 2.09 | -0.01 | 216265.8 | 12.61 | skipped_fast |
| RIZEUSDT | IDLE | 1.9 | 6.4 | 5.85 | -0.12 | 39450.72 | 78.72 | skipped_fast |
| QNTUSDT | IDLE | 2.54 | 6.12 | 2.95 | 0.06 | 63143.16 | 7.68 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.94 | 1.24 | 0.0 | 154512.57 | 10.8 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.18 | 1.17 | -0.03 | 74271.88 | 3.93 | skipped_fast |
| HBARUSDT | IDLE | 0.53 | 0.96 | 0.62 | -0.0 | 229274.05 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 1.73 | 1.58 | -0.02 | 87252.76 | 71.26 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.47 | 0.0 | -0.03 | 323.84 | 0.78 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.62 | 0.38 | -0.01 | 50529.6 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.66 | 0.26 | -0.01 | 36086.32 | 65.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
