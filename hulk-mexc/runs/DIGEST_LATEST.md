# Hulk DIGEST — 2026-09-07T13:35:56Z

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
| XRPUSDT | IDLE | 0.7 | 1.33 | 0.47 | -0.01 | 33883889.17 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.04 | 0.41 | 0.0 | 331825115.41 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.44 | 0.28 | -0.0 | 413198893.87 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 3.43 | 1.44 | 0.02 | 574673.68 | 5.36 | skipped_fast |
| CCUSDT | IDLE | 2.0 | 3.64 | 2.39 | -0.01 | 424282.93 | 8.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.16 | 1.44 | -0.05 | 341062.66 | 5.49 | skipped_fast |
| WUSDT | IDLE | 1.24 | 2.26 | 1.44 | -0.0 | 413979.74 | 14.56 | skipped_fast |
| HBARUSDT | IDLE | 1.84 | 3.48 | 1.36 | 0.02 | 409522.56 | 7.32 | skipped_fast |
| KITEUSDT | IDLE | 2.04 | 3.75 | 2.25 | -0.03 | 58852.38 | 10.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.89 | 1.24 | 0.0 | 197289.34 | 30.84 | skipped_fast |
| EDELUSDT | IDLE | 1.8 | 5.03 | 1.72 | -0.04 | 77704.08 | 19.46 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 4.04 | 0.25 | 0.03 | 63987.58 | 24.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 9.0 | 2.47 | -0.07 | 73981.48 | 62.1 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.74 | 0.79 | -0.01 | 70633.11 | 7.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.11 | 3.8 | 0.0 | 0.08 | 5713.96 | 43.2 | skipped_fast |
| TELUSDT | IDLE | 1.74 | 3.11 | 2.45 | 0.0 | 108845.96 | 40.85 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 2.12 | 0.56 | 0.01 | 43308.81 | 15.1 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.73 | 0.29 | -0.01 | 53692.39 | 14.44 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 1.32 | 0.0 | -0.01 | 1152.45 | 21.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.16 | -0.0 | 37984.42 | 2.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
