# Hulk DIGEST — 2026-08-22T04:58:47Z

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
| PYTHUSDT | IDLE | 3.01 | 15.45 | 2.02 | 0.19 | 13106523.66 | 18.27 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 17.46 | 0.85 | 0.26 | 180439948.38 | 5.44 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.54 | 9.87 | 0.42 | 0.15 | 1089629.65 | 3.48 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.37 | 0.2 | 742317.7 | 7.38 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.62 | 0.01 | 446489.16 | 5.98 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 8.62 | 1.2 | 0.15 | 448440.5 | 10.61 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.0 | 8.28 | 0.52 | 0.08 | 201855.42 | 2.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 0.93 | 0.11 | 537297.26 | 26.15 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 9.16 | 4.13 | 0.1 | 186805.72 | 14.7 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.07 | 2.28 | -0.02 | 80245.04 | 22.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.68 | 0.09 | 58618.63 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.71 | 0.2 | 157891.19 | 10.36 | skipped_fast |
| KITEUSDT | IDLE | 1.75 | 6.71 | 0.06 | 0.15 | 68375.36 | 21.81 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.39 | 0.1 | 183492.44 | 19.84 | skipped_fast |
| RWAUSDT | IDLE | 1.58 | 3.13 | 0.16 | 0.07 | 56536.69 | 15.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3692.42 | 22.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
