# Hulk DIGEST — 2026-08-22T01:07:11Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 8.23 | 0.08 | 0.14 | 6574514.75 | 3.96 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.4 | 0.68 | 0.16 | 148874572.72 | 3.4 | n/a |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.76 | 0.08 | 953815.24 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.85 | 0.11 | 542928.58 | 30.03 | n/a |
| CCUSDT | IDLE | 1.73 | 6.94 | 0.14 | 0.16 | 653018.11 | 6.13 | no_map |
| WUSDT | IDLE | 2.69 | 6.65 | 0.51 | 0.09 | 392293.77 | 10.16 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.4 | 0.02 | 538274.67 | 3.06 | no_map |
| BIOUSDT | IDLE | 2.44 | 5.53 | 0.03 | 0.05 | 187038.29 | 3.05 | n/a |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.28 | -0.02 | 79702.06 | 22.2 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.13 | 0.11 | 60384.68 | 45.81 | no_map |
| REDUSDT | IDLE | 0.93 | 8.27 | 2.23 | 0.22 | 159912.55 | 19.44 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.76 | 0.07 | 170499.97 | 6.02 | n/a |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.77 | 0.06 | 183685.9 | 36.09 | no_map |
| KITEUSDT | IDLE | 1.37 | 4.01 | 0.12 | 0.11 | 60823.98 | 9.05 | no_map |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | no_map |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 55112.41 | 16.41 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 18.14 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
