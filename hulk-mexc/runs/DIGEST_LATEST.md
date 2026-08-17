# Hulk DIGEST — 2026-08-17T04:07:46Z

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
| XRPUSDT | IDLE | 0.82 | 1.62 | 0.15 | 0.0 | 8152019.61 | 1.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 26.44 | 17.13 | 0.07 | 44121.05 | 20.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 7.11 | 1.77 | 0.05 | 292037.07 | 6.93 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.6 | 0.97 | -0.02 | 288183.77 | 6.28 | skipped_fast |
| EDELUSDT | IDLE | 1.83 | 3.58 | 0.51 | 0.04 | 55281.48 | 38.73 | skipped_fast |
| WUSDT | IDLE | 0.93 | 1.66 | 1.36 | 0.01 | 188629.62 | 11.73 | skipped_fast |
| PYTHUSDT | IDLE | 0.94 | 1.88 | 0.05 | -0.01 | 151927.34 | 2.57 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.62 | 1.45 | -0.01 | 54564.56 | 15.91 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 1.48 | 0.8 | -0.0 | 194447.83 | 15.31 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.15 | 2.1 | -0.06 | 59440.52 | 29.35 | skipped_fast |
| BIOUSDT | IDLE | 0.75 | 1.46 | 0.21 | -0.01 | 64227.02 | 4.11 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 3.35 | 0.54 | 0.0 | 90492.87 | 40.79 | skipped_fast |
| QNTUSDT | IDLE | 1.28 | 2.28 | 1.93 | -0.03 | 32508.04 | 5.36 | skipped_fast |
| RWAINCUSDT | IDLE | 0.65 | 1.25 | 0.34 | 0.01 | 3226.81 | 73.3 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.15 | 0.22 | -0.0 | 88372.5 | 1.54 | skipped_fast |
| QAITUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 2142.08 | 61.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.14 | 0.15 | 0.01 | 411.11 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.88 | 0.09 | 0.01 | 50485.13 | 34.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
