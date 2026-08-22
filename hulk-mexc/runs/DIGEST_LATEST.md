# Hulk DIGEST — 2026-08-22T12:43:24Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.0 | 0.1 | 216328328.92 | 2.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 7.83 | 1.36 | 0.05 | 51600545.32 | 11.82 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.19 | 0.02 | 1251440.55 | 2.57 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 8.38 | 3.47 | 0.14 | 777863.89 | 8.42 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.63 | 0.0 | 576724.76 | 13.75 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.72 | -0.01 | 335581.03 | 19.47 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.65 | -0.1 | 603307.64 | 3.36 | skipped_fast |
| KITEUSDT | IDLE | 2.69 | 6.37 | 1.01 | 0.02 | 84911.19 | 8.86 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 3.89 | 2.87 | -0.02 | 78229.76 | 45.2 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.67 | -0.05 | 237938.81 | 3.23 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2406.15 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.6 | 0.01 | 152969.5 | 9.82 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.78 | -0.03 | 163239.46 | 47.83 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.59 | -0.0 | 187687.9 | 6.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.93 | 0.2 | -0.0 | 46775.9 | 23.89 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57812.98 | 24.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.04 | 5072.55 | 20.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
