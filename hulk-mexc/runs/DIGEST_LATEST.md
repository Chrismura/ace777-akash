# Hulk DIGEST — 2026-08-21T23:01:07Z

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
| PYTHUSDT | IDLE | 1.55 | 5.77 | 0.28 | 0.12 | 5935157.11 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.73 | 6.54 | 0.59 | 0.15 | 137329607.77 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 7.42 | 0.4 | 0.14 | 661931.97 | 7.07 | skipped_fast |
| HBARUSDT | IDLE | 2.36 | 5.03 | 0.08 | 0.09 | 879612.91 | 5.02 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 9.96 | 0.52 | 0.15 | 508820.8 | 43.94 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 1.03 | 0.09 | 376380.98 | 18.38 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.16 | 0.05 | 543387.9 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.02 | 0.03 | 187871.42 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.02 | 82542.93 | 32.73 | skipped_fast |
| TELUSDT | IDLE | 2.68 | 6.45 | 0.87 | 0.06 | 186661.68 | 10.36 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10217.99 | 16.16 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.77 | 0.18 | 157205.44 | 20.19 | skipped_fast |
| QNTUSDT | IDLE | 2.45 | 4.92 | 0.02 | 0.07 | 91922.03 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.8 | 0.1 | 61373.38 | 12.93 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 4.7 | 2.03 | 0.06 | 56409.87 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.25 | 0.04 | 54230.87 | 24.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
