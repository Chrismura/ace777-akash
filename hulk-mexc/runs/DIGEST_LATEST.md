# Hulk DIGEST — 2026-08-22T15:58:00Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.44 | 0.04 | 51480031.89 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.2 | 0.02 | 216051869.92 | 1.39 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 5.65 | 2.41 | 0.09 | 759681.41 | 4.27 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.48 | -0.02 | 1151215.31 | 5.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 2.09 | -0.1 | 604362.95 | 6.79 | skipped_fast |
| WUSDT | IDLE | 0.8 | 3.17 | 2.15 | -0.02 | 554152.07 | 13.96 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 6.37 | 1.82 | 0.03 | 85580.29 | 10.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 2.07 | -0.04 | 320426.76 | 23.17 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.2 | -0.07 | 218762.56 | 3.32 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.48 | -0.14 | 134179.94 | 22.02 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.24 | 0.03 | 56503.95 | 45.5 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.01 | 138820.59 | 42.71 | skipped_fast |
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
