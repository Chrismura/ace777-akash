# Hulk DIGEST — 2026-08-22T16:54:29Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.09 | 10.19 | 1.0 | 0.08 | 49350723.54 | 11.48 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.25 | 0.06 | 214834975.76 | 3.38 | n/a |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.89 | -0.01 | 1130890.87 | 3.87 | empty_tvl |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.43 | 0.08 | 760984.83 | 5.98 | no_map |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.73 | -0.1 | 629303.65 | 3.35 | no_map |
| WUSDT | IDLE | 0.61 | 2.58 | 0.61 | -0.01 | 544868.24 | 13.72 | tvl≈1,556,368,553 |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.34 | -0.03 | 313447.67 | 7.17 | n/a |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.64 | -0.08 | 226071.36 | 6.68 | n/a |
| KITEUSDT | IDLE | 1.87 | 4.35 | 1.2 | 0.03 | 86745.47 | 12.44 | no_map |
| EDELUSDT | IDLE | 1.72 | 3.0 | 2.91 | -0.03 | 74824.14 | 34.5 | no_map |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.83 | -0.14 | 128125.71 | 11.83 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.44 | 3.47 | 0.42 | 0.05 | 46592.18 | 45.5 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.91 | -0.01 | 181233.05 | 3.14 | n/a |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.89 | 0.0 | 136476.51 | 58.93 | no_map |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7704.25 | 113.06 | no_map |
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
