# Hulk DIGEST — 2026-09-10T20:15:53Z

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
| XRPUSDT | IDLE | 0.88 | 1.66 | 0.67 | -0.03 | 45741521.41 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.71 | 0.26 | 0.0 | 456056484.65 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.93 | 0.28 | -0.01 | 554631949.72 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.85 | 3.5 | 1.39 | -0.03 | 837117.91 | 1.94 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 16.37 | 11.51 | 0.09 | 263205.49 | 36.1 | skipped_fast |
| CCUSDT | IDLE | 2.18 | 3.96 | 2.62 | -0.05 | 527239.6 | 9.07 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 41.82 | 14.26 | -0.49 | 124581.26 | 30.85 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 3.52 | 2.55 | 0.0 | 201467.5 | 18.6 | skipped_fast |
| WUSDT | IDLE | 1.64 | 3.07 | 1.45 | -0.05 | 193637.3 | 13.52 | skipped_fast |
| BIOUSDT | IDLE | 1.71 | 3.1 | 2.15 | -0.06 | 80492.33 | 3.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 5.95 | 0.75 | -0.11 | 85656.08 | 37.04 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 2.54 | 1.26 | -0.04 | 57944.53 | 10.0 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.48 | 1.2 | -0.06 | 67459.19 | 18.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.38 | 1.55 | -0.02 | 4955.09 | 16.87 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.63 | 0.16 | -0.02 | 256874.56 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 2.03 | 1.31 | -0.01 | 36826.85 | 6.1 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.92 | 0.89 | -0.01 | 87312.63 | 39.23 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 1.84 | 1.81 | -0.07 | 1805.54 | 21.31 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.99 | 0.45 | -0.04 | 52408.64 | 7.58 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.62 | 0.0 | -0.02 | 31469.68 | 5.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
