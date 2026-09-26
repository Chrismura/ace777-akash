# Hulk DIGEST — 2026-09-26T03:51:32Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.15 | 2.08 | 1.4 | 0.02 | 109847424.48 | 1.92 | skipped_fast |
| ETHUSDT | IDLE | 0.32 | 0.59 | 0.28 | 0.0 | 304234758.96 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.23 | 0.43 | 0.23 | -0.0 | 656435071.69 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 3.48 | 3.2 | 0.06 | 1246290.4 | 1.37 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 6.39 | 1.95 | 0.14 | 911845.32 | 1.51 | skipped_fast |
| HBARUSDT | IDLE | 1.35 | 2.41 | 1.94 | 0.02 | 887842.72 | 1.06 | skipped_fast |
| WUSDT | IDLE | 1.88 | 3.49 | 2.29 | 0.05 | 452852.78 | 10.63 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 4.72 | 4.15 | 0.05 | 148079.33 | 8.22 | skipped_fast |
| KITEUSDT | IDLE | 2.12 | 6.01 | 0.5 | 0.1 | 79790.05 | 7.92 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 3.94 | 0.25 | 0.09 | 557386.65 | 10.92 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 3.38 | 3.27 | 0.04 | 86631.1 | 14.15 | skipped_fast |
| BIOUSDT | IDLE | 1.27 | 3.32 | 2.76 | 0.06 | 113598.34 | 3.09 | skipped_fast |
| ZBCNUSDT | IDLE | 0.98 | 2.14 | 2.01 | 0.05 | 233545.81 | 25.2 | skipped_fast |
| EDELUSDT | IDLE | 0.77 | 1.5 | 0.27 | -0.01 | 186671.47 | 6.76 | skipped_fast |
| RIZEUSDT | IDLE | 0.2 | 2.64 | 1.44 | -0.08 | 89214.83 | 54.64 | skipped_fast |
| TELUSDT | IDLE | 0.7 | 1.23 | 1.15 | 0.02 | 107446.37 | 18.39 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 1.83 | 1.79 | 0.0 | 3437.87 | 21.87 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.04 | 0.66 | -0.01 | 53188.82 | 7.39 | skipped_fast |
| RWAINCUSDT | IDLE | 0.03 | 0.1 | 0.05 | -0.09 | 12811.79 | 95.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.91 | 0.31 | 0.01 | 41178.4 | 38.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
