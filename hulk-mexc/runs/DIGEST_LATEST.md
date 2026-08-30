# Hulk DIGEST — 2026-08-30T16:14:17Z

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
| ETHUSDT | IDLE | 0.92 | 1.83 | 0.09 | 0.02 | 168791976.19 | 1.64 | skipped_fast |
| XRPUSDT | IDLE | 0.82 | 1.57 | 0.43 | 0.01 | 18253246.53 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.24 | 0.08 | 0.01 | 259591536.13 | 0.1 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 8.01 | 5.7 | -0.04 | 559687.03 | 4.99 | skipped_fast |
| PYTHUSDT | IDLE | 3.13 | 5.93 | 2.19 | 0.02 | 407905.41 | 2.04 | skipped_fast |
| ZBCNUSDT | IDLE | 2.54 | 4.6 | 3.26 | -0.03 | 164991.31 | 14.66 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 5.99 | 4.68 | 0.06 | 72207.37 | 42.14 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.63 | 0.3 | 0.04 | 219898.09 | 8.37 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.62 | 0.9 | 0.02 | 269124.75 | 6.73 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 2.14 | 0.25 | 0.02 | 60042.73 | 3.6 | skipped_fast |
| BIOUSDT | IDLE | 0.69 | 1.36 | 0.18 | -0.01 | 73784.35 | 10.89 | skipped_fast |
| KITEUSDT | IDLE | 0.64 | 1.21 | 0.52 | -0.04 | 60924.84 | 12.47 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.37 | 0.12 | -0.01 | 82035.37 | 23.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 2.45 | 0.76 | -0.05 | 45958.98 | 58.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 3.01 | 0.0 | 0.0 | 1671.88 | 127.74 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.13 | 0.62 | -0.0 | 130154.56 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.48 | 0.96 | 0.02 | 0.01 | 38309.1 | 1.61 | skipped_fast |
| MNSRYUSDT | IDLE | 0.77 | 1.41 | 0.82 | 0.02 | 33106.15 | 42.7 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.82 | 0.24 | 0.01 | 53203.93 | 24.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.83 | 0.0 | 0.02 | 2467.03 | 21.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
