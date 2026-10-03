# Hulk DIGEST — 2026-10-03T15:49:57Z

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
| QNTUSDT | IDLE | 1.23 | 5.6 | 4.01 | 0.0 | 3509167.08 | 6.82 | skipped_fast |
| XRPUSDT | IDLE | 0.37 | 0.74 | 0.05 | -0.01 | 37219420.35 | 2.01 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.46 | 0.12 | -0.01 | 463038871.9 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.19 | 0.35 | 0.2 | -0.01 | 203679032.84 | 0.15 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 16.15 | 13.47 | -0.04 | 45615.77 | 25.03 | skipped_fast |
| EDELUSDT | IDLE | 0.82 | 7.02 | 0.74 | 0.33 | 718409.88 | 23.33 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.91 | 2.54 | -0.02 | 531256.93 | 7.68 | skipped_fast |
| REDUSDT | IDLE | 2.75 | 7.64 | 0.0 | 0.03 | 66731.87 | 17.86 | skipped_fast |
| ZBCNUSDT | IDLE | 2.12 | 3.91 | 2.26 | -0.02 | 238290.59 | 26.16 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.93 | 0.56 | -0.02 | 751655.71 | 3.92 | skipped_fast |
| WUSDT | IDLE | 1.28 | 3.43 | 0.34 | -0.03 | 389275.34 | 10.25 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 1.74 | 0.81 | -0.01 | 369846.47 | 9.01 | skipped_fast |
| BIOUSDT | IDLE | 1.67 | 3.46 | 0.35 | 0.0 | 76437.82 | 9.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.42 | 2.83 | 0.02 | -0.01 | 80449.74 | 15.79 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.05 | 1.65 | 0.0 | 84276.57 | 7.33 | skipped_fast |
| RWAINCUSDT | IDLE | 1.25 | 3.02 | 1.71 | 0.02 | 4939.95 | 4.15 | skipped_fast |
| TELUSDT | IDLE | 1.61 | 4.74 | 3.36 | -0.1 | 138696.42 | 21.15 | skipped_fast |
| MNSRYUSDT | IDLE | 1.24 | 2.35 | 0.86 | -0.01 | 33646.02 | 21.98 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.44 | 0.29 | -0.01 | 54990.63 | 14.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.39 | 0.74 | 0.31 | 0.02 | 2238.47 | 20.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
