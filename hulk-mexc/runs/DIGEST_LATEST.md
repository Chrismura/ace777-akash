# Hulk DIGEST — 2026-10-17T18:01:18Z

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
| XRPUSDT | IDLE | 0.71 | 1.3 | 0.79 | -0.0 | 17407014.62 | 1.55 | n/a |
| ETHUSDT | IDLE | 0.67 | 1.23 | 0.68 | 0.0 | 88783154.29 | 0.04 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 7.26 | 5.06 | -0.03 | 1205175.08 | 13.78 | tvl≈1,577,047,737 |
| PYTHUSDT | IDLE | 2.89 | 7.06 | 4.35 | -0.03 | 1080268.0 | 2.45 | tvl≈179,398,395 |
| BTCUSDT | IDLE | 0.28 | 0.51 | 0.27 | 0.0 | 183882136.23 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.19 | 3.97 | 2.75 | -0.01 | 537713.48 | 1.52 | n/a |
| CCUSDT | IDLE | 1.4 | 2.56 | 1.64 | 0.01 | 264212.31 | 10.6 | no_map |
| CHIPUSDT | IDLE | 2.04 | 3.65 | 2.9 | -0.04 | 86964.21 | 13.68 | no_map |
| EDELUSDT | IDLE | 1.45 | 2.55 | 2.31 | -0.06 | 154904.29 | 21.17 | no_map |
| ZBCNUSDT | IDLE | 1.27 | 2.34 | 1.31 | -0.02 | 197261.92 | 24.46 | n/a |
| BIOUSDT | IDLE | 1.45 | 2.62 | 1.83 | -0.03 | 68930.09 | 4.13 | n/a |
| KITEUSDT | IDLE | 1.43 | 2.71 | 1.68 | -0.02 | 64387.29 | 10.18 | no_map |
| FLUIDUSDT | IDLE | 2.68 | 4.89 | 3.2 | 0.03 | 3708.5 | 21.58 | tvl≈2,229,624,756 |
| REDUSDT | IDLE | 0.97 | 1.78 | 1.11 | -0.04 | 59674.65 | 7.88 | tvl≈3,487,263 |
| RWAINCUSDT | IDLE | 1.0 | 4.34 | 0.57 | 0.05 | 25123.35 | 10.45 | no_map |
| RIZEUSDT | IDLE | 0.94 | 1.8 | 0.71 | -0.04 | 49341.59 | 31.77 | no_map |
| HBARUSDT | IDLE | 1.08 | 1.97 | 1.23 | 0.01 | 136680.27 | 3.63 | empty_tvl |
| TELUSDT | IDLE | 1.2 | 2.11 | 1.89 | -0.06 | 86160.59 | 18.06 | no_map |
| RWAUSDT | IDLE | 0.57 | 1.04 | 0.71 | 0.0 | 50564.6 | 15.89 | no_map |
| MNSRYUSDT | IDLE | 0.53 | 1.05 | 0.13 | 0.01 | 29196.44 | 26.78 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
