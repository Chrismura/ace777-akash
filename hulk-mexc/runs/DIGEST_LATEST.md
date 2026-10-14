# Hulk DIGEST — 2026-10-14T13:17:43Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| PYTHUSDT | IDLE | 2.55 | 6.19 | 2.34 | 0.02 | 2016414.26 | 3.59 | skipped_fast |
| WUSDT | IDLE | 1.97 | 8.89 | 7.69 | -0.17 | 3387371.85 | 16.85 | skipped_fast |
| XRPUSDT | IDLE | 1.55 | 2.73 | 2.45 | -0.0 | 33218107.18 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 1.5 | 2.65 | 2.39 | -0.01 | 133170470.69 | 0.24 | skipped_fast |
| BTCUSDT | IDLE | 1.18 | 2.08 | 1.92 | -0.01 | 346579490.61 | 0.09 | skipped_fast |
| QNTUSDT | IDLE | 2.63 | 6.2 | 4.81 | -0.0 | 1616533.93 | 4.39 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 5.13 | 4.8 | -0.07 | 501351.33 | 4.26 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 17.46 | 11.41 | 0.01 | 49424.88 | 55.05 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 6.77 | 6.15 | -0.06 | 76089.56 | 16.53 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 8.39 | 7.53 | 0.04 | 81004.74 | 10.65 | skipped_fast |
| REDUSDT | IDLE | 2.57 | 4.5 | 4.31 | -0.0 | 63099.27 | 7.23 | skipped_fast |
| BIOUSDT | IDLE | 2.33 | 4.08 | 3.88 | -0.02 | 67248.81 | 7.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.73 | 3.02 | 2.91 | -0.01 | 198200.08 | 18.11 | skipped_fast |
| HBARUSDT | IDLE | 1.96 | 3.44 | 3.26 | -0.03 | 307909.69 | 4.71 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.49 | 2.4 | -0.02 | 171225.05 | 35.42 | skipped_fast |
| RWAINCUSDT | IDLE | 1.05 | 2.52 | 1.64 | -0.05 | 33296.76 | 41.67 | skipped_fast |
| FLUIDUSDT | IDLE | 1.98 | 5.82 | 3.8 | 0.06 | 22616.8 | 21.71 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.29 | 0.83 | 0.03 | 107402.9 | 27.91 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.31 | -0.01 | 55886.85 | 23.39 | skipped_fast |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
