# Hulk DIGEST — 2026-08-17T22:16:32Z

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
| XRPUSDT | IDLE | 0.3 | 0.56 | 0.32 | 0.01 | 12411435.53 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 0.98 | 4.24 | 3.52 | -0.02 | 333926.63 | 3.54 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.74 | 1.12 | -0.04 | 247827.16 | 6.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 2.04 | 1.69 | 0.01 | 205003.48 | 15.22 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 3.69 | 1.52 | 0.02 | 66338.76 | 38.63 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.49 | 2.19 | 0.02 | 79695.13 | 4.07 | skipped_fast |
| TELUSDT | IDLE | 2.63 | 5.93 | 2.38 | -0.03 | 136675.19 | 35.83 | skipped_fast |
| PYTHUSDT | IDLE | 0.97 | 1.74 | 1.28 | 0.0 | 146388.6 | 2.59 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.61 | 0.94 | -0.03 | 1000.03 | 52.68 | skipped_fast |
| REDUSDT | IDLE | 1.13 | 2.11 | 0.97 | -0.0 | 58591.35 | 18.47 | skipped_fast |
| WUSDT | IDLE | 0.72 | 1.31 | 0.8 | -0.03 | 136227.9 | 15.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.56 | 4.72 | 2.48 | 0.09 | 85437.94 | 47.76 | skipped_fast |
| KITEUSDT | IDLE | 0.56 | 1.03 | 0.66 | -0.01 | 60671.45 | 11.9 | skipped_fast |
| RWAINCUSDT | IDLE | 0.41 | 0.76 | 0.41 | -0.04 | 1108.46 | 58.58 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 1.35 | 1.18 | 0.01 | 35242.8 | 5.27 | skipped_fast |
| HBARUSDT | IDLE | 0.34 | 0.62 | 0.39 | 0.01 | 112580.35 | 1.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.62 | 1.24 | 0.0 | -0.02 | 772.33 | 24.14 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.61 | 0.43 | 0.01 | 49748.24 | 25.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
