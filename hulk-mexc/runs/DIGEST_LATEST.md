# Hulk DIGEST — 2026-10-10T17:54:45Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 10.11 | 6.91 | 0.01 | 1228668.46 | 11.9 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.84 | 0.36 | 0.01 | 88158338.86 | 0.16 | skipped_fast |
| XRPUSDT | IDLE | 0.39 | 0.7 | 0.53 | 0.01 | 14951014.57 | 1.42 | skipped_fast |
| QNTUSDT | IDLE | 3.66 | 6.57 | 4.97 | -0.01 | 1216197.93 | 2.89 | skipped_fast |
| BTCUSDT | IDLE | 0.23 | 0.46 | 0.02 | 0.01 | 180194681.28 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 2.34 | 0.58 | -0.03 | 868540.44 | 2.53 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.04 | 15.68 | 1.21 | 0.2 | 118192.04 | 10.19 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.47 | 2.35 | -0.03 | 383372.85 | 10.14 | skipped_fast |
| EDELUSDT | IDLE | 1.89 | 3.9 | 2.33 | -0.04 | 220443.18 | 12.97 | skipped_fast |
| KITEUSDT | IDLE | 1.7 | 4.64 | 1.62 | 0.08 | 72404.69 | 16.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 1.96 | 0.71 | 0.01 | 199398.39 | 8.71 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.24 | 1.45 | -0.03 | 9708.33 | 78.35 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.2 | 0.92 | 0.03 | 88028.42 | 3.45 | skipped_fast |
| TELUSDT | IDLE | 2.43 | 4.37 | 3.26 | -0.04 | 125545.45 | 33.75 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.45 | 1.29 | 0.02 | 353900.77 | 2.16 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.55 | 0.85 | 0.02 | 54383.26 | 7.31 | skipped_fast |
| RIZEUSDT | IDLE | 0.57 | 1.26 | 1.1 | -0.01 | 43615.73 | 39.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 1.94 | 1.28 | -0.01 | 15301.86 | 21.5 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.71 | 0.63 | -0.0 | 53949.0 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.12 | 0.0 | 38868.73 | 13.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
