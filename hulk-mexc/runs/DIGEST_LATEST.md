# Hulk DIGEST — 2026-08-21T20:37:01Z

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
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.44 | 0.08 | 5537072.35 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.15 | 0.11 | 128944068.99 | 2.18 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.77 | 0.17 | 153995.4 | 17.84 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 10.86 | 5.25 | 0.12 | 478490.02 | 18.43 | skipped_fast |
| CCUSDT | IDLE | 1.4 | 3.91 | 0.14 | 0.09 | 637274.15 | 10.11 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.85 | 0.05 | 809484.67 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.34 | 0.08 | 514025.9 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.63 | 0.06 | 368320.71 | 8.45 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.73 | 0.02 | 189032.72 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.83 | 5.01 | 4.77 | -0.06 | 81408.81 | 22.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10934.71 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.62 | 0.02 | 56283.26 | 47.09 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.53 | 0.1 | 60726.62 | 12.11 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 183207.78 | 21.46 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.69 | 0.04 | 59971.99 | 3.13 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53838.94 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 20.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
