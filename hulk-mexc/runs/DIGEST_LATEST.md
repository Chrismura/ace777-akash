# Hulk DIGEST — 2026-08-22T00:39:08Z

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
| PYTHUSDT | IDLE | 1.77 | 6.61 | 0.14 | 0.12 | 6432857.97 | 2.02 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.09 | 8.72 | 1.94 | 0.15 | 146392562.45 | 2.75 | n/a |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.88 | 0.07 | 939588.36 | 2.52 | empty_tvl |
| ZBCNUSDT | IDLE | 2.88 | 11.25 | 2.66 | 0.12 | 542622.17 | 2.42 | n/a |
| CCUSDT | IDLE | 1.94 | 7.42 | 0.85 | 0.14 | 640367.62 | 4.44 | no_map |
| WUSDT | IDLE | 2.72 | 6.91 | 0.78 | 0.09 | 388601.26 | 14.25 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.79 | 0.03 | 553233.62 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.26 | 5.14 | 0.0 | 0.03 | 186081.53 | 9.2 | n/a |
| EDELUSDT | IDLE | 2.57 | 5.5 | 1.19 | -0.02 | 79875.72 | 32.88 | no_map |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.28 | 0.12 | 59946.04 | 45.4 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | no_map |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.05 | 186259.31 | 36.04 | no_map |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.31 | 0.06 | 170517.85 | 3.03 | n/a |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.04 | 9787.93 | 43.15 | no_map |
| REDUSDT | IDLE | 0.73 | 6.54 | 1.09 | 0.24 | 158085.06 | 51.82 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.09 | 0.1 | 61128.18 | 11.93 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54684.56 | 16.43 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 39.25 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
