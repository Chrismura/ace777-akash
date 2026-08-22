# Hulk DIGEST — 2026-08-22T01:10:04Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 8.23 | 0.0 | 0.13 | 6592263.09 | 9.9 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.4 | 0.78 | 0.16 | 149060102.93 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.52 | 0.09 | 956365.13 | 2.49 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.81 | 0.11 | 541097.41 | 17.92 | skipped_fast |
| CCUSDT | IDLE | 1.73 | 6.94 | 0.14 | 0.16 | 655168.79 | 7.0 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.54 | 0.09 | 391982.7 | 9.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.7 | 0.02 | 535685.37 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.53 | 0.43 | 0.04 | 187162.36 | 3.06 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79676.98 | 22.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.2 | 0.11 | 60418.91 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 8.27 | 2.2 | 0.22 | 159194.15 | 17.1 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.81 | 0.07 | 170402.29 | 3.01 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.66 | 0.05 | 181212.32 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 4.34 | 0.0 | 0.11 | 60889.73 | 23.41 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 55207.22 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4888.85 | 22.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
