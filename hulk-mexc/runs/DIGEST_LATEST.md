# Hulk DIGEST — 2026-08-12T18:27:38Z

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
| XRPUSDT | IDLE | 0.65 | 1.19 | 0.75 | -0.0 | 16105913.83 | 1.98 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 32.19 | 18.06 | 0.09 | 45310.34 | 48.76 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 6.56 | 5.04 | 0.04 | 106084.2 | 8.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 3.46 | 2.99 | -0.02 | 190993.39 | 18.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 2.37 | 1.02 | -0.05 | 319522.91 | 2.46 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 5.62 | 1.5 | 0.06 | 61989.26 | 33.84 | skipped_fast |
| CCUSDT | IDLE | 1.55 | 2.83 | 1.83 | -0.02 | 229557.23 | 7.09 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 3.92 | 2.51 | -0.04 | 61051.01 | 15.9 | skipped_fast |
| WUSDT | IDLE | 1.57 | 2.84 | 2.05 | -0.0 | 181676.25 | 12.25 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 2.82 | 2.48 | 0.0 | 60209.04 | 17.55 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.73 | 0.93 | -0.02 | 62957.6 | 4.09 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.05 | 2.96 | -0.03 | 916.14 | 81.28 | skipped_fast |
| QAITUSDT | IDLE | 0.94 | 3.49 | 2.48 | -0.04 | 5137.76 | 60.7 | skipped_fast |
| QNTUSDT | IDLE | 1.51 | 2.69 | 2.16 | 0.02 | 61474.41 | 6.85 | skipped_fast |
| TELUSDT | IDLE | 1.46 | 2.69 | 1.56 | 0.03 | 106522.44 | 44.4 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.71 | 0.97 | -0.0 | 78926.17 | 1.51 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.02 | 52136.37 | 16.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.12 | 1.03 | -0.02 | 1052.71 | 21.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
