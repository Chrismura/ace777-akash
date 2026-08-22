# Hulk DIGEST — 2026-08-22T15:38:07Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| PYTHUSDT | IDLE | 1.57 | 7.62 | 0.88 | 0.05 | 51501309.44 | 1.96 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.04 | 0.03 | 215250210.75 | 4.87 | n/a |
| CCUSDT | IDLE | 1.34 | 5.65 | 3.45 | 0.07 | 795618.41 | 7.76 | no_map |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.35 | -0.01 | 1157862.78 | 5.24 | empty_tvl |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 1.86 | -0.09 | 605255.08 | 3.38 | no_map |
| WUSDT | IDLE | 0.78 | 3.17 | 1.59 | -0.02 | 554634.99 | 13.87 | tvl≈1,556,368,553 |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.71 | 0.03 | 85239.78 | 11.59 | no_map |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.88 | -0.05 | 320617.64 | 31.82 | n/a |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.85 | -0.07 | 221132.52 | 3.31 | n/a |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.04 | 79024.85 | 22.78 | no_map |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.88 | -0.1 | 144793.29 | 13.81 | tvl≈2,005,037 |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.22 | 0.03 | 56466.97 | 23.62 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.24 | -0.02 | 185203.48 | 7.89 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 75.23 | no_map |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.0 | 140695.89 | 48.04 | no_map |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
