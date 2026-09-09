# Hulk DIGEST — 2026-09-09T20:13:09Z

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
| XRPUSDT | IDLE | 1.39 | 2.45 | 2.2 | -0.02 | 40288158.67 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 1.15 | 2.03 | 1.82 | -0.01 | 338383417.98 | 0.85 | skipped_fast |
| BTCUSDT | IDLE | 0.94 | 1.68 | 1.39 | -0.0 | 525991887.81 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 7.32 | 6.31 | -0.01 | 619808.82 | 1.87 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 7.68 | 6.67 | -0.03 | 180289.79 | 39.64 | skipped_fast |
| WUSDT | IDLE | 3.24 | 5.91 | 3.8 | -0.01 | 199503.28 | 12.85 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.43 | 1.06 | -0.04 | 592217.43 | 4.79 | skipped_fast |
| CHIPUSDT | IDLE | 1.82 | 6.28 | 5.68 | 0.04 | 112025.84 | 12.75 | skipped_fast |
| ZBCNUSDT | IDLE | 1.73 | 3.25 | 1.39 | 0.03 | 198303.71 | 4.94 | skipped_fast |
| REDUSDT | IDLE | 2.17 | 3.84 | 3.29 | 0.0 | 61329.69 | 17.82 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 2.28 | 1.69 | -0.03 | 420413.77 | 1.29 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.7 | 1.66 | 0.01 | 62512.25 | 9.64 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.34 | 1.44 | -0.04 | 95272.52 | 3.74 | skipped_fast |
| FLUIDUSDT | IDLE | 2.66 | 4.7 | 4.08 | -0.06 | 896.61 | 21.53 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.29 | 1.58 | -0.01 | 7125.32 | 27.6 | skipped_fast |
| RIZEUSDT | IDLE | 0.81 | 8.76 | 7.66 | -0.03 | 71403.25 | 95.29 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 2.95 | 2.33 | 0.03 | 101852.93 | 33.26 | skipped_fast |
| RWAUSDT | IDLE | 1.46 | 2.56 | 2.35 | -0.01 | 54721.77 | 14.6 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.4 | 1.26 | -0.01 | 44246.64 | 6.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.61 | 0.22 | 0.01 | 24096.3 | 59.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
