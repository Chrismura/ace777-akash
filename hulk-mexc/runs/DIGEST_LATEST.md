# Hulk DIGEST — 2026-08-21T20:54:40Z

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
| PYTHUSDT | IDLE | 1.3 | 4.78 | 2.17 | 0.09 | 5564127.26 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.45 | 0.1 | 128412357.92 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.81 | 0.17 | 153009.0 | 18.7 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 10.86 | 6.37 | 0.12 | 478965.15 | 71.81 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.39 | 0.09 | 643657.2 | 4.61 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.23 | 1.72 | 0.06 | 808749.23 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.64 | 0.08 | 514497.48 | 6.19 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.92 | 0.87 | 0.07 | 368115.69 | 13.63 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.52 | 0.01 | 188032.7 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.92 | 5.73 | 4.88 | -0.06 | 82433.19 | 56.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.42 | 0.02 | 56220.07 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 26.89 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 4.0 | 2.1 | 0.11 | 61249.85 | 12.07 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.43 | 0.01 | 181213.96 | 48.32 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60224.37 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 206.51 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53898.43 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
