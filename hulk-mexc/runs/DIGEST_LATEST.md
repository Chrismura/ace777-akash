# Hulk DIGEST — 2026-08-29T15:11:44Z

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
| XRPUSDT | IDLE | 0.92 | 1.75 | 0.56 | -0.02 | 28608805.43 | 2.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.76 | 0.89 | -0.12 | 1074780.7 | 2.44 | skipped_fast |
| PYTHUSDT | IDLE | 2.11 | 4.07 | 1.05 | 0.01 | 395173.39 | 2.08 | skipped_fast |
| KITEUSDT | IDLE | 2.93 | 10.27 | 3.64 | 0.07 | 71260.08 | 10.37 | skipped_fast |
| EDELUSDT | IDLE | 2.93 | 10.29 | 2.42 | -0.07 | 103167.27 | 92.42 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 3.9 | 0.0 | 0.03 | 208409.98 | 7.73 | skipped_fast |
| REDUSDT | IDLE | 2.15 | 5.92 | 5.45 | 0.02 | 77429.47 | 13.86 | skipped_fast |
| RIZEUSDT | IDLE | 2.57 | 5.39 | 1.73 | -0.02 | 26679.14 | 55.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.19 | 2.27 | 0.8 | -0.08 | 189040.31 | 17.88 | skipped_fast |
| WUSDT | IDLE | 0.93 | 1.82 | 0.2 | -0.03 | 205077.39 | 10.94 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.57 | 0.61 | -0.03 | 69587.09 | 7.24 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.55 | 0.32 | -0.02 | 352904.02 | 1.32 | skipped_fast |
| TELUSDT | IDLE | 0.85 | 1.56 | 0.91 | -0.03 | 74746.92 | 51.77 | skipped_fast |
| RWAINCUSDT | IDLE | 0.39 | 0.78 | 0.0 | -0.0 | 4407.74 | 111.3 | skipped_fast |
| QNTUSDT | IDLE | 0.53 | 1.05 | 0.08 | -0.01 | 32424.82 | 4.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 1.31 | 0.0 | -0.03 | 1829.9 | 21.44 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.5 | 0.41 | -0.03 | 54949.84 | 8.25 | skipped_fast |
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
