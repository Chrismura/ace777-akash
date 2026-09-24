# Hulk DIGEST — 2026-09-24T23:23:38Z

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
| XRPUSDT | IDLE | 1.12 | 2.12 | 0.81 | 0.02 | 68725769.41 | 1.95 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.52 | 0.4 | 0.0 | 352432330.01 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.9 | 0.37 | -0.0 | 723509197.71 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 41.19 | 25.53 | 0.04 | 198241.08 | 34.25 | skipped_fast |
| PYTHUSDT | IDLE | 0.75 | 2.68 | 1.46 | 0.08 | 1024484.69 | 4.44 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 3.91 | 1.62 | 0.04 | 478336.32 | 7.95 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 31.75 | 6.5 | 0.38 | 72559.74 | 104.49 | skipped_fast |
| HBARUSDT | IDLE | 1.52 | 2.88 | 1.01 | 0.03 | 793167.73 | 1.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.38 | 12.95 | 4.56 | 0.14 | 94796.56 | 12.52 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 17.26 | 5.05 | 0.27 | 293049.81 | 18.88 | skipped_fast |
| ZBCNUSDT | IDLE | 1.69 | 2.99 | 2.55 | 0.01 | 209760.2 | 10.77 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 2.93 | 2.42 | -0.02 | 65440.76 | 9.91 | skipped_fast |
| WUSDT | IDLE | 0.87 | 1.7 | 0.28 | 0.05 | 248903.01 | 5.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.44 | 7.19 | 4.27 | 0.16 | 12736.16 | 13.92 | skipped_fast |
| REDUSDT | IDLE | 0.81 | 2.07 | 1.76 | 0.06 | 100187.25 | 13.74 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 2.29 | 1.5 | 0.09 | 87898.07 | 12.97 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 2.9 | 1.26 | -0.05 | 106685.18 | 42.59 | skipped_fast |
| RWAUSDT | IDLE | 0.94 | 1.77 | 0.73 | 0.01 | 57354.52 | 7.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.13 | 1.05 | 0.03 | 1191.45 | 21.39 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.16 | 0.0 | 37863.12 | 28.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
