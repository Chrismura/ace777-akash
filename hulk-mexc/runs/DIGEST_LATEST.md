# Hulk DIGEST — 2026-08-22T01:54:17Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 10.86 | 1.39 | 0.14 | 6846547.79 | 1.96 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 10.52 | 1.75 | 0.14 | 153373804.17 | 2.7 | n/a |
| HBARUSDT | IDLE | 3.04 | 6.36 | 1.23 | 0.07 | 948455.26 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.76 | 0.08 | 551260.65 | 3.87 | n/a |
| CCUSDT | IDLE | 1.8 | 7.36 | 0.58 | 0.16 | 661327.41 | 7.01 | no_map |
| WUSDT | IDLE | 2.7 | 6.65 | 0.64 | 0.08 | 393320.27 | 13.22 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.94 | 0.02 | 512056.94 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.61 | 5.86 | 0.36 | 0.05 | 185159.31 | 12.25 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79546.15 | 22.15 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.97 | 0.11 | 61031.14 | 45.71 | no_map |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.91 | 0.16 | 157197.73 | 10.51 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.44 | 5.18 | 1.3 | 0.06 | 171385.08 | 3.03 | n/a |
| KITEUSDT | IDLE | 1.6 | 5.17 | 0.25 | 0.12 | 61359.2 | 10.76 | no_map |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | no_map |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.48 | 0.05 | 181446.06 | 57.07 | no_map |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9181.85 | 91.03 | no_map |
| FLUIDUSDT | IDLE | 1.46 | 3.74 | 2.03 | 0.08 | 4799.07 | 21.27 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54624.24 | 16.39 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
