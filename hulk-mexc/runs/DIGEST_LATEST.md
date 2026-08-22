# Hulk DIGEST — 2026-08-22T08:44:18Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.58 | 0.04 | 32152367.71 | 21.79 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 23.87 | 11.79 | 0.1 | 224507722.68 | 4.67 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 15.8 | 10.39 | 0.01 | 1330015.7 | 5.13 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.53 | -0.1 | 688642.89 | 13.41 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.11 | 0.02 | 602093.45 | 18.85 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.02 | -0.06 | 257265.06 | 12.8 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.51 | 0.04 | 155393.55 | 12.42 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 11.25 | 3.17 | 0.16 | 805287.9 | 7.43 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 8.47 | 6.56 | -0.0 | 507034.97 | 23.61 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.36 | 0.02 | 192867.66 | 6.22 | skipped_fast |
| KITEUSDT | IDLE | 3.79 | 9.68 | 3.72 | 0.05 | 73680.82 | 21.73 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 4.52 | 3.78 | -0.05 | 86818.4 | 33.65 | skipped_fast |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6885.76 | 37.7 | skipped_fast |
| TELUSDT | IDLE | 2.33 | 5.85 | 5.48 | -0.02 | 174665.34 | 52.25 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 1.99 | 0.02 | 11077.63 | 128.82 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.86 | 3.73 | 1.42 | 0.01 | 52245.01 | 46.44 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.04 | 58325.5 | 16.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
