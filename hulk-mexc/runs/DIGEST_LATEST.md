# Hulk DIGEST — 2026-09-07T04:33:19Z

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
| XRPUSDT | IDLE | 1.19 | 2.12 | 1.67 | -0.01 | 28656508.0 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.94 | 1.65 | 1.56 | -0.0 | 289185113.68 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.22 | 1.14 | -0.0 | 396058586.54 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.81 | 4.96 | 4.46 | -0.02 | 594997.0 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 2.73 | 5.56 | 3.99 | -0.02 | 399045.51 | 3.49 | skipped_fast |
| EDELUSDT | IDLE | 3.93 | 7.34 | 3.51 | 0.01 | 67823.4 | 65.15 | skipped_fast |
| WUSDT | IDLE | 1.58 | 2.87 | 1.9 | 0.03 | 408622.15 | 6.73 | skipped_fast |
| CCUSDT | IDLE | 1.57 | 2.82 | 2.18 | 0.0 | 394912.44 | 8.19 | skipped_fast |
| RWAINCUSDT | IDLE | 2.07 | 8.05 | 4.26 | 0.08 | 6092.32 | 19.19 | skipped_fast |
| BIOUSDT | IDLE | 1.58 | 2.8 | 2.37 | -0.03 | 78613.01 | 3.68 | skipped_fast |
| TELUSDT | IDLE | 2.93 | 5.18 | 4.54 | 0.01 | 95575.35 | 40.62 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.08 | 1.79 | -0.01 | 419008.0 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.21 | 0.88 | -0.01 | 135569.75 | 10.23 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.24 | 1.65 | -0.03 | 56904.3 | 10.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.0 | 8.5 | 4.51 | -0.19 | 71153.3 | 59.82 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.09 | 1.28 | 0.01 | 66840.92 | 11.81 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.22 | 0.82 | 0.02 | 37888.4 | 6.0 | skipped_fast |
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
