# Hulk DIGEST — 2026-09-01T23:27:51Z

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
| XRPUSDT | IDLE | 1.1 | 1.99 | 1.43 | -0.03 | 35229155.58 | 2.23 | n/a |
| ETHUSDT | IDLE | 0.9 | 1.74 | 0.42 | -0.02 | 341804360.41 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.74 | 1.44 | 0.29 | -0.02 | 527992408.52 | 0.0 | no_map |
| CHIPUSDT | IDLE | 2.26 | 11.2 | 3.96 | 0.14 | 737570.54 | 2.26 | no_map |
| PYTHUSDT | IDLE | 2.91 | 5.74 | 0.5 | 0.05 | 695784.72 | 3.86 | tvl≈113,597,849 |
| WUSDT | IDLE | 2.28 | 4.18 | 3.56 | 0.04 | 409781.85 | 1.04 | tvl≈1,509,553,891 |
| ZBCNUSDT | IDLE | 2.3 | 4.07 | 3.58 | -0.01 | 205184.42 | 12.08 | n/a |
| REDUSDT | IDLE | 1.92 | 5.85 | 3.83 | 0.1 | 117521.02 | 16.68 | tvl≈2,090,812 |
| CCUSDT | IDLE | 0.86 | 1.94 | 1.2 | -0.07 | 326277.7 | 9.68 | no_map |
| KITEUSDT | IDLE | 1.45 | 2.78 | 0.82 | 0.04 | 68077.24 | 8.95 | no_map |
| RIZEUSDT | IDLE | 1.97 | 4.22 | 1.82 | -0.06 | 40869.05 | 64.54 | no_map |
| EDELUSDT | IDLE | 0.7 | 5.41 | 4.24 | -0.09 | 144672.27 | 27.79 | no_map |
| BIOUSDT | IDLE | 1.07 | 1.9 | 1.55 | -0.05 | 69513.24 | 3.94 | n/a |
| FLUIDUSDT | IDLE | 2.56 | 4.47 | 4.28 | -0.03 | 229.45 | 14.16 | tvl≈2,574,882,028 |
| RWAINCUSDT | IDLE | 1.41 | 2.61 | 1.45 | -0.02 | 5822.68 | 29.4 | no_map |
| TELUSDT | IDLE | 2.16 | 3.91 | 2.71 | -0.05 | 94530.39 | 48.43 | no_map |
| HBARUSDT | IDLE | 0.87 | 1.58 | 1.1 | 0.0 | 249464.46 | 1.35 | empty_tvl |
| QNTUSDT | IDLE | 1.51 | 2.91 | 0.79 | 0.05 | 45987.69 | 4.69 | n/a |
| RWAUSDT | IDLE | 0.4 | 0.93 | 0.54 | -0.03 | 58735.69 | 7.71 | no_map |
| MNSRYUSDT | IDLE | 0.82 | 1.46 | 1.14 | -0.02 | 34447.71 | 52.24 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
