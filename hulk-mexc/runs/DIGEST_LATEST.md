# Hulk DIGEST — 2026-08-19T09:55:18Z

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
| XRPUSDT | IDLE | 0.54 | 1.01 | 0.49 | 0.01 | 10350475.49 | 1.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 1.94 | 1.7 | 0.02 | 163557.08 | 2.58 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 4.43 | 3.07 | -0.13 | 145530.21 | 26.26 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.63 | 1.14 | 0.03 | 64712.8 | 3.98 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 1.89 | 0.19 | 0.01 | 154536.86 | 5.68 | skipped_fast |
| CHIPUSDT | IDLE | 0.78 | 2.44 | 1.65 | -0.11 | 163991.09 | 7.8 | skipped_fast |
| CCUSDT | IDLE | 0.55 | 1.07 | 0.18 | -0.01 | 212716.83 | 9.99 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.19 | 1.31 | -0.0 | 64852.5 | 14.36 | skipped_fast |
| WUSDT | IDLE | 0.92 | 1.73 | 0.71 | -0.01 | 102541.05 | 14.88 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.86 | 1.31 | -0.05 | 28516.9 | 51.39 | skipped_fast |
| EDELUSDT | IDLE | 1.32 | 2.44 | 1.32 | -0.03 | 59335.24 | 66.89 | skipped_fast |
| QAITUSDT | IDLE | 0.76 | 4.96 | 1.59 | -0.17 | 12068.34 | 62.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 1.49 | 1.12 | -0.02 | 10001.11 | 112.59 | skipped_fast |
| HBARUSDT | IDLE | 0.5 | 0.91 | 0.66 | 0.03 | 126535.6 | 1.48 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.41 | 0.87 | -0.01 | 52652.27 | 8.78 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 1.42 | 0.86 | 0.01 | 38421.54 | 5.31 | skipped_fast |
| TELUSDT | IDLE | 0.64 | 1.25 | 0.21 | 0.03 | 87010.14 | 34.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.66 | 0.0 | -0.01 | 1163.31 | 19.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
