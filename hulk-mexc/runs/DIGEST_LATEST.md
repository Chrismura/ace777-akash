# Hulk DIGEST — 2026-08-17T07:10:51Z

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
| XRPUSDT | IDLE | 0.49 | 0.96 | 0.19 | 0.0 | 9486272.89 | 1.99 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.3 | 14.28 | 0.4 | 0.16 | 326440.52 | 12.47 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 3.28 | 0.12 | 0.01 | 63646.1 | 8.04 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.71 | 2.42 | -0.05 | 58264.27 | 15.41 | skipped_fast |
| CCUSDT | IDLE | 0.67 | 1.34 | 0.02 | -0.01 | 249136.8 | 9.38 | skipped_fast |
| PYTHUSDT | IDLE | 0.98 | 1.89 | 0.41 | -0.0 | 162594.03 | 5.11 | skipped_fast |
| WUSDT | IDLE | 0.83 | 1.45 | 1.42 | 0.02 | 188591.08 | 14.19 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 2.38 | 2.02 | -0.0 | 53576.97 | 11.73 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 2.76 | 1.92 | 0.03 | 55230.91 | 39.09 | skipped_fast |
| ZBCNUSDT | IDLE | 0.5 | 0.97 | 0.23 | 0.01 | 190573.25 | 17.14 | skipped_fast |
| QAITUSDT | IDLE | 1.08 | 2.41 | 2.0 | -0.03 | 2151.91 | 61.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.58 | 1.02 | 0.9 | -0.01 | 2282.92 | 79.55 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.65 | 1.15 | -0.01 | 87665.23 | 41.1 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.53 | 0.6 | -0.02 | 31847.09 | 3.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.94 | 1.69 | 1.27 | 0.01 | 802.22 | 22.54 | skipped_fast |
| HBARUSDT | IDLE | 0.34 | 0.66 | 0.14 | 0.0 | 91330.42 | 1.53 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.87 | 0.09 | 0.01 | 49542.43 | 26.01 | skipped_fast |
| RIZEUSDT | IDLE | 1.47 | 11.66 | 3.61 | 0.13 | 47247.48 | 426.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
