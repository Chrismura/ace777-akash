# Hulk DIGEST — 2026-10-25T19:40:18Z

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
| XRPUSDT | IDLE | 0.79 | 1.46 | 0.75 | 0.01 | 14397681.51 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.45 | 0.57 | 0.0 | 81211295.14 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.8 | 0.42 | 0.0 | 143266322.07 | 0.0 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.51 | 8.06 | 1.29 | 0.04 | 394486.11 | 25.47 | skipped_fast |
| ZBCNUSDT | IDLE | 4.19 | 8.0 | 3.31 | 0.03 | 196944.18 | 6.72 | skipped_fast |
| PYTHUSDT | IDLE | 2.85 | 6.11 | 0.11 | 0.08 | 498928.14 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 2.87 | 9.11 | 2.86 | 0.09 | 619456.97 | 2.57 | skipped_fast |
| WUSDT | IDLE | 2.09 | 3.99 | 1.28 | -0.01 | 579415.38 | 18.22 | skipped_fast |
| CHIPUSDT | IDLE | 3.05 | 5.84 | 1.75 | 0.05 | 90990.97 | 17.62 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 5.12 | 3.05 | -0.01 | 52750.14 | 11.57 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.2 | 16.72 | 0.56 | 0.05 | 19349.45 | 21.55 | skipped_fast |
| REDUSDT | IDLE | 2.21 | 4.24 | 1.22 | -0.01 | 63431.2 | 8.94 | skipped_fast |
| RIZEUSDT | IDLE | 2.45 | 6.05 | 4.1 | -0.0 | 48374.96 | 58.13 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.64 | 0.69 | 0.02 | 176696.55 | 7.8 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 2.26 | 0.84 | -0.01 | 60003.06 | 4.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 1.83 | 1.36 | -0.01 | 64160.74 | 27.75 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 2.14 | 0.22 | 0.0 | 122850.36 | 7.7 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.96 | 0.24 | 0.0 | 51408.99 | 7.96 | skipped_fast |
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
