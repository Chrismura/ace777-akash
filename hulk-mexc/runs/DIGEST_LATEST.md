# Hulk DIGEST — 2026-08-28T08:07:35Z

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
| PYTHUSDT | IDLE | 1.4 | 2.57 | 1.52 | 0.01 | 12713348.38 | 4.11 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 55.46 | 31.55 | -0.19 | 60287.39 | 49.93 | skipped_fast |
| XRPUSDT | IDLE | 0.74 | 1.34 | 0.97 | 0.0 | 55971732.83 | 2.81 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 7.0 | 1.23 | 0.08 | 693979.09 | 2.5 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.69 | 1.25 | -0.03 | 474217.56 | 6.23 | skipped_fast |
| KITEUSDT | IDLE | 2.08 | 3.8 | 2.4 | -0.01 | 72806.47 | 10.92 | skipped_fast |
| REDUSDT | IDLE | 2.07 | 3.68 | 3.1 | -0.02 | 81321.89 | 22.06 | skipped_fast |
| ZBCNUSDT | IDLE | 0.85 | 2.15 | 1.36 | 0.02 | 255195.88 | 12.0 | skipped_fast |
| WUSDT | IDLE | 0.94 | 1.72 | 1.07 | -0.01 | 201905.45 | 9.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.87 | 10.92 | 1.49 | -0.16 | 119415.77 | 51.22 | skipped_fast |
| TELUSDT | IDLE | 1.97 | 3.44 | 3.33 | -0.0 | 138079.1 | 5.46 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.34 | 0.42 | -0.0 | 92715.34 | 3.49 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.51 | 0.41 | 0.0 | 306228.01 | 1.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 4.28 | 4.1 | -0.03 | 20682.7 | 137.78 | skipped_fast |
| EDELUSDT | IDLE | 0.47 | 3.22 | 2.44 | 0.09 | 46014.97 | 51.77 | skipped_fast |
| FLUIDUSDT | IDLE | 1.43 | 2.68 | 1.16 | -0.02 | 7663.46 | 21.87 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.26 | 0.03 | -0.0 | 43281.07 | 7.98 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.33 | 0.01 | 54475.01 | 8.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
