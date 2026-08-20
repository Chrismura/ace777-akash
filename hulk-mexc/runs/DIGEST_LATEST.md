# Hulk DIGEST — 2026-08-20T04:21:41Z

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
| XRPUSDT | IDLE | 0.83 | 2.58 | 1.8 | 0.1 | 46005087.1 | 1.83 | skipped_fast |
| CCUSDT | IDLE | 1.25 | 4.08 | 1.89 | 0.12 | 381141.68 | 4.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 5.71 | 1.44 | 0.12 | 207345.83 | 3.47 | skipped_fast |
| RIZEUSDT | IDLE | 3.26 | 22.95 | 4.86 | 0.18 | 58909.29 | 251.11 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 11.14 | 7.29 | 0.22 | 99128.95 | 21.81 | skipped_fast |
| WUSDT | IDLE | 1.35 | 2.93 | 2.59 | 0.06 | 272353.97 | 15.21 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 5.81 | 1.51 | 0.15 | 168915.18 | 6.97 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 3.98 | 2.39 | 0.14 | 237788.73 | 15.2 | skipped_fast |
| PYTHUSDT | IDLE | 0.77 | 2.41 | 0.26 | 0.1 | 291109.05 | 2.34 | skipped_fast |
| REDUSDT | IDLE | 1.5 | 7.09 | 0.0 | 0.14 | 102458.83 | 23.65 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.71 | 0.62 | 0.05 | 356991.79 | 1.41 | skipped_fast |
| QAITUSDT | IDLE | 1.19 | 3.23 | 1.06 | 0.05 | 10308.39 | 30.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.71 | 1.68 | 0.04 | 17311.81 | 5.69 | skipped_fast |
| KITEUSDT | IDLE | 0.62 | 1.15 | 1.07 | 0.06 | 59085.33 | 22.94 | skipped_fast |
| FLUIDUSDT | IDLE | 1.72 | 4.41 | 4.22 | 0.05 | 3480.84 | 23.27 | skipped_fast |
| TELUSDT | IDLE | 0.53 | 2.37 | 1.59 | 0.11 | 190386.98 | 49.6 | skipped_fast |
| QNTUSDT | IDLE | 0.68 | 1.31 | 0.35 | 0.05 | 36715.12 | 8.46 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.69 | 0.52 | 0.01 | 54040.79 | 17.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
