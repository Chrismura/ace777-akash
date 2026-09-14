# Hulk DIGEST — 2026-09-14T00:41:14Z

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
| ETHUSDT | IDLE | 1.13 | 2.06 | 1.38 | -0.02 | 286033726.51 | 0.4 | no_map |
| XRPUSDT | IDLE | 1.15 | 2.12 | 1.26 | -0.02 | 18914418.59 | 2.23 | n/a |
| BTCUSDT | IDLE | 0.76 | 1.39 | 0.86 | -0.01 | 297233602.84 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.31 | 4.44 | 2.87 | 0.02 | 458816.94 | 1.78 | tvl≈129,171,771 |
| WUSDT | IDLE | 2.87 | 5.11 | 4.23 | -0.02 | 218475.58 | 8.17 | tvl≈1,449,743,040 |
| RWAINCUSDT | IDLE | 3.86 | 7.11 | 4.01 | -0.01 | 9357.03 | 27.42 | no_map |
| EDELUSDT | IDLE | 1.9 | 6.54 | 1.53 | 0.11 | 202317.52 | 7.42 | no_map |
| CHIPUSDT | IDLE | 1.87 | 7.47 | 5.79 | -0.14 | 95483.09 | 19.28 | no_map |
| CCUSDT | IDLE | 1.17 | 2.17 | 1.13 | -0.03 | 314832.05 | 6.3 | no_map |
| ZBCNUSDT | IDLE | 1.8 | 3.32 | 1.92 | 0.0 | 201232.83 | 25.38 | n/a |
| BIOUSDT | IDLE | 2.07 | 3.8 | 2.26 | -0.01 | 70322.07 | 3.98 | n/a |
| HBARUSDT | IDLE | 2.02 | 3.62 | 2.8 | 0.01 | 253604.42 | 1.33 | empty_tvl |
| KITEUSDT | IDLE | 1.48 | 2.76 | 1.31 | -0.01 | 60450.48 | 12.2 | no_map |
| REDUSDT | IDLE | 1.47 | 2.74 | 1.28 | -0.01 | 64059.64 | 16.91 | tvl≈2,364,635 |
| QNTUSDT | IDLE | 2.57 | 4.52 | 4.1 | -0.03 | 37999.45 | 3.2 | n/a |
| RIZEUSDT | IDLE | 0.49 | 6.89 | 6.09 | -0.08 | 65680.41 | 76.4 | no_map |
| TELUSDT | IDLE | 1.51 | 2.7 | 2.13 | -0.05 | 84202.89 | 31.96 | no_map |
| FLUIDUSDT | IDLE | 1.15 | 2.0 | 1.96 | -0.01 | 1325.28 | 21.23 | tvl≈2,652,574,761 |
| RWAUSDT | IDLE | 0.37 | 0.67 | 0.52 | 0.0 | 54676.64 | 7.44 | no_map |
| MNSRYUSDT | IDLE | 0.27 | 0.47 | 0.42 | -0.0 | 30268.95 | 15.31 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
