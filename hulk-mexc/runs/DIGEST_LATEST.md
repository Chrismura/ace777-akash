# Hulk DIGEST — 2026-08-21T20:20:58Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 2.95 | 0.08 | 5497595.55 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 4.21 | 2.89 | 0.12 | 129175279.92 | 1.45 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.33 | 0.16 | 153451.17 | 17.99 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.9 | 0.12 | 478498.1 | 32.52 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 3.91 | 1.27 | 0.08 | 632434.22 | 7.44 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.23 | 1.94 | 0.06 | 802268.74 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.55 | 0.08 | 510433.76 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.1 | 3.92 | 1.9 | 0.06 | 367340.93 | 13.78 | skipped_fast |
| BIOUSDT | IDLE | 2.54 | 5.33 | 2.94 | 0.02 | 190073.28 | 3.16 | skipped_fast |
| EDELUSDT | IDLE | 2.73 | 4.77 | 4.55 | -0.05 | 80218.05 | 22.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.54 | 0.02 | 56220.77 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.68 | 0.1 | 61107.32 | 14.95 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2801.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.42 | 3.39 | 2.01 | 0.01 | 183685.93 | 32.41 | skipped_fast |
| QNTUSDT | IDLE | 1.42 | 2.65 | 1.28 | 0.04 | 59881.09 | 6.23 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.03 | 54473.89 | 16.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 23.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
