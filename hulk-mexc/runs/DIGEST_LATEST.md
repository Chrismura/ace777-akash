# Hulk DIGEST — 2026-09-16T22:14:29Z

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
| XRPUSDT | IDLE | 2.91 | 5.48 | 2.28 | 0.01 | 58984637.19 | 2.33 | skipped_fast |
| ETHUSDT | IDLE | 1.38 | 2.56 | 1.34 | 0.0 | 369090905.66 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.05 | 1.96 | 0.93 | 0.01 | 506299871.22 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.37 | 7.06 | 0.75 | 0.06 | 475498.29 | 6.26 | skipped_fast |
| PYTHUSDT | IDLE | 2.15 | 4.01 | 1.97 | -0.01 | 409693.77 | 1.92 | skipped_fast |
| RWAINCUSDT | IDLE | 4.2 | 7.81 | 3.93 | -0.01 | 20541.51 | 81.59 | skipped_fast |
| KITEUSDT | IDLE | 2.58 | 9.06 | 4.21 | 0.04 | 68238.9 | 10.53 | skipped_fast |
| WUSDT | IDLE | 2.25 | 4.33 | 1.16 | -0.01 | 216229.83 | 6.72 | skipped_fast |
| CHIPUSDT | IDLE | 2.51 | 5.22 | 3.86 | -0.03 | 74458.2 | 14.03 | skipped_fast |
| BIOUSDT | IDLE | 2.17 | 4.17 | 1.12 | -0.0 | 79115.28 | 8.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 2.67 | 1.89 | 0.02 | 200796.57 | 27.29 | skipped_fast |
| EDELUSDT | IDLE | 0.49 | 3.78 | 1.34 | 0.04 | 323987.14 | 22.51 | skipped_fast |
| REDUSDT | IDLE | 1.75 | 3.64 | 1.0 | -0.01 | 65184.1 | 20.27 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 2.88 | 1.36 | -0.02 | 263461.81 | 2.74 | skipped_fast |
| TELUSDT | IDLE | 2.49 | 4.87 | 0.96 | -0.03 | 113917.28 | 55.17 | skipped_fast |
| QNTUSDT | IDLE | 2.03 | 3.96 | 0.72 | -0.0 | 37215.34 | 3.29 | skipped_fast |
| RIZEUSDT | IDLE | 0.28 | 4.14 | 2.9 | 0.25 | 61083.2 | 9.04 | skipped_fast |
| RWAUSDT | IDLE | 1.97 | 3.87 | 0.52 | 0.01 | 53547.24 | 22.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | -0.02 | 1573.23 | 21.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.66 | 0.24 | -0.01 | 30674.1 | 2.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
