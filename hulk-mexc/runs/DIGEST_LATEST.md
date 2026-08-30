# Hulk DIGEST — 2026-08-30T17:17:59Z

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
| ETHUSDT | IDLE | 1.59 | 3.05 | 0.81 | 0.02 | 207218885.63 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 2.44 | 0.3 | 0.02 | 20294493.02 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.58 | 0.41 | 0.01 | 272367596.64 | 0.01 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 7.33 | 5.68 | -0.02 | 523617.04 | 2.49 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 9.26 | 5.23 | -0.06 | 195280.0 | 12.3 | skipped_fast |
| PYTHUSDT | IDLE | 3.02 | 5.66 | 2.51 | 0.03 | 394296.79 | 4.08 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 5.99 | 4.04 | 0.07 | 72537.33 | 25.14 | skipped_fast |
| WUSDT | IDLE | 1.54 | 3.02 | 0.39 | 0.05 | 224380.37 | 11.5 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.62 | 1.28 | 0.01 | 256016.15 | 10.99 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 2.02 | 1.21 | 0.02 | 62284.92 | 13.59 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.65 | 0.36 | -0.0 | 79567.63 | 3.62 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 1.67 | 1.47 | -0.02 | 60956.03 | 10.19 | skipped_fast |
| TELUSDT | IDLE | 2.2 | 4.37 | 0.23 | 0.0 | 83485.83 | 28.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 3.18 | 3.08 | -0.07 | 37385.1 | 43.4 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.63 | 0.0 | 0.02 | 1921.2 | 120.81 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.21 | 0.13 | 0.0 | 131337.98 | 1.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.0 | 32295.53 | 2.67 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.08 | 0.02 | 52707.92 | 8.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 22.23 | skipped_fast |
| QNTUSDT | IDLE | 0.52 | 0.97 | 0.42 | 0.01 | 38426.63 | 4.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
