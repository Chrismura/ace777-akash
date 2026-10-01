# Hulk DIGEST — 2026-10-01T07:53:20Z

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
| QNTUSDT | IDLE | 1.34 | 6.56 | 0.66 | 0.05 | 9320881.96 | 10.66 | n/a |
| XRPUSDT | IDLE | 1.12 | 2.02 | 1.42 | -0.01 | 49712975.35 | 2.02 | n/a |
| ETHUSDT | IDLE | 0.88 | 1.54 | 1.42 | 0.0 | 399183140.69 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.72 | 1.28 | 1.01 | 0.0 | 648524431.1 | 0.0 | no_map |
| CCUSDT | IDLE | 2.14 | 3.77 | 3.46 | -0.01 | 908039.66 | 6.48 | no_map |
| HBARUSDT | IDLE | 1.86 | 3.5 | 1.41 | -0.01 | 1238228.12 | 5.68 | empty_tvl |
| WUSDT | IDLE | 2.11 | 3.91 | 2.09 | -0.0 | 727099.92 | 9.65 | tvl≈1,827,826,885 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 12.64 | 10.35 | 0.03 | 427370.15 | 46.05 | n/a |
| PYTHUSDT | IDLE | 2.24 | 4.13 | 2.33 | -0.01 | 469277.64 | 6.46 | tvl≈175,477,380 |
| BIOUSDT | IDLE | 1.65 | 2.98 | 2.1 | -0.01 | 91114.08 | 9.76 | n/a |
| CHIPUSDT | IDLE | 1.63 | 3.41 | 2.85 | -0.03 | 66000.27 | 16.28 | no_map |
| KITEUSDT | IDLE | 1.47 | 2.66 | 1.82 | 0.03 | 87207.48 | 15.33 | no_map |
| RWAINCUSDT | IDLE | 2.34 | 5.09 | 1.57 | -0.02 | 10783.95 | 84.07 | no_map |
| REDUSDT | IDLE | 1.25 | 4.75 | 1.08 | 0.12 | 80224.81 | 12.53 | tvl≈4,539,723 |
| TELUSDT | IDLE | 1.63 | 3.56 | 3.14 | 0.02 | 216380.9 | 26.61 | no_map |
| EDELUSDT | IDLE | 0.49 | 4.2 | 1.65 | 0.22 | 151419.06 | 28.58 | no_map |
| RIZEUSDT | IDLE | 0.54 | 1.0 | 0.53 | 0.03 | 37096.76 | 73.37 | no_map |
| MNSRYUSDT | IDLE | 0.91 | 1.61 | 1.35 | -0.01 | 38890.89 | 3.91 | no_map |
| RWAUSDT | IDLE | 0.33 | 0.59 | 0.44 | -0.0 | 55278.93 | 21.94 | no_map |
| FLUIDUSDT | IDLE | 0.15 | 0.26 | 0.22 | -0.01 | 1181.47 | 21.74 | tvl≈2,576,862,244 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
