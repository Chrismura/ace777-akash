# Hulk DIGEST — 2026-09-12T15:32:31Z

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
| ETHUSDT | IDLE | 0.32 | 0.61 | 0.24 | -0.03 | 342394724.7 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.33 | 0.62 | 0.24 | -0.02 | 26487234.36 | 1.46 | skipped_fast |
| BTCUSDT | IDLE | 0.16 | 0.31 | 0.06 | -0.02 | 423651174.56 | 0.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 6.86 | 5.73 | -0.03 | 227292.93 | 17.44 | skipped_fast |
| PYTHUSDT | IDLE | 1.78 | 4.28 | 0.42 | 0.02 | 386400.1 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 2.95 | 7.97 | 0.63 | 0.02 | 80655.45 | 17.72 | skipped_fast |
| RWAINCUSDT | IDLE | 2.79 | 5.17 | 4.81 | -0.01 | 11826.52 | 5.54 | skipped_fast |
| RIZEUSDT | IDLE | 1.58 | 57.62 | 10.04 | 0.9 | 146928.62 | 911.08 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.67 | 1.48 | -0.02 | 259439.62 | 7.14 | skipped_fast |
| WUSDT | IDLE | 0.87 | 1.72 | 0.08 | -0.02 | 125252.58 | 14.19 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.57 | 0.58 | 0.0 | 72761.75 | 7.78 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.72 | 1.13 | 0.02 | 62280.6 | 18.66 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.32 | 0.78 | -0.03 | 60559.52 | 10.33 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 2.05 | 1.07 | -0.08 | 90262.27 | 29.95 | skipped_fast |
| HBARUSDT | IDLE | 0.34 | 0.69 | 0.0 | -0.02 | 202973.78 | 1.34 | skipped_fast |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
