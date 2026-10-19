# Hulk DIGEST — 2026-10-19T23:07:21Z

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
| XRPUSDT | IDLE | 0.61 | 1.15 | 0.44 | 0.0 | 21547970.24 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.14 | 0.41 | 0.01 | 128595205.21 | 0.71 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.57 | 0.23 | 0.0 | 325824432.28 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.92 | 3.64 | 1.36 | -0.01 | 817082.72 | 1.36 | skipped_fast |
| WUSDT | IDLE | 2.19 | 4.1 | 1.89 | 0.03 | 706169.51 | 14.34 | skipped_fast |
| QNTUSDT | IDLE | 1.32 | 2.46 | 1.22 | 0.03 | 707992.69 | 0.51 | skipped_fast |
| EDELUSDT | IDLE | 2.15 | 3.95 | 2.3 | 0.01 | 200471.23 | 44.78 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 1.99 | 0.84 | 0.04 | 369506.39 | 6.71 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 3.71 | 1.35 | 0.07 | 76157.83 | 10.61 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 2.64 | 1.16 | 0.02 | 229604.29 | 20.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.55 | 2.93 | 1.13 | 0.03 | 78483.86 | 14.27 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.79 | 0.36 | -0.03 | 468447.84 | 4.82 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.7 | 0.54 | 0.01 | 57558.87 | 16.64 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.11 | 0.46 | 0.01 | 68822.35 | 8.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.85 | 1.7 | 1.42 | 0.04 | 71439.83 | 10.3 | skipped_fast |
| RIZEUSDT | IDLE | 0.61 | 1.98 | 1.69 | -0.05 | 53442.01 | 53.51 | skipped_fast |
| LAUSDT | IDLE | 1.21 | 2.3 | 0.81 | 0.0 | 55927.21 | 19.06 | skipped_fast |
| IOTAUSDT | IDLE | 1.17 | 2.28 | 0.44 | 0.01 | 90515.4 | 31.08 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.87 | 0.16 | 0.01 | 54387.87 | 23.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.29 | 0.16 | 0.0 | 40694.78 | 7.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.04 | 4713.92 | 19.91 | skipped_fast |
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
