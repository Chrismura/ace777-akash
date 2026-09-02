# Hulk DIGEST — 2026-09-02T07:34:35Z

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
| XRPUSDT | IDLE | 1.02 | 1.95 | 0.64 | -0.03 | 37290908.6 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.4 | 0.27 | -0.02 | 367699590.71 | 0.41 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.08 | 0.28 | -0.02 | 512651415.59 | 0.12 | skipped_fast |
| PYTHUSDT | IDLE | 2.08 | 8.14 | 2.43 | 0.09 | 829039.6 | 9.1 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 7.27 | 1.28 | 0.14 | 947142.75 | 8.8 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 16.8 | 5.0 | 0.05 | 176699.71 | 48.66 | skipped_fast |
| WUSDT | IDLE | 2.19 | 4.06 | 2.12 | 0.01 | 410229.12 | 14.54 | skipped_fast |
| RWAINCUSDT | IDLE | 3.47 | 10.57 | 2.48 | 0.09 | 9131.67 | 21.57 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 10.71 | 0.96 | 0.14 | 74033.95 | 8.91 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 2.99 | 2.59 | -0.07 | 335959.56 | 7.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 4.13 | 1.89 | -0.01 | 210466.94 | 9.85 | skipped_fast |
| REDUSDT | IDLE | 1.28 | 2.62 | 2.25 | 0.0 | 155300.35 | 11.74 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.34 | 0.74 | -0.03 | 73792.14 | 3.91 | skipped_fast |
| QNTUSDT | IDLE | 2.0 | 4.03 | 0.4 | 0.07 | 61697.54 | 7.63 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 4.15 | 0.23 | -0.01 | 88995.96 | 41.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.04 | 2.8 | 1.72 | -0.06 | 40304.07 | 78.03 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.63 | 0.28 | -0.01 | 237708.1 | 1.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 2.81 | 0.0 | -0.03 | 323.84 | 15.52 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.54 | 0.15 | -0.02 | 52442.32 | 15.37 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.69 | 0.34 | -0.01 | 35926.64 | 37.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
