# Hulk DIGEST — 2026-08-22T04:44:09Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.94 | 15.22 | 0.13 | 0.21 | 11739632.23 | 19.77 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.35 | 16.16 | 0.09 | 0.26 | 174865012.63 | 3.03 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 8.85 | 0.12 | 0.14 | 1068871.92 | 3.5 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.1 | 0.2 | 736271.21 | 4.91 | skipped_fast |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.29 | 0.02 | 450737.1 | 5.96 | skipped_fast |
| WUSDT | IDLE | 2.0 | 7.62 | 0.09 | 0.15 | 432411.88 | 14.44 | skipped_fast |
| BIOUSDT | IDLE | 2.95 | 7.36 | 1.26 | 0.06 | 200464.39 | 5.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 4.29 | 0.75 | 0.13 | 537744.42 | 22.22 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 4.07 | 2.82 | -0.03 | 80160.37 | 11.17 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.29 | 0.1 | 181890.57 | 2.95 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.65 | 0.1 | 58597.38 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.47 | 0.2 | 158149.29 | 17.5 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.26 | 0.14 | 68032.23 | 13.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.48 | 0.01 | 9348.0 | 27.23 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 5.31 | 0.35 | 0.11 | 179228.26 | 14.9 | skipped_fast |
| RWAUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.06 | 56684.09 | 24.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
