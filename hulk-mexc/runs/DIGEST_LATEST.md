# Hulk DIGEST — 2026-09-12T00:17:48Z

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
| RIZEUSDT | IDLE | 1.51 | 102.76 | 43.91 | 0.67 | 215828.72 | 148.38 | no_map |
| ETHUSDT | IDLE | 0.8 | 1.71 | 1.24 | 0.03 | 656733207.79 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.8 | 1.63 | 0.87 | 0.01 | 54276697.56 | 2.21 | n/a |
| BTCUSDT | IDLE | 0.36 | 0.68 | 0.26 | 0.01 | 593565375.02 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.26 | 2.47 | 1.05 | -0.01 | 413499.05 | 1.97 | tvl≈114,765,176 |
| CCUSDT | IDLE | 1.25 | 2.28 | 1.45 | -0.01 | 420606.82 | 7.19 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 5.32 | 5.06 | 0.01 | 14801.21 | 5.55 | no_map |
| EDELUSDT | IDLE | 2.09 | 5.98 | 1.71 | 0.07 | 166605.45 | 26.05 | no_map |
| ZBCNUSDT | IDLE | 1.77 | 3.25 | 1.88 | 0.01 | 194879.12 | 11.1 | n/a |
| WUSDT | IDLE | 1.24 | 2.45 | 1.15 | 0.01 | 200210.43 | 14.55 | tvl≈1,495,834,373 |
| CHIPUSDT | IDLE | 1.29 | 3.82 | 1.15 | 0.01 | 121835.77 | 8.47 | no_map |
| BIOUSDT | IDLE | 1.17 | 2.3 | 0.28 | 0.02 | 82250.01 | 3.96 | n/a |
| REDUSDT | IDLE | 1.17 | 2.27 | 0.79 | 0.05 | 64282.68 | 18.08 | tvl≈2,295,785 |
| TELUSDT | IDLE | 1.91 | 3.74 | 3.04 | -0.03 | 103590.19 | 17.44 | no_map |
| KITEUSDT | IDLE | 0.73 | 1.35 | 0.73 | 0.0 | 59132.92 | 13.86 | no_map |
| HBARUSDT | IDLE | 0.63 | 1.18 | 0.59 | -0.01 | 248645.64 | 2.69 | empty_tvl |
| QNTUSDT | IDLE | 1.2 | 2.26 | 0.93 | -0.01 | 46292.68 | 7.85 | n/a |
| RWAUSDT | IDLE | 0.36 | 0.67 | 0.3 | 0.03 | 52922.66 | 7.45 | no_map |
| FLUIDUSDT | IDLE | 0.36 | 0.73 | 0.0 | 0.03 | 807.07 | 22.45 | tvl≈2,656,618,920 |
| MNSRYUSDT | IDLE | 0.35 | 0.65 | 0.39 | 0.01 | 35121.6 | 44.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
