# Hulk DIGEST — 2026-10-25T12:01:14Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| ETHUSDT | IDLE | 0.81 | 1.53 | 0.61 | -0.01 | 129754994.94 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.01 | 22572976.16 | 3.08 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.76 | 0.16 | 0.0 | 202601718.6 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.02 | 3.71 | 2.2 | -0.04 | 804916.38 | 17.52 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.08 | 520590.05 | 30.5 | skipped_fast |
| PYTHUSDT | IDLE | 1.57 | 3.1 | 0.21 | 0.02 | 513248.83 | 4.2 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 10.5 | 7.14 | -0.02 | 17159.63 | 20.21 | skipped_fast |
| REDUSDT | IDLE | 2.55 | 4.48 | 4.07 | -0.04 | 68487.92 | 10.51 | skipped_fast |
| QNTUSDT | IDLE | 2.12 | 4.04 | 1.37 | 0.03 | 406796.54 | 1.09 | skipped_fast |
| CHIPUSDT | IDLE | 1.38 | 4.41 | 0.11 | 0.06 | 92802.05 | 17.71 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.55 | 0.84 | -0.04 | 65586.22 | 4.47 | skipped_fast |
| ZBCNUSDT | IDLE | 0.75 | 1.73 | 0.74 | 0.01 | 225339.46 | 20.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.49 | 2.78 | 1.3 | -0.02 | 57626.04 | 21.89 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.71 | 0.0 | -0.01 | 191641.68 | 10.9 | skipped_fast |
| KITEUSDT | IDLE | 0.96 | 1.83 | 0.56 | -0.05 | 59122.65 | 11.66 | skipped_fast |
| LAUSDT | IDLE | 1.45 | 6.45 | 4.23 | -0.1 | 78871.36 | 24.58 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.79 | 1.07 | 0.0 | 196550.71 | 10.4 | skipped_fast |
| IOTAUSDT | IDLE | 1.27 | 2.35 | 1.26 | -0.02 | 65145.26 | 6.98 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.14 | 0.71 | -0.03 | 40619.63 | 64.89 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.19 | 1.02 | -0.0 | 51916.3 | 15.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.12 | -0.01 | 38133.48 | 77.07 | skipped_fast |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
