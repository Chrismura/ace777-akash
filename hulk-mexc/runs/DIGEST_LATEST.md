# Hulk DIGEST — 2026-09-19T06:57:28Z

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
| XRPUSDT | IDLE | 1.48 | 3.26 | 1.11 | 0.08 | 71150016.48 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.0 | 0.85 | 0.05 | 713771383.36 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.15 | 0.23 | 0.06 | 607970093.6 | 0.61 | skipped_fast |
| WUSDT | IDLE | 1.55 | 4.45 | 3.13 | 0.06 | 967699.71 | 6.48 | skipped_fast |
| PYTHUSDT | IDLE | 2.61 | 4.8 | 2.76 | 0.01 | 689391.27 | 3.32 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 3.7 | 3.02 | 0.01 | 513607.28 | 10.88 | skipped_fast |
| CHIPUSDT | IDLE | 2.38 | 7.81 | 6.07 | 0.05 | 150296.66 | 13.39 | skipped_fast |
| EDELUSDT | IDLE | 1.81 | 8.41 | 2.95 | -0.04 | 183732.48 | 22.72 | skipped_fast |
| RIZEUSDT | IDLE | 2.02 | 16.62 | 10.02 | -0.07 | 42554.91 | 101.01 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.89 | 0.91 | 0.04 | 623532.2 | 2.53 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 6.12 | 2.26 | 0.07 | 116581.35 | 16.24 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 3.12 | 0.38 | 0.04 | 70033.01 | 12.22 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 2.73 | 1.67 | 0.02 | 83106.65 | 14.79 | skipped_fast |
| ZBCNUSDT | IDLE | 0.75 | 1.47 | 0.25 | 0.02 | 196097.75 | 21.4 | skipped_fast |
| RWAINCUSDT | IDLE | 0.67 | 1.21 | 0.8 | 0.06 | 5644.33 | 11.44 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 4.0 | 2.86 | 0.09 | 130792.76 | 38.34 | skipped_fast |
| QNTUSDT | IDLE | 0.75 | 1.38 | 0.74 | 0.01 | 73763.15 | 9.47 | skipped_fast |
| RWAUSDT | IDLE | 0.9 | 1.71 | 0.66 | 0.01 | 55502.73 | 29.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.65 | 2.65 | 2.24 | 0.16 | 5391.67 | 21.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.55 | 0.12 | 0.04 | 40665.27 | 31.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
