# Hulk DIGEST — 2026-08-22T00:37:44Z

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
| PYTHUSDT | IDLE | 1.76 | 6.5 | 0.64 | 0.11 | 6421023.6 | 4.05 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.09 | 8.72 | 1.8 | 0.15 | 146160285.61 | 1.38 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.78 | 0.07 | 939439.2 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 11.25 | 2.69 | 0.11 | 542572.36 | 25.15 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.67 | 0.15 | 639546.57 | 5.32 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 0.83 | 0.08 | 388433.64 | 12.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.7 | 0.03 | 553446.18 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.23 | 5.04 | 0.22 | 0.03 | 186073.0 | 3.08 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.3 | 0.13 | 59938.68 | 45.4 | skipped_fast |
| EDELUSDT | IDLE | 2.54 | 5.5 | 0.76 | -0.02 | 79850.61 | 43.86 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.05 | 186239.37 | 25.75 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.34 | 0.06 | 170486.91 | 6.05 | skipped_fast |
| REDUSDT | IDLE | 0.71 | 6.54 | 0.29 | 0.24 | 157939.43 | 17.87 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.2 | 0.1 | 61069.34 | 11.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.62 | 2.99 | 1.64 | 0.05 | 9754.58 | 48.48 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54657.53 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
