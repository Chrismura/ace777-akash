# Hulk DIGEST — 2026-08-17T17:11:54Z

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
| XRPUSDT | IDLE | 0.61 | 1.13 | 0.61 | -0.0 | 13094619.56 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 10.15 | 7.6 | 0.02 | 340821.88 | 3.43 | skipped_fast |
| RIZEUSDT | IDLE | 2.03 | 19.21 | 14.91 | 0.12 | 85742.22 | 46.43 | skipped_fast |
| CCUSDT | IDLE | 2.37 | 4.14 | 3.98 | -0.04 | 238430.75 | 12.05 | skipped_fast |
| EDELUSDT | IDLE | 2.94 | 5.45 | 4.8 | 0.02 | 65115.45 | 51.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.91 | 3.71 | 0.71 | -0.01 | 178263.38 | 15.87 | skipped_fast |
| REDUSDT | IDLE | 2.4 | 4.78 | 0.18 | -0.01 | 57707.06 | 39.33 | skipped_fast |
| TELUSDT | IDLE | 2.72 | 4.79 | 4.36 | -0.04 | 108432.46 | 42.74 | skipped_fast |
| WUSDT | IDLE | 0.64 | 1.14 | 0.87 | -0.03 | 153742.61 | 10.79 | skipped_fast |
| PYTHUSDT | IDLE | 0.63 | 1.16 | 0.69 | -0.01 | 141076.36 | 2.56 | skipped_fast |
| QAITUSDT | IDLE | 1.57 | 2.87 | 1.8 | -0.02 | 831.63 | 62.04 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 1.45 | 1.34 | -0.03 | 59784.45 | 15.18 | skipped_fast |
| BIOUSDT | IDLE | 0.6 | 1.1 | 0.69 | -0.0 | 73191.34 | 8.13 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 3.77 | 0.83 | 0.0 | 37111.29 | 5.24 | skipped_fast |
| FLUIDUSDT | IDLE | 2.07 | 3.61 | 3.49 | -0.03 | 815.84 | 22.48 | skipped_fast |
| RWAINCUSDT | IDLE | 1.1 | 1.92 | 1.88 | -0.0 | 1860.75 | 81.35 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.44 | 0.57 | 0.01 | 125264.39 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.96 | 0.17 | 0.01 | 49649.06 | 25.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
