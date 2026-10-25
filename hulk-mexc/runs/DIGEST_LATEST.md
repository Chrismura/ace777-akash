# Hulk DIGEST — 2026-10-25T13:37:59Z

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
| ETHUSDT | IDLE | 0.7 | 1.29 | 0.75 | -0.02 | 132400719.5 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.59 | 1.09 | 0.56 | 0.01 | 21967334.89 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.75 | 0.51 | -0.01 | 197678138.0 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.39 | 3.06 | -0.04 | 816438.92 | 17.75 | skipped_fast |
| PYTHUSDT | IDLE | 1.59 | 3.1 | 0.49 | 0.03 | 489343.69 | 2.81 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.5 | 10.5 | 8.86 | -0.03 | 19080.13 | 16.84 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 3.37 | 1.0 | -0.03 | 489003.05 | 37.13 | skipped_fast |
| REDUSDT | IDLE | 2.25 | 3.98 | 3.53 | -0.03 | 67302.2 | 18.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 5.7 | 3.32 | 0.04 | 101997.13 | 20.3 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.07 | 0.23 | 0.02 | 404424.54 | 1.64 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 2.2 | 0.57 | -0.0 | 189232.81 | 8.93 | skipped_fast |
| ZBCNUSDT | IDLE | 0.88 | 1.9 | 1.85 | 0.03 | 231501.46 | 18.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.32 | 2.5 | 0.92 | -0.03 | 58146.32 | 5.46 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 2.09 | 0.85 | -0.03 | 65433.48 | 4.49 | skipped_fast |
| KITEUSDT | IDLE | 0.92 | 1.7 | 0.92 | -0.05 | 59035.59 | 11.7 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 2.14 | 0.87 | -0.03 | 39958.31 | 39.35 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.79 | 1.5 | -0.0 | 194464.87 | 10.43 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.43 | 1.33 | -0.0 | 51646.86 | 23.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.09 | -0.01 | 37251.57 | 77.07 | skipped_fast |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
