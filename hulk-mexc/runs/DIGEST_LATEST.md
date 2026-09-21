# Hulk DIGEST — 2026-09-21T22:08:09Z

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
| XRPUSDT | IDLE | 1.83 | 5.13 | 0.49 | 0.11 | 103525630.15 | 2.57 | skipped_fast |
| ETHUSDT | IDLE | 1.43 | 2.66 | 1.28 | 0.05 | 732564556.47 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.07 | 2.02 | 0.91 | 0.07 | 1037764208.61 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 18.24 | 13.62 | 0.09 | 281753.58 | 23.16 | skipped_fast |
| PYTHUSDT | IDLE | 2.22 | 5.22 | 3.73 | 0.02 | 695554.95 | 6.38 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.74 | 0.15 | 0.07 | 1157440.64 | 1.08 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 3.27 | 2.84 | 0.06 | 587646.25 | 8.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 6.77 | 3.67 | 0.08 | 254462.13 | 30.2 | skipped_fast |
| WUSDT | IDLE | 1.04 | 2.38 | 0.84 | 0.0 | 569054.37 | 7.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 7.23 | 0.0 | 0.12 | 19608.5 | 75.8 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 5.1 | 3.41 | 0.08 | 142853.76 | 13.09 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 2.54 | 1.96 | -0.01 | 104314.58 | 16.6 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 2.14 | 0.96 | 0.04 | 104666.72 | 10.43 | skipped_fast |
| RIZEUSDT | IDLE | 1.37 | 9.87 | 8.47 | -0.19 | 48019.1 | 103.4 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.8 | 1.02 | 0.02 | 81471.33 | 9.29 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 3.03 | 0.65 | 0.05 | 116220.59 | 2.96 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 3.18 | 2.01 | 0.09 | 107483.33 | 18.12 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 2.43 | 1.37 | 0.08 | 11900.28 | 23.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 0.97 | 0.28 | 0.04 | 42641.48 | 6.4 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.16 | 0.29 | 0.02 | 57604.34 | 43.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
