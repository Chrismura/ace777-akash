# Hulk DIGEST — 2026-08-22T15:49:42Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.36 | 0.04 | 51491813.93 | 3.95 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.38 | 7.64 | 5.73 | 0.02 | 216136412.13 | 2.08 | n/a |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.69 | 0.08 | 769472.25 | 10.28 | no_map |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.3 | -0.02 | 1153998.65 | 2.62 | empty_tvl |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.19 | -0.1 | 603640.64 | 6.78 | no_map |
| WUSDT | IDLE | 0.78 | 3.17 | 1.62 | -0.02 | 554347.85 | 14.93 | tvl≈1,556,368,553 |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.74 | 0.03 | 85499.91 | 13.41 | no_map |
| ZBCNUSDT | IDLE | 1.33 | 3.49 | 2.17 | -0.05 | 320997.93 | 25.26 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.98 | -0.07 | 219614.95 | 3.31 | n/a |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.02 | 75056.56 | 22.78 | no_map |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.6 | -0.16 | 134987.63 | 11.91 | tvl≈2,005,037 |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.15 | 0.03 | 56481.32 | 45.5 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.27 | -0.02 | 184220.93 | 1.58 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 64.45 | no_map |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.01 | 140061.87 | 42.69 | no_map |
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
