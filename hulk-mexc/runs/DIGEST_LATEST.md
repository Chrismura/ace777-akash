# Hulk DIGEST — 2026-10-26T09:18:42Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.86 | 1.63 | 0.6 | -0.01 | 19543083.04 | 2.33 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.39 | 0.33 | -0.0 | 110686707.95 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 1.04 | 0.14 | 0.0 | 223554233.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 3.17 | 0.67 | 0.07 | 809742.97 | 4.03 | skipped_fast |
| QNTUSDT | IDLE | 2.27 | 6.86 | 0.05 | 0.13 | 850586.19 | 7.42 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.89 | 0.0 | 0.0 | 500295.57 | 15.06 | skipped_fast |
| CHIPUSDT | IDLE | 2.75 | 6.52 | 4.08 | 0.04 | 109153.99 | 19.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.74 | 3.14 | 2.63 | 0.01 | 186784.16 | 34.08 | skipped_fast |
| LAUSDT | IDLE | 3.42 | 7.18 | 1.77 | 0.04 | 64409.21 | 23.91 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 3.61 | 0.83 | 0.02 | 61156.1 | 17.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.58 | 2.95 | 2.35 | -0.07 | 67248.28 | 5.86 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.61 | 1.69 | 0.02 | 54732.86 | 11.59 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.77 | 0.44 | 0.02 | 163694.88 | 9.83 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.33 | 0.89 | 0.01 | 60368.72 | 4.51 | skipped_fast |
| EDELUSDT | IDLE | 0.85 | 2.16 | 0.96 | 0.08 | 139406.06 | 21.92 | skipped_fast |
| MNSRYUSDT | IDLE | 2.38 | 4.38 | 2.53 | -0.01 | 41546.18 | 76.46 | skipped_fast |
| RIZEUSDT | IDLE | 0.51 | 0.93 | 0.55 | 0.0 | 33173.7 | 4.62 | skipped_fast |
| WAXLUSDT | IDLE | 2.14 | 3.86 | 2.82 | -0.0 | 52650.61 | 63.26 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.78 | 0.31 | 0.01 | 172349.85 | 7.74 | skipped_fast |
| IOTAUSDT | IDLE | 1.06 | 2.06 | 0.42 | 0.0 | 63767.14 | 23.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.28 | 1.49 | 0.0 | 0.0 | 19108.67 | 21.87 | skipped_fast |
| RWAUSDT | IDLE | 0.12 | 0.24 | 0.0 | -0.01 | 53291.32 | 23.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
