# Hulk DIGEST — 2026-09-11T21:16:56Z

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
| RIZEUSDT | IDLE | 2.15 | 149.56 | 43.79 | 0.94 | 225362.88 | 68.55 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 2.81 | 1.4 | 0.01 | 54885491.62 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 1.1 | 2.37 | 1.68 | 0.03 | 639155159.36 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.5 | 0.89 | 0.0 | 562951650.49 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.48 | 4.61 | 3.6 | -0.02 | 414262.77 | 1.96 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.59 | 10.48 | 1.79 | 0.04 | 166339.5 | 26.14 | skipped_fast |
| WUSDT | IDLE | 2.18 | 4.23 | 2.6 | 0.01 | 202101.28 | 10.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 6.1 | 4.51 | -0.06 | 143762.84 | 17.0 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.74 | 1.11 | -0.01 | 443821.95 | 9.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 2.9 | 2.3 | -0.01 | 189663.81 | 15.95 | skipped_fast |
| RWAINCUSDT | IDLE | 2.53 | 5.21 | 1.16 | 0.05 | 13169.78 | 53.39 | skipped_fast |
| BIOUSDT | IDLE | 1.73 | 3.19 | 1.8 | 0.0 | 83310.69 | 7.96 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 2.31 | 0.73 | 0.05 | 62746.85 | 18.04 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 2.65 | 1.74 | -0.02 | 241038.05 | 1.34 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 1.55 | 0.74 | -0.01 | 59307.17 | 11.98 | skipped_fast |
| TELUSDT | IDLE | 1.59 | 3.23 | 1.85 | -0.02 | 103405.89 | 45.66 | skipped_fast |
| QNTUSDT | IDLE | 1.19 | 2.1 | 1.92 | -0.02 | 41374.83 | 4.69 | skipped_fast |
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
