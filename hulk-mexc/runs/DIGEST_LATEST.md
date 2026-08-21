# Hulk DIGEST — 2026-08-21T21:18:26Z

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
| PYTHUSDT | IDLE | 1.19 | 4.51 | 1.13 | 0.09 | 5612851.97 | 2.08 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.15 | 3.73 | 2.0 | 0.1 | 128597941.18 | 2.89 | n/a |
| ZBCNUSDT | IDLE | 1.98 | 8.19 | 4.49 | 0.09 | 483377.28 | 15.7 | n/a |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.38 | 0.06 | 515488.3 | 6.24 | no_map |
| CCUSDT | IDLE | 1.16 | 3.14 | 0.73 | 0.09 | 644386.5 | 6.47 | no_map |
| HBARUSDT | IDLE | 1.59 | 3.04 | 0.87 | 0.06 | 810877.53 | 1.29 | empty_tvl |
| WUSDT | IDLE | 1.98 | 3.83 | 0.83 | 0.06 | 367065.05 | 13.63 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.45 | 5.2 | 2.4 | 0.01 | 187216.27 | 3.15 | n/a |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.35 | 0.16 | 153580.52 | 13.95 | tvl≈2,358,074 |
| EDELUSDT | IDLE | 2.06 | 4.12 | 2.86 | -0.06 | 82550.24 | 11.33 | no_map |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 10.75 | no_map |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.46 | 0.01 | 56191.53 | 45.77 | no_map |
| QAITUSDT | IDLE | 2.5 | 4.38 | 4.2 | -0.04 | 3753.25 | 95.92 | no_map |
| KITEUSDT | IDLE | 1.3 | 4.0 | 1.95 | 0.11 | 60989.09 | 11.12 | no_map |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.43 | 0.01 | 179205.52 | 5.35 | no_map |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.03 | 61270.13 | 1.56 | n/a |
| RWAUSDT | IDLE | 0.64 | 1.17 | 0.74 | 0.03 | 53754.03 | 41.55 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 22.16 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
