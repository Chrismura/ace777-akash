# Hulk DIGEST — 2026-10-12T11:29:30Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.04 | 13.96 | 1.45 | 0.16 | 1899760.18 | 16.87 | skipped_fast |
| WUSDT | IDLE | 1.06 | 20.44 | 12.84 | 0.58 | 14919752.85 | 14.46 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.42 | 1.17 | 0.02 | 259961249.25 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.32 | 1.21 | 0.01 | 24166668.26 | 1.43 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.22 | 1.08 | 0.0 | 241836142.45 | 0.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 25.76 | 13.33 | 0.12 | 169909.06 | 19.39 | skipped_fast |
| QNTUSDT | IDLE | 2.39 | 4.25 | 3.48 | -0.04 | 841699.53 | 5.57 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 11.51 | 6.8 | 0.02 | 29072.8 | 43.98 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 4.03 | 3.87 | -0.06 | 232821.81 | 8.18 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.13 | 2.08 | 0.03 | 396056.07 | 4.82 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 6.08 | 2.81 | -0.05 | 193058.2 | 12.45 | skipped_fast |
| KITEUSDT | IDLE | 2.29 | 4.44 | 0.87 | 0.04 | 63120.36 | 11.38 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.9 | 0.94 | 0.06 | 278287.5 | 12.1 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 2.43 | 1.91 | 0.02 | 479502.49 | 7.52 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 2.15 | 1.81 | 0.0 | 101582.01 | 3.4 | skipped_fast |
| RIZEUSDT | IDLE | 1.2 | 6.62 | 3.97 | 0.14 | 48459.91 | 39.26 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 3.78 | 0.5 | 0.03 | 182459.33 | 45.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.51 | 2.76 | 1.8 | -0.01 | 22732.29 | 21.53 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.54 | 0.46 | 0.02 | 52417.53 | 7.73 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.29 | 0.14 | 0.0 | 38492.95 | 12.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
