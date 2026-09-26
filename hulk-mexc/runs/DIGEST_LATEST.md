# Hulk DIGEST — 2026-09-26T02:27:23Z

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
| XRPUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.02 | 112195675.81 | 1.91 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.69 | 0.07 | 0.0 | 314566503.45 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.31 | 0.6 | 0.11 | -0.01 | 666810373.65 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 3.66 | 1.47 | 0.07 | 1249384.18 | 2.7 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 7.09 | 0.58 | 0.17 | 902790.75 | 8.93 | skipped_fast |
| HBARUSDT | IDLE | 1.3 | 2.43 | 1.17 | 0.01 | 901197.12 | 1.05 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.49 | 1.98 | 0.04 | 460944.01 | 2.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.83 | 4.72 | 3.66 | 0.06 | 153685.42 | 18.38 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 4.29 | 0.44 | 0.12 | 565740.99 | 8.97 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 4.6 | 0.0 | 0.08 | 79210.6 | 10.91 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 2.1 | 1.34 | 0.05 | 246760.24 | 30.6 | skipped_fast |
| REDUSDT | IDLE | 1.3 | 2.76 | 1.74 | 0.05 | 104404.47 | 12.19 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 3.32 | 1.26 | 0.08 | 113361.07 | 6.08 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 1.5 | 0.13 | -0.02 | 183379.82 | 6.75 | skipped_fast |
| RIZEUSDT | IDLE | 0.15 | 2.06 | 0.36 | -0.04 | 88489.66 | 64.86 | skipped_fast |
| RWAINCUSDT | IDLE | 0.42 | 1.27 | 0.75 | -0.07 | 13235.39 | 50.76 | skipped_fast |
| TELUSDT | IDLE | 0.69 | 1.23 | 1.03 | 0.01 | 106707.46 | 36.72 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.11 | 0.81 | -0.01 | 53357.86 | 7.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.91 | 0.41 | 0.01 | 41048.48 | 38.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.21 | 0.36 | 0.36 | 0.02 | 3296.62 | 22.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
