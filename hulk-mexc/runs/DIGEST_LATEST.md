# Hulk DIGEST — 2026-08-22T02:48:44Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.61 | 11.02 | 0.43 | 0.17 | 7258466.28 | 1.9 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 12.56 | 0.15 | 0.2 | 157561102.34 | 1.3 | skipped_fast |
| HBARUSDT | IDLE | 2.49 | 6.12 | 0.09 | 0.1 | 982635.81 | 1.23 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 8.33 | 0.09 | 0.16 | 657468.32 | 6.82 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 9.63 | 2.19 | 0.11 | 539421.15 | 32.22 | skipped_fast |
| CHIPUSDT | IDLE | 2.39 | 5.51 | 0.0 | -0.02 | 454088.64 | 2.98 | skipped_fast |
| BIOUSDT | IDLE | 3.2 | 8.18 | 2.02 | 0.09 | 193287.36 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.98 | 5.85 | 0.14 | 0.11 | 415020.14 | 10.95 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 5.02 | 2.28 | -0.03 | 79853.94 | 44.54 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.34 | 0.1 | 61357.24 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.8 | 0.19 | 157895.58 | 8.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9400.35 | 5.43 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.24 | 0.09 | 172574.62 | 5.96 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.26 | 0.12 | 62396.8 | 11.66 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.12 | 5.11 | 0.66 | 0.06 | 174243.78 | 61.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.11 | skipped_fast |
| RWAUSDT | IDLE | 1.46 | 2.92 | 0.0 | 0.05 | 55968.36 | 40.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
