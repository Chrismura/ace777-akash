# Hulk DIGEST — 2026-09-01T17:25:44Z

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
| XRPUSDT | IDLE | 1.02 | 1.89 | 1.0 | -0.0 | 30815314.72 | 2.92 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.59 | 0.96 | -0.01 | 291642159.75 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.41 | 1.09 | -0.01 | 519133672.21 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 3.44 | 14.28 | 4.86 | 0.1 | 500926.33 | 4.71 | skipped_fast |
| ZBCNUSDT | IDLE | 3.66 | 6.8 | 3.44 | 0.03 | 217088.95 | 19.15 | skipped_fast |
| PYTHUSDT | IDLE | 1.55 | 2.96 | 0.88 | 0.05 | 630789.59 | 3.94 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 4.86 | 3.5 | -0.03 | 417482.92 | 9.59 | skipped_fast |
| WUSDT | IDLE | 2.23 | 4.35 | 0.72 | 0.07 | 284077.21 | 13.41 | skipped_fast |
| REDUSDT | IDLE | 2.37 | 5.3 | 1.41 | 0.06 | 74887.8 | 14.25 | skipped_fast |
| RIZEUSDT | IDLE | 2.33 | 5.19 | 4.2 | -0.06 | 43536.97 | 25.48 | skipped_fast |
| KITEUSDT | IDLE | 2.06 | 3.97 | 1.04 | 0.04 | 70104.81 | 10.56 | skipped_fast |
| BIOUSDT | IDLE | 1.27 | 2.26 | 1.83 | -0.02 | 67125.6 | 3.88 | skipped_fast |
| EDELUSDT | IDLE | 0.75 | 5.12 | 3.42 | -0.06 | 172549.87 | 53.0 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 2.05 | 1.34 | 0.02 | 230005.45 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.92 | 3.79 | 0.39 | 0.04 | 43191.54 | 4.69 | skipped_fast |
| RWAINCUSDT | IDLE | 1.51 | 2.86 | 1.1 | -0.03 | 6195.38 | 116.28 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 1.89 | 1.56 | 0.01 | 97194.01 | 5.87 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.62 | 1.44 | -0.02 | 60692.02 | 7.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.13 | 0.85 | -0.01 | 32645.08 | 47.65 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 266.03 | 21.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
