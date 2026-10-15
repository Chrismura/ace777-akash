# Hulk DIGEST — 2026-10-15T08:37:31Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.01 | 9.59 | 1.58 | 0.06 | 2770969.12 | 3.43 | skipped_fast |
| WUSDT | IDLE | 2.11 | 6.39 | 5.35 | -0.12 | 2761335.55 | 16.47 | skipped_fast |
| XRPUSDT | IDLE | 1.42 | 2.73 | 0.77 | -0.04 | 61322815.78 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.93 | 1.9 | 0.48 | -0.05 | 347281036.52 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.5 | 0.46 | -0.03 | 547935317.12 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.63 | 4.53 | 0.18 | -0.06 | 1159500.14 | 5.49 | skipped_fast |
| CCUSDT | IDLE | 1.24 | 4.08 | 3.92 | -0.13 | 454825.61 | 8.43 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 16.03 | 8.87 | -0.04 | 65236.63 | 57.45 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 2.82 | 0.89 | -0.06 | 602502.09 | 6.1 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 4.66 | 4.3 | -0.09 | 207277.8 | 54.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 8.26 | 6.69 | -0.21 | 122255.35 | 17.93 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 2.84 | 0.4 | -0.05 | 220005.18 | 17.2 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 3.98 | 2.01 | -0.1 | 84147.28 | 4.04 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.27 | 0.29 | 0.01 | 67324.36 | 15.11 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 3.59 | 1.12 | -0.13 | 68728.78 | 10.73 | skipped_fast |
| RWAINCUSDT | IDLE | 1.08 | 2.37 | 1.01 | 0.01 | 26127.15 | 15.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.98 | 5.96 | 3.91 | -0.05 | 20373.18 | 21.52 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 2.0 | 0.75 | -0.04 | 100263.83 | 40.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.14 | 1.07 | -0.02 | 31309.62 | 19.99 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.73 | 0.48 | -0.04 | 54925.4 | 16.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
