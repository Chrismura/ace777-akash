# Hulk DIGEST — 2026-08-21T23:30:21Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.73 | 0.11 | 6086276.46 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.52 | 0.15 | 140199672.41 | 2.72 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 11.25 | 1.28 | 0.13 | 512909.35 | 16.2 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.29 | 0.63 | 0.09 | 902810.52 | 3.74 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.03 | 0.13 | 645406.83 | 9.79 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.45 | 0.08 | 379055.06 | 7.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.28 | 0.04 | 550102.98 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.58 | 0.02 | 187081.59 | 3.09 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82515.5 | 10.92 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 9.82 | 3.51 | 0.15 | 58916.66 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.21 | 0.07 | 186625.12 | 20.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.01 | 10152.37 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.18 | 0.18 | 157815.76 | 8.92 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.63 | 0.04 | 0.07 | 120165.11 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.17 | 0.08 | 61409.51 | 11.12 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54545.81 | 16.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
