# Hulk DIGEST — 2026-09-11T02:16:03Z

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
| XRPUSDT | IDLE | 1.1 | 2.07 | 0.85 | -0.03 | 41244320.78 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.2 | 0.35 | -0.0 | 420073267.7 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.05 | 0.41 | -0.01 | 533880071.69 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 4.02 | 9.46 | 3.89 | -0.02 | 99921.53 | 22.84 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 2.94 | 2.46 | -0.01 | 418390.79 | 1.95 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 2.07 | 2.03 | -0.06 | 470507.11 | 6.15 | skipped_fast |
| ZBCNUSDT | IDLE | 2.06 | 3.79 | 2.14 | -0.01 | 205368.48 | 26.09 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 53.98 | 3.16 | -0.32 | 142336.41 | 281.29 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 5.24 | 4.36 | -0.02 | 221064.8 | 27.89 | skipped_fast |
| WUSDT | IDLE | 1.16 | 2.17 | 0.99 | -0.02 | 166964.09 | 9.41 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 1.91 | 0.68 | -0.01 | 77797.21 | 4.02 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 2.08 | 0.85 | -0.02 | 57295.31 | 11.93 | skipped_fast |
| REDUSDT | IDLE | 0.73 | 1.32 | 0.99 | -0.05 | 60125.47 | 19.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.24 | 0.28 | 0.0 | 4220.66 | 11.18 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 3.08 | 2.55 | -0.02 | 88547.98 | 51.18 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.67 | 0.78 | -0.01 | 185234.48 | 1.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.69 | 3.38 | 0.0 | -0.03 | 2341.05 | 19.96 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.04 | 1.47 | -0.04 | 36062.41 | 7.76 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.07 | 0.45 | -0.02 | 50575.82 | 22.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.56 | 0.32 | -0.01 | 35346.86 | 47.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
