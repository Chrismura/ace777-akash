# Hulk DIGEST — 2026-09-27T20:37:01Z

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
| WUSDT | IDLE | 1.64 | 11.06 | 2.38 | 0.23 | 4715198.32 | 17.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.57 | 4.98 | 1.78 | 0.08 | 2247470.6 | 10.6 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 17.78 | 2.97 | 0.57 | 6978271.8 | 10.0 | skipped_fast |
| XRPUSDT | IDLE | 1.11 | 2.11 | 0.77 | 0.01 | 41707518.72 | 1.31 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.65 | 0.34 | 0.0 | 201251631.83 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.6 | 0.29 | 0.01 | 437601789.55 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 42.2 | 13.21 | 0.2 | 28948.19 | 16.08 | skipped_fast |
| CCUSDT | IDLE | 2.7 | 5.22 | 1.21 | 0.02 | 614521.29 | 8.74 | skipped_fast |
| RIZEUSDT | IDLE | 2.44 | 17.64 | 14.92 | -0.18 | 48835.02 | 72.55 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 10.45 | 7.87 | -0.14 | 138242.68 | 19.15 | skipped_fast |
| HBARUSDT | IDLE | 1.42 | 2.75 | 0.59 | 0.02 | 730491.63 | 1.05 | skipped_fast |
| KITEUSDT | IDLE | 2.04 | 4.47 | 1.85 | 0.03 | 140177.03 | 7.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 2.35 | 0.6 | 0.01 | 205209.74 | 17.4 | skipped_fast |
| REDUSDT | IDLE | 1.71 | 3.22 | 1.31 | 0.02 | 64797.29 | 12.84 | skipped_fast |
| BIOUSDT | IDLE | 1.47 | 2.8 | 0.88 | -0.01 | 87452.88 | 6.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 2.45 | 1.43 | -0.03 | 99558.9 | 10.65 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 3.83 | 2.9 | 0.13 | 168904.68 | 48.85 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 2.5 | 1.31 | 0.03 | 2331.19 | 21.57 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.64 | 0.49 | 0.01 | 57251.44 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.39 | 0.05 | 0.01 | 40268.97 | 12.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
