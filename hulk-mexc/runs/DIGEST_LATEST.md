# Hulk DIGEST — 2026-09-22T02:08:18Z

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
| XRPUSDT | IDLE | 1.86 | 4.67 | 3.91 | 0.07 | 112127622.89 | 0.66 | skipped_fast |
| BTCUSDT | IDLE | 1.05 | 1.86 | 1.6 | 0.05 | 1078571043.64 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 1.03 | 1.84 | 1.41 | 0.03 | 691915349.63 | 0.69 | skipped_fast |
| PYTHUSDT | IDLE | 2.26 | 5.01 | 2.37 | 0.04 | 751700.99 | 7.88 | skipped_fast |
| CCUSDT | IDLE | 2.35 | 4.43 | 1.81 | 0.06 | 666407.05 | 6.79 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 17.48 | 13.82 | 0.06 | 238226.24 | 23.26 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 2.49 | 2.02 | 0.07 | 1103944.25 | 1.09 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.45 | 0.77 | 0.05 | 540659.46 | 5.05 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 19.17 | 13.03 | -0.21 | 54699.15 | 86.98 | skipped_fast |
| ZBCNUSDT | IDLE | 2.1 | 4.61 | 3.74 | 0.03 | 264133.4 | 42.28 | skipped_fast |
| REDUSDT | IDLE | 2.43 | 4.77 | 0.64 | 0.04 | 99199.04 | 7.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 5.8 | 1.09 | 0.11 | 166633.9 | 21.18 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 2.73 | 1.09 | 0.06 | 110612.64 | 10.33 | skipped_fast |
| KITEUSDT | IDLE | 1.54 | 2.87 | 1.43 | 0.04 | 80920.47 | 10.86 | skipped_fast |
| RWAINCUSDT | IDLE | 0.82 | 1.92 | 1.73 | 0.08 | 19770.73 | 5.48 | skipped_fast |
| QNTUSDT | IDLE | 1.68 | 3.17 | 1.25 | 0.04 | 115196.96 | 13.39 | skipped_fast |
| TELUSDT | IDLE | 1.16 | 3.35 | 2.28 | 0.07 | 116003.11 | 67.55 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.46 | 0.93 | 0.0 | 57849.92 | 36.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.79 | 1.5 | 0.51 | 0.03 | 41539.04 | 39.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.33 | 1.02 | 0.09 | 12018.84 | 21.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
