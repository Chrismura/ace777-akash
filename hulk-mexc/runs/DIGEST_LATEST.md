# Hulk DIGEST — 2026-08-22T07:09:19Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.42 | 0.05 | 21256767.37 | 3.91 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 23.87 | 6.31 | 0.22 | 217217256.75 | 2.51 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 8.7 | 0.06 | 1385558.97 | 5.05 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.35 | -0.1 | 705572.73 | 6.64 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 17.58 | 6.95 | 0.07 | 620631.05 | 13.33 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.07 | -0.03 | 247649.4 | 3.29 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.3 | 0.07 | 160586.44 | 31.13 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.05 | 11.25 | 3.48 | 0.19 | 793461.44 | 7.46 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 8.47 | 5.65 | 0.04 | 543669.2 | 71.95 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 13.91 | 8.01 | 0.05 | 199655.64 | 7.68 | n/a |
| KITEUSDT | IDLE | 3.4 | 9.68 | 2.92 | 0.11 | 74309.98 | 10.78 | no_map |
| EDELUSDT | IDLE | 2.26 | 4.52 | 3.14 | -0.02 | 87581.67 | 33.43 | no_map |
| FLUIDUSDT | IDLE | 3.34 | 7.38 | 4.29 | 0.05 | 6989.9 | 21.17 | tvl≈2,556,657,142 |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.03 | 11448.14 | 101.69 | no_map |
| TELUSDT | IDLE | 2.06 | 5.36 | 3.55 | 0.06 | 196632.96 | 46.14 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3298.33 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.5 | 0.02 | 56908.86 | 46.34 | no_map |
| RWAUSDT | IDLE | 1.77 | 3.29 | 1.67 | 0.04 | 58001.95 | 24.32 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
