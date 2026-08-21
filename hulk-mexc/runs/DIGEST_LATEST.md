# Hulk DIGEST — 2026-08-21T20:57:31Z

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
| PYTHUSDT | IDLE | 1.29 | 4.78 | 2.05 | 0.09 | 5568481.66 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.44 | 0.11 | 128344828.07 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.7 | 0.17 | 152963.84 | 23.56 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 10.86 | 7.04 | 0.1 | 479506.97 | 26.92 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.39 | 0.1 | 642537.42 | 7.37 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.23 | 1.75 | 0.06 | 808883.2 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.73 | 0.08 | 515086.97 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.92 | 0.97 | 0.07 | 368093.85 | 13.65 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.7 | 0.01 | 188015.61 | 3.14 | skipped_fast |
| EDELUSDT | IDLE | 2.89 | 5.73 | 4.33 | -0.06 | 82463.23 | 22.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.47 | 0.03 | 56227.54 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 37.52 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 4.0 | 2.21 | 0.11 | 61356.09 | 9.29 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.43 | 0.01 | 181259.76 | 32.21 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.03 | 60171.44 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 198.65 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 53882.97 | 33.25 | skipped_fast |
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
