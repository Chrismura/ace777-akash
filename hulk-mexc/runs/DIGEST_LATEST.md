# Hulk DIGEST — 2026-08-21T04:13:38Z

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
| PYTHUSDT | IDLE | 2.13 | 4.63 | 1.32 | 0.06 | 1925231.15 | 2.2 | tvl≈101,647,402 |
| XRPUSDT | IDLE | 0.97 | 5.29 | 0.79 | 0.2 | 113082620.39 | 1.53 | n/a |
| CHIPUSDT | IDLE | 2.14 | 12.78 | 4.61 | 0.14 | 431214.46 | 15.05 | no_map |
| CCUSDT | IDLE | 1.75 | 3.47 | 0.26 | 0.01 | 472676.52 | 7.9 | no_map |
| EDELUSDT | IDLE | 2.74 | 5.22 | 1.69 | 0.02 | 77389.65 | 10.75 | no_map |
| ZBCNUSDT | IDLE | 1.79 | 5.53 | 1.32 | 0.06 | 299878.53 | 64.92 | n/a |
| HBARUSDT | IDLE | 1.7 | 3.31 | 0.58 | 0.06 | 493133.94 | 1.33 | empty_tvl |
| BIOUSDT | IDLE | 1.04 | 4.71 | 1.6 | 0.08 | 225185.28 | 3.2 | n/a |
| REDUSDT | IDLE | 1.16 | 4.77 | 3.11 | 0.04 | 181623.65 | 11.48 | tvl≈1,905,423 |
| WUSDT | IDLE | 1.02 | 1.88 | 1.07 | 0.06 | 266614.36 | 12.17 | tvl≈1,529,129,765 |
| RWAINCUSDT | IDLE | 1.97 | 3.77 | 1.14 | 0.04 | 8350.49 | 87.43 | no_map |
| KITEUSDT | IDLE | 1.02 | 1.97 | 0.41 | 0.04 | 62147.95 | 15.02 | no_map |
| QAITUSDT | IDLE | 1.0 | 2.55 | 0.47 | -0.02 | 6718.75 | 67.45 | no_map |
| TELUSDT | IDLE | 0.68 | 3.43 | 2.14 | 0.13 | 200072.63 | 38.28 | no_map |
| RIZEUSDT | IDLE | 1.1 | 5.34 | 1.64 | -0.14 | 39790.94 | 208.98 | no_map |
| QNTUSDT | IDLE | 0.78 | 1.48 | 1.12 | 0.04 | 64822.41 | 8.09 | n/a |
| FLUIDUSDT | IDLE | 1.03 | 2.26 | 0.8 | 0.09 | 2600.53 | 21.53 | tvl≈2,534,518,410 |
| RWAUSDT | IDLE | 0.42 | 0.77 | 0.42 | 0.02 | 54463.32 | 8.5 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
