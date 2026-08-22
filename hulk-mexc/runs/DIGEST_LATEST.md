# Hulk DIGEST — 2026-08-22T16:14:30Z

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
| PYTHUSDT | IDLE | 1.52 | 7.24 | 1.87 | 0.04 | 51452014.71 | 1.98 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.08 | 0.03 | 215444847.1 | 1.39 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.35 | -0.01 | 1140895.16 | 1.31 | skipped_fast |
| CCUSDT | IDLE | 1.0 | 4.14 | 2.95 | 0.08 | 766648.87 | 4.3 | skipped_fast |
| CHIPUSDT | IDLE | 0.58 | 3.36 | 1.46 | -0.11 | 623788.19 | 6.73 | skipped_fast |
| WUSDT | IDLE | 0.67 | 2.58 | 2.36 | -0.03 | 546243.96 | 11.8 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 3.49 | 2.53 | -0.06 | 318012.15 | 17.59 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.26 | -0.08 | 219670.99 | 6.65 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 4.35 | 1.17 | 0.04 | 85449.6 | 12.43 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.78 | -0.12 | 134904.93 | 13.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.18 | 0.03 | 56528.96 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.73 | -0.0 | 137275.5 | 31.98 | skipped_fast |
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
