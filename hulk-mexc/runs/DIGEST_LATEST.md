# Hulk DIGEST — 2026-09-23T03:16:22Z

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
| PYTHUSDT | IDLE | 1.03 | 4.83 | 2.05 | 0.06 | 1762599.29 | 4.48 | skipped_fast |
| XRPUSDT | IDLE | 1.5 | 2.94 | 0.38 | 0.05 | 104129451.38 | 2.51 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.41 | 0.37 | 0.01 | 392285880.62 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.95 | 0.35 | 0.01 | 868667124.99 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.18 | 3.04 | 1.03 | 0.09 | 1792342.55 | 1.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.62 | 5.23 | 0.0 | 0.03 | 215696.66 | 12.85 | skipped_fast |
| WUSDT | IDLE | 2.05 | 4.06 | 0.27 | 0.05 | 325620.52 | 5.64 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 2.41 | 1.35 | -0.02 | 401542.47 | 8.75 | skipped_fast |
| EDELUSDT | IDLE | 1.32 | 6.49 | 2.11 | -0.01 | 267474.26 | 23.13 | skipped_fast |
| RIZEUSDT | IDLE | 1.46 | 26.82 | 0.27 | 0.54 | 49472.58 | 84.96 | skipped_fast |
| CHIPUSDT | IDLE | 2.13 | 4.44 | 0.42 | 0.0 | 118744.55 | 19.09 | skipped_fast |
| BIOUSDT | IDLE | 1.77 | 3.43 | 0.69 | 0.05 | 109165.55 | 9.94 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 3.34 | 2.97 | 0.02 | 21193.29 | 5.4 | skipped_fast |
| KITEUSDT | IDLE | 0.78 | 3.1 | 1.24 | 0.16 | 125293.89 | 7.88 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 2.44 | 0.0 | 0.04 | 59807.91 | 8.71 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 3.98 | 1.65 | 0.13 | 215548.62 | 9.32 | skipped_fast |
| TELUSDT | IDLE | 0.85 | 3.6 | 1.28 | 0.14 | 108237.03 | 48.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.83 | 0.0 | 0.02 | 5475.4 | 21.56 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.02 | 0.29 | 0.01 | 52565.96 | 7.22 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.72 | 0.03 | 0.01 | 40017.03 | 10.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
