# Hulk DIGEST — 2026-09-07T11:47:12Z

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
| XRPUSDT | IDLE | 0.9 | 1.65 | 1.03 | -0.02 | 33006938.08 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.37 | 0.78 | -0.0 | 319946802.5 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.05 | 0.53 | -0.01 | 407084206.39 | 0.01 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 7.14 | 5.55 | -0.09 | 353292.62 | 3.71 | skipped_fast |
| CCUSDT | IDLE | 2.32 | 4.05 | 3.87 | -0.04 | 424623.34 | 5.64 | skipped_fast |
| PYTHUSDT | IDLE | 1.59 | 3.09 | 0.61 | -0.0 | 585542.76 | 1.79 | skipped_fast |
| WUSDT | IDLE | 1.8 | 3.3 | 1.96 | -0.01 | 446329.16 | 12.63 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 7.33 | 4.58 | -0.05 | 73661.86 | 29.37 | skipped_fast |
| KITEUSDT | IDLE | 2.54 | 4.52 | 3.78 | -0.05 | 58408.16 | 10.73 | skipped_fast |
| REDUSDT | IDLE | 2.47 | 4.77 | 1.09 | 0.01 | 64637.72 | 16.02 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 3.08 | 1.09 | -0.0 | 178693.5 | 7.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 8.73 | 6.35 | -0.13 | 72484.48 | 64.79 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 2.16 | 0.77 | -0.03 | 70207.64 | 3.68 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.79 | 0.23 | -0.0 | 370470.43 | 1.23 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 3.11 | 2.33 | 0.0 | 105834.43 | 11.65 | skipped_fast |
| RWAINCUSDT | IDLE | 0.86 | 2.83 | 0.68 | 0.05 | 6093.94 | 14.57 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.61 | 2.11 | -0.0 | 41545.52 | 7.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.81 | 1.58 | 0.25 | -0.01 | 1152.45 | 21.16 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.58 | 0.5 | -0.01 | 53172.76 | 14.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.13 | -0.0 | 38053.26 | 5.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
