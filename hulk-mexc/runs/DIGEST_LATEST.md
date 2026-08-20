# Hulk DIGEST — 2026-08-20T13:25:20Z

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
| XRPUSDT | IDLE | 1.89 | 9.19 | 0.33 | 0.19 | 64437803.93 | 2.48 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.81 | 12.13 | 1.58 | 0.13 | 287914.56 | 3.27 | skipped_fast |
| PYTHUSDT | IDLE | 1.33 | 5.32 | 2.58 | 0.14 | 752228.67 | 2.29 | skipped_fast |
| BIOUSDT | IDLE | 1.81 | 11.75 | 10.16 | 0.18 | 278700.43 | 6.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.7 | 7.43 | 6.43 | 0.12 | 260493.32 | 35.66 | skipped_fast |
| CCUSDT | IDLE | 0.7 | 2.89 | 0.19 | 0.16 | 489433.81 | 9.55 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.65 | 1.17 | 0.07 | 328779.63 | 13.74 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.63 | 6.97 | 0.22 | 199908.11 | 12.03 | skipped_fast |
| HBARUSDT | IDLE | 1.52 | 3.2 | 0.88 | 0.08 | 441441.38 | 1.37 | skipped_fast |
| QAITUSDT | IDLE | 2.12 | 6.03 | 4.35 | -0.01 | 8372.58 | 34.92 | skipped_fast |
| RIZEUSDT | IDLE | 1.2 | 8.15 | 3.71 | 0.1 | 65080.28 | 31.74 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.94 | 0.45 | 0.05 | 59948.23 | 15.52 | skipped_fast |
| TELUSDT | IDLE | 1.17 | 5.94 | 1.4 | 0.18 | 208231.87 | 29.66 | skipped_fast |
| QNTUSDT | IDLE | 1.8 | 4.44 | 0.21 | 0.09 | 59228.61 | 6.45 | skipped_fast |
| EDELUSDT | IDLE | 0.4 | 3.05 | 1.54 | 0.18 | 103293.05 | 44.59 | skipped_fast |
| RWAINCUSDT | IDLE | 0.97 | 1.82 | 0.84 | 0.03 | 13535.34 | 78.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 3.3 | 0.16 | 0.11 | 3400.7 | 23.26 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.3 | 0.51 | 0.01 | 52238.49 | 25.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
