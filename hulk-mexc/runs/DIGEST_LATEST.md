# Hulk DIGEST — 2026-08-26T06:53:06Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 2.71 | 6.13 | 0.02 | 0.06 | 2907847.06 | 5.59 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 73.61 | 38.91 | 0.09 | 63007.19 | 65.57 | skipped_fast |
| XRPUSDT | IDLE | 0.95 | 1.75 | 0.98 | -0.04 | 58967653.47 | 0.7 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.93 | 31.72 | 12.21 | 0.12 | 16511.01 | 21.61 | skipped_fast |
| WUSDT | IDLE | 2.42 | 4.58 | 1.75 | -0.01 | 295913.61 | 14.58 | skipped_fast |
| CHIPUSDT | IDLE | 2.09 | 4.31 | 2.49 | -0.03 | 319891.28 | 6.23 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 2.08 | 1.43 | -0.05 | 498065.64 | 10.1 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 4.1 | 3.57 | -0.04 | 97911.66 | 7.04 | skipped_fast |
| REDUSDT | IDLE | 2.02 | 4.82 | 4.6 | -0.02 | 76356.87 | 20.41 | skipped_fast |
| EDELUSDT | IDLE | 0.9 | 12.46 | 8.7 | 0.02 | 160012.2 | 28.02 | skipped_fast |
| KITEUSDT | IDLE | 1.81 | 3.41 | 1.4 | -0.01 | 61039.3 | 7.86 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 2.78 | 0.88 | -0.02 | 156662.25 | 15.76 | skipped_fast |
| HBARUSDT | IDLE | 0.6 | 1.08 | 0.76 | -0.04 | 527558.28 | 1.28 | skipped_fast |
| QAITUSDT | IDLE | 1.64 | 3.03 | 1.69 | 0.03 | 8910.47 | 63.52 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.33 | 0.27 | -0.01 | 93298.23 | 27.21 | skipped_fast |
| QNTUSDT | IDLE | 0.64 | 1.19 | 0.55 | -0.04 | 130470.29 | 6.31 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 1.84 | 1.81 | -0.05 | 56776.51 | 25.07 | skipped_fast |
| RWAINCUSDT | IDLE | 0.78 | 1.37 | 1.3 | -0.01 | 1277.4 | 121.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
