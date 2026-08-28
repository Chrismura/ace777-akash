# Hulk DIGEST — 2026-08-28T11:06:12Z

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
| XRPUSDT | IDLE | 1.1 | 2.15 | 0.31 | 0.0 | 48905182.46 | 2.8 | skipped_fast |
| PYTHUSDT | IDLE | 1.77 | 3.19 | 2.39 | -0.02 | 1320318.81 | 2.07 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 10.9 | 1.59 | 0.14 | 767433.79 | 21.07 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 5.77 | 5.0 | -0.05 | 81357.32 | 13.22 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 2.55 | 0.87 | -0.03 | 431163.97 | 8.87 | skipped_fast |
| KITEUSDT | IDLE | 2.4 | 4.27 | 3.48 | -0.02 | 76299.85 | 11.05 | skipped_fast |
| WUSDT | IDLE | 0.93 | 1.82 | 0.2 | -0.02 | 190223.08 | 10.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.83 | 9.5 | 5.67 | -0.22 | 114321.45 | 56.03 | skipped_fast |
| ZBCNUSDT | IDLE | 0.56 | 1.53 | 0.12 | 0.0 | 233722.66 | 12.89 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 2.02 | 0.52 | 0.0 | 84297.63 | 3.5 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.58 | 0.33 | -0.0 | 323505.53 | 1.28 | skipped_fast |
| EDELUSDT | IDLE | 0.5 | 2.43 | 1.1 | 0.04 | 52487.16 | 25.76 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 2.54 | 1.99 | -0.02 | 134250.87 | 16.46 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 3.17 | 0.0 | -0.02 | 19840.28 | 118.79 | skipped_fast |
| QAITUSDT | IDLE | 0.35 | 4.58 | 1.39 | -0.17 | 45424.83 | 152.67 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.16 | 0.03 | 0.0 | 39765.07 | 3.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.21 | 1.06 | 0.01 | 2618.7 | 21.29 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.66 | 0.58 | 0.01 | 53391.07 | 16.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
