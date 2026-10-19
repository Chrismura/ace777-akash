# Hulk DIGEST — 2026-10-19T22:05:29Z

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
| ETHUSDT | IDLE | 0.4 | 0.78 | 0.11 | 0.01 | 136119497.68 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.76 | 0.06 | 0.01 | 22645243.61 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 0.26 | 0.49 | 0.14 | 0.01 | 336345712.75 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.89 | 3.58 | 1.39 | -0.0 | 820485.2 | 4.09 | skipped_fast |
| WUSDT | IDLE | 2.47 | 4.69 | 1.61 | 0.03 | 697002.01 | 16.56 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.32 | 0.64 | 0.04 | 742656.24 | 5.11 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.95 | 1.98 | 0.02 | 202920.85 | 22.36 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.57 | 0.0 | 0.06 | 410203.32 | 9.55 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 2.64 | 1.44 | 0.02 | 243921.1 | 7.68 | skipped_fast |
| KITEUSDT | IDLE | 1.62 | 3.71 | 0.04 | 0.09 | 71200.64 | 7.24 | skipped_fast |
| HBARUSDT | IDLE | 0.69 | 1.35 | 0.22 | -0.02 | 479527.12 | 4.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 2.25 | 0.76 | 0.04 | 78748.01 | 16.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 2.01 | 1.37 | 0.04 | 72263.37 | 10.23 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.94 | 0.32 | 0.01 | 56608.99 | 16.73 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 1.55 | 0.04 | 0.01 | 69468.34 | 12.74 | skipped_fast |
| RIZEUSDT | IDLE | 0.39 | 1.3 | 0.69 | -0.04 | 53241.2 | 29.94 | skipped_fast |
| WAXLUSDT | IDLE | 1.13 | 2.91 | 1.89 | -0.04 | 62491.38 | 25.22 | skipped_fast |
| IOTAUSDT | IDLE | 0.94 | 1.85 | 0.22 | 0.02 | 90564.37 | 26.7 | skipped_fast |
| LAUSDT | IDLE | 0.79 | 1.54 | 0.27 | 0.0 | 56091.59 | 41.99 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.95 | 0.08 | 0.02 | 55870.16 | 7.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.11 | 0.0 | 40748.6 | 21.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.05 | 4749.48 | 19.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
