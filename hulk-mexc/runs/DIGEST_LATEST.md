# Hulk DIGEST — 2026-08-29T02:06:55Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.73 | 1.42 | 0.29 | -0.04 | 48985393.55 | 2.17 | skipped_fast |
| QAITUSDT | IDLE | 2.08 | 27.55 | 20.0 | -0.02 | 82499.69 | 66.82 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.06 | 0.63 | -0.03 | 590307.58 | 2.1 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 6.84 | 6.26 | -0.08 | 34987.34 | 55.32 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.88 | 1.3 | -0.02 | 267354.47 | 9.94 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.79 | 1.6 | -0.04 | 469434.31 | 1.32 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.67 | 1.8 | -0.02 | 78954.05 | 8.67 | skipped_fast |
| WUSDT | IDLE | 0.8 | 1.54 | 0.4 | -0.05 | 219279.14 | 13.11 | skipped_fast |
| ZBCNUSDT | IDLE | 0.68 | 1.76 | 0.94 | -0.08 | 171640.23 | 9.23 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.76 | 1.47 | -0.04 | 62082.56 | 12.13 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.3 | 0.25 | -0.04 | 85464.47 | 3.58 | skipped_fast |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
