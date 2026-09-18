# Hulk DIGEST — 2026-09-18T03:17:58Z

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
| XRPUSDT | IDLE | 1.26 | 2.52 | 0.02 | 0.01 | 34884481.4 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.88 | 1.75 | 0.0 | 0.02 | 286477663.82 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.58 | 0.03 | 0.01 | 420786680.61 | 0.0 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 9.78 | 0.55 | 0.12 | 545715.83 | 5.5 | skipped_fast |
| PYTHUSDT | IDLE | 2.24 | 6.05 | 0.15 | 0.08 | 572999.8 | 3.41 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.43 | 15.92 | 0.3 | 0.18 | 195081.36 | 18.67 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 23.2 | 11.8 | -0.0 | 47009.38 | 85.62 | skipped_fast |
| REDUSDT | IDLE | 3.23 | 6.43 | 0.23 | 0.04 | 67291.68 | 13.85 | skipped_fast |
| HBARUSDT | IDLE | 1.89 | 3.77 | 0.04 | 0.04 | 522860.44 | 1.3 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 4.74 | 0.0 | 0.03 | 69522.66 | 11.5 | skipped_fast |
| EDELUSDT | IDLE | 0.98 | 10.73 | 2.76 | -0.13 | 287676.54 | 52.59 | skipped_fast |
| WUSDT | IDLE | 0.72 | 1.76 | 0.06 | 0.09 | 319403.22 | 10.95 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 2.69 | 0.75 | 0.02 | 61403.94 | 10.26 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.42 | 0.77 | -0.0 | 220570.56 | 49.08 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 2.06 | 1.84 | -0.04 | 14689.04 | 18.17 | skipped_fast |
| RWAUSDT | IDLE | 1.69 | 3.15 | 1.53 | 0.02 | 60751.81 | 44.25 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.75 | 0.0 | 0.03 | 40788.99 | 4.8 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 2.78 | 0.14 | -0.0 | 73867.96 | 48.66 | skipped_fast |
| MNSRYUSDT | IDLE | 0.95 | 1.85 | 0.32 | 0.02 | 43878.53 | 59.36 | skipped_fast |
| FLUIDUSDT | IDLE | 0.22 | 0.39 | 0.39 | 0.02 | 148.34 | 21.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
