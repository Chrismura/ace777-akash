# Hulk DIGEST — 2026-08-21T20:11:56Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.26 | 0.08 | 5476718.05 | 4.23 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.35 | 0.11 | 129063352.85 | 2.91 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.21 | 0.17 | 154019.8 | 19.57 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 10.86 | 6.55 | 0.11 | 477883.21 | 25.27 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.66 | 0.07 | 632493.15 | 8.4 | skipped_fast |
| HBARUSDT | IDLE | 1.76 | 3.23 | 2.41 | 0.05 | 795734.94 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.46 | 0.08 | 513002.45 | 6.18 | skipped_fast |
| WUSDT | IDLE | 2.14 | 3.92 | 2.34 | 0.05 | 366983.49 | 9.58 | skipped_fast |
| BIOUSDT | IDLE | 2.58 | 5.33 | 3.44 | 0.0 | 189882.18 | 3.18 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.41 | 4.23 | -0.05 | 80210.15 | 11.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.54 | 0.02 | 56222.1 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.04 | 11178.26 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.79 | 0.1 | 61333.92 | 14.01 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.0 | 2817.74 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 3.39 | 2.17 | 0.01 | 183526.17 | 48.69 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.65 | 1.51 | 0.04 | 59890.44 | 6.25 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.9 | 0.04 | 54395.53 | 8.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
