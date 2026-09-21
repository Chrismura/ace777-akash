# Hulk DIGEST — 2026-09-21T08:03:35Z

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
| XRPUSDT | IDLE | 1.09 | 2.16 | 0.08 | 0.04 | 45407321.75 | 2.08 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.19 | 0.42 | 0.03 | 347023788.65 | 0.97 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.77 | 0.03 | 0.02 | 450470422.46 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.22 | 8.2 | 4.02 | 0.08 | 548767.02 | 8.41 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 2.32 | 0.86 | 0.07 | 1204427.19 | 1.15 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 25.26 | 12.26 | -0.11 | 42702.8 | 97.76 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 4.59 | 2.55 | 0.03 | 195522.15 | 39.38 | skipped_fast |
| PYTHUSDT | IDLE | 0.7 | 1.6 | 0.31 | 0.06 | 527097.61 | 6.5 | skipped_fast |
| CHIPUSDT | IDLE | 2.64 | 6.98 | 0.2 | 0.07 | 89001.87 | 24.5 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 2.35 | 0.38 | 0.09 | 415704.59 | 8.83 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.71 | 0.42 | 0.05 | 80948.51 | 10.61 | skipped_fast |
| EDELUSDT | IDLE | 0.44 | 5.59 | 0.93 | 0.47 | 215527.59 | 17.41 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 1.86 | 0.69 | -0.01 | 74281.14 | 9.9 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.92 | 0.56 | 0.02 | 63369.68 | 11.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.08 | 1.91 | 1.64 | -0.0 | 5409.57 | 23.84 | skipped_fast |
| TELUSDT | IDLE | 1.56 | 2.8 | 2.08 | 0.03 | 87287.13 | 53.02 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 1.83 | 0.29 | 0.03 | 109654.37 | 7.59 | skipped_fast |
| FLUIDUSDT | IDLE | 1.13 | 2.12 | 0.91 | 0.03 | 4792.57 | 21.16 | skipped_fast |
| RWAUSDT | IDLE | 0.75 | 1.32 | 1.16 | 0.01 | 55232.12 | 22.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.34 | 0.16 | 0.01 | 40872.35 | 7.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
