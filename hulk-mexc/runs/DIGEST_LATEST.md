# Hulk DIGEST — 2026-08-22T04:45:41Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.95 | 15.22 | 0.56 | 0.21 | 11803097.47 | 5.41 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.35 | 16.16 | 0.15 | 0.26 | 175372426.08 | 1.82 | n/a |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 8.85 | 0.04 | 0.14 | 1070334.29 | 1.17 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.06 | 0.2 | 736429.65 | 7.37 | no_map |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.59 | 0.02 | 450629.45 | 2.99 | no_map |
| WUSDT | IDLE | 2.01 | 7.75 | 0.0 | 0.15 | 432544.23 | 12.51 | tvl≈1,672,612,247 |
| BIOUSDT | IDLE | 2.95 | 7.36 | 1.23 | 0.06 | 200713.85 | 2.97 | n/a |
| ZBCNUSDT | IDLE | 1.4 | 4.29 | 0.51 | 0.13 | 537740.12 | 20.75 | n/a |
| EDELUSDT | IDLE | 2.03 | 4.07 | 2.71 | -0.03 | 80135.4 | 11.17 | no_map |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.34 | 0.1 | 181553.03 | 1.47 | n/a |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.65 | 0.1 | 58597.38 | 46.02 | no_map |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.41 | 0.21 | 158141.79 | 10.32 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.36 | 0.13 | 68027.77 | 10.62 | no_map |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.48 | 0.01 | 9348.0 | 27.23 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.35 | 0.11 | 181767.17 | 39.66 | no_map |
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
