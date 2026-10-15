# Hulk DIGEST — 2026-10-15T02:24:37Z

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
| WUSDT | IDLE | 2.43 | 8.22 | 5.05 | -0.1 | 2621270.65 | 22.07 | skipped_fast |
| PYTHUSDT | IDLE | 2.04 | 5.51 | 3.62 | 0.06 | 2241398.63 | 15.34 | skipped_fast |
| XRPUSDT | IDLE | 1.73 | 3.03 | 2.86 | -0.05 | 49228682.4 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 1.43 | 2.5 | 2.4 | -0.05 | 264232642.98 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.15 | 1.13 | -0.03 | 475047930.24 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 8.8 | 7.88 | -0.09 | 1056149.61 | 21.28 | skipped_fast |
| CCUSDT | IDLE | 1.87 | 5.74 | 5.3 | -0.11 | 423908.83 | 12.71 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.76 | 7.91 | 7.33 | -0.1 | 70081.85 | 4.05 | skipped_fast |
| CHIPUSDT | IDLE | 2.14 | 11.63 | 10.42 | -0.17 | 111834.82 | 19.12 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 4.52 | 4.32 | -0.06 | 176963.0 | 36.89 | skipped_fast |
| HBARUSDT | IDLE | 1.94 | 3.4 | 3.2 | -0.06 | 550336.74 | 8.52 | skipped_fast |
| ZBCNUSDT | IDLE | 1.74 | 3.88 | 3.73 | -0.07 | 194575.65 | 19.86 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 4.7 | 4.49 | -0.06 | 87127.87 | 12.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.93 | 4.25 | 1.74 | 0.01 | 25479.38 | 30.3 | skipped_fast |
| REDUSDT | IDLE | 1.24 | 2.16 | 2.12 | -0.0 | 63649.67 | 12.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 7.12 | 3.8 | -0.04 | 55047.84 | 61.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.75 | 5.03 | 4.79 | 0.01 | 20366.69 | 21.33 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 3.03 | 2.88 | -0.05 | 98358.32 | 46.67 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.8 | 0.72 | -0.04 | 56989.87 | 24.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.72 | 0.72 | -0.01 | 33235.19 | 73.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
