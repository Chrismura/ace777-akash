# Hulk DIGEST — 2026-09-27T17:11:03Z

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
| PYTHUSDT | IDLE | 1.88 | 6.98 | 3.34 | 0.11 | 2172931.08 | 3.52 | skipped_fast |
| WUSDT | IDLE | 1.66 | 10.92 | 0.4 | 0.19 | 4099145.2 | 11.51 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 20.99 | 2.29 | 0.51 | 6140237.7 | 12.4 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 2.43 | 1.66 | -0.01 | 44630402.55 | 1.32 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.28 | 1.05 | -0.0 | 192601717.05 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.95 | 0.88 | 0.0 | 453071181.68 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 42.2 | 24.12 | 0.08 | 25271.9 | 147.81 | skipped_fast |
| CCUSDT | IDLE | 2.7 | 5.02 | 2.57 | -0.02 | 538183.85 | 6.66 | skipped_fast |
| CHIPUSDT | IDLE | 3.31 | 5.98 | 4.71 | -0.06 | 99991.9 | 21.24 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.07 | 2.34 | -0.01 | 691773.11 | 1.07 | skipped_fast |
| EDELUSDT | IDLE | 2.33 | 8.31 | 6.64 | -0.11 | 137430.66 | 22.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 1.95 | 1.87 | -0.02 | 211410.63 | 6.69 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 3.05 | 1.31 | -0.04 | 93978.03 | 9.48 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 3.18 | 1.02 | 0.04 | 172783.27 | 8.66 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.76 | 0.47 | 0.01 | 64721.72 | 14.09 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 6.49 | 2.49 | 0.16 | 147720.15 | 81.41 | skipped_fast |
| RIZEUSDT | IDLE | 0.52 | 1.94 | 1.03 | -0.05 | 46262.27 | 64.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.79 | 0.15 | 0.02 | 1556.07 | 21.51 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.85 | 0.35 | 0.01 | 56388.6 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.52 | 0.34 | 0.01 | 39612.25 | 37.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
