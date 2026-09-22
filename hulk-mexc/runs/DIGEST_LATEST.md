# Hulk DIGEST — 2026-09-22T12:10:17Z

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
| XRPUSDT | IDLE | 1.54 | 2.93 | 0.94 | 0.03 | 109254225.32 | 1.95 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.42 | 0.45 | 0.01 | 1011350588.6 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.19 | 0.4 | 0.01 | 561863687.09 | 0.04 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 5.11 | 3.66 | 0.05 | 1248075.04 | 1.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.95 | 3.73 | 1.93 | -0.02 | 767535.17 | 3.2 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 6.86 | 5.62 | -0.05 | 166193.52 | 17.4 | skipped_fast |
| CCUSDT | IDLE | 1.39 | 2.56 | 1.42 | 0.03 | 558246.01 | 6.76 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 9.95 | 4.62 | 0.12 | 247088.56 | 18.28 | skipped_fast |
| QNTUSDT | IDLE | 3.52 | 8.97 | 3.38 | 0.05 | 150644.1 | 9.94 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.23 | 8.2 | 0.9 | 0.11 | 115939.81 | 8.25 | skipped_fast |
| REDUSDT | IDLE | 2.39 | 4.35 | 2.84 | 0.02 | 91277.84 | 9.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 3.01 | 1.88 | -0.03 | 268383.55 | 20.8 | skipped_fast |
| WUSDT | IDLE | 1.02 | 1.93 | 0.8 | -0.01 | 371187.72 | 5.92 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.47 | 1.86 | -0.02 | 127090.29 | 3.5 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 2.02 | 0.33 | 0.07 | 26476.0 | 5.51 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 3.65 | 0.43 | 0.02 | 109289.54 | 6.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.36 | 3.36 | 1.6 | -0.17 | 48791.08 | 115.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.11 | 2.07 | 1.04 | 0.02 | 8942.69 | 12.83 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.58 | 0.36 | -0.0 | 54835.73 | 7.29 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.36 | 0.03 | 0.01 | 40417.3 | 2.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
