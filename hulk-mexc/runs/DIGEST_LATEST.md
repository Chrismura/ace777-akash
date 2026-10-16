# Hulk DIGEST — 2026-10-16T13:00:25Z

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
| PYTHUSDT | IDLE | 1.8 | 10.19 | 7.36 | 0.07 | 3830369.7 | 17.02 | tvl≈206,072,259 |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 6.5 | 5.79 | 0.01 | 1835094.44 | 16.57 | tvl≈1,652,485,183 |
| ETHUSDT | IDLE | 1.07 | 1.96 | 1.2 | 0.05 | 238581042.85 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.89 | 1.58 | 1.3 | 0.03 | 27877411.72 | 2.25 | n/a |
| BTCUSDT | IDLE | 0.74 | 1.33 | 1.04 | 0.02 | 406106335.73 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.52 | 3.89 | 2.78 | 0.06 | 1259365.87 | 0.97 | n/a |
| CCUSDT | IDLE | 3.04 | 5.45 | 4.16 | -0.03 | 421060.85 | 6.72 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 9.55 | 6.04 | -0.02 | 67936.97 | 34.0 | no_map |
| RWAINCUSDT | IDLE | 2.94 | 5.35 | 3.55 | -0.0 | 24929.23 | 4.97 | no_map |
| ZBCNUSDT | IDLE | 1.53 | 2.98 | 2.22 | 0.05 | 205186.19 | 14.26 | n/a |
| EDELUSDT | IDLE | 1.18 | 3.17 | 0.1 | 0.01 | 212802.01 | 22.92 | no_map |
| REDUSDT | IDLE | 1.46 | 4.67 | 1.0 | 0.01 | 91574.02 | 8.53 | tvl≈3,681,377 |
| CHIPUSDT | IDLE | 0.89 | 4.34 | 3.96 | 0.12 | 167451.88 | 10.3 | no_map |
| KITEUSDT | IDLE | 1.18 | 2.17 | 1.2 | 0.02 | 70105.17 | 13.0 | no_map |
| BIOUSDT | IDLE | 0.97 | 1.71 | 1.6 | 0.05 | 66154.12 | 3.88 | n/a |
| HBARUSDT | IDLE | 0.87 | 1.76 | 0.54 | 0.07 | 299694.17 | 5.77 | empty_tvl |
| FLUIDUSDT | IDLE | 1.35 | 2.36 | 2.3 | -0.01 | 7578.02 | 19.09 | tvl≈2,268,397,026 |
| TELUSDT | IDLE | 0.93 | 1.86 | 1.16 | 0.05 | 93164.68 | 11.19 | no_map |
| MNSRYUSDT | IDLE | 0.12 | 0.21 | 0.21 | 0.01 | 39452.4 | 7.07 | no_map |
| RWAUSDT | IDLE | 0.26 | 0.47 | 0.31 | 0.02 | 50785.96 | 31.55 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
