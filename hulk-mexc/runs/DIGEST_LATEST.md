# Hulk DIGEST — 2026-10-26T08:17:09Z

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
| XRPUSDT | IDLE | 0.92 | 1.63 | 1.45 | -0.02 | 19236137.93 | 2.35 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.59 | 0.9 | -0.01 | 109198827.2 | 0.87 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.14 | 0.67 | -0.01 | 216647481.82 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.31 | 2.73 | 2.4 | 0.03 | 804172.61 | 4.12 | skipped_fast |
| CHIPUSDT | IDLE | 4.03 | 9.75 | 4.61 | 0.02 | 107141.4 | 26.82 | skipped_fast |
| WUSDT | IDLE | 1.39 | 2.51 | 1.77 | -0.04 | 509585.11 | 15.37 | skipped_fast |
| QNTUSDT | IDLE | 1.24 | 3.69 | 0.64 | 0.06 | 748555.77 | 2.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.14 | 2.88 | 0.0 | 181864.31 | 23.08 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 3.63 | 3.05 | -0.02 | 61034.39 | 15.37 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 2.83 | 2.38 | -0.0 | 54442.14 | 9.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.41 | 2.7 | 1.95 | -0.05 | 67969.73 | 11.68 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.52 | 2.15 | -0.02 | 60981.36 | 9.14 | skipped_fast |
| CCUSDT | IDLE | 0.84 | 1.49 | 1.33 | 0.0 | 162572.74 | 6.96 | skipped_fast |
| EDELUSDT | IDLE | 0.82 | 2.0 | 1.15 | 0.06 | 140819.07 | 22.0 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.57 | 1.19 | -0.01 | 170421.68 | 7.84 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 0.93 | 0.28 | 0.0 | 33105.72 | 59.87 | skipped_fast |
| FLUIDUSDT | IDLE | 0.28 | 1.49 | 0.0 | -0.02 | 19116.06 | 21.53 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.01 | 52787.25 | 23.89 | skipped_fast |
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
