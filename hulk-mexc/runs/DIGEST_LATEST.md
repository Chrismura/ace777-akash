# Hulk DIGEST — 2026-09-14T11:42:28Z

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
| XRPUSDT | IDLE | 1.28 | 2.46 | 0.68 | 0.04 | 35162577.22 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.28 | 0.7 | 0.01 | 402905429.63 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.08 | 0.86 | 0.01 | 312737180.2 | 1.39 | skipped_fast |
| PYTHUSDT | IDLE | 2.93 | 5.67 | 4.8 | 0.04 | 517867.4 | 1.8 | skipped_fast |
| REDUSDT | IDLE | 2.2 | 5.39 | 0.73 | 0.06 | 162953.21 | 17.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 5.97 | 3.39 | -0.09 | 105767.23 | 14.41 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.59 | 2.5 | 0.01 | 227148.57 | 9.01 | skipped_fast |
| EDELUSDT | IDLE | 1.23 | 6.15 | 0.48 | 0.2 | 235004.44 | 13.88 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 2.12 | 0.6 | 0.01 | 241311.85 | 7.28 | skipped_fast |
| ZBCNUSDT | IDLE | 0.97 | 1.9 | 0.21 | 0.01 | 211049.84 | 17.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 12.36 | 6.72 | 0.23 | 70998.42 | 74.16 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 2.4 | 2.04 | -0.03 | 61729.43 | 12.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.41 | 2.61 | 1.4 | 0.02 | 9387.11 | 5.47 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.89 | 0.66 | 0.01 | 76088.3 | 7.79 | skipped_fast |
| HBARUSDT | IDLE | 0.67 | 1.29 | 0.27 | 0.02 | 286896.91 | 1.3 | skipped_fast |
| TELUSDT | IDLE | 1.75 | 3.38 | 0.8 | 0.01 | 91727.65 | 43.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.06 | 1.64 | 0.0 | 809.03 | 21.82 | skipped_fast |
| QNTUSDT | IDLE | 0.59 | 1.13 | 0.28 | 0.0 | 38352.44 | 6.25 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.37 | 0.3 | 0.02 | 53082.33 | 22.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.48 | 0.42 | -0.0 | 29248.71 | 25.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
