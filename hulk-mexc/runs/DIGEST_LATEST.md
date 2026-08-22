# Hulk DIGEST — 2026-08-22T04:56:17Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 1.04 | 0.19 | 12825678.81 | 9.05 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 17.46 | 0.68 | 0.26 | 179942219.32 | 6.62 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 9.63 | 0.36 | 0.14 | 1078050.29 | 1.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.29 | 0.2 | 741306.11 | 5.73 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.62 | 0.02 | 454120.08 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 8.62 | 0.82 | 0.15 | 447732.06 | 3.84 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.99 | 8.28 | 0.41 | 0.09 | 201465.1 | 11.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 4.29 | 0.77 | 0.11 | 538121.35 | 19.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.39 | 0.1 | 58589.96 | 25.53 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 8.56 | 3.71 | 0.11 | 184310.26 | 13.19 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.07 | 2.17 | -0.02 | 80245.1 | 33.31 | skipped_fast |
| KITEUSDT | IDLE | 1.73 | 6.54 | 0.03 | 0.15 | 68269.68 | 11.35 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.38 | 0.21 | 158052.11 | 11.92 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.49 | 0.1 | 183354.78 | 14.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.02 | 9533.0 | 86.77 | skipped_fast |
| RWAUSDT | IDLE | 1.58 | 3.13 | 0.24 | 0.06 | 56560.02 | 23.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3692.42 | 21.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
