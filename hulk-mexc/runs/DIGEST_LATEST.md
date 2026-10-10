# Hulk DIGEST — 2026-10-10T13:40:22Z

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
| WUSDT | IDLE | 3.75 | 7.31 | 1.23 | -0.0 | 1050753.78 | 6.81 | skipped_fast |
| XRPUSDT | IDLE | 0.36 | 0.65 | 0.49 | 0.02 | 18003712.95 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.13 | 0.26 | 0.06 | 0.01 | 87019262.1 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.11 | 0.2 | 0.13 | 0.0 | 205445018.99 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 2.45 | 1.46 | -0.08 | 1107182.81 | 2.55 | skipped_fast |
| QNTUSDT | IDLE | 1.41 | 2.72 | 0.68 | 0.02 | 1159548.16 | 0.4 | skipped_fast |
| EDELUSDT | IDLE | 3.63 | 7.46 | 4.75 | 0.02 | 231386.07 | 10.38 | skipped_fast |
| KITEUSDT | IDLE | 2.53 | 6.59 | 1.65 | 0.05 | 75166.16 | 8.54 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 1.96 | 1.56 | -0.03 | 394445.91 | 7.51 | skipped_fast |
| ZBCNUSDT | IDLE | 0.58 | 1.08 | 0.51 | -0.01 | 228891.22 | 10.07 | skipped_fast |
| CHIPUSDT | IDLE | 0.88 | 2.58 | 2.37 | 0.09 | 87595.58 | 9.61 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.19 | 0.61 | 0.03 | 55279.17 | 14.58 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.76 | 0.38 | 0.03 | 76292.83 | 3.47 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.14 | 0.27 | 0.01 | 335533.48 | 4.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.97 | 1.88 | 0.39 | -0.02 | 9630.91 | 58.51 | skipped_fast |
| TELUSDT | IDLE | 1.59 | 2.82 | 2.37 | -0.01 | 113244.45 | 55.13 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 1.56 | 0.83 | 0.05 | 50186.34 | 53.53 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.55 | 0.47 | -0.01 | 53544.95 | 15.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.67 | 0.2 | 0.0 | 39444.79 | 17.59 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 1.2 | 0.1 | 0.02 | 9768.72 | 21.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
