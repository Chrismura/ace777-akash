# Hulk DIGEST — 2026-08-16T11:04:46Z

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
| XRPUSDT | IDLE | 0.28 | 0.54 | 0.19 | -0.0 | 4917848.78 | 1.0 | skipped_fast |
| QAITUSDT | IDLE | 3.27 | 10.06 | 3.54 | -0.06 | 1447.01 | 58.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.82 | 13.01 | 0.65 | 0.28 | 191920.57 | 36.2 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 2.34 | 2.24 | 0.0 | 309488.04 | 8.41 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 3.85 | 1.46 | -0.01 | 67562.25 | 13.41 | skipped_fast |
| WUSDT | IDLE | 1.26 | 2.52 | 0.02 | 0.01 | 112936.02 | 12.95 | skipped_fast |
| ZBCNUSDT | IDLE | 0.74 | 1.35 | 0.87 | -0.01 | 222308.39 | 18.61 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.68 | 0.08 | -0.0 | 67822.67 | 8.07 | skipped_fast |
| KITEUSDT | IDLE | 0.67 | 1.25 | 0.65 | -0.02 | 57858.52 | 14.84 | skipped_fast |
| PYTHUSDT | IDLE | 0.43 | 0.84 | 0.2 | -0.01 | 90290.75 | 2.54 | skipped_fast |
| REDUSDT | IDLE | 0.27 | 2.21 | 1.95 | 0.01 | 91427.46 | 17.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 2.06 | 0.44 | -0.03 | 38509.33 | 61.61 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.91 | 1.05 | 0.09 | 8535.95 | 16.76 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.15 | 1.36 | -0.02 | 94777.85 | 41.29 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.74 | 0.0 | 0.04 | 122.34 | 19.09 | skipped_fast |
| QNTUSDT | IDLE | 0.59 | 1.14 | 0.23 | -0.02 | 32024.82 | 5.22 | skipped_fast |
| HBARUSDT | IDLE | 0.12 | 0.22 | 0.12 | -0.01 | 75648.96 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.53 | 0.17 | -0.0 | 52341.41 | 8.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
