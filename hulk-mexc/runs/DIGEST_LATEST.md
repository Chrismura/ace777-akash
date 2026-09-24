# Hulk DIGEST — 2026-09-24T16:38:16Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 2.22 | 4.41 | 0.24 | 0.02 | 67123598.55 | 3.27 | skipped_fast |
| PYTHUSDT | IDLE | 3.42 | 12.87 | 2.46 | 0.12 | 1247254.21 | 1.44 | skipped_fast |
| ETHUSDT | IDLE | 1.14 | 2.24 | 0.24 | 0.01 | 323133859.15 | 0.63 | skipped_fast |
| BTCUSDT | IDLE | 1.11 | 2.14 | 0.58 | 0.01 | 737205402.77 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 3.25 | 6.19 | 2.08 | 0.03 | 872271.9 | 1.08 | skipped_fast |
| CCUSDT | IDLE | 3.52 | 6.91 | 0.8 | 0.05 | 469094.33 | 9.7 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.81 | 12.77 | 0.45 | 0.07 | 73450.94 | 15.21 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.27 | 9.85 | 0.45 | 0.1 | 83703.17 | 6.42 | skipped_fast |
| WUSDT | IDLE | 2.68 | 5.31 | 0.39 | 0.03 | 241098.39 | 5.91 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.22 | 17.89 | 0.6 | 0.18 | 172112.83 | 11.89 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.81 | 12.06 | 0.34 | 0.12 | 11279.61 | 96.9 | skipped_fast |
| ZBCNUSDT | IDLE | 2.43 | 4.84 | 0.13 | 0.04 | 217703.85 | 26.91 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 5.47 | 1.0 | -0.02 | 157846.34 | 7.18 | skipped_fast |
| REDUSDT | IDLE | 2.28 | 6.22 | 0.72 | 0.04 | 101036.55 | 13.66 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.29 | 0.92 | 0.0 | 84613.87 | 10.53 | skipped_fast |
| TELUSDT | IDLE | 3.08 | 5.45 | 4.76 | -0.05 | 107263.39 | 49.29 | skipped_fast |
| FLUIDUSDT | IDLE | 2.42 | 4.73 | 0.78 | 0.04 | 2784.26 | 21.43 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 5.55 | 2.5 | 0.06 | 49002.67 | 100.87 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.3 | 0.29 | 0.02 | 55424.75 | 21.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.67 | 1.31 | 0.17 | 0.0 | 36810.72 | 2.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
