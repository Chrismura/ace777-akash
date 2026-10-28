# Hulk DIGEST — 2026-10-28T01:22:19Z

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
| XRPUSDT | IDLE | 0.67 | 1.27 | 0.43 | 0.02 | 19050956.44 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.03 | 0.75 | 0.01 | 239449527.73 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.81 | 0.66 | 0.01 | 325071300.81 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.09 | 3.95 | 1.58 | 0.02 | 428051.56 | 24.26 | skipped_fast |
| WUSDT | IDLE | 0.91 | 2.02 | 1.26 | 0.03 | 672080.52 | 24.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.83 | 6.42 | 4.25 | -0.02 | 245096.69 | 37.19 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 1.94 | 0.65 | -0.01 | 395942.58 | 5.43 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 3.57 | 2.93 | -0.04 | 55344.61 | 6.7 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 1.55 | 0.05 | -0.0 | 224947.67 | 7.04 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 2.53 | 1.11 | 0.08 | 128070.03 | 22.0 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.38 | 1.89 | 0.05 | 59753.22 | 14.28 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 1.83 | 0.85 | 0.04 | 58085.16 | 9.29 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.6 | 0.92 | 0.02 | 59829.31 | 13.25 | skipped_fast |
| HBARUSDT | IDLE | 0.71 | 1.31 | 0.68 | -0.01 | 309280.18 | 11.81 | skipped_fast |
| RIZEUSDT | IDLE | 0.61 | 1.19 | 0.25 | 0.01 | 33813.78 | 62.38 | skipped_fast |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
