# Hulk DIGEST — 2026-10-25T21:09:02Z

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
| XRPUSDT | IDLE | 0.58 | 1.04 | 0.83 | 0.01 | 13989318.12 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 0.98 | 0.79 | 0.0 | 78732118.27 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.63 | 0.55 | 0.0 | 141413153.15 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.85 | 6.2 | 1.37 | 0.06 | 575063.21 | 2.68 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.24 | 8.14 | 0.87 | 0.06 | 365483.35 | 15.73 | skipped_fast |
| QNTUSDT | IDLE | 2.5 | 7.63 | 4.23 | 0.08 | 636919.14 | 2.61 | skipped_fast |
| WUSDT | IDLE | 1.43 | 2.5 | 2.4 | -0.01 | 578888.11 | 23.44 | skipped_fast |
| ZBCNUSDT | IDLE | 2.83 | 5.45 | 1.92 | 0.05 | 200283.73 | 24.29 | skipped_fast |
| CHIPUSDT | IDLE | 2.88 | 5.17 | 4.0 | 0.0 | 91570.92 | 15.78 | skipped_fast |
| RIZEUSDT | IDLE | 2.44 | 6.05 | 3.88 | -0.0 | 36735.38 | 65.12 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.99 | 1.24 | -0.03 | 58290.68 | 16.51 | skipped_fast |
| CCUSDT | IDLE | 0.71 | 1.25 | 1.09 | 0.01 | 200638.58 | 7.84 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 2.45 | 1.69 | -0.01 | 53454.61 | 12.42 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.57 | 1.54 | -0.02 | 59266.83 | 4.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.34 | 1.32 | -0.02 | 64435.97 | 5.57 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.32 | 1.04 | -0.0 | 122412.02 | 6.46 | skipped_fast |
| WAXLUSDT | IDLE | 1.35 | 2.39 | 2.04 | 0.01 | 53350.38 | 46.94 | skipped_fast |
| LAUSDT | IDLE | 0.83 | 2.98 | 2.63 | -0.1 | 70872.89 | 22.83 | skipped_fast |
| IOTAUSDT | IDLE | 0.96 | 1.76 | 1.1 | -0.01 | 62875.84 | 34.9 | skipped_fast |
| FLUIDUSDT | IDLE | 0.77 | 3.7 | 2.21 | 0.03 | 18967.95 | 21.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.88 | 1.59 | 1.07 | -0.01 | 37483.48 | 60.17 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.56 | 0.08 | 0.0 | 51420.14 | 7.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
