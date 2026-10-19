# Hulk DIGEST — 2026-10-19T01:12:56Z

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
| XRPUSDT | IDLE | 2.13 | 4.26 | 0.06 | 0.01 | 29187978.53 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 1.9 | 3.78 | 0.09 | 0.01 | 127086661.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.13 | 2.25 | 0.09 | 0.01 | 264877371.36 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 5.98 | 0.03 | -0.04 | 1311143.66 | 2.65 | skipped_fast |
| WUSDT | IDLE | 1.87 | 4.84 | 0.14 | -0.04 | 816949.36 | 17.5 | skipped_fast |
| CCUSDT | IDLE | 3.3 | 6.48 | 0.75 | -0.01 | 290084.1 | 9.77 | skipped_fast |
| HBARUSDT | IDLE | 2.0 | 4.85 | 1.41 | -0.02 | 785619.37 | 5.91 | skipped_fast |
| ZBCNUSDT | IDLE | 3.12 | 6.69 | 0.07 | -0.01 | 262330.3 | 15.82 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.35 | 9.75 | 6.6 | -0.01 | 63198.71 | 5.31 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 6.22 | 0.77 | -0.02 | 593880.63 | 3.64 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 5.12 | 1.26 | 0.01 | 251202.23 | 3.77 | skipped_fast |
| REDUSDT | IDLE | 2.7 | 5.38 | 0.1 | -0.01 | 95628.84 | 10.08 | skipped_fast |
| CHIPUSDT | IDLE | 2.33 | 7.46 | 0.26 | -0.04 | 79074.98 | 9.61 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 4.91 | 0.0 | -0.03 | 81278.11 | 12.65 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 4.25 | 0.35 | -0.01 | 66750.88 | 12.16 | skipped_fast |
| IOTAUSDT | IDLE | 2.73 | 5.97 | 0.2 | -0.03 | 68242.14 | 46.48 | skipped_fast |
| LAUSDT | IDLE | 2.2 | 5.38 | 0.28 | -0.05 | 58821.49 | 22.59 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 3.1 | 2.54 | -0.05 | 58949.4 | 46.26 | skipped_fast |
| RWAUSDT | IDLE | 1.37 | 2.65 | 0.63 | 0.02 | 50579.75 | 7.88 | skipped_fast |
| WAXLUSDT | IDLE | 1.09 | 5.04 | 1.93 | 0.02 | 79817.81 | 31.1 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.75 | 0.0 | -0.04 | 4309.77 | 21.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.57 | 1.05 | 0.64 | -0.01 | 35612.79 | 55.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
