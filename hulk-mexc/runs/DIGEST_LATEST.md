# Hulk DIGEST — 2026-09-14T15:42:42Z

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
| XRPUSDT | IDLE | 0.96 | 1.87 | 0.28 | 0.05 | 42116972.2 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.5 | 0.6 | 0.01 | 351213776.36 | 0.16 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.55 | 0.21 | 0.02 | 456754615.98 | 0.08 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.96 | 10.34 | 6.4 | 0.06 | 176948.51 | 18.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.12 | 1.25 | 0.01 | 486512.65 | 3.61 | skipped_fast |
| WUSDT | IDLE | 2.35 | 4.27 | 2.89 | -0.01 | 221253.56 | 5.04 | skipped_fast |
| RIZEUSDT | IDLE | 1.63 | 18.12 | 13.54 | 0.04 | 68169.56 | 53.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 4.89 | 2.68 | -0.04 | 87861.37 | 19.16 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 5.75 | 3.22 | 0.14 | 253261.13 | 27.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 2.8 | 0.5 | 0.01 | 206725.55 | 25.61 | skipped_fast |
| CCUSDT | IDLE | 0.81 | 1.49 | 0.91 | 0.01 | 273827.25 | 8.33 | skipped_fast |
| BIOUSDT | IDLE | 1.27 | 2.42 | 0.81 | 0.01 | 83624.71 | 3.9 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.07 | 1.91 | -0.02 | 62117.62 | 10.49 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.61 | 0.88 | 0.01 | 289048.03 | 2.6 | skipped_fast |
| TELUSDT | IDLE | 1.27 | 2.33 | 1.42 | 0.01 | 89153.36 | 49.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 2.78 | 0.0 | 0.04 | 10229.63 | 169.17 | skipped_fast |
| QNTUSDT | IDLE | 0.84 | 1.68 | 0.0 | 0.01 | 41229.81 | 4.63 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 1.9 | 1.86 | 0.0 | 623.71 | 22.83 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.15 | 0.01 | 54819.45 | 29.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.38 | 0.22 | -0.0 | 28705.87 | 18.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
