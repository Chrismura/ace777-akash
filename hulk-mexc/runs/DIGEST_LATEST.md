# Hulk DIGEST — 2026-08-19T22:19:52Z

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
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 8.01 | 0.66 | 0.13 | 38515353.2 | 0.89 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.14 | 8.37 | 1.93 | 0.0 | 46702.19 | 50.62 | skipped_fast |
| PYTHUSDT | IDLE | 2.42 | 7.21 | 1.24 | 0.09 | 306309.1 | 2.37 | skipped_fast |
| CCUSDT | IDLE | 2.18 | 6.61 | 0.43 | 0.1 | 323588.15 | 9.01 | skipped_fast |
| ZBCNUSDT | IDLE | 2.35 | 10.52 | 2.38 | 0.15 | 222991.82 | 18.37 | skipped_fast |
| REDUSDT | IDLE | 2.42 | 10.48 | 6.58 | 0.02 | 103555.85 | 7.27 | skipped_fast |
| WUSDT | IDLE | 1.82 | 4.13 | 1.27 | 0.07 | 243146.04 | 11.57 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 10.91 | 0.66 | 0.2 | 82259.03 | 33.35 | skipped_fast |
| HBARUSDT | IDLE | 2.1 | 4.1 | 0.72 | 0.06 | 311091.15 | 1.4 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 3.32 | 2.48 | 0.07 | 183712.25 | 3.58 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 5.1 | 3.47 | 0.13 | 147208.95 | 3.59 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.9 | 1.11 | 0.05 | 58775.55 | 14.54 | skipped_fast |
| TELUSDT | IDLE | 1.64 | 7.85 | 1.94 | 0.11 | 186065.73 | 43.3 | skipped_fast |
| QAITUSDT | IDLE | 1.11 | 2.92 | 1.69 | 0.03 | 11144.08 | 62.16 | skipped_fast |
| FLUIDUSDT | IDLE | 2.08 | 6.09 | 0.26 | 0.09 | 2878.05 | 22.16 | skipped_fast |
| QNTUSDT | IDLE | 1.83 | 3.49 | 1.08 | 0.05 | 40981.38 | 3.41 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 2.82 | 0.9 | 0.05 | 16772.38 | 67.68 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.57 | 0.0 | 0.01 | 53945.68 | 17.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
