# Hulk DIGEST — 2026-08-21T23:46:19Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.49 | 0.1 | 6172112.99 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.64 | 0.16 | 141741500.92 | 2.73 | n/a |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.73 | 0.13 | 514166.36 | 14.37 | n/a |
| HBARUSDT | IDLE | 2.59 | 6.36 | 0.66 | 0.09 | 909630.72 | 1.25 | empty_tvl |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.92 | 0.13 | 644497.76 | 7.11 | no_map |
| WUSDT | IDLE | 2.77 | 6.91 | 1.69 | 0.07 | 378655.87 | 12.33 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.37 | 0.03 | 547361.09 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.83 | 0.02 | 186533.29 | 3.11 | n/a |
| EDELUSDT | IDLE | 2.59 | 5.5 | 1.52 | -0.03 | 82506.83 | 33.02 | no_map |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.83 | 0.12 | 58849.67 | 46.02 | no_map |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.31 | 0.07 | 190276.02 | 25.66 | no_map |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10299.86 | 21.39 | no_map |
| REDUSDT | IDLE | 0.86 | 7.3 | 4.49 | 0.19 | 157810.58 | 12.92 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.04 | 0.08 | 147474.92 | 1.49 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.86 | 0.1 | 61432.19 | 12.93 | no_map |
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
