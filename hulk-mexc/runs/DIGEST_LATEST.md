# Hulk DIGEST — 2026-08-31T18:18:40Z

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
| XRPUSDT | IDLE | 1.08 | 2.16 | 0.02 | -0.02 | 39775766.94 | 2.16 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.73 | 0.05 | -0.01 | 422737663.75 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.7 | 0.03 | 0.0 | 599308354.42 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 4.65 | 3.52 | -0.03 | 475738.91 | 2.58 | skipped_fast |
| PYTHUSDT | IDLE | 1.7 | 4.38 | 0.0 | -0.01 | 446650.7 | 2.06 | skipped_fast |
| RIZEUSDT | IDLE | 3.21 | 5.78 | 4.21 | -0.02 | 40267.63 | 64.08 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.37 | 1.19 | -0.0 | 258219.05 | 10.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 2.85 | 0.27 | -0.0 | 204838.23 | 12.54 | skipped_fast |
| EDELUSDT | IDLE | 0.99 | 5.9 | 4.7 | -0.0 | 128364.51 | 16.68 | skipped_fast |
| WUSDT | IDLE | 0.89 | 1.64 | 0.96 | -0.03 | 210772.26 | 2.19 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 2.56 | 1.56 | -0.06 | 99140.87 | 9.29 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.23 | 0.49 | -0.04 | 77060.78 | 3.78 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.24 | 1.53 | -0.03 | 66164.2 | 12.25 | skipped_fast |
| RWAUSDT | IDLE | 2.63 | 6.31 | 1.26 | 0.07 | 57917.2 | 30.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.37 | 2.55 | 1.24 | -0.04 | 2358.98 | 40.24 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.45 | 0.67 | -0.03 | 280638.13 | 1.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.68 | 2.95 | 2.74 | -0.03 | 1979.56 | 22.05 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.15 | 0.76 | -0.02 | 87452.12 | 35.31 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.33 | 0.13 | -0.0 | 51802.94 | 4.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.64 | 0.04 | -0.01 | 25025.57 | 2.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
