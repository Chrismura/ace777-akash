# Hulk DIGEST — 2026-10-27T23:18:43Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.56 | 1.03 | 0.61 | 0.02 | 236207139.16 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 1.03 | 0.47 | 0.01 | 324043561.92 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.54 | 1.06 | 0.11 | 0.03 | 20250467.81 | 2.26 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 3.95 | 0.75 | 0.04 | 466627.94 | 30.14 | skipped_fast |
| WUSDT | IDLE | 0.94 | 2.09 | 1.35 | 0.04 | 684119.55 | 19.57 | skipped_fast |
| ZBCNUSDT | IDLE | 2.26 | 6.93 | 6.19 | -0.02 | 237364.17 | 43.11 | skipped_fast |
| PYTHUSDT | IDLE | 1.34 | 2.43 | 1.66 | -0.02 | 393098.33 | 6.87 | skipped_fast |
| QNTUSDT | IDLE | 1.3 | 2.39 | 1.35 | -0.01 | 686482.97 | 5.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 3.57 | 1.74 | 0.06 | 131862.5 | 18.47 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 3.57 | 2.99 | -0.05 | 60485.36 | 26.83 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.44 | 0.89 | -0.01 | 222795.43 | 8.13 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 3.68 | 0.21 | 0.01 | 33224.58 | 57.77 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.83 | 1.01 | 0.02 | 59173.83 | 8.86 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.87 | 1.18 | 0.06 | 60086.6 | 14.19 | skipped_fast |
| KITEUSDT | IDLE | 0.73 | 1.47 | 0.16 | 0.05 | 57677.25 | 13.44 | skipped_fast |
| HBARUSDT | IDLE | 0.72 | 1.31 | 0.83 | -0.01 | 312177.43 | 9.21 | skipped_fast |
| IOTAUSDT | IDLE | 0.7 | 1.36 | 0.21 | 0.0 | 79081.13 | 30.76 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.72 | 0.72 | -0.01 | 58039.1 | 16.03 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 0.63 | 0.12 | 0.02 | 2583.56 | 21.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.44 | 0.81 | 0.45 | 0.0 | 37619.28 | 79.41 | skipped_fast |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
