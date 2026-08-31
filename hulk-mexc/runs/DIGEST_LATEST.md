# Hulk DIGEST — 2026-08-31T17:09:58Z

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
| XRPUSDT | IDLE | 1.0 | 1.92 | 0.48 | -0.03 | 40411399.71 | 2.18 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.68 | 0.31 | -0.02 | 431199704.65 | 1.34 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.54 | 0.22 | -0.01 | 592548153.98 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 4.2 | 3.91 | -0.04 | 478233.53 | 2.59 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 3.91 | 0.06 | -0.02 | 434616.26 | 2.08 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 6.17 | 5.45 | -0.06 | 40813.57 | 62.5 | skipped_fast |
| CCUSDT | IDLE | 1.52 | 2.89 | 1.0 | 0.0 | 256628.51 | 6.75 | skipped_fast |
| REDUSDT | IDLE | 2.05 | 3.72 | 2.47 | -0.04 | 67964.93 | 10.33 | skipped_fast |
| WUSDT | IDLE | 1.47 | 2.61 | 2.15 | -0.05 | 210663.71 | 16.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 2.86 | 0.0 | -0.02 | 205409.61 | 25.17 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.86 | 2.16 | -0.08 | 98221.85 | 9.32 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.23 | 0.79 | -0.05 | 77602.61 | 7.58 | skipped_fast |
| EDELUSDT | IDLE | 0.99 | 5.81 | 5.41 | -0.01 | 128380.13 | 67.11 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 1.97 | 1.8 | -0.03 | 292250.47 | 2.73 | skipped_fast |
| RWAUSDT | IDLE | 2.3 | 4.42 | 1.21 | 0.06 | 57386.12 | 38.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.3 | 2.55 | 0.28 | -0.02 | 2271.88 | 91.32 | skipped_fast |
| TELUSDT | IDLE | 1.76 | 3.16 | 2.43 | -0.02 | 87885.04 | 59.17 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 1.71 | 1.11 | -0.01 | 51459.16 | 8.17 | skipped_fast |
| FLUIDUSDT | IDLE | 0.94 | 1.76 | 0.81 | -0.01 | 1876.21 | 21.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.64 | 0.0 | -0.01 | 25355.05 | 5.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
