# Hulk DIGEST — 2026-08-22T09:57:02Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 19.14 | 11.23 | 0.02 | 50444964.15 | 6.05 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 11.95 | 0.05 | 216206009.17 | 5.35 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 15.8 | 10.72 | 0.02 | 1261841.9 | 3.86 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 23.96 | 12.62 | -0.1 | 665022.72 | 3.38 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 17.58 | 9.58 | 0.02 | 592597.17 | 14.73 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.16 | -0.02 | 236878.12 | 3.22 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 41.27 | 12.43 | 0.05 | 153971.88 | 11.57 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.29 | 0.12 | 806575.59 | 9.57 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 8.0 | 7.2 | -0.02 | 438599.15 | 27.93 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 9.68 | 5.0 | 0.04 | 73312.08 | 11.01 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.15 | 0.01 | 191948.67 | 4.66 | n/a |
| EDELUSDT | IDLE | 2.64 | 4.64 | 4.22 | -0.03 | 79190.58 | 33.76 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 7.2 | 6.56 | -0.02 | 171072.05 | 21.14 | no_map |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 19.19 | tvl≈2,553,890,177 |
| RWAINCUSDT | IDLE | 2.45 | 4.36 | 3.61 | 0.01 | 11477.95 | 75.72 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.82 | -0.0 | 49318.51 | 46.77 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.02 | 57604.0 | 16.17 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
