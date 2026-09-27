# Hulk DIGEST — 2026-09-27T17:36:21Z

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
| PYTHUSDT | IDLE | 1.88 | 6.98 | 3.48 | 0.11 | 2247690.76 | 5.86 | tvl≈187,214,025 |
| WUSDT | IDLE | 1.75 | 11.52 | 0.47 | 0.22 | 4178283.29 | 17.17 | tvl≈1,883,924,565 |
| QNTUSDT | IDLE | 1.41 | 22.14 | 2.3 | 0.52 | 6204507.71 | 1.6 | n/a |
| XRPUSDT | IDLE | 1.33 | 2.43 | 1.51 | -0.01 | 44314075.06 | 1.97 | n/a |
| ETHUSDT | IDLE | 0.72 | 1.28 | 1.01 | 0.0 | 192557558.15 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.53 | 0.95 | 0.75 | 0.01 | 451121028.02 | 0.0 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 42.2 | 24.29 | 0.06 | 24488.76 | 69.82 | no_map |
| CCUSDT | IDLE | 2.69 | 5.02 | 2.45 | -0.01 | 551658.77 | 5.16 | no_map |
| CHIPUSDT | IDLE | 3.29 | 5.98 | 4.46 | -0.06 | 99851.44 | 10.61 | no_map |
| HBARUSDT | IDLE | 1.71 | 3.07 | 2.3 | -0.01 | 681420.41 | 1.07 | empty_tvl |
| EDELUSDT | IDLE | 2.34 | 8.31 | 6.81 | -0.11 | 135205.38 | 25.85 | no_map |
| KITEUSDT | IDLE | 1.68 | 4.7 | 0.36 | 0.07 | 172819.06 | 7.82 | no_map |
| BIOUSDT | IDLE | 1.63 | 3.05 | 1.37 | -0.03 | 89741.9 | 6.33 | n/a |
| ZBCNUSDT | IDLE | 1.13 | 2.0 | 1.76 | -0.02 | 208840.71 | 29.59 | n/a |
| REDUSDT | IDLE | 0.93 | 1.76 | 0.72 | 0.01 | 64700.96 | 13.54 | tvl≈3,066,590 |
| TELUSDT | IDLE | 1.53 | 6.49 | 2.17 | 0.15 | 151897.49 | 27.08 | no_map |
| RIZEUSDT | IDLE | 0.51 | 1.94 | 0.77 | -0.04 | 46295.42 | 49.25 | no_map |
| FLUIDUSDT | IDLE | 0.91 | 1.79 | 0.15 | 0.02 | 1556.07 | 21.52 | tvl≈2,586,161,003 |
| RWAUSDT | IDLE | 0.53 | 1.0 | 0.35 | 0.02 | 56409.34 | 7.06 | no_map |
| MNSRYUSDT | IDLE | 0.29 | 0.52 | 0.42 | 0.01 | 39753.87 | 37.96 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
