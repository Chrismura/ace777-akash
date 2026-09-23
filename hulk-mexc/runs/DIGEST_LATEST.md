# Hulk DIGEST — 2026-09-23T04:17:03Z

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
| XRPUSDT | IDLE | 2.02 | 5.38 | 0.02 | 0.08 | 111104206.59 | 3.02 | skipped_fast |
| PYTHUSDT | IDLE | 0.99 | 4.62 | 2.37 | 0.04 | 1774876.38 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.35 | 0.19 | 0.01 | 402524990.33 | 0.47 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.99 | 0.12 | 0.02 | 869416426.74 | 0.04 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 2.84 | 0.73 | 0.06 | 1788410.72 | 1.0 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.84 | 9.88 | 0.63 | 0.06 | 221250.39 | 18.78 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.68 | 1.19 | 0.04 | 325121.2 | 10.55 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 2.56 | 0.48 | -0.02 | 412113.84 | 6.06 | skipped_fast |
| EDELUSDT | IDLE | 1.34 | 6.66 | 1.49 | -0.01 | 271977.95 | 26.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 2.69 | 1.75 | -0.01 | 196038.39 | 15.05 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.31 | 0.88 | 0.04 | 110396.08 | 6.6 | skipped_fast |
| KITEUSDT | IDLE | 0.91 | 3.34 | 3.23 | 0.12 | 128297.51 | 9.54 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 2.57 | 0.45 | 0.03 | 59324.33 | 14.96 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 16.71 | 0.51 | 0.53 | 51797.29 | 85.4 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 3.79 | 2.24 | 0.11 | 212605.11 | 9.4 | skipped_fast |
| RWAINCUSDT | IDLE | 0.59 | 1.51 | 0.59 | 0.03 | 20931.57 | 5.34 | skipped_fast |
| TELUSDT | IDLE | 0.88 | 3.93 | 0.48 | 0.15 | 107425.64 | 42.85 | skipped_fast |
| FLUIDUSDT | IDLE | 1.21 | 2.42 | 0.03 | 0.04 | 5535.59 | 21.44 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.02 | 0.5 | 0.01 | 53077.88 | 7.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.72 | 0.01 | 0.01 | 40098.43 | 6.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
