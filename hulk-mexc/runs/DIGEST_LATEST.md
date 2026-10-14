# Hulk DIGEST — 2026-10-14T23:29:27Z

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
| PYTHUSDT | IDLE | 2.71 | 7.97 | 2.24 | 0.09 | 2081362.01 | 3.52 | tvl≈190,557,763 |
| WUSDT | IDLE | 1.29 | 4.66 | 2.57 | -0.1 | 2396258.89 | 3.26 | tvl≈1,621,216,093 |
| ETHUSDT | IDLE | 0.73 | 1.35 | 0.7 | -0.03 | 238142481.08 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.66 | 1.28 | 0.29 | -0.02 | 46939951.08 | 1.5 | n/a |
| BTCUSDT | IDLE | 0.36 | 0.64 | 0.5 | -0.02 | 446263315.53 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.95 | 3.6 | 2.04 | -0.04 | 1065093.82 | 4.9 | n/a |
| CCUSDT | IDLE | 1.05 | 2.15 | 1.9 | -0.08 | 400946.09 | 10.4 | no_map |
| RWAINCUSDT | IDLE | 2.46 | 5.89 | 2.33 | -0.03 | 25699.89 | 30.46 | no_map |
| EDELUSDT | IDLE | 1.72 | 3.21 | 1.51 | -0.03 | 174088.38 | 9.02 | no_map |
| ZBCNUSDT | IDLE | 1.43 | 2.62 | 1.89 | -0.04 | 201796.63 | 14.28 | n/a |
| CHIPUSDT | IDLE | 1.4 | 4.82 | 4.02 | -0.1 | 101532.57 | 13.65 | no_map |
| HBARUSDT | IDLE | 0.97 | 1.87 | 0.44 | -0.03 | 523200.59 | 4.73 | empty_tvl |
| TELUSDT | IDLE | 2.58 | 4.58 | 3.89 | -0.03 | 98351.76 | 17.09 | no_map |
| REDUSDT | IDLE | 1.3 | 2.6 | 0.01 | 0.02 | 62936.93 | 15.13 | tvl≈3,918,721 |
| KITEUSDT | IDLE | 0.73 | 2.09 | 1.5 | -0.02 | 86772.37 | 11.84 | no_map |
| BIOUSDT | IDLE | 0.81 | 1.56 | 0.41 | -0.04 | 67054.29 | 3.77 | n/a |
| RIZEUSDT | IDLE | 0.68 | 3.64 | 2.93 | -0.01 | 50864.02 | 51.56 | no_map |
| FLUIDUSDT | IDLE | 1.28 | 4.0 | 1.36 | 0.05 | 19165.45 | 21.58 | tvl≈2,270,790,818 |
| RWAUSDT | IDLE | 0.49 | 0.88 | 0.71 | -0.03 | 56498.32 | 8.0 | no_map |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.46 | -0.01 | 35182.67 | 23.94 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
