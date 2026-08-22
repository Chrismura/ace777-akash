# Hulk DIGEST — 2026-08-22T01:05:58Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 8.06 | 0.12 | 0.14 | 6570660.88 | 1.99 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.4 | 0.71 | 0.16 | 148780613.17 | 3.4 | skipped_fast |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.87 | 0.08 | 953508.51 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.75 | 0.11 | 543053.11 | 9.19 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 6.71 | 0.04 | 0.16 | 650455.05 | 6.13 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.48 | 0.1 | 392132.07 | 10.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.46 | 0.02 | 539041.94 | 3.05 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 5.37 | 0.03 | 0.06 | 187011.08 | 3.05 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.28 | -0.02 | 79737.01 | 22.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.95 | 0.11 | 60370.87 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 8.27 | 2.17 | 0.22 | 160049.71 | 10.87 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.78 | 0.07 | 170481.02 | 9.03 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.66 | 0.06 | 183711.4 | 41.26 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 4.01 | 0.08 | 0.11 | 60797.11 | 10.85 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 0.7 | skipped_fast |
| RWAUSDT | IDLE | 1.1 | 2.08 | 0.82 | 0.03 | 55068.94 | 24.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
