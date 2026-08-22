# Hulk DIGEST — 2026-08-22T01:57:53Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.77 | 0.15 | 6863545.8 | 1.95 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 10.52 | 1.56 | 0.14 | 153803609.22 | 3.36 | n/a |
| HBARUSDT | IDLE | 3.03 | 6.36 | 0.97 | 0.07 | 948625.71 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.81 | 0.09 | 550572.53 | 16.94 | n/a |
| CCUSDT | IDLE | 1.81 | 7.36 | 0.88 | 0.15 | 662292.91 | 4.39 | no_map |
| WUSDT | IDLE | 2.66 | 6.65 | 0.04 | 0.09 | 398431.92 | 12.13 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.67 | 0.02 | 510498.8 | 12.22 | no_map |
| BIOUSDT | IDLE | 2.58 | 5.86 | 0.03 | 0.06 | 184845.86 | 6.08 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79496.09 | 11.08 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.98 | 0.11 | 61059.68 | 22.04 | no_map |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.2 | 0.16 | 156901.64 | 19.45 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.36 | 0.12 | 61273.95 | 13.46 | no_map |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.15 | 0.07 | 171375.37 | 9.06 | n/a |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.13 | 0.05 | 180942.61 | 41.37 | no_map |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | no_map |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9181.85 | 101.69 | no_map |
| FLUIDUSDT | IDLE | 1.46 | 3.74 | 2.03 | 0.07 | 4799.07 | 21.96 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54623.22 | 16.39 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
