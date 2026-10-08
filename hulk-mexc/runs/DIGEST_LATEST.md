# Hulk DIGEST — 2026-10-08T07:13:15Z

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
| WUSDT | IDLE | 1.75 | 14.23 | 9.85 | 0.15 | 3242215.3 | 9.6 | skipped_fast |
| QNTUSDT | IDLE | 3.41 | 6.6 | 4.63 | -0.05 | 2577341.43 | 9.08 | skipped_fast |
| XRPUSDT | IDLE | 1.48 | 2.73 | 1.55 | -0.05 | 41823983.85 | 2.84 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.5 | 0.64 | -0.02 | 437938016.95 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.27 | 0.32 | -0.01 | 729825169.11 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 4.16 | 0.2 | 0.02 | 566759.91 | 4.02 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 15.32 | 11.34 | -0.17 | 407056.24 | 119.38 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 3.65 | 1.94 | -0.03 | 385473.55 | 8.56 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 4.81 | 3.8 | -0.06 | 283872.07 | 16.23 | skipped_fast |
| CHIPUSDT | IDLE | 2.3 | 8.29 | 5.69 | 0.04 | 135905.95 | 15.17 | skipped_fast |
| BIOUSDT | IDLE | 2.36 | 4.64 | 3.52 | 0.01 | 73033.34 | 6.81 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 2.92 | 1.09 | -0.04 | 465863.57 | 3.23 | skipped_fast |
| RIZEUSDT | IDLE | 1.39 | 8.93 | 1.84 | -0.07 | 52457.29 | 33.38 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 2.63 | 1.97 | -0.02 | 56525.94 | 8.72 | skipped_fast |
| KITEUSDT | IDLE | 1.48 | 2.95 | 0.0 | -0.03 | 67259.24 | 11.1 | skipped_fast |
| RWAINCUSDT | IDLE | 1.49 | 7.69 | 2.2 | -0.13 | 48209.48 | 65.15 | skipped_fast |
| TELUSDT | IDLE | 1.44 | 2.63 | 1.91 | -0.06 | 135228.03 | 40.94 | skipped_fast |
| FLUIDUSDT | IDLE | 1.33 | 3.94 | 2.64 | 0.09 | 17388.54 | 21.45 | skipped_fast |
| MNSRYUSDT | IDLE | 1.25 | 2.27 | 1.49 | -0.02 | 35777.0 | 51.64 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.45 | 0.3 | -0.0 | 50439.45 | 14.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
