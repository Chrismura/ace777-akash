# Hulk DIGEST — 2026-10-27T03:38:12Z

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
| XRPUSDT | IDLE | 1.16 | 2.19 | 0.84 | 0.02 | 24348253.94 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.35 | 0.59 | 0.01 | 125455477.77 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.92 | 0.57 | 0.0 | 359090368.11 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.62 | 4.66 | 3.85 | -0.02 | 676931.68 | 2.76 | skipped_fast |
| QNTUSDT | IDLE | 0.52 | 2.21 | 1.01 | 0.07 | 1398083.94 | 2.95 | skipped_fast |
| WUSDT | IDLE | 1.57 | 3.06 | 1.86 | 0.05 | 644379.77 | 25.95 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 2.89 | 2.51 | -0.03 | 204992.81 | 9.23 | skipped_fast |
| REDUSDT | IDLE | 1.75 | 3.13 | 2.48 | 0.02 | 61485.66 | 8.93 | skipped_fast |
| EDELUSDT | IDLE | 1.21 | 2.22 | 1.35 | 0.02 | 193144.05 | 21.71 | skipped_fast |
| CHIPUSDT | IDLE | 0.48 | 3.36 | 1.0 | 0.18 | 319664.51 | 21.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.04 | 1.83 | 1.65 | -0.04 | 242837.58 | 32.01 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.19 | 1.16 | 0.01 | 56312.48 | 9.04 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 2.1 | 1.62 | 0.01 | 53292.39 | 11.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.52 | 2.7 | 2.23 | -0.02 | 43225.02 | 63.63 | skipped_fast |
| RWAINCUSDT | IDLE | 0.81 | 2.6 | 1.46 | -0.1 | 58613.19 | 6.43 | skipped_fast |
| LAUSDT | IDLE | 2.05 | 3.77 | 2.25 | 0.04 | 67706.59 | 25.75 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 1.92 | 1.33 | -0.0 | 207824.18 | 5.22 | skipped_fast |
| IOTAUSDT | IDLE | 1.61 | 2.89 | 2.23 | -0.0 | 90852.88 | 16.64 | skipped_fast |
| WAXLUSDT | IDLE | 2.01 | 3.68 | 2.22 | -0.01 | 53541.44 | 44.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.14 | 2.28 | 0.04 | 0.05 | 2115.4 | 21.53 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.96 | 0.32 | -0.0 | 54251.38 | 23.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.8 | 0.23 | -0.0 | 41377.38 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
