# Hulk DIGEST — 2026-08-22T04:41:34Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.91 | 14.56 | 0.09 | 0.21 | 11642108.05 | 19.89 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 15.74 | 0.07 | 0.26 | 174037277.91 | 2.43 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 8.8 | 0.11 | 0.14 | 1064867.04 | 1.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.42 | 0.2 | 736789.66 | 3.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.81 | 5.36 | 1.79 | 0.01 | 451270.91 | 8.96 | skipped_fast |
| WUSDT | IDLE | 1.99 | 7.53 | 0.09 | 0.15 | 435222.34 | 15.41 | skipped_fast |
| BIOUSDT | IDLE | 2.95 | 7.36 | 1.23 | 0.07 | 200869.37 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.19 | 0.12 | 537468.17 | 26.61 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 4.07 | 2.71 | -0.03 | 80236.64 | 11.17 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.33 | 0.1 | 181819.06 | 2.95 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.83 | 0.09 | 58576.53 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.75 | 0.2 | 158247.08 | 11.17 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.33 | 0.13 | 67958.91 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.48 | 0.01 | 9349.48 | 38.12 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 1.74 | 4.48 | 0.15 | 0.1 | 177846.11 | 39.96 | skipped_fast |
| RWAUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.07 | 56652.24 | 32.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
