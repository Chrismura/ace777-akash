# Hulk DIGEST — 2026-08-22T16:12:58Z

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
| PYTHUSDT | IDLE | 1.53 | 7.24 | 2.18 | 0.04 | 51452010.93 | 3.98 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.38 | 7.64 | 5.87 | 0.03 | 215396703.16 | 1.39 | n/a |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.19 | -0.01 | 1141174.01 | 6.53 | empty_tvl |
| CCUSDT | IDLE | 1.0 | 4.14 | 2.97 | 0.09 | 766520.77 | 0.86 | no_map |
| CHIPUSDT | IDLE | 0.59 | 3.36 | 1.69 | -0.11 | 627250.7 | 6.76 | no_map |
| WUSDT | IDLE | 0.66 | 2.58 | 2.06 | -0.03 | 546556.4 | 5.36 | tvl≈1,556,368,553 |
| ZBCNUSDT | IDLE | 1.34 | 3.49 | 2.29 | -0.05 | 318056.16 | 20.64 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.2 | -0.07 | 219000.71 | 6.66 | n/a |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.47 | 0.03 | 85431.66 | 10.68 | no_map |
| EDELUSDT | IDLE | 1.44 | 2.52 | 2.46 | -0.03 | 74791.3 | 22.86 | no_map |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.47 | -0.13 | 135581.9 | 13.75 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.24 | 0.03 | 56546.98 | 25.25 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.39 | -0.02 | 183565.01 | 7.9 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 59.06 | no_map |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.84 | -0.0 | 137234.78 | 48.04 | no_map |
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
