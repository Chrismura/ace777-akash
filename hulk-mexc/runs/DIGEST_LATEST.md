# Hulk DIGEST — 2026-09-22T20:06:23Z

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
| XRPUSDT | IDLE | 2.14 | 4.05 | 1.52 | 0.05 | 122134344.8 | 1.89 | skipped_fast |
| PYTHUSDT | IDLE | 0.86 | 4.01 | 2.1 | 0.04 | 1659021.46 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.66 | 1.24 | 0.47 | -0.01 | 442284834.39 | 0.8 | skipped_fast |
| HBARUSDT | IDLE | 2.32 | 5.48 | 0.5 | 0.09 | 1589463.7 | 1.01 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.71 | 0.53 | -0.0 | 938751775.24 | 0.38 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 14.88 | 9.1 | -0.0 | 291005.99 | 39.25 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 3.72 | 1.76 | -0.02 | 493530.54 | 9.63 | skipped_fast |
| RWAINCUSDT | IDLE | 3.73 | 9.63 | 3.43 | 0.1 | 26364.91 | 46.89 | skipped_fast |
| ZBCNUSDT | IDLE | 2.54 | 4.6 | 3.23 | -0.02 | 220005.7 | 31.82 | skipped_fast |
| WUSDT | IDLE | 1.56 | 2.81 | 2.04 | 0.01 | 356190.7 | 6.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.73 | 19.63 | 8.18 | -0.16 | 44218.89 | 90.11 | skipped_fast |
| CHIPUSDT | IDLE | 1.98 | 3.51 | 3.03 | -0.04 | 140096.96 | 17.73 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.23 | 1.34 | 0.02 | 139330.58 | 6.81 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 3.77 | 0.45 | 0.18 | 116101.95 | 9.34 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.15 | 0.8 | 0.04 | 64008.52 | 14.6 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 6.87 | 0.22 | 0.08 | 105445.58 | 22.38 | skipped_fast |
| QNTUSDT | IDLE | 0.91 | 2.7 | 2.14 | 0.07 | 188168.41 | 6.95 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.24 | 0.22 | 0.0 | 54214.47 | 7.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.33 | 0.45 | 0.01 | 7785.91 | 21.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.05 | -0.0 | 40223.44 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
