# Hulk DIGEST — 2026-08-18T15:39:11Z

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
| XRPUSDT | IDLE | 0.6 | 1.16 | 0.25 | -0.0 | 11417372.88 | 1.99 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 9.74 | 8.64 | -0.1 | 242865.76 | 7.56 | skipped_fast |
| QAITUSDT | IDLE | 2.05 | 27.25 | 17.22 | -0.18 | 17578.25 | 63.09 | skipped_fast |
| REDUSDT | IDLE | 1.53 | 11.8 | 9.91 | 0.11 | 121740.43 | 18.23 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.61 | 1.43 | -0.02 | 244555.71 | 9.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 5.4 | 5.07 | -0.09 | 52076.52 | 42.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.89 | 0.95 | -0.0 | 201135.19 | 13.3 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.78 | 0.4 | 0.0 | 74725.74 | 4.05 | skipped_fast |
| PYTHUSDT | IDLE | 0.9 | 1.77 | 0.21 | -0.01 | 191867.54 | 2.6 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 4.34 | 2.99 | -0.03 | 74838.54 | 53.4 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.17 | 0.53 | -0.01 | 65324.52 | 16.33 | skipped_fast |
| RWAINCUSDT | IDLE | 1.16 | 2.46 | 0.64 | -0.01 | 5068.18 | 17.71 | skipped_fast |
| WUSDT | IDLE | 0.48 | 0.93 | 0.2 | -0.03 | 139107.81 | 12.26 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 4.42 | 0.55 | 0.03 | 116186.49 | 48.06 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.96 | 0.42 | 0.0 | 115678.6 | 1.51 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 1.73 | 0.07 | -0.01 | 36038.3 | 3.54 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.69 | -0.01 | 50388.36 | 17.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.82 | 0.0 | -0.04 | 145.03 | 22.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
