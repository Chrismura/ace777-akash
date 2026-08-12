# Hulk DIGEST — 2026-08-12T17:24:10Z

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
| XRPUSDT | IDLE | 1.09 | 1.9 | 1.82 | -0.0 | 16706875.95 | 1.99 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 33.18 | 18.15 | 0.08 | 44505.62 | 48.76 | skipped_fast |
| ZBCNUSDT | IDLE | 2.27 | 4.03 | 3.45 | -0.02 | 190718.43 | 12.61 | skipped_fast |
| EDELUSDT | IDLE | 2.87 | 6.56 | 1.66 | 0.07 | 62912.88 | 33.78 | skipped_fast |
| WUSDT | IDLE | 2.12 | 3.75 | 3.32 | -0.01 | 183109.47 | 14.75 | skipped_fast |
| PYTHUSDT | IDLE | 1.34 | 2.52 | 1.09 | -0.05 | 334921.87 | 2.46 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 3.15 | 1.74 | -0.01 | 223694.67 | 11.1 | skipped_fast |
| CHIPUSDT | IDLE | 2.15 | 4.94 | 1.12 | 0.06 | 76990.04 | 8.44 | skipped_fast |
| KITEUSDT | IDLE | 2.17 | 3.99 | 2.36 | -0.03 | 61168.43 | 13.87 | skipped_fast |
| REDUSDT | IDLE | 1.58 | 2.82 | 2.33 | 0.0 | 59935.27 | 31.54 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.85 | 1.05 | -0.02 | 63242.48 | 8.16 | skipped_fast |
| QAITUSDT | IDLE | 1.03 | 4.07 | 1.1 | -0.02 | 5872.54 | 51.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 2.04 | 1.95 | -0.02 | 904.14 | 70.1 | skipped_fast |
| QNTUSDT | IDLE | 1.49 | 2.69 | 1.98 | 0.03 | 65664.61 | 6.83 | skipped_fast |
| TELUSDT | IDLE | 1.52 | 2.69 | 2.31 | 0.03 | 106435.06 | 44.77 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.03 | 1.43 | -0.0 | 77879.38 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.02 | 51955.29 | 8.33 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.55 | 1.45 | -0.03 | 1130.06 | 22.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
