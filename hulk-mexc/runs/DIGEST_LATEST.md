# Hulk DIGEST — 2026-10-13T18:06:57Z

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
| WUSDT | IDLE | 2.05 | 15.52 | 11.79 | -0.23 | 4918504.82 | 13.39 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 7.99 | 6.12 | -0.07 | 2061465.62 | 3.82 | skipped_fast |
| XRPUSDT | IDLE | 0.85 | 1.59 | 0.8 | 0.0 | 37393046.67 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.3 | 0.68 | -0.0 | 238299547.81 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.03 | 0.61 | 0.01 | 393184215.9 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.22 | 4.56 | 0.92 | -0.08 | 1345890.99 | 7.67 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 4.35 | 1.83 | 0.05 | 611982.46 | 7.04 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 10.66 | 6.84 | -0.08 | 77135.89 | 60.12 | skipped_fast |
| EDELUSDT | IDLE | 2.38 | 5.03 | 1.88 | 0.03 | 285897.56 | 61.02 | skipped_fast |
| CHIPUSDT | IDLE | 2.23 | 4.82 | 3.49 | -0.04 | 111439.54 | 12.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 2.89 | 2.29 | -0.01 | 232736.55 | 16.69 | skipped_fast |
| RWAINCUSDT | IDLE | 2.47 | 4.82 | 0.76 | 0.04 | 29471.33 | 14.36 | skipped_fast |
| REDUSDT | IDLE | 1.65 | 3.6 | 0.0 | -0.01 | 147414.06 | 7.1 | skipped_fast |
| HBARUSDT | IDLE | 1.55 | 2.86 | 1.61 | -0.02 | 329369.92 | 7.99 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.85 | 0.86 | -0.03 | 71010.76 | 3.62 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 1.78 | 0.45 | 0.02 | 59637.4 | 10.19 | skipped_fast |
| TELUSDT | IDLE | 1.53 | 2.83 | 1.57 | 0.01 | 104936.93 | 39.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 2.02 | 0.6 | 0.03 | 26318.55 | 21.24 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.78 | 0.62 | -0.0 | 52627.32 | 7.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.6 | 1.06 | 0.87 | -0.02 | 37938.72 | 29.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
