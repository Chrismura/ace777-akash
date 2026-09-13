# Hulk DIGEST — 2026-09-13T02:38:16Z

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
| XRPUSDT | IDLE | 0.25 | 0.5 | 0.05 | 0.0 | 14191473.26 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 0.19 | 0.34 | 0.21 | 0.0 | 196054947.76 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.12 | 0.23 | 0.06 | 0.0 | 316894101.29 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.72 | 46.78 | 29.68 | 0.04 | 94499.11 | 66.45 | skipped_fast |
| WUSDT | IDLE | 2.16 | 4.05 | 1.82 | 0.03 | 203692.1 | 5.94 | skipped_fast |
| PYTHUSDT | IDLE | 1.18 | 2.3 | 1.01 | 0.07 | 418945.55 | 3.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.83 | 5.39 | 2.66 | -0.01 | 226170.51 | 16.94 | skipped_fast |
| RWAINCUSDT | IDLE | 2.95 | 5.75 | 3.17 | 0.02 | 9775.45 | 32.68 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 5.27 | 1.21 | 0.08 | 169656.28 | 16.34 | skipped_fast |
| CCUSDT | IDLE | 1.02 | 1.95 | 0.57 | -0.01 | 185383.21 | 9.19 | skipped_fast |
| REDUSDT | IDLE | 1.57 | 2.97 | 1.08 | 0.01 | 56267.88 | 18.21 | skipped_fast |
| RWAUSDT | IDLE | 2.66 | 4.77 | 3.7 | 0.01 | 55288.59 | 36.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.88 | 1.68 | 1.53 | -0.01 | 76028.55 | 14.69 | skipped_fast |
| KITEUSDT | IDLE | 0.91 | 1.65 | 1.13 | -0.01 | 63030.84 | 10.29 | skipped_fast |
| BIOUSDT | IDLE | 0.4 | 0.79 | 0.12 | 0.0 | 70053.16 | 11.76 | skipped_fast |
| HBARUSDT | IDLE | 0.47 | 0.95 | 0.0 | 0.01 | 123647.27 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 0.79 | 1.41 | 1.15 | -0.04 | 89813.8 | 30.52 | skipped_fast |
| QNTUSDT | IDLE | 0.61 | 1.2 | 0.12 | 0.0 | 35131.28 | 3.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 1.34 | 0.91 | -0.0 | 436.08 | 21.18 | skipped_fast |
| MNSRYUSDT | IDLE | 0.07 | 0.14 | 0.03 | 0.0 | 28794.02 | 15.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
