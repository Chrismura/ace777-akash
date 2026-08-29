# Hulk DIGEST — 2026-08-29T23:12:29Z

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
| XRPUSDT | IDLE | 0.46 | 0.83 | 0.6 | 0.01 | 16478255.31 | 2.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.78 | 5.18 | 3.76 | -0.02 | 889347.0 | 2.48 | skipped_fast |
| ZBCNUSDT | IDLE | 2.78 | 5.15 | 2.71 | -0.02 | 199491.02 | 13.53 | skipped_fast |
| RIZEUSDT | IDLE | 3.2 | 8.97 | 2.41 | -0.01 | 41478.88 | 59.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.78 | 1.91 | 0.01 | 322802.6 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.23 | 0.66 | 0.06 | 231208.47 | 3.38 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.61 | 0.77 | 0.02 | 75660.15 | 14.62 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 3.19 | 1.66 | 0.02 | 68429.28 | 8.48 | skipped_fast |
| TELUSDT | IDLE | 2.51 | 4.4 | 4.1 | -0.03 | 70213.79 | 29.7 | skipped_fast |
| WUSDT | IDLE | 0.57 | 1.02 | 0.85 | -0.0 | 176919.73 | 6.58 | skipped_fast |
| BIOUSDT | IDLE | 0.45 | 0.84 | 0.36 | -0.01 | 66673.73 | 3.63 | skipped_fast |
| EDELUSDT | IDLE | 0.16 | 3.0 | 0.97 | 0.09 | 124881.7 | 26.7 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.32 | 2.21 | -0.03 | 1574.56 | 112.87 | skipped_fast |
| QNTUSDT | IDLE | 0.84 | 1.56 | 0.77 | 0.01 | 29865.36 | 3.25 | skipped_fast |
| HBARUSDT | IDLE | 0.29 | 0.54 | 0.22 | -0.01 | 148045.3 | 1.32 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.33 | 0.0 | 54066.64 | 24.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.06 | 0.11 | 0.11 | -0.0 | 1915.06 | 21.31 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
