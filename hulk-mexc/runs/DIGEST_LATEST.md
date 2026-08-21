# Hulk DIGEST — 2026-08-21T22:55:56Z

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
| PYTHUSDT | IDLE | 1.45 | 5.54 | 0.02 | 0.11 | 5911535.69 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 6.54 | 0.15 | 0.15 | 136875335.52 | 2.76 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 7.47 | 0.08 | 0.15 | 660548.56 | 9.7 | skipped_fast |
| HBARUSDT | IDLE | 2.17 | 4.77 | 0.0 | 0.08 | 876693.55 | 1.26 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.2 | 9.48 | 0.02 | 0.15 | 508401.14 | 16.73 | skipped_fast |
| WUSDT | IDLE | 2.66 | 6.84 | 0.0 | 0.09 | 372590.06 | 11.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 4.54 | 2.26 | 0.05 | 541953.44 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.86 | 0.03 | 187743.51 | 6.21 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.61 | 0.19 | 157319.13 | 19.32 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.03 | 82543.5 | 32.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10217.99 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.06 | 186720.51 | 10.36 | skipped_fast |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3896.16 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 1.08 | 0.11 | 61276.86 | 9.22 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 4.85 | 0.0 | 0.07 | 88318.39 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.81 | 0.06 | 56408.54 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.92 | 0.25 | 0.04 | 54096.62 | 16.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 4.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
