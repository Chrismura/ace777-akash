# Hulk DIGEST — 2026-08-22T16:26:01Z

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
| PYTHUSDT | IDLE | 1.47 | 7.24 | 0.08 | 0.07 | 51439921.95 | 1.95 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.34 | 7.64 | 3.97 | 0.05 | 215589281.06 | 2.72 | n/a |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.12 | -0.0 | 1138509.99 | 2.58 | empty_tvl |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.59 | 0.09 | 761752.13 | 5.99 | no_map |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.66 | -0.1 | 627774.7 | 3.35 | no_map |
| WUSDT | IDLE | 0.61 | 2.58 | 0.72 | -0.01 | 544402.74 | 8.46 | tvl≈1,556,368,553 |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.54 | -0.04 | 316089.59 | 17.95 | n/a |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.29 | -0.06 | 219670.87 | 3.29 | n/a |
| KITEUSDT | IDLE | 1.88 | 4.35 | 1.38 | 0.03 | 85433.55 | 8.89 | no_map |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.13 | -0.03 | 74831.15 | 22.86 | no_map |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.97 | -0.13 | 133000.59 | 21.9 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.13 | 0.03 | 56578.41 | 45.5 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8652.8 | 53.68 | no_map |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.16 | 0.01 | 137673.43 | 21.23 | no_map |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
