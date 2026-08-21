# Hulk DIGEST — 2026-08-21T20:30:20Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.7 | 0.08 | 5520903.54 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.25 | 0.11 | 129113878.05 | 2.91 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.99 | 25.8 | 11.75 | 0.18 | 153694.68 | 20.88 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.65 | 0.11 | 478140.25 | 18.01 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 3.91 | 1.15 | 0.08 | 632357.85 | 6.5 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.23 | 1.94 | 0.06 | 796399.11 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.34 | 0.08 | 509755.03 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.1 | 3.92 | 1.82 | 0.06 | 365483.19 | 10.59 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.39 | 0.02 | 189791.37 | 3.14 | skipped_fast |
| EDELUSDT | IDLE | 2.79 | 4.89 | 4.66 | -0.05 | 80341.3 | 22.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.56 | 0.02 | 56215.5 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10934.71 | 32.14 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.48 | 0.1 | 61001.49 | 12.11 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.69 | 0.01 | 183830.92 | 16.13 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.77 | 0.04 | 59931.22 | 3.13 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 54140.79 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
