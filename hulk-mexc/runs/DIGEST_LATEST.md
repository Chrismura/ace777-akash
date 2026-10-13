# Hulk DIGEST — 2026-10-13T23:09:45Z

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
| WUSDT | IDLE | 1.64 | 11.08 | 3.28 | -0.1 | 4584801.23 | 7.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 3.48 | 3.04 | -0.05 | 2175696.15 | 1.28 | skipped_fast |
| QNTUSDT | IDLE | 2.52 | 8.98 | 3.86 | -0.06 | 1709268.44 | 5.61 | skipped_fast |
| XRPUSDT | IDLE | 0.53 | 0.95 | 0.7 | 0.02 | 35241149.52 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.66 | 0.3 | 0.02 | 384369940.83 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.34 | 0.6 | 0.56 | 0.02 | 215071155.69 | 0.04 | skipped_fast |
| CCUSDT | IDLE | 1.17 | 3.41 | 2.75 | 0.04 | 617359.18 | 7.2 | skipped_fast |
| RWAINCUSDT | IDLE | 2.79 | 4.98 | 3.94 | -0.01 | 32692.22 | 19.76 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 2.05 | 1.67 | 0.01 | 227056.57 | 14.61 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 1.7 | 1.43 | -0.02 | 220531.93 | 20.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 2.35 | 1.88 | -0.02 | 104185.29 | 14.04 | skipped_fast |
| RIZEUSDT | IDLE | 1.58 | 5.26 | 2.19 | -0.0 | 49563.94 | 61.33 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 1.76 | 0.88 | 0.0 | 131262.45 | 7.09 | skipped_fast |
| TELUSDT | IDLE | 2.28 | 4.31 | 1.65 | 0.04 | 116157.24 | 28.02 | skipped_fast |
| KITEUSDT | IDLE | 1.04 | 2.25 | 0.36 | 0.03 | 60277.29 | 9.31 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.72 | 1.04 | -0.0 | 74603.57 | 7.25 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.28 | 1.19 | -0.01 | 292436.84 | 1.15 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 2.98 | 0.0 | 0.07 | 22972.39 | 21.23 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.31 | 0.23 | 0.0 | 52262.27 | 15.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.42 | 0.15 | -0.01 | 37611.56 | 15.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
