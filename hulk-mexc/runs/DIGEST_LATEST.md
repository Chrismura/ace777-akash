# Hulk DIGEST — 2026-08-31T08:16:20Z

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
| XRPUSDT | IDLE | 1.24 | 2.44 | 0.3 | -0.01 | 37962067.56 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.71 | 0.25 | -0.01 | 413739434.94 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.19 | 0.25 | 0.0 | 468271532.27 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.96 | 25.42 | 18.59 | 0.03 | 121212.18 | 24.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 6.28 | 0.07 | 0.01 | 551840.24 | 4.93 | skipped_fast |
| PYTHUSDT | IDLE | 1.35 | 3.43 | 0.25 | 0.0 | 556929.38 | 2.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.72 | 5.3 | 3.05 | -0.08 | 228238.42 | 14.08 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 2.9 | 0.72 | 0.01 | 220766.58 | 6.68 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.54 | 1.84 | 0.02 | 229358.75 | 11.82 | skipped_fast |
| REDUSDT | IDLE | 1.88 | 3.58 | 1.16 | 0.02 | 70154.15 | 13.56 | skipped_fast |
| BIOUSDT | IDLE | 1.36 | 2.68 | 0.34 | -0.02 | 86448.98 | 3.74 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.22 | 1.62 | -0.06 | 94527.31 | 4.12 | skipped_fast |
| TELUSDT | IDLE | 2.2 | 4.18 | 1.49 | 0.02 | 93426.82 | 23.26 | skipped_fast |
| FLUIDUSDT | IDLE | 2.51 | 5.02 | 0.0 | 0.03 | 3792.7 | 21.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.01 | 1.19 | -0.02 | 36723.77 | 62.7 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.79 | 0.17 | -0.01 | 220030.18 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 2.19 | 0.21 | -0.01 | 38559.3 | 6.54 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 1.37 | 0.0 | 0.01 | 2256.88 | 118.95 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.01 | 53238.88 | 32.34 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.67 | 0.42 | -0.01 | 29713.28 | 27.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
