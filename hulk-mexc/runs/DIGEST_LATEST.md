# Hulk DIGEST — 2026-10-11T13:20:12Z

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
| XRPUSDT | IDLE | 0.34 | 0.66 | 0.14 | -0.01 | 10159801.65 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.12 | 0.0 | 178374597.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.34 | 0.17 | 0.0 | 123359833.11 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.9 | 2.42 | 1.21 | 0.0 | 1136898.45 | 12.62 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 31.62 | 16.77 | 0.05 | 56477.96 | 4.65 | skipped_fast |
| QNTUSDT | IDLE | 1.92 | 3.83 | 0.02 | -0.03 | 1048219.87 | 2.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.53 | 1.54 | -0.02 | 710841.74 | 1.3 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 3.5 | 2.47 | 0.0 | 371876.47 | 12.91 | skipped_fast |
| CCUSDT | IDLE | 1.85 | 3.67 | 0.2 | 0.03 | 290259.5 | 6.46 | skipped_fast |
| CHIPUSDT | IDLE | 0.89 | 8.41 | 2.6 | 0.29 | 373415.29 | 16.45 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.53 | 6.22 | 5.85 | -0.07 | 145128.52 | 17.7 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 6.58 | 2.65 | -0.07 | 35363.91 | 36.21 | skipped_fast |
| BIOUSDT | IDLE | 1.54 | 2.99 | 0.63 | 0.04 | 78647.66 | 3.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 2.31 | 0.33 | 0.0 | 160027.17 | 18.75 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.2 | 0.74 | -0.01 | 58326.73 | 16.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.11 | 2.23 | 0.0 | -0.01 | 22915.27 | 34.63 | skipped_fast |
| KITEUSDT | IDLE | 0.66 | 1.24 | 0.48 | -0.03 | 74672.77 | 12.67 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.65 | 0.29 | -0.01 | 225832.21 | 2.17 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.95 | 0.08 | -0.0 | 52581.48 | 15.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.16 | -0.01 | 32089.43 | 38.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
