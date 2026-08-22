# Hulk DIGEST — 2026-08-22T15:07:05Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.79 | 0.04 | 51473372.37 | 5.95 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.52 | 0.02 | 214092568.63 | 1.38 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 5.65 | 2.44 | 0.11 | 802404.55 | 9.4 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 2.85 | 2.19 | -0.02 | 1172847.06 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.59 | -0.11 | 614621.16 | 6.82 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.78 | -0.02 | 563035.34 | 13.9 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 6.37 | 1.92 | 0.03 | 83610.56 | 10.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.32 | -0.07 | 323913.67 | 28.64 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.85 | -0.06 | 225286.29 | 3.31 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.04 | 79037.04 | 34.15 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 5.1 | 4.39 | -0.03 | 150789.41 | 11.0 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.42 | 0.04 | 46487.33 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.99 | -0.01 | 188402.49 | 6.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9946.26 | 86.02 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.75 | 1.21 | 0.01 | 140961.76 | 53.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 22.41 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.48 | 0.02 | 57340.47 | 8.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
