# Hulk DIGEST — 2026-10-13T23:17:40Z

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
| WUSDT | IDLE | 1.65 | 11.08 | 3.63 | -0.1 | 4567211.8 | 9.35 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 3.48 | 2.91 | -0.04 | 2162772.35 | 2.56 | skipped_fast |
| QNTUSDT | IDLE | 2.53 | 8.98 | 4.12 | -0.06 | 1709213.89 | 5.62 | skipped_fast |
| XRPUSDT | IDLE | 0.53 | 0.95 | 0.78 | 0.01 | 35054723.04 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.62 | 0.55 | 0.02 | 212734065.19 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.66 | 0.29 | 0.02 | 382558046.5 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.17 | 3.41 | 2.78 | 0.05 | 615939.79 | 8.0 | skipped_fast |
| RWAINCUSDT | IDLE | 2.79 | 4.98 | 3.94 | -0.01 | 32867.61 | 4.94 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 2.05 | 1.67 | 0.01 | 226513.22 | 8.77 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 1.7 | 1.43 | -0.02 | 219740.1 | 20.42 | skipped_fast |
| RIZEUSDT | IDLE | 1.59 | 5.26 | 2.25 | 0.0 | 49623.54 | 29.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.08 | 2.35 | 1.59 | -0.02 | 104332.07 | 10.51 | skipped_fast |
| REDUSDT | IDLE | 0.89 | 1.76 | 1.14 | 0.0 | 130764.18 | 13.58 | skipped_fast |
| TELUSDT | IDLE | 2.27 | 4.31 | 1.6 | 0.04 | 116023.98 | 28.02 | skipped_fast |
| KITEUSDT | IDLE | 1.04 | 2.25 | 0.32 | 0.04 | 60096.76 | 9.31 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.72 | 1.08 | 0.0 | 75053.23 | 7.25 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.3 | 1.23 | -0.0 | 291592.64 | 4.59 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 2.98 | 0.0 | 0.07 | 22972.39 | 21.2 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.31 | 0.15 | -0.0 | 52228.5 | 15.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.42 | 0.11 | -0.01 | 37730.94 | 15.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
