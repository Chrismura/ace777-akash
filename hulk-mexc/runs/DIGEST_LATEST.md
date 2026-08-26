# Hulk DIGEST — 2026-08-26T03:44:42Z

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
| PYTHUSDT | IDLE | 2.62 | 5.41 | 1.51 | -0.01 | 2195069.36 | 1.94 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.94 | 76.3 | 38.43 | 0.11 | 59459.88 | 64.94 | skipped_fast |
| XRPUSDT | IDLE | 1.03 | 2.06 | 1.0 | -0.06 | 62411802.24 | 2.09 | skipped_fast |
| FLUIDUSDT | IDLE | 4.07 | 23.85 | 2.82 | 0.15 | 7593.38 | 0.65 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.58 | 2.35 | -0.06 | 522995.95 | 10.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 4.71 | 1.31 | 0.0 | 403007.49 | 6.14 | skipped_fast |
| WUSDT | IDLE | 1.56 | 3.09 | 0.45 | -0.02 | 292453.86 | 10.52 | skipped_fast |
| KITEUSDT | IDLE | 2.23 | 4.28 | 1.26 | -0.02 | 60410.16 | 5.29 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.84 | 0.77 | -0.07 | 630680.64 | 1.28 | skipped_fast |
| REDUSDT | IDLE | 1.94 | 4.97 | 2.09 | 0.01 | 80741.55 | 12.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 2.81 | 1.27 | -0.03 | 159408.13 | 14.79 | skipped_fast |
| EDELUSDT | IDLE | 0.7 | 9.87 | 8.82 | 0.04 | 158947.04 | 36.76 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 1.76 | 1.15 | -0.02 | 93838.67 | 3.44 | skipped_fast |
| QAITUSDT | IDLE | 1.17 | 3.05 | 1.48 | 0.03 | 12825.21 | 30.02 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 1.62 | 1.25 | -0.02 | 2332.29 | 95.94 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 1.83 | 1.72 | -0.05 | 55624.15 | 16.65 | skipped_fast |
| QNTUSDT | IDLE | 0.55 | 1.05 | 0.34 | -0.03 | 133995.64 | 3.15 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 2.12 | 0.05 | -0.03 | 93443.21 | 49.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
