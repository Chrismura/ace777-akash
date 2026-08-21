# Hulk DIGEST — 2026-08-21T23:37:00Z

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
| PYTHUSDT | IDLE | 1.75 | 6.39 | 1.23 | 0.11 | 6120769.82 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.61 | 0.16 | 140964381.96 | 3.41 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 11.25 | 1.54 | 0.13 | 513142.72 | 20.54 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.36 | 0.36 | 0.1 | 906893.53 | 1.24 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.04 | 0.13 | 645453.15 | 8.9 | skipped_fast |
| WUSDT | IDLE | 2.76 | 6.91 | 1.52 | 0.08 | 380088.58 | 14.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 3.56 | 1.49 | 0.03 | 549139.05 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.92 | 0.02 | 186361.78 | 6.21 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82434.52 | 10.91 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 9.82 | 4.16 | 0.13 | 58901.16 | 45.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.25 | 4.07 | 2.91 | 0.01 | 10262.4 | 21.73 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.21 | 0.07 | 188341.53 | 20.53 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.75 | 0.19 | 157723.23 | 10.49 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.08 | 138800.94 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.93 | 0.09 | 61405.26 | 11.1 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54564.17 | 8.19 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
