# Hulk DIGEST — 2026-08-22T16:43:29Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 10.19 | 0.15 | 0.09 | 50871807.89 | 1.9 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.39 | 0.06 | 214953391.08 | 2.03 | n/a |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.81 | -0.0 | 1128022.41 | 3.86 | empty_tvl |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.22 | 0.08 | 761004.81 | 4.26 | no_map |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.56 | -0.1 | 626978.35 | 3.34 | no_map |
| WUSDT | IDLE | 0.61 | 2.58 | 0.7 | -0.01 | 543851.55 | 8.45 | tvl≈1,556,368,553 |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.42 | -0.03 | 314774.32 | 18.4 | n/a |
| BIOUSDT | IDLE | 0.95 | 6.58 | 3.69 | -0.06 | 219567.36 | 3.27 | n/a |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.54 | 0.02 | 85682.18 | 12.49 | no_map |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.03 | 74851.15 | 34.15 | no_map |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.55 | -0.12 | 129202.15 | 12.69 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.32 | 3.25 | 0.0 | 0.06 | 46791.28 | 23.57 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.77 | -0.01 | 181601.64 | 6.28 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 7676.54 | 59.06 | no_map |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.89 | 0.0 | 136830.66 | 53.53 | no_map |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.55 | tvl≈2,551,700,555 |
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
