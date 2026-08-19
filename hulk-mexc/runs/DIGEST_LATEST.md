# Hulk DIGEST — 2026-08-19T01:44:21Z

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
| XRPUSDT | IDLE | 0.37 | 0.66 | 0.53 | -0.0 | 11544832.58 | 2.0 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 7.66 | 6.03 | 0.02 | 164570.45 | 17.57 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 3.85 | 1.26 | -0.05 | 184204.54 | 7.52 | skipped_fast |
| CCUSDT | IDLE | 1.08 | 1.99 | 1.07 | 0.01 | 225912.93 | 8.82 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 1.68 | 0.7 | 0.0 | 186865.5 | 5.19 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 4.37 | 3.52 | -0.05 | 30026.89 | 50.0 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.24 | 0.73 | -0.01 | 150171.39 | 10.21 | skipped_fast |
| WUSDT | IDLE | 0.53 | 1.02 | 0.32 | -0.01 | 132871.27 | 13.6 | skipped_fast |
| RWAINCUSDT | IDLE | 0.92 | 1.92 | 0.71 | -0.01 | 10674.27 | 11.86 | skipped_fast |
| EDELUSDT | IDLE | 0.8 | 2.43 | 1.06 | -0.03 | 74316.9 | 39.92 | skipped_fast |
| BIOUSDT | IDLE | 0.53 | 1.02 | 0.2 | 0.01 | 63909.67 | 4.06 | skipped_fast |
| KITEUSDT | IDLE | 0.41 | 0.76 | 0.44 | -0.0 | 65453.95 | 14.2 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 2.08 | 0.01 | 0.03 | 123010.05 | 1.48 | skipped_fast |
| QAITUSDT | IDLE | 0.36 | 3.05 | 0.9 | -0.16 | 16107.73 | 47.15 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.09 | 0.82 | 0.05 | 88421.02 | 34.45 | skipped_fast |
| QNTUSDT | IDLE | 0.35 | 0.7 | 0.05 | -0.01 | 38639.96 | 7.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.45 | 0.79 | 0.77 | -0.01 | 204.36 | 22.9 | skipped_fast |
| RWAUSDT | IDLE | 0.15 | 0.26 | 0.26 | -0.01 | 51425.84 | 17.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
