# Hulk DIGEST — 2026-09-20T14:02:43Z

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
| XRPUSDT | IDLE | 0.65 | 1.2 | 0.68 | -0.04 | 45499235.25 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 0.38 | 0.75 | 0.12 | -0.02 | 239607544.64 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.48 | 0.01 | -0.01 | 480992786.07 | 0.0 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.72 | 8.52 | 0.0 | 0.07 | 886768.28 | 16.13 | skipped_fast |
| PYTHUSDT | IDLE | 1.2 | 2.44 | 0.24 | -0.03 | 663994.16 | 5.11 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 9.83 | 5.53 | -0.05 | 65764.86 | 49.58 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.81 | 0.73 | -0.04 | 397354.83 | 6.42 | skipped_fast |
| REDUSDT | IDLE | 2.3 | 4.33 | 1.83 | 0.0 | 75573.86 | 8.65 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 2.03 | 0.15 | -0.06 | 360828.84 | 6.68 | skipped_fast |
| CHIPUSDT | IDLE | 1.77 | 3.45 | 2.43 | -0.08 | 94584.18 | 14.62 | skipped_fast |
| ZBCNUSDT | IDLE | 0.94 | 2.87 | 0.43 | 0.03 | 218007.73 | 24.9 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 2.27 | 1.51 | -0.03 | 69421.19 | 8.89 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.84 | 1.37 | -0.05 | 79472.48 | 7.48 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 2.04 | 0.0 | 0.03 | 10334.43 | 23.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.81 | 2.44 | 0.32 | -0.05 | 34211.1 | 78.54 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 2.07 | 0.13 | -0.02 | 97907.27 | 33.82 | skipped_fast |
| QNTUSDT | IDLE | 0.73 | 1.31 | 0.97 | -0.03 | 55751.59 | 6.28 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.82 | 0.44 | -0.01 | 52459.45 | 44.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.65 | 0.48 | -0.06 | 1972.21 | 29.17 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.69 | 0.21 | -0.01 | 35087.45 | 67.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
