# Hulk DIGEST — 2026-10-13T14:14:10Z

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
| WUSDT | IDLE | 1.54 | 12.63 | 9.93 | -0.29 | 6083791.26 | 17.61 | skipped_fast |
| PYTHUSDT | IDLE | 1.33 | 4.45 | 3.37 | -0.05 | 2442049.33 | 2.44 | skipped_fast |
| XRPUSDT | IDLE | 1.12 | 2.19 | 0.36 | -0.01 | 39154808.64 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.53 | 0.25 | -0.01 | 236722503.17 | 0.04 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 12.37 | 7.42 | -0.09 | 1159495.47 | 6.69 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.85 | 0.17 | 0.01 | 381535661.12 | 0.0 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.78 | 8.95 | 1.23 | 0.05 | 567538.65 | 33.97 | skipped_fast |
| EDELUSDT | IDLE | 3.51 | 7.67 | 1.11 | -0.02 | 337810.62 | 28.81 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 10.38 | 5.47 | -0.11 | 64396.85 | 88.02 | skipped_fast |
| RWAINCUSDT | IDLE | 3.0 | 5.4 | 3.94 | -0.02 | 32864.11 | 24.67 | skipped_fast |
| REDUSDT | IDLE | 1.78 | 6.14 | 3.92 | -0.05 | 202764.63 | 15.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.84 | 3.45 | 1.53 | -0.04 | 249432.4 | 30.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 4.4 | 1.67 | -0.04 | 127708.88 | 15.29 | skipped_fast |
| HBARUSDT | IDLE | 1.83 | 3.63 | 0.26 | -0.03 | 376188.01 | 7.9 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 3.07 | 0.68 | -0.05 | 75617.53 | 14.48 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 2.11 | 0.27 | 0.01 | 60872.28 | 10.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.4 | 2.88 | 1.87 | 0.03 | 12556.34 | 21.39 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.79 | 0.23 | -0.02 | 104154.7 | 34.17 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.16 | 0.68 | -0.02 | 37932.11 | 2.79 | skipped_fast |
| RWAUSDT | IDLE | 0.22 | 0.39 | 0.31 | -0.0 | 53512.94 | 15.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
