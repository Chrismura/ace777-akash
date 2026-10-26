# Hulk DIGEST — 2026-10-26T21:30:14Z

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
| ETHUSDT | IDLE | 0.78 | 1.38 | 1.14 | -0.01 | 147558014.38 | 0.13 | skipped_fast |
| XRPUSDT | IDLE | 0.76 | 1.38 | 0.94 | -0.01 | 24456821.21 | 2.32 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 0.93 | 0.62 | -0.01 | 361853006.98 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.32 | 5.55 | 4.6 | 0.06 | 1430165.64 | 2.96 | skipped_fast |
| PYTHUSDT | IDLE | 2.25 | 3.99 | 3.43 | -0.02 | 824652.96 | 4.09 | skipped_fast |
| WUSDT | IDLE | 2.01 | 3.87 | 2.76 | 0.03 | 669009.31 | 26.11 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 12.19 | 9.28 | 0.16 | 324117.71 | 17.4 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 9.85 | 6.0 | -0.12 | 55522.18 | 6.32 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 3.98 | 2.95 | 0.01 | 104324.68 | 27.92 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 2.6 | 2.32 | -0.04 | 186754.88 | 9.15 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 4.4 | 2.26 | -0.0 | 44754.46 | 65.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 2.16 | 1.25 | -0.07 | 220623.52 | 36.51 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.46 | 1.96 | -0.01 | 58563.62 | 9.09 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 2.34 | 2.04 | -0.0 | 62913.95 | 15.14 | skipped_fast |
| FLUIDUSDT | IDLE | 2.72 | 5.19 | 1.72 | -0.02 | 1901.58 | 21.61 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.85 | 0.6 | 0.01 | 53669.41 | 21.05 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.45 | 1.07 | -0.01 | 260076.23 | 7.83 | skipped_fast |
| IOTAUSDT | IDLE | 1.33 | 2.34 | 2.19 | -0.02 | 85730.3 | 26.22 | skipped_fast |
| LAUSDT | IDLE | 1.33 | 2.76 | 0.92 | 0.03 | 64582.58 | 35.65 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.88 | 0.48 | -0.0 | 54057.45 | 15.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.15 | 0.0 | 41845.94 | 76.46 | skipped_fast |
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
