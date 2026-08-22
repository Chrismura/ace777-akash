# Hulk DIGEST — 2026-08-22T12:20:07Z

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
| PYTHUSDT | IDLE | 1.67 | 7.83 | 2.97 | 0.04 | 51608909.96 | 4.0 | skipped_fast |
| XRPUSDT | IDLE | 2.47 | 14.26 | 6.57 | 0.12 | 215426272.84 | 4.6 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 4.63 | 1.86 | 0.03 | 1260009.73 | 3.84 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 8.38 | 3.86 | 0.13 | 773537.81 | 9.3 | skipped_fast |
| WUSDT | IDLE | 1.53 | 6.27 | 3.08 | 0.02 | 578325.98 | 12.61 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 5.77 | 3.91 | -0.03 | 370879.29 | 8.73 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 0.83 | -0.1 | 612240.96 | 3.32 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.28 | 0.04 | 83218.38 | 4.4 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 3.89 | 2.54 | -0.02 | 78109.0 | 45.15 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 5.65 | 0.47 | -0.02 | 240935.63 | 6.33 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.77 | 0.03 | 153121.08 | 12.34 | skipped_fast |
| TELUSDT | IDLE | 2.18 | 5.61 | 4.09 | -0.03 | 164311.88 | 47.94 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10250.54 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 3.47 | 0.81 | 0.01 | 187904.7 | 1.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.34 | -0.05 | 48103.97 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 0.99 | 1.8 | 1.2 | 0.02 | 57707.84 | 16.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 19.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
