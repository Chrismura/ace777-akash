# Hulk DIGEST — 2026-09-12T20:38:21Z

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
| ETHUSDT | IDLE | 0.59 | 1.06 | 0.78 | -0.0 | 236367913.03 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.53 | 0.96 | 0.66 | 0.0 | 17189589.47 | 2.2 | n/a |
| BTCUSDT | IDLE | 0.3 | 0.54 | 0.4 | -0.0 | 365043981.58 | 0.0 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.72 | 49.46 | 11.96 | 0.25 | 101547.87 | 61.07 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.03 | 7.43 | 5.68 | 0.02 | 74855.17 | 14.51 | no_map |
| ZBCNUSDT | IDLE | 2.16 | 5.12 | 4.03 | -0.03 | 221325.25 | 28.73 | n/a |
| EDELUSDT | IDLE | 2.31 | 5.14 | 1.33 | 0.03 | 166086.97 | 16.78 | no_map |
| PYTHUSDT | IDLE | 1.11 | 3.02 | 0.89 | 0.08 | 397819.68 | 1.81 | tvl≈124,268,543 |
| WUSDT | IDLE | 2.04 | 3.92 | 1.01 | 0.04 | 169005.47 | 9.89 | tvl≈1,473,992,646 |
| CCUSDT | IDLE | 1.06 | 1.89 | 1.54 | -0.02 | 215813.96 | 9.29 | no_map |
| RWAINCUSDT | IDLE | 2.17 | 4.01 | 3.86 | -0.03 | 10417.47 | 77.73 | no_map |
| REDUSDT | IDLE | 1.44 | 2.71 | 1.12 | 0.02 | 58848.77 | 19.2 | tvl≈2,346,858 |
| BIOUSDT | IDLE | 0.84 | 1.53 | 1.05 | 0.02 | 70173.56 | 3.92 | n/a |
| KITEUSDT | IDLE | 0.63 | 1.18 | 0.54 | -0.02 | 61537.43 | 10.33 | no_map |
| HBARUSDT | IDLE | 0.72 | 1.36 | 0.59 | 0.0 | 165920.09 | 1.34 | empty_tvl |
| TELUSDT | IDLE | 1.28 | 2.3 | 1.78 | -0.06 | 97008.01 | 36.23 | no_map |
| RWAUSDT | IDLE | 0.47 | 0.82 | 0.74 | 0.0 | 53641.31 | 7.44 | no_map |
| QNTUSDT | IDLE | 0.43 | 0.77 | 0.62 | 0.0 | 40153.58 | 6.24 | n/a |
| MNSRYUSDT | IDLE | 0.21 | 0.39 | 0.15 | -0.0 | 25203.53 | 8.34 | no_map |
| FLUIDUSDT | IDLE | 0.27 | 0.54 | 0.0 | 0.03 | 1375.44 | 20.47 | tvl≈2,676,463,086 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
