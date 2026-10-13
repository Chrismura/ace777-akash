# Hulk DIGEST — 2026-10-13T16:04:02Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 17.52 | 13.19 | -0.29 | 5692095.04 | 16.97 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.81 | 8.67 | 7.4 | -0.11 | 2299701.37 | 2.56 | skipped_fast |
| XRPUSDT | IDLE | 1.21 | 2.35 | 0.46 | -0.0 | 38771837.79 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.57 | 0.21 | -0.0 | 236522936.58 | 0.28 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.85 | 0.32 | 0.01 | 381804671.08 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 8.77 | 6.17 | -0.1 | 1273460.72 | 5.36 | skipped_fast |
| CCUSDT | IDLE | 2.43 | 7.7 | 1.91 | 0.05 | 597455.35 | 16.32 | skipped_fast |
| EDELUSDT | IDLE | 3.56 | 7.44 | 3.28 | 0.03 | 324760.74 | 23.53 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.31 | 1.45 | -0.01 | 241178.32 | 20.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.99 | 4.31 | 3.08 | -0.03 | 114519.73 | 17.44 | skipped_fast |
| HBARUSDT | IDLE | 1.97 | 3.65 | 1.97 | -0.04 | 361776.55 | 5.73 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.7 | 2.56 | -0.02 | 31406.34 | 14.84 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 2.91 | 1.49 | -0.03 | 171276.01 | 14.5 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.95 | 9.14 | 8.38 | -0.06 | 63926.05 | 198.6 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 3.0 | 1.29 | -0.04 | 74415.46 | 7.28 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.34 | 0.19 | 0.01 | 61148.98 | 11.73 | skipped_fast |
| FLUIDUSDT | IDLE | 1.76 | 3.47 | 3.35 | 0.01 | 20183.9 | 21.46 | skipped_fast |
| TELUSDT | IDLE | 1.57 | 2.95 | 1.29 | -0.0 | 107409.23 | 34.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.59 | 1.08 | 0.69 | -0.02 | 38093.69 | 6.97 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.46 | 0.38 | -0.0 | 52222.68 | 7.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
