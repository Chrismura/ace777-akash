# Hulk DIGEST — 2026-08-22T01:32:12Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 10.86 | 0.29 | 0.16 | 6750661.15 | 1.94 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.2 | 8.72 | 0.09 | 0.15 | 150381053.6 | 7.42 | n/a |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.48 | 0.08 | 952140.0 | 1.24 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.84 | 0.1 | 546996.77 | 12.59 | n/a |
| CCUSDT | IDLE | 1.77 | 7.32 | 0.0 | 0.16 | 661308.69 | 7.84 | no_map |
| WUSDT | IDLE | 2.72 | 6.65 | 1.04 | 0.09 | 391911.87 | 13.27 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.55 | -0.01 | 513371.7 | 3.09 | no_map |
| BIOUSDT | IDLE | 2.52 | 5.57 | 1.07 | 0.04 | 186078.9 | 3.08 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79541.27 | 22.15 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.15 | 0.11 | 60704.85 | 45.81 | no_map |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.49 | 0.18 | 158618.73 | 7.96 | tvl≈2,226,572 |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.23 | 0.05 | 181583.38 | 20.74 | no_map |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.88 | 0.07 | 170114.78 | 6.03 | n/a |
| KITEUSDT | IDLE | 1.55 | 4.93 | 0.0 | 0.13 | 60984.75 | 11.66 | no_map |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | no_map |
| RWAINCUSDT | IDLE | 1.3 | 2.45 | 1.01 | 0.04 | 9587.29 | 37.46 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 54944.33 | 8.21 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 20.41 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
