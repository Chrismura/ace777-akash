# Hulk DIGEST — 2026-08-19T10:10:59Z

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
| XRPUSDT | IDLE | 0.55 | 1.01 | 0.54 | 0.01 | 10413644.02 | 1.99 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.42 | 1.22 | 0.04 | 64986.5 | 3.99 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 3.42 | 2.56 | -0.14 | 145373.44 | 13.74 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 2.04 | 1.77 | -0.11 | 165036.93 | 3.92 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.19 | 1.24 | -0.0 | 64862.73 | 16.55 | skipped_fast |
| PYTHUSDT | IDLE | 0.61 | 1.06 | 1.03 | 0.02 | 163566.68 | 2.59 | skipped_fast |
| CCUSDT | IDLE | 0.46 | 0.91 | 0.07 | -0.01 | 213816.87 | 7.74 | skipped_fast |
| ZBCNUSDT | IDLE | 0.78 | 1.52 | 0.22 | 0.01 | 154800.46 | 20.15 | skipped_fast |
| WUSDT | IDLE | 0.88 | 1.66 | 0.64 | -0.01 | 102476.93 | 8.67 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.86 | 1.41 | -0.05 | 28695.51 | 51.39 | skipped_fast |
| RWAINCUSDT | IDLE | 0.76 | 1.49 | 0.18 | -0.01 | 10114.35 | 17.74 | skipped_fast |
| QAITUSDT | IDLE | 0.75 | 4.96 | 0.85 | -0.14 | 12060.33 | 66.45 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.31 | 1.86 | -0.04 | 59316.32 | 134.23 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.91 | 0.69 | 0.03 | 132135.14 | 1.48 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.42 | 0.95 | 0.01 | 38475.98 | 3.54 | skipped_fast |
| TELUSDT | IDLE | 0.64 | 1.25 | 0.14 | 0.04 | 86971.27 | 34.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.66 | 0.0 | -0.01 | 1163.31 | 20.32 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.06 | 0.44 | -0.01 | 52493.26 | 17.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
