# Hulk DIGEST — 2026-08-22T00:31:21Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.19 | 0.11 | 6387802.13 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.99 | 8.23 | 0.68 | 0.16 | 144613918.17 | 4.1 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.63 | 0.07 | 937471.51 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 11.25 | 2.4 | 0.12 | 538694.71 | 45.83 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 7.42 | 0.92 | 0.14 | 639642.17 | 4.44 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.07 | 0.08 | 385600.71 | 12.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.43 | 0.02 | 554620.77 | 9.25 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.77 | 0.02 | 185890.75 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.74 | -0.02 | 79740.56 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.63 | 0.13 | 59832.77 | 21.69 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.05 | 186408.37 | 36.04 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.28 | 0.06 | 170452.96 | 7.56 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 4.91 | 0.22 | 0.23 | 157819.76 | 17.34 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 3.12 | 0.31 | 0.1 | 61079.99 | 10.11 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9704.24 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54702.57 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
