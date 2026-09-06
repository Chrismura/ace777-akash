# Hulk DIGEST — 2026-09-06T03:30:50Z

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
| XRPUSDT | IDLE | 0.71 | 1.41 | 0.1 | 0.01 | 23781076.44 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.29 | 0.31 | 0.02 | 197247972.32 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.23 | 0.43 | 0.17 | 0.0 | 372117381.08 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.16 | 4.0 | 2.09 | 0.02 | 415343.1 | 1.81 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 4.3 | 2.95 | 0.08 | 417992.88 | 10.21 | skipped_fast |
| RWAINCUSDT | IDLE | 2.82 | 5.2 | 2.97 | 0.01 | 8659.32 | 43.01 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 2.52 | 1.09 | 0.02 | 290575.46 | 9.98 | skipped_fast |
| WUSDT | IDLE | 1.78 | 3.22 | 2.26 | 0.03 | 169367.19 | 10.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 2.5 | 1.49 | -0.01 | 215807.82 | 15.66 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 3.55 | 1.26 | -0.05 | 64590.16 | 10.11 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 8.56 | 1.58 | -0.01 | 122277.3 | 52.39 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.67 | 1.97 | -0.01 | 58243.04 | 8.7 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.98 | 0.2 | 0.03 | 382512.68 | 2.45 | skipped_fast |
| RWAUSDT | IDLE | 2.22 | 3.91 | 3.49 | 0.03 | 53715.09 | 14.17 | skipped_fast |
| BIOUSDT | IDLE | 0.65 | 1.22 | 0.53 | 0.03 | 94282.44 | 7.15 | skipped_fast |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.39 | 0.02 | 114712.76 | 9.38 | skipped_fast |
| TELUSDT | IDLE | 1.68 | 3.22 | 0.87 | 0.0 | 72134.39 | 34.97 | skipped_fast |
| QNTUSDT | IDLE | 1.32 | 2.5 | 0.9 | 0.03 | 37025.98 | 3.05 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.82 | 0.0 | 0.03 | 390.92 | 21.22 | skipped_fast |
| MNSRYUSDT | IDLE | 0.83 | 1.6 | 0.35 | 0.01 | 39114.69 | 51.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
