# Hulk DIGEST — 2026-09-23T02:16:43Z

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
| PYTHUSDT | IDLE | 1.08 | 4.83 | 3.88 | 0.04 | 1778970.43 | 3.05 | skipped_fast |
| XRPUSDT | IDLE | 1.56 | 2.92 | 1.3 | 0.04 | 104113646.13 | 2.53 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.41 | 0.79 | 0.0 | 406756712.3 | 0.65 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 0.95 | 0.5 | 0.01 | 881639655.0 | 0.03 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 2.27 | 0.15 | 0.09 | 1778149.53 | 1.0 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.56 | 2.21 | 0.02 | 319048.15 | 8.28 | skipped_fast |
| CCUSDT | IDLE | 1.39 | 2.5 | 1.87 | -0.03 | 414645.47 | 7.91 | skipped_fast |
| ZBCNUSDT | IDLE | 2.07 | 4.11 | 0.21 | 0.03 | 206878.93 | 7.23 | skipped_fast |
| RIZEUSDT | IDLE | 1.5 | 25.28 | 2.83 | 0.4 | 45022.38 | 50.36 | skipped_fast |
| CHIPUSDT | IDLE | 2.33 | 4.74 | 1.2 | -0.02 | 122068.13 | 19.26 | skipped_fast |
| BIOUSDT | IDLE | 2.07 | 3.82 | 2.1 | 0.03 | 118978.75 | 13.43 | skipped_fast |
| EDELUSDT | IDLE | 1.3 | 6.49 | 1.39 | 0.01 | 263821.14 | 65.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 3.01 | 2.82 | 0.02 | 19848.03 | 16.12 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.06 | 1.62 | 0.01 | 59365.96 | 13.95 | skipped_fast |
| KITEUSDT | IDLE | 0.66 | 2.75 | 1.05 | 0.16 | 125083.93 | 9.37 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 4.09 | 2.06 | 0.12 | 212852.35 | 4.01 | skipped_fast |
| TELUSDT | IDLE | 0.88 | 3.6 | 2.3 | 0.13 | 107962.67 | 54.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.83 | 0.0 | 0.02 | 5475.4 | 21.09 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.02 | 0.43 | 0.01 | 52682.32 | 14.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.23 | 0.01 | 40076.7 | 24.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
