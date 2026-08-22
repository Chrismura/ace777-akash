# Hulk DIGEST — 2026-08-22T01:45:29Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 10.86 | 0.5 | 0.16 | 6819707.51 | 1.94 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 9.66 | 0.15 | 0.16 | 151749057.35 | 2.67 | n/a |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.64 | 0.08 | 960562.13 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.73 | 0.08 | 549509.08 | 2.42 | n/a |
| CCUSDT | IDLE | 1.79 | 7.36 | 0.21 | 0.16 | 661515.1 | 7.86 | no_map |
| WUSDT | IDLE | 2.69 | 6.65 | 0.45 | 0.09 | 391597.76 | 8.12 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.31 | 0.02 | 512378.93 | 6.15 | no_map |
| BIOUSDT | IDLE | 2.48 | 5.57 | 0.34 | 0.05 | 186866.0 | 3.06 | n/a |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.74 | -0.02 | 79516.2 | 22.12 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.11 | 0.11 | 60926.92 | 38.93 | no_map |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.88 | 0.18 | 158179.64 | 16.79 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.39 | 0.13 | 61518.11 | 13.46 | no_map |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.53 | 0.05 | 182216.33 | 41.58 | no_map |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.08 | 0.07 | 171667.09 | 12.08 | n/a |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | no_map |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9235.4 | 90.93 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.26 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54651.09 | 16.39 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
