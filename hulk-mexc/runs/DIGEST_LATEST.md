# Hulk DIGEST — 2026-10-25T05:58:14Z

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
| XRPUSDT | IDLE | 0.75 | 1.32 | 1.15 | 0.01 | 26599137.39 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.03 | 0.83 | -0.01 | 124155172.59 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.63 | 0.55 | -0.0 | 228740896.31 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.29 | 2.35 | 1.6 | -0.06 | 772978.85 | 16.46 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.1 | 1.9 | -0.0 | 505975.76 | 1.41 | skipped_fast |
| EDELUSDT | IDLE | 0.75 | 1.77 | 1.31 | -0.07 | 594871.91 | 13.28 | skipped_fast |
| KITEUSDT | IDLE | 2.21 | 3.87 | 3.6 | -0.05 | 59637.33 | 9.78 | skipped_fast |
| QNTUSDT | IDLE | 2.06 | 3.88 | 1.6 | 0.0 | 378469.21 | 0.55 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 4.52 | 4.09 | 0.03 | 91679.83 | 18.03 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 3.84 | 1.93 | -0.03 | 83769.53 | 10.08 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.53 | 2.2 | -0.03 | 65471.98 | 4.42 | skipped_fast |
| ZBCNUSDT | IDLE | 0.82 | 1.85 | 1.14 | 0.01 | 229929.87 | 18.1 | skipped_fast |
| CCUSDT | IDLE | 0.8 | 1.41 | 1.25 | -0.03 | 212150.17 | 7.95 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 2.25 | 0.54 | -0.01 | 57218.3 | 16.21 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 1.98 | 1.78 | -0.0 | 206492.13 | 15.53 | skipped_fast |
| RIZEUSDT | IDLE | 0.72 | 2.01 | 0.67 | -0.04 | 41586.51 | 46.24 | skipped_fast |
| IOTAUSDT | IDLE | 1.06 | 1.91 | 1.4 | -0.02 | 66942.09 | 22.91 | skipped_fast |
| FLUIDUSDT | IDLE | 1.19 | 2.08 | 2.04 | -0.04 | 9992.03 | 21.65 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.43 | 0.63 | 0.0 | 52882.95 | 23.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.74 | 0.29 | -0.01 | 37505.92 | 77.07 | skipped_fast |
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
