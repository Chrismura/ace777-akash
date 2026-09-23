# Hulk DIGEST — 2026-09-23T11:18:22Z

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
| XRPUSDT | IDLE | 1.99 | 3.74 | 2.87 | 0.04 | 121716171.66 | 1.89 | skipped_fast |
| PYTHUSDT | IDLE | 0.95 | 4.33 | 0.77 | 0.1 | 1898111.26 | 2.94 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.29 | 1.08 | -0.0 | 403290334.98 | 0.04 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 3.94 | 3.79 | 0.03 | 1642241.13 | 1.04 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.09 | 1.01 | -0.0 | 846116943.85 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.29 | 4.15 | 2.89 | -0.04 | 425593.9 | 4.43 | skipped_fast |
| WUSDT | IDLE | 1.62 | 2.97 | 1.74 | 0.03 | 399194.95 | 8.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 4.57 | 2.6 | -0.01 | 194395.98 | 17.49 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 4.09 | 3.17 | 0.04 | 220983.07 | 0.48 | skipped_fast |
| KITEUSDT | IDLE | 1.77 | 3.47 | 0.52 | 0.04 | 137959.67 | 10.16 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.2 | 1.6 | 0.05 | 116325.56 | 13.26 | skipped_fast |
| REDUSDT | IDLE | 1.4 | 2.5 | 1.97 | 0.05 | 59083.68 | 6.22 | skipped_fast |
| EDELUSDT | IDLE | 0.56 | 2.53 | 2.47 | -0.08 | 242308.4 | 26.53 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 2.23 | 1.44 | 0.03 | 20323.14 | 5.38 | skipped_fast |
| QNTUSDT | IDLE | 1.3 | 2.55 | 1.33 | 0.08 | 238716.25 | 12.02 | skipped_fast |
| RIZEUSDT | IDLE | 0.58 | 12.5 | 2.16 | 0.49 | 63895.97 | 92.93 | skipped_fast |
| TELUSDT | IDLE | 1.68 | 6.24 | 5.29 | 0.11 | 152401.38 | 72.69 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.94 | 0.36 | 0.01 | 54550.21 | 21.68 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.68 | 0.54 | 0.0 | 40444.55 | 16.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.84 | 0.26 | 0.02 | 3845.47 | 17.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
