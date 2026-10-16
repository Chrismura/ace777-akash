# Hulk DIGEST — 2026-10-16T23:47:32Z

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
| PYTHUSDT | IDLE | 1.78 | 6.23 | 1.7 | -0.07 | 1931440.68 | 1.15 | skipped_fast |
| WUSDT | IDLE | 2.36 | 6.24 | 2.99 | -0.0 | 1534791.54 | 14.61 | skipped_fast |
| XRPUSDT | IDLE | 0.91 | 1.82 | 0.02 | -0.02 | 28593495.77 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.22 | 0.14 | -0.01 | 205375503.02 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.08 | 0.23 | -0.01 | 340644629.1 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 3.32 | 2.7 | -0.02 | 780763.01 | 0.5 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.08 | 2.83 | 0.01 | 186364.58 | 20.31 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 2.36 | 0.72 | -0.02 | 357178.82 | 6.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.79 | 8.45 | 5.44 | -0.11 | 27774.92 | 11.29 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 3.7 | 0.94 | -0.06 | 96954.91 | 7.55 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 2.27 | 0.97 | -0.02 | 190367.13 | 15.09 | skipped_fast |
| CHIPUSDT | IDLE | 0.75 | 2.91 | 0.47 | -0.03 | 154030.8 | 10.83 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.15 | 0.15 | -0.01 | 56869.9 | 8.22 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 2.1 | 0.12 | -0.02 | 61956.83 | 7.92 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 2.16 | 0.29 | -0.02 | 320397.65 | 8.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 2.23 | 1.98 | -0.01 | 45726.98 | 28.86 | skipped_fast |
| FLUIDUSDT | IDLE | 2.34 | 4.65 | 0.2 | 0.01 | 4785.84 | 21.47 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.18 | 2.97 | -0.03 | 92199.06 | 17.35 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.31 | 0.52 | -0.0 | 34181.2 | 4.24 | skipped_fast |
| RWAUSDT | IDLE | 0.18 | 0.32 | 0.24 | -0.0 | 53154.48 | 15.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
