# Hulk DIGEST — 2026-09-20T02:02:43Z

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
| XRPUSDT | IDLE | 1.46 | 2.61 | 2.01 | -0.01 | 56164940.17 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.54 | 0.97 | 0.68 | 0.0 | 211920171.46 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.55 | 0.28 | -0.0 | 424855896.67 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.97 | 3.88 | 0.35 | 0.02 | 665387.36 | 12.9 | skipped_fast |
| HBARUSDT | IDLE | 2.52 | 4.71 | 2.22 | 0.03 | 624463.69 | 1.22 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.73 | 0.0 | 0.02 | 500181.49 | 5.35 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 3.7 | 3.04 | -0.03 | 310253.08 | 8.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 5.28 | 4.18 | 0.07 | 214847.94 | 35.42 | skipped_fast |
| EDELUSDT | IDLE | 1.61 | 5.77 | 3.81 | -0.09 | 112149.12 | 45.08 | skipped_fast |
| CHIPUSDT | IDLE | 1.43 | 3.98 | 2.54 | -0.06 | 110472.74 | 11.59 | skipped_fast |
| BIOUSDT | IDLE | 1.32 | 2.47 | 1.13 | 0.02 | 90337.71 | 3.58 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.21 | 1.19 | 0.03 | 109325.63 | 10.78 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.86 | 0.89 | 0.01 | 80507.22 | 14.0 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.37 | 1.35 | -0.04 | 7651.63 | 5.96 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 3.14 | 2.12 | -0.07 | 103154.19 | 40.6 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.53 | 1.07 | 0.04 | 54906.22 | 4.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.3 | 2.16 | 0.02 | 8204.33 | 22.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.19 | 4.68 | 2.88 | 0.01 | 40215.73 | 205.25 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.11 | 0.95 | 0.01 | 52694.13 | 51.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.34 | -0.01 | 34544.48 | 62.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
