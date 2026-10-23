# Hulk DIGEST — 2026-10-23T17:50:44Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.92 | 1.69 | 1.05 | -0.0 | 26708521.53 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.6 | 0.37 | 0.01 | 209730041.45 | 0.17 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.15 | 0.48 | 0.0 | 295544203.82 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.17 | 0.95 | -0.04 | 1191654.89 | 1.1 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 4.93 | 1.88 | 0.02 | 479390.88 | 12.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.85 | 0.08 | -0.02 | 697663.52 | 1.38 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.45 | 1.81 | 0.0 | 608593.4 | 18.73 | skipped_fast |
| RIZEUSDT | IDLE | 2.78 | 11.5 | 4.11 | -0.01 | 67739.88 | 58.69 | skipped_fast |
| REDUSDT | IDLE | 2.43 | 4.7 | 1.01 | 0.01 | 60136.87 | 14.7 | skipped_fast |
| CHIPUSDT | IDLE | 2.1 | 4.28 | 1.1 | 0.02 | 112367.38 | 17.84 | skipped_fast |
| CCUSDT | IDLE | 1.65 | 3.07 | 1.58 | 0.02 | 181197.43 | 9.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.68 | 3.34 | 0.75 | 0.03 | 196827.05 | 28.23 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 3.93 | 0.59 | 0.06 | 50436.48 | 5.43 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 2.92 | 2.4 | -0.01 | 57279.63 | 9.25 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.71 | 0.66 | 0.02 | 72680.61 | 8.31 | skipped_fast |
| LAUSDT | IDLE | 2.67 | 6.91 | 0.29 | 0.09 | 57169.71 | 18.69 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 2.2 | 1.8 | -0.01 | 273183.15 | 5.07 | skipped_fast |
| WAXLUSDT | IDLE | 1.99 | 3.69 | 1.99 | -0.01 | 56632.85 | 53.93 | skipped_fast |
| IOTAUSDT | IDLE | 1.59 | 3.01 | 1.1 | 0.01 | 71065.98 | 31.08 | skipped_fast |
| FLUIDUSDT | IDLE | 1.78 | 3.53 | 0.14 | 0.01 | 8831.19 | 21.15 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.16 | 0.02 | 51526.11 | 15.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.32 | 1.26 | 0.0 | 35641.77 | 74.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
