# Hulk DIGEST — 2026-09-15T06:34:57Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.23 | 2.19 | 1.85 | 0.02 | 75417455.5 | 1.42 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 49.04 | 19.51 | 0.27 | 454394.12 | 22.22 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.66 | 1.26 | -0.01 | 461500232.39 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 0.97 | 0.84 | 0.0 | 518355662.77 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 40.02 | 18.85 | -0.17 | 51812.61 | 30.47 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 20.56 | 16.88 | 0.01 | 169486.71 | 16.31 | skipped_fast |
| PYTHUSDT | IDLE | 2.44 | 4.32 | 3.73 | -0.04 | 314109.36 | 1.82 | skipped_fast |
| WUSDT | IDLE | 2.02 | 3.54 | 3.29 | -0.04 | 169291.47 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 2.52 | 4.47 | 3.86 | -0.04 | 67047.61 | 19.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.51 | 1.68 | 0.01 | 197527.18 | 13.91 | skipped_fast |
| CCUSDT | IDLE | 0.77 | 1.36 | 1.17 | -0.01 | 322359.42 | 7.34 | skipped_fast |
| HBARUSDT | IDLE | 1.55 | 2.74 | 2.39 | 0.01 | 384374.68 | 1.3 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.89 | 1.12 | -0.0 | 97172.48 | 7.82 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.13 | 0.08 | -0.0 | 63133.17 | 10.26 | skipped_fast |
| TELUSDT | IDLE | 1.82 | 4.08 | 3.74 | 0.01 | 102033.37 | 56.41 | skipped_fast |
| RWAINCUSDT | IDLE | 0.62 | 1.11 | 0.82 | -0.0 | 4936.12 | 22.17 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 2.13 | 1.97 | -0.0 | 46502.91 | 9.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.47 | 2.57 | 2.41 | -0.0 | 1994.34 | 21.18 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.45 | -0.01 | 53874.62 | 14.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.55 | 0.45 | 0.01 | 34609.0 | 33.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
