# Hulk DIGEST — 2026-10-11T12:19:51Z

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
| XRPUSDT | IDLE | 0.34 | 0.66 | 0.11 | -0.0 | 10157311.93 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.1 | 0.0 | 178880326.85 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.34 | 0.11 | 0.0 | 122311478.62 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.23 | 3.27 | 1.9 | -0.0 | 1159546.42 | 7.45 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 3.75 | 0.74 | -0.02 | 1095340.03 | 1.23 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 31.62 | 15.97 | 0.06 | 55912.37 | 21.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.76 | 2.04 | -0.02 | 714547.92 | 5.22 | skipped_fast |
| RIZEUSDT | IDLE | 3.32 | 9.17 | 4.67 | -0.06 | 35785.77 | 33.98 | skipped_fast |
| EDELUSDT | IDLE | 1.81 | 3.27 | 2.29 | -0.0 | 374346.64 | 7.72 | skipped_fast |
| CHIPUSDT | IDLE | 0.9 | 8.41 | 3.21 | 0.28 | 368368.88 | 13.5 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 3.09 | 0.96 | 0.01 | 255441.27 | 9.91 | skipped_fast |
| TELUSDT | IDLE | 3.24 | 5.97 | 4.85 | -0.07 | 145441.77 | 35.17 | skipped_fast |
| BIOUSDT | IDLE | 1.63 | 2.99 | 1.74 | 0.03 | 74956.35 | 3.4 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 2.2 | 1.55 | -0.02 | 58005.72 | 7.41 | skipped_fast |
| ZBCNUSDT | IDLE | 0.83 | 1.61 | 0.32 | -0.0 | 155774.37 | 18.45 | skipped_fast |
| KITEUSDT | IDLE | 0.69 | 1.24 | 0.91 | -0.0 | 74132.29 | 10.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.73 | 1.36 | 0.65 | -0.03 | 19660.47 | 5.01 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.74 | 0.59 | -0.01 | 251413.53 | 4.36 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.39 | -0.01 | 52854.23 | 7.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.34 | 0.14 | -0.01 | 31963.15 | 16.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
