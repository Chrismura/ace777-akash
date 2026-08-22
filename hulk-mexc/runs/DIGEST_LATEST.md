# Hulk DIGEST — 2026-08-22T00:55:38Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.99 | 7.38 | 0.5 | 0.12 | 6521662.54 | 4.02 | skipped_fast |
| XRPUSDT | IDLE | 2.11 | 8.72 | 2.52 | 0.14 | 147796970.48 | 1.39 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.7 | 0.07 | 942137.96 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.45 | 0.1 | 543302.05 | 15.11 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 7.42 | 0.9 | 0.14 | 650077.78 | 8.89 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.73 | 0.09 | 391234.05 | 11.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.46 | 0.02 | 544965.33 | 6.11 | skipped_fast |
| BIOUSDT | IDLE | 2.48 | 5.62 | 0.12 | 0.04 | 186675.92 | 15.3 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.02 | 79745.09 | 33.24 | skipped_fast |
| RIZEUSDT | IDLE | 2.26 | 9.82 | 3.95 | 0.12 | 60184.49 | 43.92 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.72 | 0.06 | 183956.37 | 20.61 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.58 | 3.24 | 0.2 | 159479.39 | 17.26 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.24 | 0.07 | 170543.85 | 3.02 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.22 | 1.21 | 0.0 | 3842.9 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 4.15 | 0.0 | 0.11 | 60945.71 | 14.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.02 | 9620.44 | 32.35 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 55001.17 | 16.45 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 18.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
