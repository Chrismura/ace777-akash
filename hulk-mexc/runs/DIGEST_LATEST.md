# Hulk DIGEST — 2026-08-21T20:40:44Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.7 | 0.08 | 5543404.06 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.26 | 0.1 | 129003309.37 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.32 | 0.18 | 153958.96 | 19.38 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.75 | 0.12 | 478664.36 | 44.09 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.22 | 0.09 | 639188.43 | 9.2 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.23 | 1.94 | 0.05 | 809659.05 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 4.81 | 2.98 | 0.09 | 514089.58 | 3.07 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.56 | 0.06 | 367744.58 | 13.72 | skipped_fast |
| BIOUSDT | IDLE | 2.54 | 5.33 | 2.94 | 0.01 | 189192.36 | 6.32 | skipped_fast |
| EDELUSDT | IDLE | 2.82 | 5.01 | 4.55 | -0.05 | 81394.04 | 22.65 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10892.53 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.66 | 0.02 | 56286.69 | 47.09 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.46 | 0.11 | 60893.16 | 13.96 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 181801.71 | 26.83 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.69 | 0.04 | 59891.93 | 4.69 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53905.52 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
