# Hulk DIGEST — 2026-10-28T12:33:01Z

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
| XRPUSDT | IDLE | 1.09 | 1.93 | 1.63 | 0.01 | 20544496.18 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 1.04 | 1.83 | 1.71 | 0.01 | 241472275.35 | 0.3 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.15 | 1.1 | 0.01 | 312653895.65 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 11.76 | 8.46 | -0.02 | 167903.18 | 17.23 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.45 | 6.1 | 5.31 | 0.0 | 298977.01 | 9.08 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.0 | 9.66 | 0.19 | 0.07 | 49890.76 | 49.91 | skipped_fast |
| WUSDT | IDLE | 0.95 | 1.71 | 1.31 | 0.0 | 618355.66 | 25.09 | skipped_fast |
| PYTHUSDT | IDLE | 1.36 | 2.45 | 1.81 | -0.02 | 417459.96 | 2.8 | skipped_fast |
| QNTUSDT | IDLE | 2.21 | 3.93 | 3.29 | -0.03 | 460737.98 | 13.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.69 | 3.17 | 2.32 | -0.05 | 220977.37 | 32.91 | skipped_fast |
| EDELUSDT | IDLE | 1.25 | 2.26 | 1.63 | 0.01 | 277215.4 | 27.64 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.08 | 1.74 | -0.01 | 424458.24 | 10.58 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.87 | 1.53 | 0.02 | 85427.33 | 13.29 | skipped_fast |
| KITEUSDT | IDLE | 0.86 | 1.5 | 1.42 | 0.01 | 60804.42 | 11.25 | skipped_fast |
| RIZEUSDT | IDLE | 1.01 | 1.79 | 1.53 | 0.02 | 36405.74 | 36.66 | skipped_fast |
| REDUSDT | IDLE | 0.66 | 1.19 | 0.89 | 0.03 | 54019.86 | 15.77 | skipped_fast |
| IOTAUSDT | IDLE | 1.16 | 2.04 | 1.88 | -0.01 | 75481.79 | 23.95 | skipped_fast |
| WAXLUSDT | IDLE | 1.2 | 2.15 | 1.62 | 0.0 | 56306.8 | 24.7 | skipped_fast |
| LAUSDT | IDLE | 0.97 | 1.73 | 1.36 | 0.02 | 59500.14 | 22.13 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.37 | 0.24 | 0.01 | 54973.04 | 39.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.65 | 0.0 | 0.02 | 6677.14 | 21.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.25 | 0.12 | 0.01 | 36222.27 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
