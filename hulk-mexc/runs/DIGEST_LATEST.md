# Hulk DIGEST — 2026-08-22T01:00:54Z

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
| PYTHUSDT | IDLE | 2.21 | 7.24 | 0.4 | 0.13 | 6545810.06 | 2.01 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 8.72 | 1.4 | 0.15 | 148078944.02 | 1.37 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.44 | 0.08 | 951087.64 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.9 | 0.11 | 543528.37 | 26.17 | skipped_fast |
| CCUSDT | IDLE | 1.65 | 6.26 | 0.62 | 0.15 | 651446.4 | 8.86 | skipped_fast |
| WUSDT | IDLE | 2.71 | 6.91 | 0.6 | 0.1 | 391728.8 | 13.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 3.56 | 0.24 | 0.02 | 538314.92 | 3.05 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.18 | 0.55 | 0.04 | 186671.6 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79698.11 | 22.17 | skipped_fast |
| RIZEUSDT | IDLE | 2.26 | 9.82 | 3.95 | 0.12 | 60282.81 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.58 | 2.4 | 0.2 | 159397.19 | 14.81 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.82 | 0.06 | 183799.81 | 36.07 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.82 | 0.07 | 170514.97 | 7.53 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.22 | 1.21 | 0.01 | 3850.39 | 67.05 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 3.86 | 0.07 | 0.11 | 60908.52 | 12.69 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54899.33 | 16.45 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 11.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
