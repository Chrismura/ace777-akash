# Hulk DIGEST — 2026-08-21T23:04:59Z

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
| PYTHUSDT | IDLE | 1.67 | 6.22 | 0.24 | 0.12 | 5956523.79 | 2.02 | skipped_fast |
| XRPUSDT | IDLE | 1.72 | 6.54 | 0.19 | 0.15 | 137975847.92 | 3.45 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.42 | 0.56 | 0.14 | 665113.89 | 8.86 | skipped_fast |
| HBARUSDT | IDLE | 2.35 | 5.03 | 0.03 | 0.09 | 887292.72 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 10.07 | 0.6 | 0.14 | 509992.52 | 32.04 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.22 | 0.09 | 376444.61 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.16 | 0.05 | 544233.78 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.2 | 0.02 | 187331.71 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 5.5 | 0.43 | -0.02 | 82517.99 | 32.73 | skipped_fast |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.41 | 0.07 | 184765.41 | 5.16 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10217.99 | 16.16 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.86 | 0.18 | 157262.99 | 18.63 | skipped_fast |
| QNTUSDT | IDLE | 2.49 | 5.1 | 0.0 | 0.07 | 96077.32 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.14 | 0.1 | 61457.55 | 11.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 4.7 | 2.05 | 0.06 | 56397.46 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 2.0 | 0.16 | 0.04 | 54327.36 | 32.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
