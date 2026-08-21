# Hulk DIGEST — 2026-08-21T20:25:38Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 3.05 | 0.08 | 5508218.07 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 4.21 | 2.8 | 0.12 | 129126773.21 | 2.9 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.88 | 0.17 | 153501.87 | 17.9 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.33 | 0.12 | 478388.24 | 10.97 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 3.91 | 1.28 | 0.08 | 632782.38 | 6.5 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.9 | 0.06 | 802089.63 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.58 | 0.08 | 509805.47 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.09 | 3.92 | 1.8 | 0.06 | 366622.91 | 19.05 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.76 | 0.02 | 189624.46 | 6.31 | skipped_fast |
| EDELUSDT | IDLE | 2.73 | 4.77 | 4.55 | -0.05 | 80366.31 | 22.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.51 | 0.01 | 56217.64 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.41 | 0.11 | 61009.5 | 13.96 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2801.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.75 | 0.01 | 183871.81 | 26.9 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 2.65 | 1.45 | 0.04 | 59945.62 | 39.05 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 54311.34 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
