# Hulk DIGEST — 2026-09-02T03:31:18Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.17 | 2.29 | 0.29 | -0.02 | 37731215.14 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 0.91 | 1.78 | 0.3 | -0.02 | 368443939.26 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.71 | 1.39 | 0.23 | -0.01 | 534784983.67 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.28 | 6.05 | 4.25 | 0.12 | 835093.57 | 2.31 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 6.9 | 0.49 | 0.08 | 657680.33 | 9.16 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.5 | 1.53 | 0.03 | 417395.25 | 10.4 | skipped_fast |
| CCUSDT | IDLE | 1.25 | 3.09 | 0.13 | -0.06 | 326703.95 | 5.17 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 4.8 | 4.37 | 0.05 | 143704.55 | 11.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 4.28 | 0.47 | -0.01 | 193136.86 | 32.37 | skipped_fast |
| RIZEUSDT | IDLE | 2.34 | 6.78 | 5.17 | -0.06 | 42653.11 | 59.48 | skipped_fast |
| EDELUSDT | IDLE | 1.02 | 9.32 | 1.48 | -0.0 | 175781.29 | 8.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.54 | 0.0 | 0.03 | 5676.06 | 45.05 | skipped_fast |
| KITEUSDT | IDLE | 1.68 | 3.33 | 0.22 | 0.06 | 69040.11 | 10.36 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 2.43 | 0.31 | -0.03 | 69895.33 | 3.89 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.61 | 0.43 | -0.0 | 257815.13 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.8 | 3.54 | 0.41 | -0.0 | 90338.47 | 41.38 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 2.1 | 0.12 | 0.05 | 47885.89 | 4.65 | skipped_fast |
| FLUIDUSDT | IDLE | 1.07 | 2.04 | 0.7 | -0.04 | 319.05 | 21.79 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.93 | 0.54 | -0.03 | 57400.13 | 7.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.7 | 0.29 | -0.02 | 36101.61 | 28.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
