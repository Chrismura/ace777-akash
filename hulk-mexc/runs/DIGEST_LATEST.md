# Hulk DIGEST — 2026-10-18T07:28:50Z

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
| ETHUSDT | IDLE | 0.58 | 1.02 | 0.87 | -0.01 | 93075909.76 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.6 | 1.06 | 0.89 | -0.01 | 18757948.64 | 2.32 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.57 | 0.49 | 0.0 | 184512238.94 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.14 | 2.94 | 1.97 | -0.08 | 1309528.56 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.38 | 4.59 | 3.6 | -0.09 | 1218936.04 | 15.7 | skipped_fast |
| EDELUSDT | IDLE | 2.42 | 6.95 | 4.86 | -0.09 | 203308.65 | 14.99 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.62 | 1.86 | -0.05 | 556098.66 | 6.2 | skipped_fast |
| HBARUSDT | IDLE | 2.29 | 4.3 | 1.91 | 0.04 | 304770.77 | 5.75 | skipped_fast |
| CCUSDT | IDLE | 1.21 | 2.26 | 1.05 | -0.02 | 244810.32 | 10.77 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 2.42 | 2.02 | -0.03 | 168791.57 | 24.0 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 2.88 | 1.07 | -0.03 | 61578.91 | 9.42 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.44 | 2.17 | -0.04 | 71124.04 | 8.39 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 3.15 | 1.98 | -0.06 | 69761.23 | 11.64 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.3 | 2.12 | -0.09 | 69449.01 | 13.18 | skipped_fast |
| RIZEUSDT | IDLE | 1.19 | 2.14 | 1.65 | 0.0 | 45372.8 | 59.57 | skipped_fast |
| WAXLUSDT | IDLE | 1.77 | 6.58 | 0.0 | 0.1 | 64050.58 | 57.12 | skipped_fast |
| LAUSDT | IDLE | 1.54 | 2.76 | 2.12 | -0.05 | 54380.12 | 23.93 | skipped_fast |
| RWAINCUSDT | IDLE | 0.25 | 0.79 | 0.05 | 0.03 | 16790.5 | 5.25 | skipped_fast |
| IOTAUSDT | IDLE | 1.38 | 2.47 | 1.87 | -0.04 | 67248.29 | 21.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.56 | 1.07 | 0.35 | -0.0 | 30346.7 | 14.2 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.72 | 0.16 | 0.0 | 51002.26 | 15.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.45 | 0.85 | 0.32 | -0.02 | 1735.19 | 21.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
