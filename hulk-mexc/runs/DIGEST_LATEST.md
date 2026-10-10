# Hulk DIGEST — 2026-10-10T13:50:33Z

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
| WUSDT | IDLE | 3.75 | 7.31 | 1.21 | 0.0 | 1051226.98 | 6.81 | skipped_fast |
| XRPUSDT | IDLE | 0.35 | 0.65 | 0.38 | 0.02 | 17767299.32 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.13 | 0.26 | 0.03 | 0.01 | 86197229.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.11 | 0.2 | 0.12 | 0.0 | 202768300.91 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.87 | 2.45 | 1.43 | -0.09 | 1093773.93 | 2.54 | skipped_fast |
| QNTUSDT | IDLE | 1.67 | 3.31 | 0.24 | 0.02 | 1175993.13 | 7.49 | skipped_fast |
| EDELUSDT | IDLE | 3.63 | 7.46 | 4.7 | 0.02 | 231281.81 | 2.59 | skipped_fast |
| KITEUSDT | IDLE | 2.55 | 6.59 | 2.0 | 0.05 | 75054.88 | 20.2 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 1.96 | 1.48 | -0.04 | 393526.74 | 5.83 | skipped_fast |
| ZBCNUSDT | IDLE | 0.58 | 1.08 | 0.49 | -0.01 | 227216.32 | 14.89 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.19 | 0.86 | 0.03 | 55063.72 | 14.62 | skipped_fast |
| CHIPUSDT | IDLE | 0.86 | 2.58 | 1.97 | 0.09 | 87568.89 | 13.41 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.76 | 0.31 | 0.03 | 78840.4 | 3.47 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.14 | 0.25 | 0.01 | 336123.86 | 4.31 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.56 | 0.65 | 0.04 | 50199.36 | 9.89 | skipped_fast |
| RWAINCUSDT | IDLE | 0.97 | 1.88 | 0.39 | -0.02 | 9630.91 | 58.51 | skipped_fast |
| TELUSDT | IDLE | 1.61 | 2.82 | 2.63 | -0.02 | 109295.08 | 49.66 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | -0.01 | 53574.09 | 23.61 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.67 | 0.2 | 0.0 | 39380.11 | 17.59 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 1.2 | 0.1 | 0.02 | 9778.7 | 21.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
