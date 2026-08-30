# Hulk DIGEST — 2026-08-30T01:11:58Z

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
| XRPUSDT | IDLE | 0.46 | 0.82 | 0.68 | 0.01 | 16549249.52 | 1.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.48 | 2.1 | -0.05 | 840879.85 | 2.48 | skipped_fast |
| PYTHUSDT | IDLE | 1.27 | 2.24 | 1.97 | 0.01 | 311204.69 | 2.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 2.57 | 1.57 | -0.02 | 199713.76 | 11.59 | skipped_fast |
| RIZEUSDT | IDLE | 2.39 | 6.94 | 0.24 | -0.02 | 41368.29 | 58.87 | skipped_fast |
| TELUSDT | IDLE | 3.04 | 5.42 | 4.4 | -0.05 | 68526.81 | 23.89 | skipped_fast |
| CCUSDT | IDLE | 0.84 | 1.62 | 0.96 | 0.07 | 230582.58 | 10.16 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.12 | 2.57 | 0.0 | 67587.83 | 9.34 | skipped_fast |
| REDUSDT | IDLE | 1.28 | 2.46 | 0.71 | 0.02 | 76400.15 | 11.87 | skipped_fast |
| WUSDT | IDLE | 0.65 | 1.19 | 0.72 | 0.0 | 178316.65 | 5.48 | skipped_fast |
| BIOUSDT | IDLE | 0.69 | 1.32 | 0.36 | -0.01 | 67357.96 | 3.63 | skipped_fast |
| EDELUSDT | IDLE | 0.2 | 3.82 | 0.61 | 0.09 | 124298.37 | 17.64 | skipped_fast |
| RWAINCUSDT | IDLE | 0.71 | 1.25 | 1.17 | -0.04 | 1572.72 | 107.19 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 1.47 | 0.92 | 0.01 | 30277.37 | 4.89 | skipped_fast |
| HBARUSDT | IDLE | 0.25 | 0.45 | 0.28 | -0.0 | 135868.18 | 1.32 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.15 | 0.16 | 0.01 | 54095.89 | 24.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.45 | 0.89 | 0.0 | 0.01 | 1978.14 | 23.15 | skipped_fast |
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
