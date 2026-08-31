# Hulk DIGEST — 2026-08-31T15:18:04Z

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
| XRPUSDT | IDLE | 1.05 | 1.91 | 1.24 | -0.02 | 42128421.03 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 0.81 | 1.53 | 0.57 | -0.01 | 462910293.01 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.32 | 0.44 | -0.0 | 584585022.52 | 1.1 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.54 | 6.62 | 5.9 | -0.02 | 551024.93 | 2.54 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 3.74 | 1.81 | -0.04 | 434994.23 | 4.24 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 3.5 | 2.56 | -0.01 | 256521.77 | 7.67 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.36 | 2.72 | -0.05 | 219759.44 | 15.37 | skipped_fast |
| ZBCNUSDT | IDLE | 0.9 | 2.17 | 0.47 | -0.05 | 231026.28 | 8.29 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.78 | 2.71 | -0.04 | 69624.54 | 12.23 | skipped_fast |
| RIZEUSDT | IDLE | 2.05 | 3.6 | 3.27 | -0.04 | 40866.5 | 63.28 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.34 | 1.76 | -0.04 | 82146.53 | 3.82 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 2.92 | 2.68 | -0.08 | 101145.7 | 10.99 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 4.27 | 1.28 | 0.04 | 124672.22 | 16.22 | skipped_fast |
| RWAUSDT | IDLE | 2.35 | 4.65 | 0.31 | 0.06 | 55530.81 | 7.69 | skipped_fast |
| QNTUSDT | IDLE | 2.13 | 3.9 | 2.41 | -0.01 | 52648.14 | 3.27 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 1.98 | 0.95 | -0.02 | 283082.99 | 1.36 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 1.68 | 1.65 | -0.05 | 2223.62 | 17.35 | skipped_fast |
| TELUSDT | IDLE | 1.88 | 3.33 | 2.82 | -0.0 | 91005.78 | 23.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.76 | 0.7 | -0.0 | 2465.4 | 22.39 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.34 | -0.02 | 25173.62 | 40.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
