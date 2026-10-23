# Hulk DIGEST — 2026-10-23T08:45:20Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.56 | 1.06 | 0.34 | -0.0 | 26155028.84 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.54 | 1.03 | 0.27 | 0.0 | 233684184.19 | 0.17 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.6 | 0.21 | -0.0 | 355216807.81 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.06 | 3.77 | 2.39 | 0.0 | 698403.98 | 16.9 | skipped_fast |
| ZBCNUSDT | IDLE | 3.57 | 8.19 | 3.04 | 0.01 | 172569.14 | 16.04 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.33 | 14.95 | 7.2 | -0.08 | 45164.85 | 61.96 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.03 | 1.04 | -0.02 | 593291.6 | 2.74 | skipped_fast |
| EDELUSDT | IDLE | 1.11 | 2.21 | 1.57 | -0.06 | 417801.74 | 21.92 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 4.48 | 1.55 | 0.04 | 132121.09 | 13.13 | skipped_fast |
| QNTUSDT | IDLE | 1.24 | 2.23 | 1.65 | -0.04 | 456539.16 | 3.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.42 | 2.7 | 0.99 | 0.02 | 50431.49 | 5.55 | skipped_fast |
| CCUSDT | IDLE | 0.59 | 1.07 | 0.73 | -0.01 | 212746.32 | 4.85 | skipped_fast |
| HBARUSDT | IDLE | 1.34 | 2.39 | 1.99 | -0.01 | 299086.39 | 6.24 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 1.62 | 1.57 | -0.01 | 82794.36 | 8.54 | skipped_fast |
| BIOUSDT | IDLE | 0.59 | 1.09 | 0.58 | 0.01 | 60067.72 | 8.34 | skipped_fast |
| KITEUSDT | IDLE | 0.57 | 1.08 | 0.4 | 0.01 | 57635.54 | 19.17 | skipped_fast |
| LAUSDT | IDLE | 1.12 | 2.1 | 0.89 | 0.01 | 53602.22 | 21.68 | skipped_fast |
| WAXLUSDT | IDLE | 1.23 | 2.24 | 1.46 | -0.01 | 56758.0 | 66.67 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.51 | 0.7 | -0.0 | 52541.82 | 15.76 | skipped_fast |
| IOTAUSDT | IDLE | 0.7 | 1.3 | 0.64 | -0.0 | 64768.8 | 26.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.42 | 0.89 | 0.32 | -0.04 | 9649.59 | 20.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.63 | 0.51 | -0.01 | 38284.93 | 65.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
