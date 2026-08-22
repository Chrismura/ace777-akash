# Hulk DIGEST — 2026-08-22T03:57:17Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.59 | 0.16 | 9063554.51 | 22.59 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.75 | 0.19 | 166145585.99 | 2.55 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 6.93 | 0.6 | 0.1 | 1033352.92 | 1.21 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.31 | 0.2 | 702489.79 | 8.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 5.36 | 1.26 | -0.03 | 459409.03 | 2.98 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.49 | 0.07 | 199189.65 | 3.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 5.37 | 1.38 | 0.13 | 537694.62 | 18.58 | skipped_fast |
| WUSDT | IDLE | 1.87 | 6.27 | 0.08 | 0.13 | 425011.45 | 14.67 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80683.66 | 33.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.5 | 0.11 | 59299.06 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.77 | 0.23 | 157690.42 | 10.18 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 5.3 | 0.42 | 0.13 | 67556.55 | 12.42 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 38.1 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 4.68 | 0.68 | 0.09 | 178485.25 | 7.42 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.63 | 3.22 | 0.24 | 0.06 | 56326.38 | 16.01 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.41 | 0.07 | 174121.88 | 40.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
