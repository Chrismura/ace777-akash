# Hulk DIGEST — 2026-09-06T14:31:10Z

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
| XRPUSDT | IDLE | 0.78 | 1.37 | 1.27 | -0.0 | 25836743.8 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.19 | 0.96 | 0.01 | 242236961.99 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.31 | 0.55 | 0.48 | -0.0 | 403915743.74 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 8.0 | 7.17 | -0.01 | 404702.83 | 5.25 | skipped_fast |
| PYTHUSDT | IDLE | 1.97 | 3.5 | 2.9 | -0.0 | 473257.09 | 1.83 | skipped_fast |
| WUSDT | IDLE | 2.41 | 4.36 | 3.09 | 0.02 | 243594.58 | 11.79 | skipped_fast |
| ZBCNUSDT | IDLE | 1.85 | 3.32 | 2.55 | -0.02 | 197879.74 | 20.3 | skipped_fast |
| RIZEUSDT | IDLE | 1.94 | 10.66 | 9.27 | -0.06 | 81449.64 | 62.03 | skipped_fast |
| CCUSDT | IDLE | 1.07 | 1.91 | 1.53 | 0.01 | 319604.58 | 7.3 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.71 | 3.57 | -0.01 | 67789.39 | 19.01 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 3.5 | 3.22 | 0.02 | 63980.09 | 11.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.09 | 4.5 | 2.45 | 0.05 | 5954.28 | 10.29 | skipped_fast |
| BIOUSDT | IDLE | 1.66 | 2.9 | 2.82 | -0.03 | 90830.64 | 22.09 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.05 | 1.46 | 0.01 | 61115.01 | 7.91 | skipped_fast |
| HBARUSDT | IDLE | 0.68 | 1.19 | 1.16 | 0.0 | 398321.47 | 1.24 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 1.65 | 1.56 | -0.0 | 65265.06 | 23.47 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.17 | 1.15 | 0.02 | 38503.25 | 1.53 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.15 | 1.06 | -0.01 | 52735.19 | 7.18 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.89 | 0.53 | 0.02 | 41591.77 | 10.74 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 22.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
