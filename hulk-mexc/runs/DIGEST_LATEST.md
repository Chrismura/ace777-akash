# Hulk DIGEST — 2026-09-17T19:17:18Z

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
| XRPUSDT | IDLE | 1.2 | 2.09 | 2.02 | 0.0 | 44227040.82 | 2.32 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.4 | 1.31 | 0.02 | 329603178.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.05 | 0.71 | 0.01 | 467335000.9 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 42.03 | 26.59 | -0.29 | 227316.52 | 147.6 | skipped_fast |
| PYTHUSDT | IDLE | 2.08 | 5.49 | 2.31 | 0.07 | 580043.34 | 5.35 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 4.08 | 3.92 | 0.04 | 597717.41 | 6.05 | skipped_fast |
| WUSDT | IDLE | 2.16 | 6.29 | 0.54 | 0.11 | 256450.12 | 16.26 | skipped_fast |
| CHIPUSDT | IDLE | 2.33 | 7.37 | 5.77 | 0.05 | 144453.72 | 18.57 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.67 | 19.49 | 1.62 | -0.05 | 45997.55 | 104.75 | skipped_fast |
| HBARUSDT | IDLE | 1.56 | 2.83 | 1.88 | 0.03 | 551716.12 | 1.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.9 | 3.48 | 2.14 | 0.01 | 188803.96 | 19.84 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.79 | 2.06 | 0.02 | 65119.61 | 0.77 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 3.14 | 0.92 | 0.03 | 61878.77 | 12.39 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.8 | 1.3 | 0.02 | 71220.48 | 3.98 | skipped_fast |
| RWAINCUSDT | IDLE | 0.74 | 1.37 | 0.7 | 0.01 | 22377.77 | 23.71 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 2.41 | 2.15 | 0.01 | 82493.85 | 34.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.03 | 146.13 | 21.79 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.21 | 0.83 | 0.02 | 37214.86 | 6.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 0.93 | 0.54 | 0.02 | 42448.09 | 4.19 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.13 | 0.07 | 0.0 | 58800.78 | 29.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
