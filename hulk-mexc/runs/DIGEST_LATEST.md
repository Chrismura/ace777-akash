# Hulk DIGEST — 2026-09-01T14:25:11Z

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
| XRPUSDT | IDLE | 1.1 | 2.1 | 0.66 | 0.01 | 30793708.99 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.54 | 0.62 | 0.0 | 305990696.07 | 0.9 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.13 | 0.21 | 0.0 | 553320686.2 | 0.0 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.47 | 14.5 | 0.0 | 0.12 | 454454.15 | 15.82 | skipped_fast |
| PYTHUSDT | IDLE | 2.14 | 4.8 | 2.11 | 0.06 | 594967.98 | 4.0 | skipped_fast |
| CCUSDT | IDLE | 2.3 | 4.08 | 3.43 | -0.0 | 395727.12 | 6.84 | skipped_fast |
| WUSDT | IDLE | 2.05 | 4.07 | 0.14 | 0.07 | 251546.8 | 11.31 | skipped_fast |
| KITEUSDT | IDLE | 2.83 | 5.58 | 0.48 | 0.04 | 60865.49 | 8.95 | skipped_fast |
| ZBCNUSDT | IDLE | 2.11 | 3.87 | 2.29 | 0.03 | 215681.33 | 19.99 | skipped_fast |
| EDELUSDT | IDLE | 0.84 | 5.64 | 3.17 | -0.05 | 173973.77 | 17.23 | skipped_fast |
| REDUSDT | IDLE | 1.37 | 2.57 | 1.1 | 0.03 | 64600.72 | 20.05 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 2.26 | 0.8 | 0.0 | 64856.77 | 3.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 4.79 | 2.1 | -0.08 | 39439.99 | 72.65 | skipped_fast |
| HBARUSDT | IDLE | 1.28 | 2.41 | 0.97 | 0.02 | 252057.53 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 2.06 | 4.13 | 0.0 | 0.04 | 39739.99 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.99 | 1.95 | 0.23 | -0.01 | 4856.09 | 46.59 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.57 | 1.21 | 0.01 | 62939.88 | 23.05 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 1.76 | 1.21 | 0.02 | 97239.0 | 40.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.56 | 0.45 | -0.0 | 32917.74 | 2.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 859.4 | 21.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
