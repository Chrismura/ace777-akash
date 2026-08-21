# Hulk DIGEST — 2026-08-21T05:29:28Z

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
| PYTHUSDT | IDLE | 2.23 | 5.91 | 0.28 | 0.1 | 2085658.15 | 19.26 | skipped_fast |
| XRPUSDT | IDLE | 0.92 | 4.96 | 0.86 | 0.18 | 117111131.34 | 0.76 | skipped_fast |
| CHIPUSDT | IDLE | 2.13 | 12.78 | 4.38 | 0.12 | 439650.96 | 6.04 | skipped_fast |
| CCUSDT | IDLE | 2.14 | 4.16 | 0.81 | 0.01 | 485812.96 | 12.82 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 5.22 | 1.8 | 0.03 | 76139.31 | 32.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.56 | 4.91 | 1.31 | 0.06 | 300943.68 | 34.27 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 5.07 | 1.82 | 0.09 | 225863.28 | 3.19 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 2.85 | 0.69 | 0.05 | 491526.52 | 1.33 | skipped_fast |
| WUSDT | IDLE | 1.03 | 1.88 | 1.14 | 0.06 | 269832.63 | 13.28 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 4.77 | 4.42 | -0.07 | 158371.28 | 13.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.77 | 1.09 | 0.03 | 8691.43 | 71.06 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 1.57 | 0.64 | 0.04 | 61659.64 | 13.03 | skipped_fast |
| QAITUSDT | IDLE | 0.79 | 2.08 | 0.0 | -0.02 | 6718.75 | 67.45 | skipped_fast |
| TELUSDT | IDLE | 0.59 | 2.92 | 1.87 | 0.14 | 200026.99 | 27.26 | skipped_fast |
| RIZEUSDT | IDLE | 0.73 | 3.58 | 0.98 | -0.09 | 38730.26 | 122.97 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 1.58 | 0.88 | 0.05 | 65620.87 | 8.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.26 | 1.22 | 0.08 | 2610.59 | 21.55 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.94 | 0.68 | 0.01 | 54390.96 | 17.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
