# Hulk DIGEST — 2026-08-21T22:40:46Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.35 | 0.11 | 5840209.47 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.59 | 5.94 | 0.21 | 0.14 | 134983070.57 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 7.03 | 0.17 | 0.14 | 660429.39 | 8.86 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.68 | 0.08 | 871658.88 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.51 | 5.69 | 0.03 | 0.09 | 371003.89 | 14.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.54 | 0.05 | 533610.38 | 3.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.73 | 7.43 | 0.1 | 0.12 | 506647.39 | 55.57 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.11 | 0.02 | 188134.84 | 6.22 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.06 | 0.18 | 156146.98 | 18.61 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.33 | -0.03 | 82580.37 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10279.27 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.05 | 186867.91 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.34 | 4.38 | 1.94 | -0.02 | 3835.98 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 1.0 | 0.11 | 61422.57 | 11.05 | skipped_fast |
| QNTUSDT | IDLE | 2.11 | 4.21 | 0.03 | 0.06 | 80776.62 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.83 | 0.05 | 56387.67 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.16 | 0.03 | 54145.15 | 16.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 12.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
