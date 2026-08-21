# Hulk DIGEST — 2026-08-21T18:24:05Z

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
| PYTHUSDT | IDLE | 1.23 | 4.61 | 3.0 | 0.09 | 5362026.22 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.03 | 4.08 | 2.14 | 0.1 | 133101883.66 | 2.16 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 27.48 | 9.65 | 0.22 | 151055.25 | 11.76 | skipped_fast |
| CCUSDT | IDLE | 2.42 | 6.49 | 1.9 | 0.05 | 620499.72 | 7.48 | skipped_fast |
| ZBCNUSDT | IDLE | 2.13 | 9.58 | 7.07 | 0.05 | 476292.76 | 20.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 4.81 | 3.1 | 0.11 | 514003.3 | 3.08 | skipped_fast |
| WUSDT | IDLE | 1.76 | 3.45 | 0.84 | 0.07 | 348088.88 | 12.58 | skipped_fast |
| HBARUSDT | IDLE | 1.18 | 2.57 | 1.62 | 0.07 | 729201.45 | 1.29 | skipped_fast |
| RIZEUSDT | IDLE | 2.29 | 11.35 | 3.91 | 0.02 | 56502.7 | 47.99 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 4.29 | 2.17 | -0.03 | 80648.79 | 22.15 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 3.13 | 1.75 | 0.03 | 188618.33 | 3.13 | skipped_fast |
| TELUSDT | IDLE | 2.66 | 6.33 | 3.98 | -0.04 | 202310.9 | 59.35 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.64 | 2.98 | 0.0 | 10098.54 | 49.19 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 3.15 | 1.67 | 0.1 | 60372.95 | 11.1 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.0 | 1.71 | -0.02 | 3366.03 | 63.29 | skipped_fast |
| QNTUSDT | IDLE | 1.6 | 3.01 | 1.28 | 0.04 | 60231.17 | 6.23 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.16 | 0.49 | 0.04 | 54387.77 | 16.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.71 | 1.48 | 0.78 | 0.08 | 4361.21 | 21.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
