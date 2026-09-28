# Hulk DIGEST — 2026-09-28T03:15:11Z

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
| QNTUSDT | IDLE | 2.12 | 68.44 | 30.85 | 0.5 | 14796927.15 | 19.01 | skipped_fast |
| WUSDT | IDLE | 2.32 | 8.88 | 7.98 | 0.07 | 5348057.01 | 7.49 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 3.33 | 2.13 | 0.01 | 2001850.24 | 12.03 | skipped_fast |
| XRPUSDT | IDLE | 1.51 | 2.69 | 2.23 | -0.01 | 48043625.08 | 0.67 | skipped_fast |
| ETHUSDT | IDLE | 1.15 | 2.04 | 1.7 | -0.02 | 248405168.52 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.09 | 1.9 | 1.81 | -0.01 | 482453044.26 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.12 | 7.73 | 0.96 | 0.06 | 723899.55 | 4.17 | skipped_fast |
| HBARUSDT | IDLE | 2.4 | 4.38 | 2.86 | 0.01 | 919504.6 | 1.05 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 7.74 | 6.67 | -0.07 | 109993.96 | 7.61 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 6.05 | 5.43 | -0.03 | 89157.71 | 6.52 | skipped_fast |
| ZBCNUSDT | IDLE | 1.7 | 3.05 | 2.37 | -0.03 | 248705.97 | 14.25 | skipped_fast |
| REDUSDT | IDLE | 2.21 | 3.86 | 3.71 | -0.03 | 66576.37 | 8.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.95 | 4.35 | 3.81 | -0.06 | 94915.97 | 15.41 | skipped_fast |
| RIZEUSDT | IDLE | 1.4 | 13.55 | 6.22 | -0.22 | 65414.23 | 39.51 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 7.71 | 5.21 | -0.13 | 157652.45 | 48.27 | skipped_fast |
| FLUIDUSDT | IDLE | 2.36 | 4.13 | 3.97 | 0.01 | 3567.99 | 21.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 6.69 | 3.65 | 0.22 | 31261.1 | 107.63 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.24 | 1.76 | 0.02 | 174749.5 | 21.74 | skipped_fast |
| MNSRYUSDT | IDLE | 1.13 | 1.98 | 1.92 | -0.0 | 39653.61 | 65.46 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.22 | 0.92 | 0.0 | 59301.55 | 35.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
