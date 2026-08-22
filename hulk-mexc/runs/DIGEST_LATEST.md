# Hulk DIGEST — 2026-08-22T02:17:12Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.2 | 0.13 | 6933212.68 | 1.96 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 10.08 | 0.67 | 0.17 | 154044659.06 | 2.0 | skipped_fast |
| HBARUSDT | IDLE | 2.32 | 4.9 | 0.53 | 0.08 | 961405.61 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.5 | 9.63 | 3.11 | 0.08 | 545129.01 | 23.78 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.14 | 0.12 | 0.15 | 653571.72 | 6.97 | skipped_fast |
| CHIPUSDT | IDLE | 2.13 | 4.91 | 0.06 | -0.0 | 514743.93 | 3.0 | skipped_fast |
| BIOUSDT | IDLE | 2.98 | 7.01 | 0.0 | 0.09 | 192649.67 | 14.78 | skipped_fast |
| WUSDT | IDLE | 1.81 | 4.81 | 0.19 | 0.09 | 401885.58 | 8.05 | skipped_fast |
| EDELUSDT | IDLE | 2.35 | 5.02 | 1.09 | -0.01 | 79581.79 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.85 | 0.11 | 61238.63 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.11 | 0.18 | 156943.58 | 9.71 | skipped_fast |
| QNTUSDT | IDLE | 2.27 | 4.89 | 0.72 | 0.07 | 171146.9 | 9.03 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.5 | 0.12 | 61556.97 | 9.89 | skipped_fast |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9515.06 | 59.6 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.23 | 0.04 | 179452.37 | 62.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.81 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54839.84 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
