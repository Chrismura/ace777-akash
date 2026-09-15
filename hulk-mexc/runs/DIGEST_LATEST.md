# Hulk DIGEST — 2026-09-15T16:46:39Z

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
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 6.39 | 5.17 | -0.02 | 82204167.09 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 1.92 | 4.09 | 2.7 | -0.04 | 501718174.56 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.16 | 2.15 | 1.1 | -0.03 | 578901421.94 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 1.77 | 22.79 | 17.31 | 0.24 | 461515.5 | 43.38 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 8.41 | 5.3 | -0.02 | 209318.21 | 34.71 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 11.92 | 9.4 | -0.1 | 94427.96 | 13.33 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 3.41 | 2.74 | -0.04 | 338369.61 | 6.45 | skipped_fast |
| HBARUSDT | IDLE | 2.24 | 4.08 | 2.7 | 0.0 | 469248.12 | 1.29 | skipped_fast |
| PYTHUSDT | IDLE | 1.74 | 3.6 | 0.15 | -0.02 | 298511.71 | 3.66 | skipped_fast |
| KITEUSDT | IDLE | 2.41 | 4.4 | 2.81 | -0.01 | 62627.4 | 12.48 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 4.35 | 3.33 | -0.05 | 8125.88 | 5.73 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.44 | 1.99 | -0.05 | 182733.4 | 10.5 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 2.84 | 0.91 | -0.02 | 82940.47 | 7.97 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 5.38 | 4.68 | -0.05 | 104270.39 | 18.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.21 | 10.95 | 7.53 | 0.04 | 54736.99 | 71.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.57 | 2.82 | 2.2 | -0.04 | 2071.8 | 21.99 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 4.37 | 2.92 | -0.04 | 100001.11 | 65.23 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 2.22 | 0.84 | -0.03 | 50431.31 | 7.98 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.68 | 0.22 | -0.01 | 51894.58 | 14.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.58 | 1.04 | 0.76 | -0.0 | 32628.78 | 55.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
