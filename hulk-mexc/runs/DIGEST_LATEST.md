# Hulk DIGEST — 2026-08-18T07:23:11Z

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
| XRPUSDT | IDLE | 0.6 | 1.16 | 0.28 | -0.01 | 12209089.47 | 1.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 29.58 | 12.91 | 0.18 | 72862.02 | 10.08 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 11.21 | 7.68 | -0.01 | 81655.25 | 26.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.28 | 6.57 | 0.72 | -0.08 | 300723.22 | 3.46 | skipped_fast |
| KITEUSDT | IDLE | 2.4 | 4.36 | 2.96 | -0.02 | 60407.17 | 16.26 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.86 | 0.6 | -0.05 | 292856.36 | 9.86 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 10.79 | 7.86 | -0.03 | 11604.8 | 60.2 | skipped_fast |
| ZBCNUSDT | IDLE | 0.94 | 1.7 | 1.18 | -0.01 | 215324.67 | 14.07 | skipped_fast |
| PYTHUSDT | IDLE | 0.95 | 1.81 | 0.6 | -0.03 | 181039.5 | 2.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.62 | 2.82 | 2.75 | -0.06 | 1654.71 | 18.0 | skipped_fast |
| WUSDT | IDLE | 0.84 | 1.63 | 0.4 | -0.03 | 144933.85 | 15.9 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.79 | 0.2 | -0.02 | 82070.06 | 4.1 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 3.2 | 2.15 | -0.01 | 76156.38 | 49.39 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.2 | 0.24 | 0.01 | 141025.69 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.88 | 0.78 | -0.04 | 134327.68 | 50.2 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.65 | 1.46 | -0.0 | 37156.79 | 5.37 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.78 | 0.78 | -0.0 | 49992.72 | 17.35 | skipped_fast |
| FLUIDUSDT | IDLE | 0.56 | 0.99 | 0.82 | -0.04 | 223.15 | 21.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
