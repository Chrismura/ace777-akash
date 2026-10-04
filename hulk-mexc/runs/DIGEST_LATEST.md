# Hulk DIGEST — 2026-10-04T02:59:31Z

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
| QNTUSDT | IDLE | 2.95 | 9.2 | 2.63 | 0.06 | 3502945.89 | 9.2 | skipped_fast |
| XRPUSDT | IDLE | 0.27 | 0.51 | 0.16 | 0.0 | 16959718.96 | 1.34 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.12 | 0.01 | 98951109.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.36 | 0.08 | 0.0 | 300578017.9 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.42 | 5.87 | 0.1 | 0.07 | 401438.1 | 6.94 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 4.09 | 0.31 | 0.06 | 338175.27 | 6.32 | skipped_fast |
| RIZEUSDT | IDLE | 2.43 | 12.94 | 11.34 | -0.16 | 51992.76 | 56.23 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 5.27 | 3.94 | 0.02 | 80658.79 | 9.85 | skipped_fast |
| EDELUSDT | IDLE | 0.88 | 5.45 | 0.06 | 0.19 | 444152.67 | 24.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.79 | 5.42 | 1.13 | 0.04 | 4448.47 | 3.94 | skipped_fast |
| TELUSDT | IDLE | 3.45 | 6.69 | 2.79 | -0.01 | 125345.58 | 35.83 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 2.76 | 0.99 | -0.02 | 220096.82 | 30.23 | skipped_fast |
| PYTHUSDT | IDLE | 0.74 | 1.33 | 0.97 | -0.02 | 278059.43 | 1.29 | skipped_fast |
| FLUIDUSDT | IDLE | 2.61 | 8.51 | 4.1 | 0.09 | 2510.44 | 21.99 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 1.88 | 1.71 | -0.01 | 70244.41 | 3.23 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 3.0 | 1.58 | 0.08 | 62711.52 | 12.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.12 | 2.17 | 0.42 | 0.02 | 58457.22 | 15.71 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.43 | 1.27 | 0.0 | 332052.01 | 2.96 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.73 | 0.51 | -0.0 | 55127.24 | 14.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.61 | 0.19 | 0.0 | 34462.86 | 42.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
