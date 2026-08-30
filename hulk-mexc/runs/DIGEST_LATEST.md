# Hulk DIGEST — 2026-08-30T05:12:40Z

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
| XRPUSDT | IDLE | 0.46 | 0.86 | 0.36 | 0.0 | 16172553.24 | 2.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 5.18 | 1.94 | -0.05 | 824570.85 | 2.47 | skipped_fast |
| RIZEUSDT | IDLE | 2.97 | 12.31 | 3.0 | -0.04 | 44849.38 | 60.45 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 3.04 | 1.73 | 0.07 | 301120.51 | 7.56 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 1.88 | 1.04 | 0.01 | 317711.77 | 2.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 2.27 | 0.1 | -0.02 | 185640.0 | 11.45 | skipped_fast |
| WUSDT | IDLE | 1.03 | 1.97 | 0.57 | -0.0 | 192178.01 | 14.14 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.87 | 0.47 | 0.02 | 76826.43 | 9.89 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 1.39 | 0.94 | -0.01 | 68567.61 | 3.63 | skipped_fast |
| EDELUSDT | IDLE | 0.27 | 5.05 | 1.63 | 0.08 | 121419.01 | 17.44 | skipped_fast |
| KITEUSDT | IDLE | 0.7 | 1.77 | 1.63 | 0.01 | 69214.93 | 12.47 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.75 | 1.12 | -0.01 | 142248.14 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.35 | 0.29 | -0.03 | 72603.6 | 23.63 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.57 | 1.3 | 0.0 | 54349.47 | 16.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.61 | 1.24 | 0.01 | 1482.06 | 22.25 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.09 | 0.73 | -0.0 | 31652.34 | 6.5 | skipped_fast |
| RWAINCUSDT | IDLE | 0.16 | 0.28 | 0.28 | -0.04 | 1577.44 | 107.37 | skipped_fast |
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
