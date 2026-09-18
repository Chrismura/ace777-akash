# Hulk DIGEST — 2026-09-18T07:27:51Z

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
| XRPUSDT | IDLE | 1.18 | 2.34 | 0.09 | 0.02 | 38439830.84 | 1.5 | n/a |
| ETHUSDT | IDLE | 0.93 | 1.85 | 0.09 | 0.02 | 325262582.11 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.77 | 1.53 | 0.01 | 0.02 | 490778308.11 | 0.0 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 46.36 | 22.88 | 0.07 | 53406.65 | 103.66 | no_map |
| PYTHUSDT | IDLE | 1.86 | 5.99 | 1.66 | 0.1 | 600734.75 | 1.67 | tvl≈135,621,931 |
| CCUSDT | IDLE | 1.83 | 5.88 | 0.16 | 0.12 | 628930.09 | 11.66 | no_map |
| CHIPUSDT | IDLE | 1.83 | 8.93 | 1.87 | 0.17 | 212867.0 | 20.68 | no_map |
| HBARUSDT | IDLE | 1.78 | 3.34 | 1.52 | 0.03 | 567774.78 | 1.31 | empty_tvl |
| WUSDT | IDLE | 1.34 | 3.86 | 1.04 | 0.11 | 354283.29 | 16.64 | tvl≈1,537,229,298 |
| BIOUSDT | IDLE | 2.43 | 4.79 | 0.41 | 0.05 | 76507.33 | 7.52 | n/a |
| ZBCNUSDT | IDLE | 1.65 | 3.14 | 1.07 | 0.03 | 247374.38 | 27.5 | n/a |
| KITEUSDT | IDLE | 2.12 | 4.19 | 0.38 | 0.02 | 74167.19 | 11.76 | no_map |
| EDELUSDT | IDLE | 0.76 | 7.93 | 1.06 | -0.07 | 262088.97 | 30.0 | no_map |
| REDUSDT | IDLE | 1.36 | 2.63 | 0.56 | 0.05 | 68225.34 | 17.44 | tvl≈2,487,844 |
| RWAINCUSDT | IDLE | 0.88 | 1.76 | 0.0 | -0.03 | 16063.97 | 5.95 | no_map |
| RWAUSDT | IDLE | 1.69 | 3.15 | 1.6 | 0.01 | 59793.44 | 29.59 | no_map |
| TELUSDT | IDLE | 1.26 | 2.4 | 0.76 | 0.0 | 73966.66 | 27.8 | no_map |
| QNTUSDT | IDLE | 1.15 | 2.22 | 0.52 | 0.04 | 43843.15 | 14.33 | n/a |
| MNSRYUSDT | IDLE | 1.11 | 2.21 | 0.12 | 0.03 | 43214.46 | 13.65 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 148.34 | 21.8 | tvl≈2,619,963,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
