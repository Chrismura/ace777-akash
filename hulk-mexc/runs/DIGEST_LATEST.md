# Hulk DIGEST — 2026-08-22T01:14:49Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.75 | 9.41 | 0.63 | 0.14 | 6634944.1 | 1.97 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 8.4 | 0.55 | 0.16 | 149433234.65 | 2.04 | n/a |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.52 | 0.09 | 956651.85 | 1.24 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.88 | 0.1 | 540402.33 | 12.59 | n/a |
| CCUSDT | IDLE | 1.76 | 7.13 | 0.26 | 0.16 | 658711.58 | 5.25 | no_map |
| WUSDT | IDLE | 2.71 | 6.65 | 0.81 | 0.09 | 392362.84 | 12.22 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.66 | 3.56 | 1.86 | 0.01 | 537911.95 | 3.1 | no_map |
| BIOUSDT | IDLE | 2.49 | 5.57 | 0.52 | 0.04 | 186943.11 | 3.06 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.03 | 79630.34 | 22.15 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.16 | 0.11 | 60479.25 | 45.81 | no_map |
| REDUSDT | IDLE | 0.95 | 8.27 | 3.08 | 0.21 | 159818.69 | 16.52 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.93 | 0.07 | 170438.03 | 1.51 | n/a |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.66 | 0.05 | 181040.63 | 41.22 | no_map |
| KITEUSDT | IDLE | 1.47 | 4.48 | 0.3 | 0.11 | 60991.15 | 12.65 | no_map |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | no_map |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 20.29 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 55229.8 | 24.62 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
