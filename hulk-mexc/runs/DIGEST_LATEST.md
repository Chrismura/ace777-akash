# Hulk DIGEST — 2026-10-12T23:50:31Z

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
| WUSDT | IDLE | 1.05 | 16.34 | 12.8 | -0.13 | 15242517.94 | 5.78 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 5.95 | 4.97 | 0.03 | 3478059.41 | 1.23 | skipped_fast |
| ETHUSDT | IDLE | 1.93 | 3.39 | 3.16 | -0.03 | 241098350.64 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.42 | 2.5 | 2.32 | -0.05 | 31401063.76 | 2.24 | skipped_fast |
| BTCUSDT | IDLE | 0.94 | 1.65 | 1.56 | -0.02 | 315684140.36 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 3.59 | 2.49 | -0.05 | 790952.03 | 5.3 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 2.92 | 2.42 | -0.05 | 401427.75 | 6.7 | skipped_fast |
| HBARUSDT | IDLE | 1.83 | 3.98 | 3.52 | -0.07 | 610688.92 | 5.75 | skipped_fast |
| KITEUSDT | IDLE | 2.54 | 4.5 | 3.84 | -0.04 | 65761.73 | 8.87 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 14.0 | 8.23 | -0.06 | 73394.88 | 88.7 | skipped_fast |
| BIOUSDT | IDLE | 2.04 | 4.82 | 4.42 | -0.09 | 75346.04 | 7.34 | skipped_fast |
| EDELUSDT | IDLE | 0.88 | 3.69 | 3.07 | -0.1 | 295011.38 | 2.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.23 | 1.56 | 0.01 | 264639.76 | 26.1 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 4.24 | 2.84 | 0.02 | 272776.66 | 14.19 | skipped_fast |
| CHIPUSDT | IDLE | 0.87 | 4.12 | 3.14 | -0.15 | 160733.42 | 12.06 | skipped_fast |
| RWAINCUSDT | IDLE | 1.01 | 2.85 | 0.44 | 0.02 | 33556.16 | 4.88 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 3.69 | 3.28 | -0.0 | 116595.62 | 52.74 | skipped_fast |
| FLUIDUSDT | IDLE | 2.08 | 3.83 | 2.26 | -0.02 | 15627.17 | 21.51 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.78 | 0.62 | -0.0 | 52871.56 | 15.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.57 | 1.06 | 0.56 | -0.01 | 41247.89 | 49.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
