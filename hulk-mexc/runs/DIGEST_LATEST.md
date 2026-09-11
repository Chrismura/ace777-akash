# Hulk DIGEST — 2026-09-11T09:15:57Z

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
| ETHUSDT | IDLE | 0.8 | 1.54 | 0.4 | -0.0 | 466700990.19 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.74 | 1.38 | 0.66 | -0.02 | 39373911.17 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.78 | 0.28 | -0.01 | 541034243.04 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.68 | 42.67 | 26.89 | 0.08 | 139137.52 | 156.17 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 6.62 | 4.0 | -0.06 | 125224.69 | 10.97 | skipped_fast |
| CCUSDT | IDLE | 0.9 | 1.7 | 0.7 | -0.04 | 451588.9 | 6.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.24 | 0.92 | -0.01 | 345088.27 | 1.94 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.18 | 2.07 | -0.01 | 139633.16 | 3.14 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 1.92 | 0.65 | -0.03 | 199107.9 | 7.72 | skipped_fast |
| EDELUSDT | IDLE | 0.77 | 3.53 | 1.2 | -0.06 | 198481.34 | 46.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.04 | 1.85 | 1.49 | 0.0 | 3093.7 | 5.6 | skipped_fast |
| KITEUSDT | IDLE | 0.9 | 1.8 | 0.01 | 0.02 | 58548.22 | 11.91 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 1.55 | 1.38 | -0.02 | 59584.11 | 18.99 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.17 | 1.07 | -0.02 | 72102.03 | 4.02 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.79 | 1.69 | -0.03 | 189313.97 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.26 | 1.47 | -0.04 | 96008.61 | 40.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.26 | 2.04 | -0.03 | 2138.71 | 16.57 | skipped_fast |
| QNTUSDT | IDLE | 0.55 | 0.99 | 0.8 | -0.03 | 36219.6 | 1.55 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.92 | 0.15 | -0.02 | 50404.72 | 7.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.6 | 0.03 | -0.01 | 36183.27 | 4.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
