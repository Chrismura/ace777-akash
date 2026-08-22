# Hulk DIGEST — 2026-08-22T01:35:32Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.95 | 0.16 | 6766328.93 | 11.71 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.24 | 9.03 | 0.28 | 0.15 | 150847152.99 | 2.69 | skipped_fast |
| HBARUSDT | IDLE | 2.97 | 6.36 | 0.19 | 0.08 | 954606.29 | 6.2 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.8 | 0.09 | 551581.17 | 17.91 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.13 | 0.16 | 661549.93 | 6.11 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.65 | 0.59 | 0.09 | 391013.63 | 10.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.94 | 0.01 | 513649.3 | 12.28 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.57 | 1.16 | 0.04 | 186140.63 | 3.09 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79466.17 | 33.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.23 | 0.11 | 60759.13 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 5.0 | 0.17 | 158625.31 | 9.6 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.92 | 0.05 | 181951.63 | 36.13 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.75 | 0.07 | 170031.34 | 6.02 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 4.93 | 0.11 | 0.13 | 61090.32 | 13.46 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.3 | 2.45 | 1.01 | 0.04 | 9587.29 | 53.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.14 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54833.46 | 16.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
