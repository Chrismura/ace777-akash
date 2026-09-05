# Hulk DIGEST — 2026-09-05T15:26:37Z

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
| XRPUSDT | IDLE | 0.67 | 1.28 | 0.38 | 0.01 | 22819453.23 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.25 | 0.48 | 0.09 | 0.0 | 181369624.15 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.27 | 0.0 | 0.01 | 359160706.42 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.85 | 6.25 | 2.59 | 0.11 | 447730.87 | 1.74 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 3.39 | 1.73 | 0.02 | 345664.85 | 1.83 | skipped_fast |
| KITEUSDT | IDLE | 2.66 | 6.21 | 4.53 | -0.03 | 61112.05 | 10.26 | skipped_fast |
| RIZEUSDT | IDLE | 1.26 | 11.89 | 5.53 | 0.04 | 153563.58 | 33.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 2.59 | 1.69 | -0.01 | 187368.9 | 4.24 | skipped_fast |
| REDUSDT | IDLE | 1.9 | 3.4 | 2.72 | 0.02 | 62262.78 | 11.99 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.32 | 2.26 | 0.04 | 164487.15 | 6.08 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.51 | 0.47 | 0.01 | 296842.16 | 9.14 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.86 | 0.68 | 0.04 | 80499.34 | 7.18 | skipped_fast |
| RWAINCUSDT | IDLE | 1.8 | 3.17 | 2.92 | -0.02 | 7361.85 | 21.82 | skipped_fast |
| EDELUSDT | IDLE | 0.27 | 4.89 | 2.43 | -0.03 | 193111.56 | 19.08 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.81 | 1.08 | 0.04 | 308668.27 | 1.24 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 2.14 | 0.64 | -0.01 | 70310.13 | 5.85 | skipped_fast |
| RWAUSDT | IDLE | 1.16 | 2.23 | 0.63 | 0.03 | 51743.44 | 21.21 | skipped_fast |
| QNTUSDT | IDLE | 0.62 | 1.15 | 0.64 | -0.01 | 38478.64 | 1.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 0.95 | 0.91 | 0.01 | 800.01 | 20.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.3 | 0.05 | 0.0 | 38367.27 | 5.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
