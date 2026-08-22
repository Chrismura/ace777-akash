# Hulk DIGEST — 2026-08-22T01:36:26Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.91 | 0.15 | 6771663.91 | 11.7 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 9.03 | 0.42 | 0.15 | 150983393.28 | 3.37 | n/a |
| HBARUSDT | IDLE | 2.98 | 6.36 | 0.28 | 0.08 | 955121.8 | 1.24 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.8 | 0.09 | 551676.91 | 15.49 | n/a |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.13 | 0.17 | 661493.34 | 7.86 | no_map |
| WUSDT | IDLE | 2.7 | 6.65 | 0.67 | 0.09 | 391192.27 | 21.37 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.01 | 513706.59 | 6.13 | no_map |
| BIOUSDT | IDLE | 2.52 | 5.57 | 1.07 | 0.03 | 186105.85 | 6.16 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79516.2 | 22.15 | no_map |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.23 | 0.11 | 60765.82 | 45.81 | no_map |
| REDUSDT | IDLE | 0.98 | 8.27 | 5.02 | 0.17 | 158615.25 | 9.62 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.55 | 4.94 | 0.0 | 0.13 | 61100.05 | 9.85 | no_map |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.81 | 0.07 | 170034.66 | 7.52 | n/a |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | no_map |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.92 | 0.05 | 181975.26 | 51.63 | no_map |
| RWAINCUSDT | IDLE | 1.3 | 2.45 | 1.01 | 0.04 | 9587.29 | 64.31 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.12 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54823.65 | 16.41 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
