# Hulk DIGEST — 2026-08-20T01:19:38Z

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
| XRPUSDT | IDLE | 1.95 | 6.45 | 2.21 | 0.11 | 43537307.69 | 2.7 | skipped_fast |
| PYTHUSDT | IDLE | 1.49 | 4.44 | 1.75 | 0.1 | 314814.12 | 2.38 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 4.08 | 1.99 | 0.1 | 364959.73 | 7.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 7.77 | 2.4 | 0.14 | 215649.46 | 21.71 | skipped_fast |
| WUSDT | IDLE | 1.67 | 3.85 | 1.77 | 0.07 | 260154.21 | 15.07 | skipped_fast |
| RIZEUSDT | IDLE | 2.28 | 6.87 | 0.46 | 0.05 | 49707.9 | 46.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.15 | 3.54 | 2.24 | 0.04 | 192593.68 | 3.57 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 8.62 | 1.1 | 0.2 | 83176.28 | 22.25 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.35 | 1.46 | 0.05 | 344672.41 | 1.41 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 6.19 | 1.53 | 0.08 | 98727.12 | 11.17 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 4.57 | 1.26 | 0.15 | 156042.94 | 7.07 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.23 | 1.04 | 0.05 | 58392.37 | 13.49 | skipped_fast |
| FLUIDUSDT | IDLE | 2.24 | 6.0 | 3.95 | 0.06 | 3465.16 | 37.53 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 2.88 | 0.22 | 0.05 | 16928.28 | 56.34 | skipped_fast |
| TELUSDT | IDLE | 1.26 | 6.05 | 1.21 | 0.12 | 187625.81 | 67.51 | skipped_fast |
| QAITUSDT | IDLE | 0.74 | 2.03 | 0.5 | 0.03 | 10647.2 | 61.42 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 2.01 | 0.66 | 0.05 | 38913.08 | 1.7 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.17 | 0.01 | 53929.6 | 8.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
