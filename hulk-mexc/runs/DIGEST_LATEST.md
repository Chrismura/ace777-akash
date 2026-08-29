# Hulk DIGEST — 2026-08-29T23:07:15Z

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
| XRPUSDT | IDLE | 0.45 | 0.83 | 0.48 | 0.01 | 16435460.19 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.78 | 5.18 | 3.83 | -0.01 | 889785.37 | 7.45 | skipped_fast |
| ZBCNUSDT | IDLE | 2.81 | 5.15 | 3.13 | -0.02 | 199073.45 | 11.47 | skipped_fast |
| RIZEUSDT | IDLE | 3.19 | 8.97 | 2.24 | -0.03 | 41565.73 | 59.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 2.78 | 1.71 | 0.02 | 325370.07 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.16 | 2.23 | 0.81 | 0.06 | 228201.63 | 5.08 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.61 | 0.72 | 0.02 | 75474.39 | 11.87 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.19 | 1.95 | 0.02 | 68423.21 | 8.51 | skipped_fast |
| TELUSDT | IDLE | 2.51 | 4.4 | 4.1 | -0.03 | 70352.55 | 29.72 | skipped_fast |
| WUSDT | IDLE | 0.56 | 1.02 | 0.66 | -0.0 | 175865.34 | 13.13 | skipped_fast |
| EDELUSDT | IDLE | 0.16 | 3.0 | 0.88 | 0.09 | 124882.69 | 17.78 | skipped_fast |
| BIOUSDT | IDLE | 0.45 | 0.84 | 0.36 | -0.01 | 66546.91 | 3.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.32 | 2.21 | -0.03 | 1574.56 | 112.87 | skipped_fast |
| QNTUSDT | IDLE | 0.84 | 1.56 | 0.86 | 0.01 | 29848.69 | 1.63 | skipped_fast |
| HBARUSDT | IDLE | 0.29 | 0.54 | 0.22 | -0.0 | 148025.78 | 1.32 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.33 | 0.01 | 54226.9 | 16.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.06 | 0.11 | 0.11 | -0.0 | 1915.06 | 21.32 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
