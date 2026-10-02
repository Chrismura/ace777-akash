# Hulk DIGEST — 2026-10-02T15:43:46Z

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
| QNTUSDT | IDLE | 1.84 | 9.53 | 0.86 | -0.03 | 5743646.19 | 10.79 | skipped_fast |
| XRPUSDT | IDLE | 1.86 | 3.29 | 2.82 | 0.02 | 54103433.32 | 1.99 | skipped_fast |
| ETHUSDT | IDLE | 1.6 | 2.82 | 2.51 | 0.01 | 505664612.07 | 0.52 | skipped_fast |
| BTCUSDT | IDLE | 1.21 | 2.13 | 1.94 | 0.02 | 840109167.55 | 0.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 12.16 | 10.48 | -0.04 | 116825.77 | 15.56 | skipped_fast |
| PYTHUSDT | IDLE | 2.49 | 5.86 | 1.84 | 0.06 | 496058.09 | 11.34 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.04 | 11.05 | 7.73 | -0.01 | 280337.8 | 34.29 | skipped_fast |
| CCUSDT | IDLE | 2.36 | 4.28 | 2.9 | 0.02 | 502298.58 | 6.5 | skipped_fast |
| WUSDT | IDLE | 2.65 | 5.08 | 1.49 | 0.06 | 443587.02 | 15.68 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.06 | 6.69 | 5.35 | -0.03 | 287973.24 | 31.13 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.44 | 10.92 | 8.02 | -0.03 | 4453.94 | 93.42 | skipped_fast |
| HBARUSDT | IDLE | 1.75 | 3.09 | 2.74 | 0.01 | 684203.19 | 3.84 | skipped_fast |
| BIOUSDT | IDLE | 2.31 | 5.05 | 3.17 | 0.06 | 91305.43 | 6.36 | skipped_fast |
| KITEUSDT | IDLE | 2.26 | 4.17 | 2.3 | 0.0 | 90756.99 | 10.04 | skipped_fast |
| CHIPUSDT | IDLE | 1.81 | 4.37 | 2.05 | 0.08 | 85083.6 | 17.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.45 | 8.78 | 5.9 | -0.1 | 35236.48 | 171.15 | skipped_fast |
| TELUSDT | IDLE | 2.02 | 3.61 | 2.89 | -0.02 | 138378.03 | 33.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.77 | 2.24 | 1.84 | 0.11 | 7438.13 | 21.46 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.8 | 0.65 | 0.0 | 53913.44 | 14.45 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.57 | 0.31 | 0.02 | 38764.35 | 20.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
