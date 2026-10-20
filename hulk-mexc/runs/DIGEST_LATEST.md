# Hulk DIGEST — 2026-10-20T23:26:51Z

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
| XRPUSDT | IDLE | 1.09 | 2.08 | 0.61 | 0.02 | 24742720.24 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.6 | 0.68 | 0.02 | 175314537.73 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.94 | 0.27 | 0.01 | 330895692.74 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.76 | 5.49 | 1.87 | 0.09 | 1183416.42 | 1.26 | skipped_fast |
| WUSDT | IDLE | 1.47 | 2.76 | 1.2 | 0.02 | 656799.44 | 14.12 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 3.39 | 2.17 | -0.0 | 814088.26 | 0.51 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 9.94 | 7.86 | -0.03 | 76676.64 | 5.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 4.01 | 2.61 | 0.05 | 444674.92 | 6.74 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 13.83 | 11.0 | 0.06 | 17162.46 | 21.63 | skipped_fast |
| CCUSDT | IDLE | 0.9 | 1.63 | 1.17 | 0.0 | 383142.77 | 8.56 | skipped_fast |
| RIZEUSDT | IDLE | 2.14 | 8.6 | 5.1 | 0.06 | 75083.87 | 57.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 2.86 | 1.15 | 0.02 | 192923.53 | 28.54 | skipped_fast |
| EDELUSDT | IDLE | 0.41 | 3.73 | 1.02 | 0.33 | 363307.23 | 19.53 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.17 | 1.0 | 0.05 | 62272.61 | 8.11 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.83 | 0.08 | 0.02 | 353573.38 | 5.92 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.8 | 0.31 | 0.01 | 58385.32 | 10.66 | skipped_fast |
| KITEUSDT | IDLE | 0.7 | 1.23 | 1.12 | -0.01 | 73647.88 | 11.54 | skipped_fast |
| IOTAUSDT | IDLE | 1.11 | 2.06 | 1.08 | 0.03 | 72968.35 | 25.78 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.95 | 0.08 | 0.0 | 51998.49 | 23.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.43 | 0.07 | 0.0 | 39273.35 | 11.4 | skipped_fast |
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
