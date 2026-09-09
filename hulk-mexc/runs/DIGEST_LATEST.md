# Hulk DIGEST — 2026-09-09T21:14:11Z

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
| XRPUSDT | IDLE | 1.18 | 2.1 | 1.72 | -0.01 | 40871497.13 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.98 | 1.79 | 1.19 | -0.01 | 351798530.12 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.18 | 0.85 | -0.0 | 533229592.9 | 0.16 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 7.55 | 5.0 | 0.01 | 761298.39 | 9.23 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 7.09 | 6.15 | -0.03 | 177523.08 | 29.78 | skipped_fast |
| WUSDT | IDLE | 2.81 | 5.0 | 4.1 | -0.01 | 190548.93 | 10.91 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 2.1 | 1.04 | -0.04 | 583818.7 | 10.57 | skipped_fast |
| CHIPUSDT | IDLE | 2.13 | 7.16 | 6.3 | 0.04 | 112445.16 | 16.53 | skipped_fast |
| REDUSDT | IDLE | 2.16 | 3.84 | 3.23 | 0.01 | 61236.35 | 18.58 | skipped_fast |
| ZBCNUSDT | IDLE | 1.16 | 2.28 | 0.32 | 0.03 | 198638.16 | 10.33 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.18 | 1.87 | -0.02 | 426618.63 | 1.3 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.18 | 1.88 | -0.05 | 95338.39 | 3.76 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 2.37 | 1.06 | 0.01 | 60692.97 | 12.22 | skipped_fast |
| RWAUSDT | IDLE | 2.5 | 4.46 | 3.56 | -0.02 | 55482.18 | 22.15 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.29 | 1.8 | -0.01 | 7079.08 | 55.34 | skipped_fast |
| RIZEUSDT | IDLE | 0.44 | 5.18 | 1.42 | 0.0 | 71536.08 | 93.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.47 | 2.57 | 2.51 | -0.06 | 915.77 | 21.58 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.18 | 0.55 | 0.04 | 105000.47 | 38.43 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 1.6 | 0.95 | -0.01 | 43743.56 | 4.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.61 | 0.19 | 0.01 | 24431.15 | 57.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
