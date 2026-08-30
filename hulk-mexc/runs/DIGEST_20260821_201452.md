# Hulk DIGEST — 2026-08-21T20:14:52Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.34 | 0.08 | 5482531.68 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.47 | 0.11 | 128937103.81 | 0.73 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.38 | 0.17 | 153870.8 | 17.21 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 10.86 | 6.09 | 0.11 | 477688.23 | 31.18 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.79 | 0.07 | 632401.22 | 10.28 | skipped_fast |
| HBARUSDT | IDLE | 1.75 | 3.23 | 2.32 | 0.06 | 796054.1 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.82 | 0.08 | 512713.41 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.14 | 3.92 | 2.45 | 0.05 | 367298.51 | 14.92 | skipped_fast |
| BIOUSDT | IDLE | 2.56 | 5.33 | 3.16 | 0.02 | 190143.8 | 3.17 | skipped_fast |
| EDELUSDT | IDLE | 2.51 | 4.41 | 4.12 | -0.05 | 80160.15 | 11.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.68 | 0.01 | 56225.68 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.04 | 11178.26 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.82 | 0.1 | 61284.86 | 11.2 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2806.14 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 3.39 | 2.17 | 0.01 | 183536.64 | 43.27 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.65 | 1.49 | 0.04 | 59935.75 | 6.25 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 54508.48 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
