# Hulk DIGEST — 2026-09-14T09:34:34Z

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
| XRPUSDT | IDLE | 0.85 | 1.65 | 0.39 | 0.03 | 30603808.22 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 0.96 | 0.43 | 0.02 | 326449097.71 | 0.59 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.8 | 0.17 | 0.02 | 386764444.39 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.66 | 5.67 | 4.68 | 0.04 | 515761.33 | 1.79 | skipped_fast |
| CHIPUSDT | IDLE | 2.36 | 7.72 | 6.65 | -0.12 | 104701.35 | 17.05 | skipped_fast |
| REDUSDT | IDLE | 2.33 | 5.82 | 0.01 | 0.06 | 138858.14 | 17.44 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 6.62 | 4.76 | 0.14 | 219654.31 | 21.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 19.88 | 6.83 | 0.18 | 72989.29 | 96.4 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 2.12 | 1.73 | -0.0 | 244704.14 | 7.35 | skipped_fast |
| WUSDT | IDLE | 1.26 | 2.25 | 1.78 | 0.02 | 211707.39 | 4.97 | skipped_fast |
| KITEUSDT | IDLE | 1.68 | 2.96 | 2.63 | -0.02 | 60995.69 | 12.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 1.85 | 1.36 | -0.01 | 195869.16 | 20.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.79 | 3.35 | 1.51 | 0.02 | 9380.2 | 21.91 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.65 | 1.05 | 0.01 | 73219.93 | 3.92 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 1.01 | 0.65 | 0.02 | 270374.06 | 1.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 2.06 | 1.16 | 0.01 | 783.0 | 21.64 | skipped_fast |
| QNTUSDT | IDLE | 0.61 | 1.1 | 0.76 | 0.0 | 38149.34 | 4.71 | skipped_fast |
| TELUSDT | IDLE | 0.77 | 1.53 | 0.13 | 0.0 | 87201.3 | 69.12 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.49 | 0.17 | -0.0 | 29697.56 | 6.97 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.45 | 0.22 | 0.01 | 53150.93 | 22.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
