# Hulk DIGEST — 2026-09-24T17:38:29Z

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
| XRPUSDT | IDLE | 2.68 | 5.27 | 0.54 | 0.02 | 68992872.7 | 2.61 | skipped_fast |
| PYTHUSDT | IDLE | 3.5 | 12.86 | 4.35 | 0.08 | 1269086.28 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 1.33 | 2.49 | 1.09 | 0.01 | 327566673.4 | 0.49 | skipped_fast |
| BTCUSDT | IDLE | 1.15 | 2.14 | 1.01 | 0.0 | 722577627.63 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 3.26 | 6.19 | 2.23 | 0.03 | 909001.0 | 1.08 | skipped_fast |
| CCUSDT | IDLE | 3.44 | 6.62 | 1.78 | 0.04 | 447135.39 | 7.13 | skipped_fast |
| CHIPUSDT | IDLE | 3.92 | 12.77 | 2.96 | 0.06 | 72946.44 | 13.33 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.36 | 10.97 | 1.2 | 0.1 | 85854.31 | 6.4 | skipped_fast |
| WUSDT | IDLE | 2.82 | 5.44 | 1.38 | 0.03 | 242973.98 | 5.96 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.19 | 18.9 | 1.42 | 0.18 | 182072.77 | 20.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.59 | 5.08 | 0.72 | 0.04 | 214469.86 | 22.2 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.53 | 13.97 | 0.0 | 0.15 | 11920.51 | 79.91 | skipped_fast |
| EDELUSDT | IDLE | 2.42 | 6.41 | 1.83 | -0.0 | 153435.79 | 39.45 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 11.52 | 5.99 | 0.1 | 59545.64 | 55.95 | skipped_fast |
| REDUSDT | IDLE | 2.07 | 5.56 | 1.28 | 0.04 | 101273.3 | 15.61 | skipped_fast |
| TELUSDT | IDLE | 3.05 | 5.45 | 4.29 | -0.04 | 107680.87 | 6.14 | skipped_fast |
| KITEUSDT | IDLE | 1.73 | 3.29 | 1.13 | -0.01 | 84903.47 | 9.79 | skipped_fast |
| FLUIDUSDT | IDLE | 2.69 | 5.37 | 0.0 | 0.04 | 2717.35 | 22.03 | skipped_fast |
| RWAUSDT | IDLE | 1.1 | 2.15 | 0.29 | 0.02 | 55838.29 | 7.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.3 | 0.0 | 0.01 | 37250.39 | 9.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
