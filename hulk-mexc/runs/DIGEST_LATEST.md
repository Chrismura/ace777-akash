# Hulk DIGEST — 2026-08-22T11:47:51Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.84 | 0.01 | 51614868.77 | 14.35 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.5 | 0.08 | 216582313.29 | 3.36 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.51 | 0.14 | 787394.76 | 10.26 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.3 | 0.02 | 1254955.59 | 6.46 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.52 | 0.02 | 582761.67 | 14.79 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.19 | -0.03 | 387988.16 | 15.95 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.29 | -0.1 | 618836.96 | 6.69 | skipped_fast |
| KITEUSDT | IDLE | 2.52 | 6.08 | 0.12 | 0.05 | 80553.29 | 10.55 | skipped_fast |
| EDELUSDT | IDLE | 2.76 | 4.93 | 3.93 | -0.03 | 79232.73 | 56.85 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 6.64 | 1.95 | -0.03 | 242670.44 | 6.42 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.66 | -0.03 | 167302.39 | 42.85 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2456.68 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.43 | 0.04 | 154555.72 | 23.17 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.64 | 0.01 | 188324.45 | 4.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.94 | -0.03 | 48664.25 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.56 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57670.68 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
