# Hulk DIGEST — 2026-10-16T09:58:17Z

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
| WUSDT | IDLE | 2.07 | 5.0 | 4.43 | 0.01 | 1896052.23 | 15.5 | skipped_fast |
| PYTHUSDT | IDLE | 0.53 | 3.03 | 1.97 | 0.08 | 3849290.4 | 5.35 | skipped_fast |
| XRPUSDT | IDLE | 0.64 | 1.2 | 0.55 | 0.01 | 29856343.29 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.13 | 0.48 | 0.03 | 225657266.72 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.57 | 0.43 | 0.01 | 391959725.69 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.02 | 2.76 | 1.85 | 0.04 | 1167067.48 | 0.48 | skipped_fast |
| CCUSDT | IDLE | 2.62 | 4.6 | 4.28 | -0.01 | 438939.55 | 3.84 | skipped_fast |
| RWAINCUSDT | IDLE | 3.19 | 6.21 | 4.5 | 0.02 | 26257.2 | 15.05 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 8.35 | 5.34 | -0.02 | 64804.41 | 62.08 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 5.24 | 0.39 | -0.01 | 225474.04 | 13.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.03 | 5.34 | 3.5 | 0.12 | 190116.41 | 6.02 | skipped_fast |
| ZBCNUSDT | IDLE | 1.08 | 2.09 | 0.52 | 0.04 | 208712.92 | 11.98 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 2.52 | 0.44 | 0.04 | 69597.19 | 10.54 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 2.99 | 1.95 | -0.04 | 88208.5 | 15.5 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.11 | 0.46 | 0.05 | 68984.91 | 3.84 | skipped_fast |
| HBARUSDT | IDLE | 1.41 | 2.78 | 0.63 | 0.06 | 194722.87 | 5.79 | skipped_fast |
| TELUSDT | IDLE | 1.33 | 2.94 | 1.48 | 0.05 | 95213.81 | 44.59 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.07 | 1.48 | -0.01 | 8177.36 | 21.17 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.03 | 0.16 | 0.02 | 51732.81 | 7.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.33 | 0.14 | 0.01 | 39579.63 | 12.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
