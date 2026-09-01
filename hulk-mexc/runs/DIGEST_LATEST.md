# Hulk DIGEST — 2026-09-01T11:22:50Z

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
| XRPUSDT | IDLE | 1.32 | 2.45 | 1.21 | -0.0 | 29150476.86 | 2.18 | skipped_fast |
| BTCUSDT | IDLE | 1.02 | 1.81 | 1.59 | -0.01 | 563891359.06 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 1.01 | 1.83 | 1.24 | -0.0 | 292917019.06 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 27.51 | 20.06 | -0.05 | 178847.14 | 17.38 | skipped_fast |
| PYTHUSDT | IDLE | 2.13 | 5.52 | 1.04 | 0.06 | 585793.79 | 1.98 | skipped_fast |
| CHIPUSDT | IDLE | 2.6 | 4.67 | 3.57 | -0.04 | 340792.77 | 5.11 | skipped_fast |
| CCUSDT | IDLE | 2.13 | 3.79 | 3.16 | -0.0 | 389717.5 | 2.51 | skipped_fast |
| REDUSDT | IDLE | 3.21 | 6.02 | 2.61 | 0.0 | 61109.23 | 14.62 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.09 | 1.19 | 0.03 | 235564.56 | 14.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 2.97 | 1.1 | 0.04 | 181176.42 | 13.38 | skipped_fast |
| RWAUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.26 | 6.19 | 0.03 | 64458.07 | 38.51 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.13 | 2.1 | -0.01 | 62162.18 | 3.83 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 2.66 | 1.13 | -0.02 | 62006.1 | 10.97 | skipped_fast |
| RIZEUSDT | IDLE | 1.52 | 5.19 | 1.57 | -0.07 | 37556.09 | 71.37 | skipped_fast |
| RWAINCUSDT | IDLE | 1.34 | 2.62 | 0.41 | -0.02 | 4544.94 | 29.06 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.73 | 0.63 | 0.0 | 243675.66 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.28 | 2.35 | 1.43 | -0.01 | 83957.92 | 5.82 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.69 | 0.23 | 0.0 | 48959.33 | 1.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.71 | 0.47 | 0.0 | 30062.34 | 12.2 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1143.37 | 20.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
