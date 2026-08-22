# Hulk DIGEST — 2026-08-22T00:43:13Z

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
| PYTHUSDT | IDLE | 1.97 | 7.38 | 0.0 | 0.13 | 6454917.83 | 7.99 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.3 | 0.15 | 147112337.52 | 4.15 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.81 | 0.07 | 940405.82 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.81 | 0.12 | 543961.38 | 24.21 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.4 | 0.14 | 640493.87 | 5.35 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.91 | 0.39 | 0.09 | 388171.83 | 11.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.03 | 553173.39 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.5 | 5.62 | 0.31 | 0.03 | 186320.45 | 6.14 | skipped_fast |
| EDELUSDT | IDLE | 2.55 | 5.5 | 0.87 | -0.01 | 79947.7 | 21.93 | skipped_fast |
| RIZEUSDT | IDLE | 2.2 | 9.82 | 2.29 | 0.13 | 60091.31 | 43.33 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.06 | 186422.59 | 30.9 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.54 | 0.06 | 170547.75 | 3.03 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.03 | 9787.93 | 16.16 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 7.82 | 0.0 | 0.25 | 158139.47 | 70.22 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.18 | 0.1 | 61159.63 | 11.93 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54795.56 | 16.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
