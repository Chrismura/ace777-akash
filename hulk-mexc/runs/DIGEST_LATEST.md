# Hulk DIGEST — 2026-09-07T16:36:14Z

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
| XRPUSDT | IDLE | 1.39 | 2.55 | 1.47 | -0.01 | 36204584.54 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 1.0 | 1.79 | 1.37 | -0.0 | 338156775.94 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.18 | 0.84 | -0.01 | 449414240.28 | 0.31 | skipped_fast |
| PYTHUSDT | IDLE | 2.79 | 5.01 | 3.86 | -0.0 | 570977.71 | 1.83 | skipped_fast |
| CCUSDT | IDLE | 2.0 | 3.58 | 2.81 | -0.03 | 434770.42 | 4.72 | skipped_fast |
| CHIPUSDT | IDLE | 2.16 | 8.22 | 5.64 | -0.1 | 256743.19 | 11.52 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.62 | 1.63 | -0.01 | 409863.8 | 18.48 | skipped_fast |
| HBARUSDT | IDLE | 1.79 | 3.34 | 1.66 | 0.01 | 549395.48 | 2.44 | skipped_fast |
| RIZEUSDT | IDLE | 2.14 | 9.74 | 7.32 | -0.08 | 69932.36 | 65.87 | skipped_fast |
| REDUSDT | IDLE | 2.24 | 4.06 | 2.8 | 0.03 | 63734.86 | 11.41 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 2.95 | 2.36 | -0.0 | 193300.7 | 9.73 | skipped_fast |
| KITEUSDT | IDLE | 2.0 | 3.65 | 2.29 | -0.05 | 59870.97 | 12.47 | skipped_fast |
| BIOUSDT | IDLE | 1.85 | 3.39 | 2.09 | -0.02 | 69224.51 | 3.68 | skipped_fast |
| EDELUSDT | IDLE | 1.84 | 5.5 | 4.35 | -0.05 | 83313.38 | 50.38 | skipped_fast |
| MNSRYUSDT | IDLE | 2.77 | 5.34 | 1.34 | -0.01 | 38029.28 | 53.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.07 | 3.34 | 2.19 | 0.05 | 5160.77 | 111.52 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.19 | 1.45 | -0.01 | 111219.64 | 17.61 | skipped_fast |
| QNTUSDT | IDLE | 1.15 | 2.12 | 1.25 | -0.0 | 47158.34 | 3.04 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.65 | -0.01 | 51818.03 | 21.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.07 | 0.14 | 0.0 | -0.0 | 1182.44 | 22.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
