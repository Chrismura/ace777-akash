# Hulk DIGEST — 2026-08-21T01:12:47Z

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
| XRPUSDT | IDLE | 0.64 | 3.76 | 0.23 | 0.15 | 103983386.38 | 1.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.23 | 2.38 | 0.47 | 0.06 | 1471706.41 | 2.25 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 9.31 | 0.5 | 0.15 | 323463.28 | 6.22 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.46 | 2.05 | -0.02 | 473708.45 | 6.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.75 | 5.58 | 0.24 | 0.04 | 279610.96 | 14.45 | skipped_fast |
| WUSDT | IDLE | 1.28 | 2.39 | 1.12 | 0.04 | 255288.71 | 9.99 | skipped_fast |
| EDELUSDT | IDLE | 1.87 | 5.22 | 2.32 | 0.03 | 91999.33 | 21.62 | skipped_fast |
| RIZEUSDT | IDLE | 1.78 | 9.36 | 5.95 | -0.05 | 46330.28 | 51.01 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.57 | 0.34 | 0.04 | 444105.39 | 1.35 | skipped_fast |
| BIOUSDT | IDLE | 0.63 | 2.91 | 0.57 | 0.11 | 231254.64 | 6.34 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.76 | 0.09 | 0.03 | 62783.87 | 15.08 | skipped_fast |
| REDUSDT | IDLE | 0.66 | 3.84 | 1.67 | 0.07 | 183738.38 | 20.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.84 | 3.43 | 1.69 | 0.01 | 7878.39 | 49.96 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 3.22 | 2.82 | -0.03 | 6244.55 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 4.98 | 2.53 | 0.14 | 192615.81 | 48.66 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 1.81 | 0.91 | 0.05 | 63773.18 | 1.61 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.9 | 0.25 | 0.01 | 54046.43 | 8.5 | skipped_fast |
| FLUIDUSDT | IDLE | 0.56 | 1.3 | 0.02 | 0.08 | 1529.61 | 19.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
