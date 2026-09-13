# Hulk DIGEST — 2026-09-13T14:40:21Z

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
| ETHUSDT | IDLE | 0.73 | 1.43 | 0.21 | -0.02 | 234960207.93 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.49 | 0.1 | -0.01 | 14810881.52 | 2.96 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.97 | 0.03 | -0.0 | 287302145.7 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 14.26 | 7.74 | 0.1 | 203052.63 | 15.81 | skipped_fast |
| PYTHUSDT | IDLE | 2.02 | 3.99 | 0.32 | 0.03 | 447511.51 | 1.81 | skipped_fast |
| CHIPUSDT | IDLE | 2.07 | 8.36 | 5.25 | -0.09 | 91371.2 | 8.98 | skipped_fast |
| WUSDT | IDLE | 1.36 | 2.68 | 0.33 | 0.03 | 252596.82 | 8.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 2.96 | 0.06 | -0.03 | 204435.85 | 12.21 | skipped_fast |
| CCUSDT | IDLE | 0.83 | 1.6 | 0.42 | -0.03 | 285362.92 | 9.45 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 2.93 | 0.68 | 0.03 | 60879.74 | 16.58 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 12.36 | 0.86 | 0.1 | 100812.3 | 49.81 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 2.03 | 0.55 | -0.0 | 70341.99 | 3.92 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 1.45 | 1.01 | 0.01 | 63316.22 | 10.14 | skipped_fast |
| RWAINCUSDT | IDLE | 0.89 | 1.65 | 0.84 | -0.02 | 6620.9 | 5.61 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 2.44 | 0.31 | 0.02 | 199399.8 | 1.31 | skipped_fast |
| TELUSDT | IDLE | 1.14 | 2.17 | 0.69 | -0.05 | 89190.79 | 31.48 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 1.96 | 0.89 | -0.01 | 53325.97 | 7.47 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 1.7 | 0.37 | -0.0 | 37091.55 | 4.66 | skipped_fast |
| FLUIDUSDT | IDLE | 0.57 | 1.11 | 0.18 | 0.01 | 1243.49 | 21.11 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.01 | -0.0 | 32494.48 | 15.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
