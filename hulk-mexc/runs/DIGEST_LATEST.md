# Hulk DIGEST — 2026-09-10T17:15:49Z

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
| XRPUSDT | IDLE | 1.59 | 2.9 | 1.87 | -0.05 | 45044614.42 | 2.21 | skipped_fast |
| ETHUSDT | IDLE | 1.32 | 2.55 | 0.55 | -0.02 | 435137344.68 | 1.06 | skipped_fast |
| BTCUSDT | IDLE | 0.87 | 1.59 | 0.97 | -0.02 | 548384630.18 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.73 | 4.44 | 2.61 | -0.09 | 898026.81 | 1.94 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 56.91 | 25.04 | -0.56 | 124970.63 | 138.89 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 16.37 | 11.99 | 0.07 | 260169.37 | 27.26 | skipped_fast |
| CCUSDT | IDLE | 1.84 | 3.35 | 2.24 | -0.04 | 584343.66 | 3.01 | skipped_fast |
| ZBCNUSDT | IDLE | 2.52 | 4.54 | 3.28 | -0.0 | 192655.4 | 50.54 | skipped_fast |
| WUSDT | IDLE | 1.0 | 2.81 | 0.76 | -0.07 | 229612.42 | 11.45 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 3.3 | 1.17 | -0.06 | 81465.41 | 3.94 | skipped_fast |
| CHIPUSDT | IDLE | 0.89 | 4.83 | 3.58 | -0.19 | 89826.44 | 2.13 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.93 | 1.56 | -0.08 | 67811.21 | 10.7 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 2.8 | 0.84 | -0.04 | 56740.55 | 14.62 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.26 | 1.32 | -0.04 | 270752.3 | 1.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 1.7 | 0.22 | -0.02 | 5140.32 | 39.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.75 | 3.36 | 2.33 | -0.07 | 2232.87 | 20.88 | skipped_fast |
| TELUSDT | IDLE | 1.47 | 2.68 | 1.78 | -0.02 | 80558.96 | 28.26 | skipped_fast |
| RWAUSDT | IDLE | 1.14 | 2.06 | 1.5 | -0.05 | 52465.1 | 7.6 | skipped_fast |
| QNTUSDT | IDLE | 1.22 | 2.33 | 0.72 | -0.02 | 35946.8 | 6.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.96 | 1.76 | 1.09 | -0.03 | 28749.98 | 19.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
