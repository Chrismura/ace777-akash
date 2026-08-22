# Hulk DIGEST — 2026-08-22T00:44:06Z

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
| PYTHUSDT | IDLE | 1.98 | 7.38 | 0.2 | 0.13 | 6461223.41 | 12.01 | skipped_fast |
| XRPUSDT | IDLE | 2.11 | 8.72 | 2.36 | 0.14 | 147134555.98 | 2.77 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.72 | 0.07 | 940435.48 | 3.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 2.99 | 0.12 | 543961.38 | 16.94 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.5 | 0.14 | 640480.74 | 5.36 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.91 | 0.43 | 0.09 | 388201.83 | 10.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.73 | 0.03 | 553160.28 | 6.13 | skipped_fast |
| BIOUSDT | IDLE | 2.5 | 5.62 | 0.31 | 0.03 | 186319.79 | 3.07 | skipped_fast |
| EDELUSDT | IDLE | 2.55 | 5.5 | 0.87 | -0.01 | 79887.57 | 21.93 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 2.44 | 0.13 | 60091.31 | 43.33 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.07 | 184207.9 | 30.9 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.52 | 0.06 | 170529.13 | 7.58 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 7.82 | 0.81 | 0.26 | 158189.2 | 50.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.03 | 9754.98 | 53.97 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.19 | 0.1 | 61170.67 | 10.11 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54821.61 | 8.21 | skipped_fast |
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
