# Hulk DIGEST — 2026-08-22T11:15:56Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.81 | 0.0 | 51653074.72 | 12.43 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.43 | 0.08 | 217531986.02 | 2.68 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.69 | 0.11 | 811603.91 | 7.8 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.76 | 0.0 | 1253911.91 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.73 | 0.02 | 584543.73 | 11.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.33 | 5.93 | 5.04 | -0.04 | 396982.62 | 28.04 | skipped_fast |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.54 | -0.11 | 645509.05 | 3.39 | skipped_fast |
| EDELUSDT | IDLE | 2.77 | 4.93 | 4.04 | -0.05 | 78798.19 | 34.19 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.65 | -0.05 | 237480.1 | 3.26 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.3 | 1.9 | 0.03 | 73657.5 | 10.03 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.61 | -0.04 | 169404.23 | 42.87 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 5.02 | 0.03 | 154572.47 | 9.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | -0.01 | 11311.88 | 59.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.97 | 0.0 | 49264.43 | 29.22 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 3.47 | 2.13 | -0.0 | 188714.51 | 9.39 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | -0.0 | 2496.35 | 189.8 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.64 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.8 | 1.69 | 0.01 | 57483.28 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
