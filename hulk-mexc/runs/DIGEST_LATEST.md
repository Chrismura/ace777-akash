# Hulk DIGEST — 2026-09-13T12:40:04Z

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
| ETHUSDT | IDLE | 1.2 | 2.15 | 1.72 | -0.02 | 236002805.39 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.03 | 1.82 | 1.62 | -0.02 | 14218884.72 | 2.24 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.88 | 0.54 | -0.01 | 306810397.58 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 14.26 | 11.02 | 0.08 | 203733.0 | 24.56 | skipped_fast |
| CCUSDT | IDLE | 2.3 | 4.14 | 3.08 | -0.03 | 300111.0 | 9.47 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 3.05 | 0.47 | 0.02 | 441203.44 | 1.83 | skipped_fast |
| WUSDT | IDLE | 1.62 | 2.92 | 2.11 | 0.01 | 245331.04 | 13.17 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 2.68 | 1.81 | -0.04 | 182735.92 | 1.13 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 4.18 | 3.09 | -0.05 | 79896.51 | 15.28 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 16.98 | 5.29 | 0.18 | 106619.86 | 96.03 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.06 | 2.97 | -0.06 | 7781.82 | 5.68 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.69 | 1.73 | 0.02 | 63637.87 | 11.93 | skipped_fast |
| BIOUSDT | IDLE | 1.2 | 2.14 | 1.67 | -0.02 | 69491.95 | 7.9 | skipped_fast |
| REDUSDT | IDLE | 0.96 | 1.8 | 0.84 | 0.02 | 56633.42 | 17.56 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 3.07 | 1.3 | -0.05 | 86262.33 | 37.71 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.57 | 0.87 | 0.0 | 156991.11 | 1.33 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 1.96 | 0.81 | -0.01 | 54914.22 | 29.83 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.26 | 0.51 | -0.01 | 36962.61 | 7.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.35 | 1.34 | -0.0 | 1225.97 | 28.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.35 | 0.08 | -0.0 | 32538.22 | 20.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
