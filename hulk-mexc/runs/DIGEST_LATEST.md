# Hulk DIGEST — 2026-08-22T16:07:14Z

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
| PYTHUSDT | IDLE | 1.51 | 7.24 | 1.6 | 0.04 | 51463168.0 | 1.98 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.37 | 7.64 | 5.33 | 0.03 | 215648693.38 | 4.83 | n/a |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.22 | -0.02 | 1149618.5 | 5.23 | empty_tvl |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.06 | 0.1 | 762690.65 | 5.96 | no_map |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.03 | -0.09 | 627789.49 | 6.71 | no_map |
| WUSDT | IDLE | 0.65 | 2.58 | 1.89 | -0.02 | 549255.63 | 13.9 | tvl≈1,556,368,553 |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 2.04 | -0.05 | 319235.1 | 23.68 | n/a |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.57 | -0.07 | 218933.73 | 3.31 | n/a |
| KITEUSDT | IDLE | 1.91 | 4.35 | 1.87 | 0.03 | 85341.12 | 12.5 | no_map |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.31 | -0.14 | 136521.28 | 0.91 | tvl≈2,005,037 |
| EDELUSDT | IDLE | 1.36 | 2.41 | 2.01 | -0.03 | 75106.94 | 22.81 | no_map |
| RIZEUSDT | IDLE | 1.31 | 3.21 | 0.15 | 0.03 | 56512.97 | 45.5 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.28 | -0.02 | 183601.87 | 6.31 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 64.45 | no_map |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.58 | -0.0 | 138519.77 | 48.01 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.04 | 4625.53 | 22.44 | tvl≈2,554,315,465 |
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
