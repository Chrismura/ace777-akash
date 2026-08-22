# Hulk DIGEST — 2026-08-22T04:11:18Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.81 | 12.59 | 0.24 | 0.2 | 10183973.25 | 3.68 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 12.22 | 1.58 | 0.2 | 166831160.45 | 4.45 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 11.56 | 0.12 | 0.22 | 720299.96 | 14.58 | skipped_fast |
| HBARUSDT | IDLE | 2.09 | 6.03 | 0.18 | 0.11 | 1008550.79 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.89 | 5.36 | 2.76 | -0.01 | 458999.76 | 6.05 | skipped_fast |
| BIOUSDT | IDLE | 3.03 | 7.36 | 2.64 | 0.07 | 200049.9 | 6.02 | skipped_fast |
| WUSDT | IDLE | 1.97 | 7.18 | 0.65 | 0.14 | 428866.58 | 10.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.42 | 0.13 | 536296.39 | 30.43 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.47 | -0.05 | 80365.2 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.09 | 59127.63 | 25.71 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.79 | 0.21 | 157898.93 | 18.96 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.26 | 0.13 | 67581.62 | 12.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.6 | 3.22 | 0.01 | 9433.64 | 91.97 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.8 | 0.65 | 0.09 | 178579.7 | 5.94 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56363.37 | 24.05 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.46 | 0.07 | 173940.01 | 40.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 18.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
