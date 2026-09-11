# Hulk DIGEST — 2026-09-11T14:19:32Z

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
| XRPUSDT | IDLE | 4.15 | 8.82 | 2.28 | 0.03 | 48767209.31 | 2.86 | skipped_fast |
| ETHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.05 | 9.44 | 1.94 | 0.07 | 520675200.74 | 0.84 | skipped_fast |
| BTCUSDT | IDLE | 2.53 | 4.93 | 0.82 | 0.03 | 525141219.98 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 75.81 | 28.57 | 0.09 | 115201.18 | 55.2 | skipped_fast |
| CCUSDT | IDLE | 3.86 | 7.68 | 0.24 | 0.01 | 448081.8 | 8.85 | skipped_fast |
| PYTHUSDT | IDLE | 3.94 | 7.72 | 1.08 | 0.04 | 389616.95 | 1.88 | skipped_fast |
| WUSDT | IDLE | 3.43 | 6.71 | 1.0 | 0.03 | 139919.1 | 19.43 | skipped_fast |
| BIOUSDT | IDLE | 3.34 | 6.49 | 1.23 | 0.02 | 79346.41 | 7.82 | skipped_fast |
| REDUSDT | IDLE | 3.29 | 6.52 | 0.36 | 0.03 | 60724.43 | 11.13 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 5.61 | 1.25 | 0.02 | 173474.37 | 30.92 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 8.23 | 5.52 | 0.03 | 9201.66 | 120.68 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 7.14 | 0.54 | 0.01 | 136238.1 | 14.7 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.07 | 8.79 | 1.13 | 0.03 | 105318.23 | 70.94 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 7.66 | 0.62 | -0.01 | 198336.36 | 26.85 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 5.04 | 0.8 | 0.01 | 210803.62 | 2.62 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 3.5 | 0.7 | 0.01 | 58816.23 | 10.03 | skipped_fast |
| QNTUSDT | IDLE | 2.76 | 5.19 | 2.18 | 0.01 | 40975.64 | 9.14 | skipped_fast |
| FLUIDUSDT | IDLE | 2.25 | 4.49 | 0.0 | 0.03 | 1300.24 | 22.49 | skipped_fast |
| RWAUSDT | IDLE | 1.52 | 2.97 | 0.44 | 0.02 | 50478.49 | 7.4 | skipped_fast |
| MNSRYUSDT | IDLE | 1.62 | 3.1 | 0.99 | 0.02 | 38315.66 | 67.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
