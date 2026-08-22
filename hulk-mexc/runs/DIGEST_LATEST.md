# Hulk DIGEST — 2026-08-22T11:43:22Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.97 | 0.0 | 51616530.51 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.65 | 0.08 | 216818716.53 | 2.02 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.54 | 0.13 | 788003.78 | 8.56 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.35 | 0.01 | 1257574.92 | 7.75 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.65 | 0.02 | 583320.05 | 13.75 | skipped_fast |
| ZBCNUSDT | IDLE | 2.28 | 5.93 | 4.11 | -0.03 | 388680.46 | 20.05 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.75 | -0.11 | 636067.69 | 3.36 | skipped_fast |
| KITEUSDT | IDLE | 2.34 | 5.62 | 0.22 | 0.04 | 80467.78 | 9.74 | skipped_fast |
| EDELUSDT | IDLE | 2.7 | 4.93 | 3.17 | -0.03 | 79039.24 | 67.8 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.26 | -0.04 | 243495.96 | 3.21 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.56 | -0.03 | 167344.54 | 42.85 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | -0.01 | 2459.51 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 3.87 | 0.04 | 154752.25 | 12.53 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10923.76 | 76.09 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.95 | -0.03 | 48664.76 | 27.5 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.76 | 0.01 | 188429.73 | 6.23 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.31 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57677.8 | 24.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
