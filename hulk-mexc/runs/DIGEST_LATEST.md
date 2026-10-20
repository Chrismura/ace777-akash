# Hulk DIGEST — 2026-10-20T10:13:10Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.84 | 1.53 | 1.06 | -0.02 | 130362039.61 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.29 | 0.96 | -0.01 | 20681124.64 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.94 | 0.64 | -0.01 | 300485283.03 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.06 | 1.94 | 1.2 | -0.04 | 967631.59 | 1.38 | skipped_fast |
| WUSDT | IDLE | 1.57 | 2.99 | 1.02 | 0.02 | 733243.85 | 13.77 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 13.56 | 1.98 | 0.17 | 298911.11 | 18.96 | skipped_fast |
| CCUSDT | IDLE | 2.01 | 3.61 | 2.73 | 0.01 | 459573.05 | 9.66 | skipped_fast |
| QNTUSDT | IDLE | 1.58 | 2.99 | 1.08 | -0.05 | 556084.61 | 3.1 | skipped_fast |
| CHIPUSDT | IDLE | 1.99 | 5.11 | 2.23 | 0.03 | 92865.84 | 13.66 | skipped_fast |
| KITEUSDT | IDLE | 2.0 | 3.5 | 3.29 | 0.02 | 81086.16 | 9.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 2.31 | 2.13 | -0.03 | 173150.91 | 17.4 | skipped_fast |
| RWAINCUSDT | IDLE | 1.45 | 2.57 | 2.15 | -0.0 | 77022.26 | 20.9 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.19 | 1.86 | -0.02 | 364552.03 | 3.64 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 1.93 | 1.74 | -0.0 | 58589.44 | 17.62 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.28 | 0.76 | -0.01 | 66810.85 | 4.25 | skipped_fast |
| WAXLUSDT | IDLE | 1.65 | 3.35 | 2.89 | -0.07 | 57855.72 | 24.22 | skipped_fast |
| LAUSDT | IDLE | 1.6 | 2.79 | 2.69 | -0.03 | 55693.62 | 21.3 | skipped_fast |
| RIZEUSDT | IDLE | 0.6 | 2.27 | 1.47 | -0.07 | 64369.03 | 66.43 | skipped_fast |
| IOTAUSDT | IDLE | 1.46 | 2.55 | 2.47 | 0.0 | 87690.48 | 22.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.52 | 0.95 | 0.62 | -0.01 | 4449.41 | 21.5 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.16 | 0.01 | 50823.45 | 15.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.11 | -0.0 | 39421.22 | 5.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
