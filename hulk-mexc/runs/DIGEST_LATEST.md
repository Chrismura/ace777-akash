# Hulk DIGEST — 2026-08-22T06:48:23Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.39 | 0.05 | 20400152.63 | 25.69 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 23.87 | 6.97 | 0.22 | 214143848.94 | 5.7 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 15.8 | 8.23 | 0.07 | 1392025.36 | 6.27 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.47 | -0.12 | 701927.57 | 6.71 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.28 | 0.07 | 617375.43 | 10.27 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.79 | -0.04 | 246528.96 | 3.31 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.64 | 0.05 | 162474.24 | 14.0 | skipped_fast |
| CCUSDT | IDLE | 2.01 | 11.25 | 3.96 | 0.18 | 783946.14 | 12.48 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 8.47 | 5.41 | 0.04 | 546316.95 | 46.69 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.21 | 0.04 | 200307.77 | 9.22 | skipped_fast |
| KITEUSDT | IDLE | 2.8 | 9.68 | 3.72 | 0.1 | 74411.33 | 10.85 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 87699.2 | 22.27 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 20.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 91.72 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.52 | 4.0 | 0.06 | 196871.81 | 15.41 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.06 | 0.09 | 59584.15 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.04 | 57982.7 | 8.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
