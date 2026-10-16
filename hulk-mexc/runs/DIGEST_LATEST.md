# Hulk DIGEST — 2026-10-16T21:05:50Z

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
| PYTHUSDT | IDLE | 1.4 | 5.17 | 2.18 | -0.09 | 2001930.4 | 10.52 | skipped_fast |
| WUSDT | IDLE | 2.08 | 5.51 | 2.45 | -0.03 | 1654722.09 | 17.42 | skipped_fast |
| ETHUSDT | IDLE | 1.2 | 2.19 | 1.35 | -0.02 | 210827681.33 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 2.04 | 0.94 | -0.03 | 28735087.11 | 2.3 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.21 | 0.18 | -0.01 | 355151216.42 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.05 | 1.74 | -0.02 | 754058.52 | 1.49 | skipped_fast |
| EDELUSDT | IDLE | 2.34 | 4.25 | 2.83 | -0.01 | 189645.66 | 20.28 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.47 | 1.56 | -0.03 | 368339.26 | 6.8 | skipped_fast |
| REDUSDT | IDLE | 1.89 | 4.74 | 3.44 | -0.09 | 96974.79 | 9.06 | skipped_fast |
| RWAINCUSDT | IDLE | 1.76 | 8.45 | 4.64 | -0.11 | 28136.91 | 5.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.56 | 1.16 | -0.01 | 188702.64 | 22.87 | skipped_fast |
| CHIPUSDT | IDLE | 0.97 | 3.58 | 2.0 | -0.03 | 154906.5 | 8.75 | skipped_fast |
| HBARUSDT | IDLE | 1.68 | 3.02 | 2.27 | -0.03 | 308427.97 | 4.84 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.63 | 1.46 | -0.03 | 61675.5 | 7.99 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 2.52 | 1.13 | -0.03 | 56995.44 | 10.75 | skipped_fast |
| FLUIDUSDT | IDLE | 2.56 | 5.1 | 0.08 | 0.0 | 7242.28 | 21.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.4 | 1.33 | -0.01 | 45875.54 | 59.53 | skipped_fast |
| RWAUSDT | IDLE | 1.53 | 2.92 | 0.87 | -0.0 | 53286.44 | 15.91 | skipped_fast |
| TELUSDT | IDLE | 1.46 | 2.58 | 2.29 | -0.01 | 91591.95 | 40.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.87 | 0.68 | -0.01 | 33857.08 | 28.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
