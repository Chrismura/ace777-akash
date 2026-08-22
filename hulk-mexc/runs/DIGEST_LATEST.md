# Hulk DIGEST — 2026-08-22T06:35:22Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.07 | 0.04 | 20055911.58 | 9.96 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 8.96 | 0.18 | 211619021.21 | 3.88 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.47 | 0.04 | 1387497.63 | 6.36 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 24.54 | 13.21 | -0.11 | 701500.47 | 3.39 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.28 | 0.05 | 615580.23 | 15.58 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 29.98 | 13.71 | -0.05 | 245812.57 | 6.69 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 42.58 | 12.34 | 0.06 | 164365.72 | 57.53 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.22 | 0.17 | 780768.91 | 8.34 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 8.47 | 6.41 | 0.02 | 545996.52 | 27.09 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.25 | 0.03 | 200337.03 | 9.32 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 9.68 | 5.12 | 0.09 | 74778.21 | 10.11 | no_map |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.24 | -0.03 | 88137.67 | 33.5 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 22.1 | tvl≈2,556,657,142 |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.01 | 11437.27 | 64.66 | no_map |
| TELUSDT | IDLE | 2.14 | 5.52 | 4.05 | 0.06 | 196551.7 | 51.47 | no_map |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.55 | 0.09 | 59540.7 | 46.34 | no_map |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.04 | 58166.46 | 24.38 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
