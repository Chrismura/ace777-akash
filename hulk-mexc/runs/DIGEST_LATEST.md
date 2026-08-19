# Hulk DIGEST — 2026-08-19T10:13:10Z

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
| XRPUSDT | IDLE | 0.55 | 1.01 | 0.56 | 0.01 | 10414891.88 | 1.0 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 3.42 | 2.78 | -0.14 | 145320.81 | 14.92 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.42 | 1.18 | 0.04 | 65060.43 | 3.99 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 2.04 | 1.81 | -0.11 | 164923.33 | 3.93 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.19 | 1.3 | -0.0 | 64823.61 | 14.36 | skipped_fast |
| PYTHUSDT | IDLE | 0.63 | 1.09 | 1.08 | 0.01 | 163738.43 | 2.59 | skipped_fast |
| ZBCNUSDT | IDLE | 0.78 | 1.52 | 0.2 | 0.01 | 154784.43 | 13.86 | skipped_fast |
| CCUSDT | IDLE | 0.46 | 0.91 | 0.09 | -0.01 | 213864.15 | 9.96 | skipped_fast |
| WUSDT | IDLE | 0.88 | 1.66 | 0.65 | -0.01 | 102426.64 | 11.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.86 | 1.44 | -0.05 | 28721.83 | 51.39 | skipped_fast |
| QAITUSDT | IDLE | 0.73 | 4.96 | 0.0 | -0.14 | 12190.26 | 15.49 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.31 | 1.86 | -0.04 | 59266.29 | 94.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.76 | 1.49 | 0.18 | -0.01 | 10114.35 | 29.58 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.91 | 0.69 | 0.03 | 132087.25 | 1.48 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.42 | 0.98 | 0.01 | 38445.02 | 3.54 | skipped_fast |
| TELUSDT | IDLE | 0.65 | 1.25 | 0.34 | 0.03 | 87014.69 | 34.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.66 | 0.0 | -0.01 | 1163.31 | 22.09 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.06 | 0.52 | -0.01 | 52493.19 | 26.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
