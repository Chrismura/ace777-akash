# Hulk DIGEST — 2026-08-18T20:44:48Z

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
| XRPUSDT | IDLE | 0.28 | 0.49 | 0.42 | -0.0 | 10604384.14 | 2.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 7.03 | 6.29 | -0.03 | 8989.49 | 11.98 | skipped_fast |
| CHIPUSDT | IDLE | 2.08 | 5.73 | 4.91 | -0.07 | 216535.08 | 7.59 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 6.77 | 5.58 | -0.04 | 34267.48 | 48.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 2.85 | 2.08 | -0.01 | 174539.01 | 2.6 | skipped_fast |
| CCUSDT | IDLE | 0.8 | 1.47 | 0.91 | -0.0 | 231711.45 | 11.05 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 1.67 | 1.28 | -0.01 | 175522.21 | 16.02 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 5.43 | 0.01 | 0.1 | 141069.73 | 1.04 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 1.76 | 1.4 | -0.0 | 64775.71 | 4.07 | skipped_fast |
| WUSDT | IDLE | 0.65 | 1.13 | 1.11 | -0.03 | 134619.72 | 11.14 | skipped_fast |
| EDELUSDT | IDLE | 0.92 | 2.71 | 1.58 | -0.03 | 74681.16 | 40.19 | skipped_fast |
| TELUSDT | IDLE | 1.78 | 3.54 | 1.5 | 0.03 | 103900.56 | 41.52 | skipped_fast |
| KITEUSDT | IDLE | 0.31 | 0.55 | 0.4 | -0.01 | 63948.56 | 15.26 | skipped_fast |
| QAITUSDT | IDLE | 0.34 | 4.5 | 3.41 | -0.18 | 18506.32 | 60.06 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.24 | 2.19 | -0.01 | 167.88 | 21.96 | skipped_fast |
| HBARUSDT | IDLE | 0.46 | 0.88 | 0.2 | 0.01 | 104985.1 | 1.51 | skipped_fast |
| QNTUSDT | IDLE | 0.74 | 1.36 | 0.85 | -0.02 | 34609.81 | 5.37 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.7 | 0.43 | -0.01 | 50559.41 | 17.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
