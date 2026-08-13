# Hulk DIGEST — 2026-08-13T01:29:06Z

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
| XRPUSDT | IDLE | 0.56 | 0.99 | 0.84 | -0.02 | 14531489.66 | 1.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 20.64 | 16.27 | 0.05 | 83990.36 | 50.13 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 18.83 | 5.53 | 0.24 | 56604.38 | 43.11 | skipped_fast |
| PYTHUSDT | IDLE | 1.11 | 2.11 | 0.71 | -0.04 | 332507.6 | 2.48 | skipped_fast |
| RWAINCUSDT | IDLE | 2.55 | 4.58 | 3.43 | -0.03 | 2062.5 | 27.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.68 | 3.05 | 2.06 | -0.05 | 173877.32 | 21.2 | skipped_fast |
| QNTUSDT | IDLE | 3.13 | 5.57 | 4.62 | 0.01 | 61027.36 | 8.6 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.66 | 0.71 | -0.05 | 174570.05 | 12.37 | skipped_fast |
| BIOUSDT | IDLE | 1.76 | 3.22 | 2.01 | -0.05 | 61360.86 | 4.19 | skipped_fast |
| CCUSDT | IDLE | 1.08 | 2.13 | 0.25 | -0.0 | 214829.13 | 9.97 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 2.99 | 0.81 | 0.03 | 105129.08 | 4.3 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.1 | 1.47 | -0.02 | 60070.61 | 15.41 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 1.94 | 1.6 | -0.05 | 54481.06 | 14.84 | skipped_fast |
| QAITUSDT | IDLE | 0.77 | 2.51 | 1.67 | -0.04 | 4081.32 | 60.51 | skipped_fast |
| HBARUSDT | IDLE | 0.39 | 0.72 | 0.44 | -0.01 | 82870.0 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 0.49 | 0.96 | 0.13 | -0.0 | 93396.01 | 44.26 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.25 | 0.01 | 52563.84 | 16.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 0.64 | 0.23 | -0.02 | 547.16 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
