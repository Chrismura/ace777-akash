# Hulk DIGEST — 2026-08-22T11:44:37Z

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
| PYTHUSDT | IDLE | 2.15 | 9.66 | 6.69 | 0.01 | 51617535.9 | 4.09 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.48 | 0.08 | 216672021.9 | 2.69 | n/a |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.5 | 0.13 | 787565.19 | 7.7 | no_map |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.33 | 0.02 | 1256106.95 | 6.45 | empty_tvl |
| WUSDT | IDLE | 1.55 | 6.27 | 3.49 | 0.02 | 583210.59 | 12.67 | tvl≈1,560,017,487 |
| ZBCNUSDT | IDLE | 2.28 | 5.93 | 4.06 | -0.03 | 388625.15 | 13.87 | n/a |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.58 | -0.11 | 624656.57 | 3.35 | no_map |
| KITEUSDT | IDLE | 2.37 | 5.73 | 0.0 | 0.05 | 80671.96 | 10.59 | no_map |
| EDELUSDT | IDLE | 2.73 | 4.93 | 3.6 | -0.03 | 79064.33 | 79.41 | no_map |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.04 | -0.04 | 243493.11 | 3.21 | n/a |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.66 | -0.03 | 167324.38 | 42.85 | no_map |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2456.68 | 67.45 | no_map |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.56 | 0.04 | 154512.98 | 12.48 | tvl≈2,031,082 |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10768.24 | 76.09 | no_map |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.76 | 0.0 | 188380.65 | 4.68 | n/a |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.95 | -0.03 | 48697.31 | 46.44 | no_map |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.56 | tvl≈2,551,694,186 |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57621.53 | 16.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
