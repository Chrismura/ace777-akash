# Hulk DIGEST — 2026-08-21T21:31:05Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.8 | 0.1 | 5633807.32 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.12 | 3.73 | 1.36 | 0.11 | 129150415.55 | 2.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 4.03 | 0.05 | 517509.28 | 3.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.29 | 0.1 | 486036.75 | 35.38 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.17 | 0.06 | 0.1 | 645309.67 | 9.18 | skipped_fast |
| HBARUSDT | IDLE | 1.56 | 3.04 | 0.49 | 0.07 | 814939.3 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.83 | 0.44 | 0.06 | 367568.06 | 14.61 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.93 | 0.02 | 186868.72 | 6.26 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.3 | 0.17 | 153981.39 | 21.3 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.59 | 0.03 | 10203.58 | 21.52 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.42 | 0.02 | 56018.01 | 45.77 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.12 | 1.87 | -0.05 | 83316.6 | 33.65 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.48 | 0.12 | 61072.48 | 9.22 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 131.66 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 4.81 | 0.42 | 0.02 | 178655.03 | 57.61 | skipped_fast |
| QNTUSDT | IDLE | 1.41 | 2.65 | 1.12 | 0.04 | 63173.33 | 15.54 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.49 | 0.03 | 53842.32 | 8.27 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 40.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
