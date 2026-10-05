# Hulk DIGEST — 2026-10-05T19:37:37Z

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
| QNTUSDT | IDLE | 1.83 | 4.06 | 3.03 | -0.02 | 2685027.48 | 6.3 | skipped_fast |
| XRPUSDT | IDLE | 1.3 | 2.38 | 1.42 | -0.0 | 38495450.89 | 0.67 | skipped_fast |
| BTCUSDT | IDLE | 1.08 | 1.99 | 1.14 | 0.0 | 705515628.76 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.98 | 1.85 | 0.74 | 0.0 | 399020085.96 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.8 | 5.23 | 2.5 | -0.01 | 662287.95 | 9.05 | skipped_fast |
| RIZEUSDT | IDLE | 2.46 | 30.69 | 13.63 | 0.32 | 69534.32 | 61.16 | skipped_fast |
| WUSDT | IDLE | 2.67 | 5.15 | 1.21 | 0.0 | 410071.59 | 8.96 | skipped_fast |
| EDELUSDT | IDLE | 2.9 | 5.59 | 1.34 | 0.04 | 311820.4 | 11.95 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 3.13 | 0.0 | -0.01 | 420860.03 | 5.52 | skipped_fast |
| BIOUSDT | IDLE | 2.77 | 5.92 | 0.64 | 0.06 | 90739.86 | 12.29 | skipped_fast |
| RWAINCUSDT | IDLE | 3.03 | 7.42 | 3.65 | -0.02 | 18783.12 | 66.39 | skipped_fast |
| CHIPUSDT | IDLE | 2.08 | 4.15 | 0.0 | 0.03 | 141214.4 | 11.95 | skipped_fast |
| HBARUSDT | IDLE | 1.5 | 2.81 | 1.32 | -0.02 | 471832.72 | 3.93 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.91 | 0.95 | -0.01 | 88439.69 | 6.45 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 2.98 | 1.18 | -0.05 | 64244.0 | 9.26 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 1.52 | 0.35 | 0.01 | 262773.34 | 14.91 | skipped_fast |
| TELUSDT | IDLE | 2.03 | 3.66 | 2.67 | 0.01 | 143482.42 | 25.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.04 | 7.23 | 1.74 | 0.23 | 63602.55 | 21.38 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.44 | 0.22 | -0.0 | 51631.01 | 14.68 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.65 | 0.09 | -0.0 | 41074.55 | 47.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
