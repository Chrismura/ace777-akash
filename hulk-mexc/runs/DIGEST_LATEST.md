# Hulk DIGEST — 2026-10-23T13:48:25Z

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
| XRPUSDT | IDLE | 0.65 | 1.2 | 0.61 | -0.0 | 25755854.48 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 1.01 | 0.11 | 0.0 | 222279312.61 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.68 | 0.08 | 0.0 | 321059145.19 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.73 | 3.21 | -0.06 | 1119011.98 | 5.47 | skipped_fast |
| PYTHUSDT | IDLE | 1.94 | 3.58 | 2.0 | -0.04 | 685348.18 | 4.16 | skipped_fast |
| WUSDT | IDLE | 2.04 | 3.68 | 2.69 | 0.0 | 604315.83 | 12.7 | skipped_fast |
| EDELUSDT | IDLE | 2.81 | 5.36 | 1.7 | 0.0 | 460193.86 | 27.69 | skipped_fast |
| ZBCNUSDT | IDLE | 3.15 | 6.69 | 0.72 | -0.02 | 163096.25 | 14.56 | skipped_fast |
| CHIPUSDT | IDLE | 2.82 | 5.33 | 4.28 | 0.02 | 124633.32 | 18.03 | skipped_fast |
| RIZEUSDT | IDLE | 2.49 | 10.85 | 6.47 | -0.09 | 48681.51 | 63.42 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 2.17 | 0.62 | 0.01 | 188391.69 | 8.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.24 | 1.15 | 0.01 | 49255.36 | 5.55 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.89 | 0.37 | -0.01 | 336829.36 | 2.5 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 1.62 | 0.83 | -0.01 | 76758.43 | 15.68 | skipped_fast |
| KITEUSDT | IDLE | 0.85 | 1.62 | 0.49 | 0.01 | 57662.17 | 10.73 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.52 | 0.62 | 0.0 | 59703.94 | 8.35 | skipped_fast |
| LAUSDT | IDLE | 1.99 | 3.83 | 0.95 | 0.02 | 56194.32 | 19.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.92 | 3.44 | 2.69 | -0.04 | 9520.11 | 46.59 | skipped_fast |
| WAXLUSDT | IDLE | 0.92 | 1.84 | 0.04 | -0.0 | 57412.82 | 60.4 | skipped_fast |
| IOTAUSDT | IDLE | 0.56 | 1.07 | 0.29 | 0.0 | 64983.51 | 28.86 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.71 | 0.08 | 0.01 | 51301.87 | 15.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.32 | 1.26 | -0.01 | 36368.45 | 74.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
