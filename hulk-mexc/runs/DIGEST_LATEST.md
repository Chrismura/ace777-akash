# Hulk DIGEST — 2026-08-21T20:55:23Z

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
| PYTHUSDT | IDLE | 1.3 | 4.78 | 2.17 | 0.09 | 5565229.41 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.49 | 0.1 | 128396044.16 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.79 | 0.17 | 152997.9 | 10.57 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 10.86 | 6.24 | 0.11 | 479743.74 | 54.9 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.32 | 0.1 | 642449.87 | 4.6 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.23 | 1.73 | 0.06 | 808744.26 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.73 | 0.08 | 514849.2 | 6.19 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.92 | 0.91 | 0.07 | 368077.18 | 14.68 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.48 | 0.01 | 188064.04 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.93 | 5.73 | 4.98 | -0.06 | 82483.21 | 22.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.42 | 0.02 | 56226.47 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 26.89 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 4.0 | 2.1 | 0.11 | 61289.32 | 12.07 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 181241.78 | 37.56 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60234.57 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 167.13 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 53880.82 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
