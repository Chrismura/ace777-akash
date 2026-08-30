# Hulk DIGEST — 2026-08-30T16:45:53Z

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
| ETHUSDT | IDLE | 1.59 | 3.14 | 0.28 | 0.03 | 201727787.78 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.88 | 1.74 | 0.11 | 0.01 | 18743570.8 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.46 | 0.08 | 0.02 | 267489646.58 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 8.01 | 5.93 | -0.03 | 538887.41 | 2.5 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 9.26 | 7.6 | -0.08 | 188303.77 | 29.1 | skipped_fast |
| PYTHUSDT | IDLE | 3.14 | 5.93 | 2.35 | 0.02 | 400114.06 | 2.04 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 5.99 | 3.15 | 0.07 | 72216.42 | 16.68 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.69 | 0.7 | 0.04 | 220649.26 | 12.61 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.62 | 1.11 | 0.01 | 260454.33 | 9.29 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 2.53 | 0.69 | 0.02 | 61437.41 | 12.62 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.62 | 0.36 | -0.0 | 76738.11 | 3.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.59 | 3.19 | 0.0 | 0.02 | 1854.4 | 55.28 | skipped_fast |
| KITEUSDT | IDLE | 0.9 | 1.67 | 0.88 | -0.03 | 61693.59 | 12.47 | skipped_fast |
| TELUSDT | IDLE | 2.02 | 4.03 | 0.06 | -0.01 | 83062.99 | 23.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 2.45 | 0.67 | -0.05 | 45984.1 | 60.63 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.13 | 0.54 | -0.0 | 126488.95 | 1.33 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.02 | 33004.13 | 2.67 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.14 | 0.39 | 0.01 | 38472.3 | 4.84 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 21.43 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.15 | 0.08 | 0.01 | 52913.47 | 16.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
