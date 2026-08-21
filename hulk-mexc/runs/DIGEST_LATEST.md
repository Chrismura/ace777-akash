# Hulk DIGEST — 2026-08-21T21:15:01Z

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
| PYTHUSDT | IDLE | 1.2 | 4.51 | 1.38 | 0.09 | 5604356.51 | 2.08 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.14 | 3.73 | 1.84 | 0.1 | 128177460.27 | 2.16 | n/a |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.32 | 0.06 | 515403.68 | 6.24 | no_map |
| ZBCNUSDT | IDLE | 2.0 | 8.19 | 5.05 | 0.09 | 482470.86 | 27.01 | n/a |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.39 | 0.1 | 642636.74 | 9.22 | no_map |
| HBARUSDT | IDLE | 1.59 | 3.04 | 0.93 | 0.06 | 809445.81 | 1.29 | empty_tvl |
| WUSDT | IDLE | 1.96 | 3.83 | 0.66 | 0.06 | 367009.41 | 9.42 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.48 | 5.2 | 2.83 | 0.0 | 187661.04 | 3.16 | n/a |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.09 | 0.16 | 153499.45 | 10.63 | tvl≈2,358,074 |
| EDELUSDT | IDLE | 2.06 | 4.12 | 2.86 | -0.06 | 82446.51 | 22.68 | no_map |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.02 | 10271.93 | 21.49 | no_map |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.41 | 0.02 | 56215.94 | 45.77 | no_map |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.06 | 0.11 | 61047.42 | 12.98 | no_map |
| QAITUSDT | IDLE | 1.75 | 3.21 | 1.91 | -0.02 | 2825.52 | 130.0 | no_map |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 179800.17 | 48.27 | no_map |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.03 | 61178.4 | 1.56 | n/a |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.82 | 0.03 | 53709.48 | 16.64 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 22.18 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
