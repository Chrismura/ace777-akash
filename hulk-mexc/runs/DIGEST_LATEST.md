# Hulk DIGEST — 2026-10-21T00:28:46Z

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
| XRPUSDT | IDLE | 1.07 | 2.08 | 0.45 | 0.03 | 24719283.31 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.6 | 0.4 | 0.02 | 174114790.86 | 0.49 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 1.0 | 0.06 | 0.02 | 326931806.27 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.55 | 5.02 | 0.36 | 0.12 | 1183273.67 | 2.47 | skipped_fast |
| WUSDT | IDLE | 1.47 | 2.76 | 1.18 | 0.03 | 665451.48 | 17.08 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 9.64 | 8.1 | -0.03 | 77811.72 | 5.34 | skipped_fast |
| QNTUSDT | IDLE | 1.77 | 3.39 | 1.01 | 0.01 | 813568.91 | 1.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 3.53 | 2.35 | 0.06 | 445201.23 | 9.01 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 13.83 | 10.48 | 0.06 | 17190.17 | 21.42 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 1.76 | 1.15 | -0.0 | 389248.55 | 4.75 | skipped_fast |
| ZBCNUSDT | IDLE | 1.47 | 2.9 | 0.3 | 0.03 | 193024.46 | 10.68 | skipped_fast |
| EDELUSDT | IDLE | 0.42 | 3.73 | 1.55 | 0.33 | 364152.6 | 14.04 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.83 | 4.56 | 0.06 | 75164.1 | 52.53 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.17 | 0.88 | 0.06 | 61388.79 | 8.1 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.32 | 0.02 | 0.04 | 58271.32 | 15.52 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.76 | 0.47 | 0.02 | 351885.08 | 3.57 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.33 | 0.68 | -0.0 | 73908.38 | 18.05 | skipped_fast |
| LAUSDT | IDLE | 1.3 | 2.56 | 0.24 | 0.04 | 54817.73 | 20.24 | skipped_fast |
| WAXLUSDT | IDLE | 1.34 | 2.59 | 0.55 | -0.02 | 56306.8 | 46.38 | skipped_fast |
| IOTAUSDT | IDLE | 1.08 | 2.06 | 0.68 | 0.04 | 72862.12 | 27.82 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.16 | 0.0 | 52445.52 | 23.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.43 | 0.09 | 0.0 | 39743.67 | 9.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
