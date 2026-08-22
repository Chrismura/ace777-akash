# Hulk DIGEST — 2026-08-22T01:34:40Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 10.86 | 0.6 | 0.15 | 6762592.76 | 3.89 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.22 | 8.96 | 0.01 | 0.15 | 150598355.87 | 4.03 | skipped_fast |
| HBARUSDT | IDLE | 2.98 | 6.36 | 0.33 | 0.08 | 954567.67 | 2.48 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.8 | 0.09 | 550947.77 | 17.42 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.0 | 0.16 | 661605.39 | 8.73 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.65 | 0.64 | 0.09 | 391312.25 | 12.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.28 | -0.01 | 513251.53 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.57 | 1.1 | 0.03 | 186119.39 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79516.21 | 33.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.16 | 0.11 | 60752.36 | 28.82 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.86 | 0.17 | 158676.22 | 17.56 | skipped_fast |
| KITEUSDT | IDLE | 1.56 | 4.93 | 0.21 | 0.12 | 61038.35 | 10.78 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.75 | 0.07 | 170033.59 | 7.52 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.87 | 0.05 | 181929.81 | 41.28 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.3 | 2.45 | 1.01 | 0.04 | 9587.29 | 37.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.11 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54845.39 | 24.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
