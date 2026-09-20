# Hulk DIGEST — 2026-09-20T07:01:44Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.54 | 2.81 | 1.79 | -0.03 | 54812659.23 | 2.9 | skipped_fast |
| ETHUSDT | IDLE | 1.3 | 2.32 | 1.85 | -0.02 | 260469946.32 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.29 | 1.04 | -0.01 | 504906805.42 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.65 | 6.47 | 5.58 | -0.03 | 711007.73 | 1.71 | skipped_fast |
| WUSDT | IDLE | 2.54 | 4.91 | 1.19 | 0.04 | 527728.34 | 8.88 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 4.36 | 3.69 | -0.05 | 334866.15 | 5.74 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.34 | 1.53 | 0.03 | 713280.18 | 1.24 | skipped_fast |
| CHIPUSDT | IDLE | 2.28 | 5.26 | 4.88 | -0.08 | 105447.45 | 16.94 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 4.12 | 3.46 | 0.0 | 89336.3 | 7.39 | skipped_fast |
| REDUSDT | IDLE | 2.49 | 4.95 | 0.2 | 0.03 | 86254.15 | 15.67 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 5.2 | 4.14 | -0.12 | 90055.93 | 15.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.05 | 3.67 | 2.01 | 0.05 | 222834.84 | 25.61 | skipped_fast |
| RIZEUSDT | IDLE | 2.06 | 7.87 | 2.64 | -0.05 | 34864.17 | 103.41 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 2.33 | 1.08 | -0.01 | 75962.53 | 11.45 | skipped_fast |
| QNTUSDT | IDLE | 1.76 | 3.11 | 2.68 | 0.01 | 54941.11 | 7.79 | skipped_fast |
| RWAINCUSDT | IDLE | 0.31 | 0.66 | 0.65 | -0.04 | 7111.81 | 5.96 | skipped_fast |
| TELUSDT | IDLE | 1.15 | 2.41 | 1.55 | -0.06 | 103928.15 | 27.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.1 | 1.6 | 0.0 | 7907.48 | 21.78 | skipped_fast |
| RWAUSDT | IDLE | 0.74 | 1.34 | 0.88 | -0.01 | 52591.55 | 22.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.75 | 0.4 | -0.01 | 33923.37 | 50.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
