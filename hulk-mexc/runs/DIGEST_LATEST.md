# Hulk DIGEST — 2026-10-10T23:00:51Z

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
| ETHUSDT | IDLE | 0.31 | 0.56 | 0.35 | 0.01 | 114893647.52 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.32 | 0.58 | 0.36 | 0.01 | 13008394.04 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.12 | 0.23 | 0.06 | 0.01 | 169337503.86 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.06 | 3.34 | 2.33 | 0.03 | 1267237.24 | 7.36 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 2.11 | 1.55 | -0.04 | 1203338.24 | 1.67 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 1.64 | 0.99 | -0.03 | 772449.04 | 2.54 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 19.13 | 1.26 | 0.34 | 242017.29 | 15.98 | skipped_fast |
| EDELUSDT | IDLE | 2.39 | 4.71 | 3.34 | -0.05 | 252208.8 | 2.61 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 2.76 | 1.95 | 0.03 | 87732.39 | 3.43 | skipped_fast |
| CCUSDT | IDLE | 0.68 | 1.3 | 0.34 | -0.03 | 275803.17 | 10.08 | skipped_fast |
| ZBCNUSDT | IDLE | 0.66 | 1.31 | 0.12 | 0.03 | 200306.05 | 22.5 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 2.18 | 1.82 | 0.07 | 61505.16 | 10.16 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 3.46 | 2.36 | -0.04 | 138230.95 | 16.85 | skipped_fast |
| RIZEUSDT | IDLE | 0.99 | 1.82 | 1.13 | -0.05 | 33096.73 | 48.16 | skipped_fast |
| REDUSDT | IDLE | 0.59 | 1.05 | 0.92 | 0.02 | 55461.19 | 15.98 | skipped_fast |
| HBARUSDT | IDLE | 0.44 | 0.79 | 0.65 | 0.01 | 309734.72 | 3.25 | skipped_fast |
| RWAINCUSDT | IDLE | 0.52 | 1.04 | 0.0 | -0.02 | 9523.81 | 49.14 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.45 | 0.87 | 0.01 | 8391.47 | 21.38 | skipped_fast |
| MNSRYUSDT | IDLE | 1.04 | 1.82 | 1.76 | -0.01 | 36880.83 | 52.18 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.79 | 0.63 | 0.0 | 53098.41 | 7.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
