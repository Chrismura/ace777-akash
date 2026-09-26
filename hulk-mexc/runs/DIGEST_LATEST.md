# Hulk DIGEST — 2026-09-26T02:49:52Z

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
| XRPUSDT | IDLE | 1.1 | 2.08 | 0.86 | 0.02 | 110857159.83 | 2.55 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.69 | 0.11 | 0.0 | 310417071.01 | 0.37 | skipped_fast |
| BTCUSDT | IDLE | 0.31 | 0.6 | 0.09 | -0.0 | 666020882.93 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 3.66 | 1.97 | 0.08 | 1245229.21 | 5.42 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 7.09 | 1.48 | 0.17 | 913549.23 | 9.0 | skipped_fast |
| HBARUSDT | IDLE | 1.32 | 2.43 | 1.35 | 0.03 | 898619.67 | 1.05 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.49 | 1.99 | 0.05 | 461052.98 | 7.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.83 | 4.72 | 3.74 | 0.06 | 153123.17 | 14.32 | skipped_fast |
| KITEUSDT | IDLE | 1.97 | 5.13 | 0.39 | 0.09 | 79338.51 | 10.16 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 4.3 | 0.18 | 0.12 | 562262.85 | 6.97 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 2.1 | 1.52 | 0.06 | 245167.42 | 19.98 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 3.32 | 2.01 | 0.07 | 113151.26 | 6.13 | skipped_fast |
| REDUSDT | IDLE | 1.31 | 2.76 | 1.93 | 0.05 | 88472.44 | 15.13 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 1.5 | 0.07 | -0.01 | 184865.82 | 6.74 | skipped_fast |
| RIZEUSDT | IDLE | 0.15 | 2.06 | 0.18 | -0.06 | 88632.59 | 38.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.42 | 1.27 | 0.75 | -0.07 | 13220.64 | 55.82 | skipped_fast |
| TELUSDT | IDLE | 0.69 | 1.23 | 1.03 | 0.02 | 106039.42 | 48.96 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.11 | 1.03 | -0.01 | 53413.78 | 51.83 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.91 | 0.42 | 0.01 | 41129.95 | 48.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.21 | 0.36 | 0.36 | 0.02 | 3296.62 | 21.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
