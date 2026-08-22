# Hulk DIGEST — 2026-08-22T11:08:17Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.81 | -0.0 | 51658266.53 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.25 | 0.07 | 218253878.6 | 2.68 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 10.24 | 7.51 | 0.11 | 813991.92 | 11.22 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.65 | 0.0 | 1255387.05 | 6.48 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.62 | 0.01 | 595866.74 | 12.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 5.12 | 4.7 | -0.04 | 425139.42 | 27.42 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.28 | -0.11 | 646124.46 | 3.37 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 4.93 | 3.82 | -0.04 | 78823.37 | 34.11 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.74 | -0.06 | 240711.49 | 3.26 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 4.3 | 1.72 | 0.03 | 73621.37 | 20.01 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.46 | -0.04 | 169213.0 | 37.46 | skipped_fast |
| QAITUSDT | IDLE | 2.29 | 4.16 | 2.83 | -0.0 | 2498.14 | 35.86 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.51 | 0.03 | 154331.92 | 15.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | -0.0 | 11326.93 | 59.83 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.94 | -0.0 | 189129.75 | 4.69 | skipped_fast |
| RIZEUSDT | IDLE | 0.68 | 2.89 | 1.31 | -0.0 | 49214.98 | 46.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.37 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.8 | 1.69 | 0.01 | 57565.04 | 24.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
