# Hulk DIGEST — 2026-09-28T13:23:59Z

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
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.46 | 29.05 | 5.32 | 0.26 | 6601477.69 | 9.29 | skipped_fast |
| QNTUSDT | IDLE | 1.27 | 39.28 | 12.64 | 0.49 | 20334452.4 | 5.47 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 14.75 | 10.63 | -0.04 | 1230694.28 | 6.85 | skipped_fast |
| WUSDT | IDLE | 1.36 | 6.03 | 0.92 | -0.03 | 3186333.49 | 7.64 | skipped_fast |
| XRPUSDT | IDLE | 1.92 | 3.79 | 0.36 | -0.0 | 57293253.17 | 1.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.98 | 4.53 | 1.91 | -0.05 | 1505680.65 | 2.47 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 2.11 | 0.34 | -0.01 | 326753634.41 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.21 | 0.25 | -0.02 | 694601154.46 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.62 | 24.05 | 4.44 | 0.03 | 192428.01 | 6.78 | skipped_fast |
| ZBCNUSDT | IDLE | 1.19 | 2.32 | 0.38 | -0.04 | 226075.39 | 0.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.89 | 0.11 | -0.04 | 82692.66 | 15.44 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 3.38 | 1.0 | -0.03 | 61689.49 | 12.85 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 3.84 | 1.4 | -0.06 | 99003.05 | 7.2 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 2.94 | 1.06 | -0.06 | 95234.44 | 3.36 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 3.41 | 0.27 | 0.01 | 163144.34 | 33.08 | skipped_fast |
| RWAINCUSDT | IDLE | 0.55 | 5.69 | 0.94 | 0.16 | 34441.39 | 63.24 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 2.89 | 0.99 | -0.15 | 60029.29 | 99.59 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.31 | 0.72 | -0.02 | 59602.07 | 28.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.73 | 0.15 | -0.02 | 34713.63 | 6.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.61 | 1.5 | 0.0 | -0.05 | 3101.03 | 21.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
