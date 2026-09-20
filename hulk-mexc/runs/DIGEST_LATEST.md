# Hulk DIGEST — 2026-09-20T17:02:47Z

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
| XRPUSDT | IDLE | 1.64 | 3.2 | 0.59 | -0.02 | 43822643.55 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 1.52 | 2.97 | 0.44 | -0.0 | 265435151.37 | 0.53 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.45 | 0.24 | -0.01 | 464727238.16 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 3.41 | 10.79 | 2.62 | 0.07 | 1269829.74 | 1.14 | skipped_fast |
| PYTHUSDT | IDLE | 3.12 | 6.38 | 0.34 | 0.01 | 664286.54 | 6.53 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 4.25 | 0.24 | -0.04 | 433305.38 | 7.38 | skipped_fast |
| WUSDT | IDLE | 1.91 | 3.77 | 0.32 | -0.0 | 384753.51 | 9.01 | skipped_fast |
| ZBCNUSDT | IDLE | 2.99 | 5.91 | 3.44 | -0.06 | 184055.99 | 75.22 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.64 | 10.74 | 0.14 | 0.06 | 74328.7 | 54.45 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 4.68 | 0.52 | -0.04 | 88695.12 | 9.46 | skipped_fast |
| BIOUSDT | IDLE | 2.12 | 4.21 | 0.14 | -0.02 | 79397.66 | 10.84 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 3.0 | 0.37 | -0.01 | 67246.03 | 12.22 | skipped_fast |
| REDUSDT | IDLE | 1.45 | 2.89 | 0.03 | 0.03 | 75435.44 | 17.07 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 5.12 | 0.71 | -0.0 | 94236.86 | 39.19 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.87 | 0.26 | -0.0 | 81456.25 | 6.14 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 1.98 | 0.12 | 0.02 | 9196.19 | 88.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.86 | 2.18 | 0.78 | -0.03 | 26080.21 | 100.39 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.57 | 0.15 | -0.0 | 53726.88 | 29.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.7 | 0.09 | -0.06 | 1844.36 | 19.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.69 | 0.15 | -0.0 | 34919.74 | 59.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
