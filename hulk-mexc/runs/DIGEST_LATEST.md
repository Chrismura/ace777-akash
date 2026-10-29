# Hulk DIGEST — 2026-10-29T16:21:05Z

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
| ETHUSDT | IDLE | 1.49 | 2.84 | 0.87 | 0.01 | 267050599.57 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 4.27 | 10.02 | 4.62 | 0.02 | 998567.72 | 12.37 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 2.5 | 0.89 | -0.0 | 25858978.98 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 1.31 | 2.53 | 0.55 | 0.01 | 387943685.13 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.11 | 7.26 | 1.62 | 0.03 | 408024.01 | 8.74 | skipped_fast |
| CHIPUSDT | IDLE | 3.24 | 9.75 | 3.26 | 0.04 | 171858.14 | 7.85 | skipped_fast |
| BIOUSDT | IDLE | 2.79 | 5.58 | 1.11 | 0.03 | 73161.8 | 8.61 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.6 | 1.0 | -0.02 | 401656.15 | 16.83 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 2.82 | 0.63 | -0.04 | 309290.71 | 19.04 | skipped_fast |
| QNTUSDT | IDLE | 2.03 | 3.87 | 1.3 | 0.02 | 435517.18 | 4.05 | skipped_fast |
| HBARUSDT | IDLE | 1.77 | 3.38 | 1.06 | -0.01 | 475532.48 | 6.67 | skipped_fast |
| REDUSDT | IDLE | 2.0 | 3.87 | 0.88 | -0.0 | 63495.89 | 16.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 2.33 | 0.51 | 0.0 | 239668.78 | 26.11 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.86 | 0.47 | 0.0 | 59277.19 | 12.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 2.01 | 0.21 | -0.04 | 32350.87 | 7.04 | skipped_fast |
| FLUIDUSDT | IDLE | 1.74 | 3.62 | 3.06 | -0.05 | 7776.36 | 21.52 | skipped_fast |
| RIZEUSDT | IDLE | 0.42 | 0.78 | 0.4 | -0.03 | 39960.31 | 51.64 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.97 | 0.16 | -0.0 | 54984.54 | 16.08 | skipped_fast |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
