# Hulk DIGEST — 2026-09-17T17:16:57Z

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
| XRPUSDT | IDLE | 1.24 | 2.29 | 1.23 | 0.03 | 57029539.28 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 1.06 | 2.02 | 0.61 | 0.03 | 408472720.51 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.77 | 1.48 | 0.44 | 0.01 | 512858543.41 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.3 | 6.15 | 0.51 | 0.09 | 615244.66 | 1.76 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 4.1 | 2.43 | 0.1 | 635219.25 | 8.94 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.79 | 8.92 | 6.35 | -0.07 | 185840.63 | 29.09 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 20.66 | 5.88 | -0.1 | 45970.84 | 73.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.23 | 7.14 | 4.94 | 0.06 | 141073.79 | 15.75 | skipped_fast |
| WUSDT | IDLE | 1.9 | 5.89 | 0.58 | 0.11 | 243992.25 | 15.39 | skipped_fast |
| HBARUSDT | IDLE | 1.79 | 3.5 | 0.54 | 0.04 | 570308.47 | 1.31 | skipped_fast |
| ZBCNUSDT | IDLE | 2.25 | 4.32 | 1.17 | 0.03 | 177233.42 | 17.99 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 3.03 | 2.23 | 0.03 | 65129.65 | 4.61 | skipped_fast |
| RWAINCUSDT | IDLE | 1.92 | 3.46 | 2.48 | 0.01 | 21400.16 | 23.68 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 2.98 | 0.01 | 0.01 | 62266.81 | 12.29 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.21 | 0.39 | 0.04 | 68457.77 | 7.88 | skipped_fast |
| TELUSDT | IDLE | 1.79 | 3.41 | 1.08 | 0.04 | 90016.66 | 81.25 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.09 | 1.19 | 0.03 | 36637.72 | 4.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.89 | 1.7 | 0.51 | 0.01 | 41668.31 | 8.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.04 | 260.02 | 22.54 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.3 | 0.01 | 57982.92 | 44.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
