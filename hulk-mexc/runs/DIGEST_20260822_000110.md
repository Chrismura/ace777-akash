# Hulk DIGEST — 2026-08-22T00:01:10Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.41 | 0.1 | 6238661.71 | 2.05 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.03 | 8.23 | 1.7 | 0.14 | 142220088.72 | 2.76 | skipped_fast |
| HBARUSDT | IDLE | 2.77 | 6.36 | 1.13 | 0.09 | 909665.87 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.76 | 0.12 | 515187.81 | 23.22 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.69 | 0.13 | 645323.68 | 6.2 | skipped_fast |
| WUSDT | IDLE | 2.79 | 6.91 | 1.88 | 0.08 | 378998.4 | 8.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.4 | 0.05 | 541244.94 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.03 | 187182.1 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 5.5 | 1.09 | -0.01 | 80067.22 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.26 | 9.82 | 4.13 | 0.13 | 58948.96 | 45.81 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.31 | 0.06 | 189780.94 | 15.4 | skipped_fast |
| QNTUSDT | IDLE | 2.48 | 5.42 | 0.3 | 0.07 | 166696.77 | 1.5 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.84 | 0.1 | 61517.95 | 12.93 | skipped_fast |
| REDUSDT | IDLE | 0.56 | 4.91 | 1.51 | 0.19 | 157898.12 | 49.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54481.87 | 16.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 51.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
