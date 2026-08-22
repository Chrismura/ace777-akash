# Hulk DIGEST — 2026-08-22T00:29:53Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.21 | 0.1 | 6377555.57 | 4.09 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.0 | 8.23 | 0.75 | 0.15 | 144167414.39 | 1.37 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.49 | 0.07 | 937378.34 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 11.25 | 2.4 | 0.12 | 533317.91 | 4.34 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 7.42 | 1.1 | 0.13 | 648550.96 | 8.01 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 0.85 | 0.08 | 384681.43 | 13.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.04 | 552764.86 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.89 | 0.02 | 185855.05 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79833.98 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.65 | 0.13 | 59812.45 | 45.1 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.06 | 189008.86 | 46.31 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.57 | 0.06 | 170480.8 | 6.06 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 4.91 | 0.5 | 0.22 | 157852.16 | 18.99 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9704.24 | 59.19 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 3.12 | 0.03 | 0.1 | 61060.21 | 11.96 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54684.14 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
