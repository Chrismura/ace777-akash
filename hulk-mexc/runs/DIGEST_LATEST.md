# Hulk DIGEST — 2026-09-11T09:18:17Z

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
| ETHUSDT | IDLE | 0.8 | 1.54 | 0.38 | 0.0 | 466650434.56 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.74 | 1.38 | 0.63 | -0.02 | 39343888.25 | 1.48 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.78 | 0.26 | -0.01 | 539604407.95 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 42.67 | 27.79 | 0.09 | 139015.39 | 217.96 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 6.62 | 3.98 | -0.06 | 125155.74 | 10.97 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.7 | 0.79 | -0.04 | 451637.66 | 7.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.24 | 0.96 | -0.01 | 345634.09 | 1.94 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.18 | 2.09 | -0.01 | 139775.64 | 5.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.0 | 1.92 | 0.59 | -0.03 | 199053.44 | 20.95 | skipped_fast |
| EDELUSDT | IDLE | 0.79 | 3.53 | 1.94 | -0.07 | 198146.24 | 46.75 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 1.87 | 0.0 | 0.03 | 58497.53 | 11.89 | skipped_fast |
| REDUSDT | IDLE | 0.89 | 1.55 | 1.48 | -0.02 | 59705.64 | 18.99 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.17 | 1.07 | -0.02 | 72047.22 | 4.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.04 | 1.85 | 1.49 | -0.0 | 3093.7 | 22.41 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.79 | 1.68 | -0.02 | 189282.89 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.26 | 1.53 | -0.04 | 96109.81 | 40.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.26 | 2.04 | -0.03 | 2138.71 | 21.81 | skipped_fast |
| QNTUSDT | IDLE | 0.55 | 0.99 | 0.8 | -0.03 | 36246.39 | 1.55 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.92 | 0.08 | -0.02 | 50378.39 | 7.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.6 | 0.01 | -0.01 | 36168.42 | 4.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
