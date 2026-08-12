# Hulk DIGEST — 2026-08-12T19:28:19Z

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
| XRPUSDT | IDLE | 0.54 | 0.95 | 0.85 | -0.0 | 15809040.38 | 1.98 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 31.59 | 17.33 | 0.1 | 46001.87 | 38.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.92 | 6.56 | 4.92 | 0.04 | 104897.34 | 8.69 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.5 | 2.36 | -0.05 | 313622.85 | 2.49 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 5.79 | 2.49 | 0.05 | 63235.69 | 33.9 | skipped_fast |
| CCUSDT | IDLE | 1.55 | 2.83 | 1.81 | -0.02 | 225243.6 | 6.07 | skipped_fast |
| WUSDT | IDLE | 1.36 | 2.4 | 2.2 | -0.02 | 177363.0 | 16.04 | skipped_fast |
| KITEUSDT | IDLE | 1.78 | 3.18 | 2.49 | -0.04 | 60370.27 | 12.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 2.22 | 1.95 | -0.03 | 193726.84 | 25.39 | skipped_fast |
| REDUSDT | IDLE | 1.5 | 2.62 | 2.48 | -0.01 | 60136.63 | 17.64 | skipped_fast |
| RWAINCUSDT | IDLE | 2.12 | 4.03 | 1.36 | -0.01 | 1699.97 | 84.7 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 1.9 | 1.74 | -0.03 | 63250.76 | 4.12 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 2.77 | 2.2 | 0.02 | 61445.57 | 6.86 | skipped_fast |
| QAITUSDT | IDLE | 0.71 | 2.54 | 2.48 | -0.04 | 4592.19 | 60.7 | skipped_fast |
| TELUSDT | IDLE | 1.36 | 2.5 | 1.5 | 0.04 | 105486.72 | 44.52 | skipped_fast |
| HBARUSDT | IDLE | 0.49 | 0.87 | 0.68 | -0.01 | 77872.19 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.25 | 0.41 | 0.02 | 52208.22 | 16.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.12 | 1.03 | -0.02 | 542.31 | 23.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
