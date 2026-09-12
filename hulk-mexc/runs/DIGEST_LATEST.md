# Hulk DIGEST — 2026-09-12T05:22:20Z

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
| XRPUSDT | IDLE | 0.41 | 0.88 | 0.19 | 0.01 | 51839373.45 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 0.14 | 0.31 | 0.2 | 0.02 | 618842764.58 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.26 | 0.18 | 0.0 | 565420778.03 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.86 | 3.82 | 0.36 | 0.02 | 423503.38 | 1.91 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 3.5 | 1.79 | -0.0 | 420287.63 | 8.13 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.74 | 0.53 | 0.01 | 196247.71 | 9.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.62 | 0.75 | -0.01 | 190398.1 | 11.69 | skipped_fast |
| EDELUSDT | IDLE | 1.34 | 3.58 | 2.77 | 0.05 | 165349.13 | 26.68 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 4.03 | 3.0 | 0.05 | 65578.34 | 11.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 3.47 | 2.33 | 0.03 | 118463.85 | 12.66 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.2 | 1.02 | 0.01 | 81164.65 | 7.9 | skipped_fast |
| KITEUSDT | IDLE | 0.91 | 1.61 | 1.44 | -0.01 | 58814.54 | 1.86 | skipped_fast |
| RIZEUSDT | IDLE | 0.12 | 7.74 | 4.0 | 0.74 | 189138.55 | 96.21 | skipped_fast |
| RWAINCUSDT | IDLE | 0.85 | 1.63 | 1.27 | -0.0 | 15225.08 | 33.69 | skipped_fast |
| HBARUSDT | IDLE | 0.33 | 0.59 | 0.52 | -0.02 | 256974.01 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 0.92 | 1.75 | 0.54 | -0.01 | 43559.74 | 6.25 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 1.83 | 1.45 | -0.03 | 101794.5 | 41.29 | skipped_fast |
| FLUIDUSDT | IDLE | 0.97 | 1.95 | 0.0 | 0.01 | 1927.49 | 22.11 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.52 | 0.0 | 0.03 | 53179.95 | 7.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.4 | 0.01 | 30585.61 | 13.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
