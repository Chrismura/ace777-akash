# Hulk DIGEST — 2026-09-23T08:17:27Z

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
| XRPUSDT | IDLE | 2.15 | 4.47 | 2.73 | 0.06 | 118944887.66 | 2.48 | skipped_fast |
| HBARUSDT | IDLE | 2.13 | 4.3 | 3.31 | 0.03 | 1779467.5 | 1.02 | skipped_fast |
| PYTHUSDT | IDLE | 0.69 | 3.18 | 1.82 | 0.05 | 1795871.25 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 1.93 | 1.52 | 0.01 | 413187462.8 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.46 | 1.17 | 0.01 | 871929874.26 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 4.03 | 3.19 | -0.06 | 404614.19 | 7.97 | skipped_fast |
| CHIPUSDT | IDLE | 2.98 | 5.37 | 4.0 | -0.06 | 204309.7 | 17.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.31 | 5.53 | 3.22 | 0.04 | 219770.72 | 16.49 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.62 | 1.24 | 0.04 | 316753.89 | 10.56 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 4.78 | 3.29 | 0.07 | 142864.13 | 10.33 | skipped_fast |
| BIOUSDT | IDLE | 1.58 | 2.92 | 1.57 | 0.05 | 112208.65 | 19.92 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 3.1 | 1.84 | -0.05 | 260568.33 | 23.05 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 2.07 | 0.18 | 0.02 | 59744.88 | 14.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 12.5 | 3.57 | 0.48 | 63806.15 | 94.26 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 2.57 | 1.05 | 0.11 | 241882.62 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 4.92 | 4.26 | 0.12 | 117889.35 | 55.25 | skipped_fast |
| RWAINCUSDT | IDLE | 0.66 | 1.68 | 0.69 | 0.04 | 20999.46 | 91.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 1.78 | 1.75 | 0.01 | 2938.19 | 21.78 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.65 | 0.01 | 53413.29 | 7.23 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.54 | 0.43 | 0.01 | 39729.85 | 26.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
