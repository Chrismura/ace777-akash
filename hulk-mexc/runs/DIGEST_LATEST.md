# Hulk DIGEST — 2026-08-22T07:13:33Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.85 | 0.03 | 21515180.91 | 27.81 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 23.87 | 6.35 | 0.21 | 217574577.9 | 3.14 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.3 | 0.05 | 1364365.15 | 1.27 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.82 | -0.1 | 706166.17 | 6.67 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.79 | 0.06 | 620448.48 | 10.34 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.36 | -0.03 | 247551.2 | 13.23 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.87 | 0.07 | 160593.6 | 21.8 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.07 | 11.25 | 4.23 | 0.18 | 796492.85 | 9.18 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 8.47 | 5.75 | 0.04 | 543189.28 | 51.43 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.29 | 0.04 | 199657.37 | 6.15 | n/a |
| KITEUSDT | IDLE | 3.38 | 9.68 | 2.7 | 0.1 | 74275.08 | 11.66 | no_map |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.03 | 87352.17 | 33.46 | no_map |
| FLUIDUSDT | IDLE | 3.34 | 7.38 | 4.29 | 0.05 | 6989.9 | 21.23 | tvl≈2,556,657,142 |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.02 | 11393.75 | 80.36 | no_map |
| TELUSDT | IDLE | 2.07 | 5.36 | 3.75 | 0.06 | 196537.99 | 46.14 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3298.33 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.47 | 0.02 | 56826.91 | 46.34 | no_map |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.59 | 0.04 | 58075.91 | 16.19 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
