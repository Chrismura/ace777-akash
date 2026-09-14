# Hulk DIGEST — 2026-09-14T08:42:09Z

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
| XRPUSDT | IDLE | 0.97 | 1.86 | 0.52 | 0.03 | 29838806.33 | 2.16 | skipped_fast |
| ETHUSDT | IDLE | 0.52 | 0.99 | 0.35 | 0.01 | 334047478.7 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.8 | 0.28 | 0.01 | 393800076.11 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 4.19 | 3.85 | 0.05 | 501677.67 | 1.78 | skipped_fast |
| REDUSDT | IDLE | 3.53 | 8.4 | 2.89 | 0.05 | 137420.63 | 18.22 | skipped_fast |
| EDELUSDT | IDLE | 1.64 | 7.81 | 4.83 | 0.14 | 251095.31 | 28.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 20.23 | 7.21 | 0.22 | 75230.51 | 59.5 | skipped_fast |
| CHIPUSDT | IDLE | 1.74 | 5.73 | 4.92 | -0.1 | 103456.1 | 16.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.61 | 2.99 | 1.53 | -0.0 | 185732.99 | 19.25 | skipped_fast |
| CCUSDT | IDLE | 1.01 | 1.78 | 1.66 | -0.0 | 239506.7 | 9.45 | skipped_fast |
| WUSDT | IDLE | 1.08 | 2.04 | 0.83 | 0.02 | 217575.32 | 6.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.76 | 3.35 | 1.08 | 0.02 | 9292.88 | 27.36 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 2.36 | 2.3 | -0.01 | 60924.61 | 12.13 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.49 | 0.85 | 0.0 | 73022.58 | 3.91 | skipped_fast |
| HBARUSDT | IDLE | 0.56 | 1.11 | 0.13 | 0.03 | 257668.41 | 1.3 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 1.53 | 0.63 | 0.0 | 87323.41 | 31.58 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 1.57 | 0.25 | 0.0 | 38289.15 | 6.25 | skipped_fast |
| FLUIDUSDT | IDLE | 1.03 | 2.06 | 0.0 | 0.02 | 765.05 | 21.68 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.52 | 0.18 | -0.0 | 29952.33 | 6.97 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.37 | 0.01 | 53078.51 | 22.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
