# Hulk DIGEST — 2026-08-28T10:07:45Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.73 | 3.02 | 2.91 | -0.05 | 1550403.5 | 2.08 | tvl≈110,055,134 |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 55.46 | 32.47 | -0.18 | 46157.36 | 60.42 | no_map |
| XRPUSDT | IDLE | 0.99 | 1.73 | 1.68 | -0.02 | 49616119.0 | 2.85 | n/a |
| CHIPUSDT | IDLE | 1.43 | 6.93 | 2.49 | 0.09 | 712854.16 | 9.9 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.45 | 6.06 | 5.64 | -0.06 | 81720.56 | 12.32 | tvl≈2,023,837 |
| CCUSDT | IDLE | 1.41 | 2.55 | 1.85 | -0.05 | 455299.81 | 6.27 | no_map |
| KITEUSDT | IDLE | 2.34 | 4.1 | 3.82 | -0.02 | 73981.39 | 8.73 | no_map |
| WUSDT | IDLE | 1.02 | 1.82 | 1.52 | -0.03 | 195389.59 | 11.76 | tvl≈1,561,281,201 |
| ZBCNUSDT | IDLE | 0.61 | 1.53 | 1.17 | 0.0 | 232813.02 | 0.97 | n/a |
| BIOUSDT | IDLE | 1.13 | 1.99 | 1.77 | -0.01 | 86768.56 | 3.55 | n/a |
| HBARUSDT | IDLE | 0.9 | 1.57 | 1.52 | -0.02 | 326184.66 | 1.3 | empty_tvl |
| RIZEUSDT | IDLE | 0.51 | 5.67 | 4.24 | -0.18 | 113366.45 | 56.88 | no_map |
| EDELUSDT | IDLE | 0.45 | 2.61 | 1.02 | 0.04 | 51518.43 | 34.25 | no_map |
| TELUSDT | IDLE | 1.19 | 2.2 | 1.78 | -0.01 | 135889.2 | 10.96 | no_map |
| RWAINCUSDT | IDLE | 1.39 | 4.28 | 4.1 | -0.04 | 19838.09 | 165.56 | no_map |
| FLUIDUSDT | IDLE | 1.42 | 2.68 | 1.06 | -0.01 | 3121.47 | 0.74 | tvl≈2,615,379,081 |
| QNTUSDT | IDLE | 0.69 | 1.26 | 0.75 | -0.02 | 42531.21 | 3.22 | n/a |
| RWAUSDT | IDLE | 0.37 | 0.66 | 0.5 | 0.01 | 54375.71 | 16.6 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
