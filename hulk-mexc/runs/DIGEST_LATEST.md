# Hulk DIGEST — 2026-08-22T03:05:13Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 9.55 | 0.96 | 0.16 | 7459762.96 | 5.71 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 11.15 | 0.55 | 0.2 | 159962488.9 | 1.94 | skipped_fast |
| HBARUSDT | IDLE | 2.16 | 5.29 | 0.43 | 0.1 | 995284.25 | 2.44 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.33 | 0.19 | 666018.76 | 8.38 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.23 | 0.07 | 194719.92 | 9.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 4.28 | 0.48 | -0.01 | 448910.14 | 5.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 5.16 | 1.86 | 0.12 | 539125.61 | 32.11 | skipped_fast |
| WUSDT | IDLE | 1.76 | 5.6 | 0.04 | 0.12 | 417773.0 | 10.82 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.44 | 0.09 | 61386.08 | 44.22 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 3.83 | 2.39 | -0.02 | 79893.58 | 22.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.27 | 0.2 | 157925.24 | 11.12 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 21.68 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 4.03 | 0.0 | 0.12 | 63729.64 | 10.75 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3931.36 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.22 | 0.08 | 172771.33 | 7.44 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.31 | 0.16 | 0.05 | 56085.5 | 8.09 | skipped_fast |
| TELUSDT | IDLE | 0.8 | 1.88 | 0.66 | 0.06 | 172968.54 | 36.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
