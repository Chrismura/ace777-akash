# Hulk DIGEST — 2026-10-24T10:27:25Z

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
| XRPUSDT | IDLE | 0.86 | 1.56 | 1.09 | -0.03 | 28796831.74 | 1.56 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.15 | 0.78 | -0.02 | 115034787.6 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.59 | 0.43 | -0.01 | 285414278.8 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.24 | 4.8 | 3.64 | -0.07 | 1066694.32 | 41.5 | skipped_fast |
| PYTHUSDT | IDLE | 1.59 | 2.83 | 2.39 | -0.03 | 658355.33 | 2.87 | skipped_fast |
| QNTUSDT | IDLE | 2.01 | 3.63 | 2.55 | -0.01 | 772440.99 | 3.35 | skipped_fast |
| EDELUSDT | IDLE | 0.93 | 1.69 | 1.17 | 0.01 | 675730.72 | 12.48 | skipped_fast |
| REDUSDT | IDLE | 1.94 | 6.55 | 2.3 | 0.09 | 82811.13 | 14.45 | skipped_fast |
| WAXLUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.56 | 10.84 | 1.7 | 0.06 | 62775.01 | 49.63 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.28 | 0.59 | 0.03 | 47822.49 | 10.74 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 1.74 | 1.58 | -0.01 | 232089.8 | 6.85 | skipped_fast |
| LAUSDT | IDLE | 2.66 | 18.76 | 3.66 | 0.23 | 84275.19 | 88.63 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 3.39 | 2.75 | -0.07 | 71621.34 | 14.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 2.08 | 1.19 | -0.05 | 199503.14 | 7.04 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 2.41 | 1.32 | -0.02 | 58483.04 | 12.68 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.61 | 1.24 | -0.03 | 79197.5 | 8.67 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.23 | 1.59 | -0.03 | 196106.6 | 3.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.72 | 3.03 | 2.77 | -0.01 | 11074.67 | 21.46 | skipped_fast |
| IOTAUSDT | IDLE | 1.4 | 2.48 | 2.08 | -0.03 | 74746.65 | 13.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.21 | 0.58 | 0.18 | 0.05 | 64219.87 | 48.77 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.79 | 0.79 | -0.01 | 52297.88 | 23.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.93 | 0.53 | -0.01 | 38019.71 | 69.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
