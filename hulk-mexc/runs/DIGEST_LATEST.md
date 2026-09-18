# Hulk DIGEST — 2026-09-18T20:00:01Z

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
| ETHUSDT | IDLE | 1.68 | 3.56 | 0.26 | 0.08 | 586749310.57 | 1.14 | no_map |
| XRPUSDT | IDLE | 1.49 | 3.51 | 0.0 | 0.09 | 60169194.38 | 0.71 | n/a |
| BTCUSDT | IDLE | 0.85 | 1.67 | 0.21 | 0.06 | 718886487.17 | 0.0 | no_map |
| WUSDT | IDLE | 2.8 | 11.09 | 2.42 | 0.11 | 867878.32 | 8.09 | tvl≈1,582,338,243 |
| PYTHUSDT | IDLE | 1.19 | 2.82 | 0.99 | 0.08 | 686404.98 | 3.32 | tvl≈133,812,138 |
| CCUSDT | IDLE | 0.91 | 2.99 | 0.97 | 0.11 | 668939.09 | 7.29 | no_map |
| RIZEUSDT | IDLE | 1.95 | 32.04 | 13.24 | -0.12 | 57767.41 | 118.56 | no_map |
| ZBCNUSDT | IDLE | 1.85 | 3.53 | 1.19 | 0.04 | 229000.89 | 28.38 | n/a |
| HBARUSDT | IDLE | 1.1 | 2.19 | 0.05 | 0.06 | 596890.48 | 1.26 | empty_tvl |
| EDELUSDT | IDLE | 0.94 | 8.04 | 7.16 | 0.21 | 201955.75 | 51.55 | no_map |
| CHIPUSDT | IDLE | 0.88 | 4.08 | 2.64 | 0.14 | 188177.8 | 18.51 | no_map |
| RWAINCUSDT | IDLE | 1.73 | 3.46 | 0.0 | 0.03 | 7895.1 | 5.77 | no_map |
| BIOUSDT | IDLE | 1.12 | 3.06 | 0.54 | 0.09 | 87061.32 | 7.29 | n/a |
| KITEUSDT | IDLE | 1.17 | 2.15 | 1.32 | 0.05 | 77122.16 | 12.69 | no_map |
| REDUSDT | IDLE | 1.1 | 3.51 | 1.14 | 0.12 | 63507.65 | 15.86 | tvl≈2,630,264 |
| FLUIDUSDT | IDLE | 2.52 | 9.71 | 2.74 | 0.12 | 2376.06 | 45.54 | tvl≈2,647,767,179 |
| QNTUSDT | IDLE | 1.14 | 2.09 | 1.32 | 0.04 | 71639.64 | 7.85 | n/a |
| TELUSDT | IDLE | 1.19 | 3.35 | 1.84 | 0.07 | 98723.15 | 45.29 | no_map |
| MNSRYUSDT | IDLE | 1.26 | 2.44 | 0.58 | 0.06 | 42887.12 | 43.38 | no_map |
| RWAUSDT | IDLE | 0.89 | 1.63 | 1.02 | 0.01 | 58630.09 | 29.54 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
