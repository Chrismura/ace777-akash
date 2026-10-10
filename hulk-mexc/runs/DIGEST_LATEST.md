# Hulk DIGEST — 2026-10-10T15:59:11Z

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
| WUSDT | IDLE | 3.9 | 12.87 | 4.87 | 0.03 | 1206909.05 | 14.99 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.95 | 0.27 | 0.01 | 86804395.84 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.73 | 0.23 | 0.02 | 15945874.02 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.36 | 0.09 | 0.0 | 187593308.98 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.47 | 4.39 | 3.63 | -0.02 | 1124961.07 | 1.63 | skipped_fast |
| PYTHUSDT | IDLE | 0.55 | 1.38 | 0.2 | -0.09 | 999283.07 | 3.82 | skipped_fast |
| EDELUSDT | IDLE | 3.18 | 6.53 | 4.21 | -0.03 | 218850.19 | 10.41 | skipped_fast |
| KITEUSDT | IDLE | 2.42 | 6.81 | 1.0 | 0.08 | 73069.95 | 9.94 | skipped_fast |
| CCUSDT | IDLE | 0.69 | 1.36 | 0.17 | -0.0 | 367652.71 | 9.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.05 | 1.96 | 1.0 | -0.01 | 204390.3 | 15.72 | skipped_fast |
| TELUSDT | IDLE | 2.72 | 4.8 | 4.21 | -0.03 | 116951.71 | 62.02 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.93 | 0.35 | 0.03 | 82809.21 | 6.92 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.16 | 1.05 | 0.03 | 54417.26 | 15.98 | skipped_fast |
| CHIPUSDT | IDLE | 0.88 | 2.11 | 1.58 | 0.06 | 91208.56 | 13.52 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.69 | 0.84 | 0.02 | 345529.94 | 4.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.78 | 0.29 | -0.0 | 9624.54 | 48.73 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 1.44 | 1.02 | -0.0 | 44853.95 | 57.67 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.71 | 0.47 | -0.01 | 54199.09 | 7.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.62 | 1.94 | 0.35 | 0.01 | 15109.76 | 21.29 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.67 | 0.24 | 0.0 | 39111.41 | 14.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
