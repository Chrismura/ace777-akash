# Hulk DIGEST — 2026-08-22T03:53:12Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 11.77 | 0.94 | 0.18 | 8789216.02 | 1.87 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.58 | 0.2 | 165862230.43 | 3.18 | n/a |
| HBARUSDT | IDLE | 2.39 | 6.93 | 0.2 | 0.11 | 1033942.16 | 2.4 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.45 | 0.19 | 700895.56 | 12.44 | no_map |
| CHIPUSDT | IDLE | 2.47 | 5.36 | 1.18 | -0.03 | 459953.01 | 5.95 | no_map |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.11 | 0.07 | 199420.46 | 12.01 | n/a |
| ZBCNUSDT | IDLE | 1.44 | 5.37 | 1.14 | 0.13 | 537538.22 | 28.46 | n/a |
| WUSDT | IDLE | 1.83 | 5.98 | 0.12 | 0.13 | 424561.35 | 10.79 | tvl≈1,672,612,247 |
| RIZEUSDT | IDLE | 1.83 | 7.71 | 4.83 | 0.11 | 59491.62 | 46.02 | no_map |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80723.74 | 44.99 | no_map |
| REDUSDT | IDLE | 0.9 | 7.96 | 2.49 | 0.23 | 157524.48 | 9.37 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.54 | 5.3 | 0.0 | 0.13 | 67751.56 | 11.51 | no_map |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 43.55 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.41 | 0.09 | 175162.45 | 59.38 | n/a |
| TELUSDT | IDLE | 1.01 | 2.45 | 0.25 | 0.07 | 173768.17 | 71.43 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 17.38 | tvl≈2,594,231,317 |
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
