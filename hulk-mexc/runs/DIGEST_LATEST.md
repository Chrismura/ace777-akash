# Hulk DIGEST — 2026-08-22T15:22:46Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.69 | 0.04 | 51484660.78 | 1.98 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 5.85 | 0.02 | 214838476.05 | 1.39 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.92 | 0.1 | 798819.07 | 6.0 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 2.96 | 2.81 | -0.02 | 1167462.58 | 5.26 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.72 | -0.1 | 613928.9 | 6.83 | skipped_fast |
| WUSDT | IDLE | 0.8 | 3.17 | 2.19 | -0.02 | 555556.78 | 11.8 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 6.37 | 2.48 | 0.02 | 85167.27 | 19.79 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 3.49 | 2.8 | -0.07 | 326896.88 | 37.3 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.26 | -0.07 | 221519.08 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.52 | 2.23 | -0.05 | 79077.41 | 22.83 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.62 | 5.17 | -0.05 | 150600.01 | 20.32 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.44 | 0.03 | 46049.0 | 23.62 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 2.69 | 2.62 | -0.02 | 188382.18 | 12.67 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9873.12 | 53.68 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 2.75 | 1.42 | -0.0 | 139914.86 | 42.62 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.77 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.57 | 0.02 | 57256.28 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
