# Hulk DIGEST — 2026-08-22T00:54:16Z

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
| PYTHUSDT | IDLE | 2.0 | 7.38 | 0.62 | 0.12 | 6511579.99 | 2.01 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 2.11 | 8.72 | 2.4 | 0.14 | 147652995.34 | 3.46 | n/a |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.87 | 0.07 | 941652.19 | 1.26 | empty_tvl |
| ZBCNUSDT | IDLE | 2.92 | 11.25 | 3.55 | 0.1 | 543407.5 | 17.56 | n/a |
| CCUSDT | IDLE | 1.95 | 7.42 | 1.36 | 0.14 | 645506.61 | 7.14 | no_map |
| WUSDT | IDLE | 2.72 | 6.91 | 0.8 | 0.09 | 391002.83 | 11.21 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.52 | 0.02 | 547414.2 | 3.05 | no_map |
| BIOUSDT | IDLE | 2.52 | 5.62 | 0.73 | 0.03 | 186603.42 | 6.16 | n/a |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.02 | 79745.11 | 33.24 | no_map |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.67 | 0.13 | 60142.86 | 45.1 | no_map |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.72 | 0.06 | 183962.28 | 20.61 | no_map |
| REDUSDT | IDLE | 0.98 | 8.58 | 2.78 | 0.2 | 159673.18 | 16.44 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.24 | 0.07 | 170523.17 | 9.07 | n/a |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.02 | 9620.44 | 32.35 | no_map |
| KITEUSDT | IDLE | 1.36 | 4.03 | 0.0 | 0.11 | 60841.03 | 30.77 | no_map |
| QAITUSDT | IDLE | 2.2 | 4.22 | 1.21 | -0.01 | 3832.89 | 134.55 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 54947.56 | 16.43 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 37.01 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
