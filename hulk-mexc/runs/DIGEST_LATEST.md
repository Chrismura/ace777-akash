# Hulk DIGEST — 2026-08-21T20:22:24Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 2.93 | 0.09 | 5500796.1 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 4.21 | 2.69 | 0.12 | 129172798.47 | 1.45 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.03 | 0.16 | 153484.61 | 8.95 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.52 | 0.12 | 478550.62 | 1.5 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 3.91 | 1.27 | 0.08 | 632655.26 | 5.58 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.88 | 0.06 | 802262.35 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.34 | 0.09 | 510549.86 | 9.25 | skipped_fast |
| WUSDT | IDLE | 2.11 | 3.92 | 1.96 | 0.06 | 367551.18 | 12.72 | skipped_fast |
| BIOUSDT | IDLE | 2.54 | 5.33 | 2.85 | 0.02 | 190122.94 | 6.32 | skipped_fast |
| EDELUSDT | IDLE | 2.73 | 4.77 | 4.55 | -0.05 | 80268.05 | 22.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.65 | 0.01 | 56220.1 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 42.87 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.69 | 0.1 | 61080.48 | 12.11 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2801.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.42 | 3.39 | 1.96 | 0.01 | 183680.44 | 32.4 | skipped_fast |
| QNTUSDT | IDLE | 1.41 | 2.65 | 1.15 | 0.04 | 59903.56 | 7.77 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54459.53 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
