# Hulk DIGEST — 2026-09-17T10:16:22Z

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
| XRPUSDT | IDLE | 0.69 | 1.23 | 1.05 | 0.01 | 56529759.29 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.88 | 0.74 | 0.01 | 372315043.3 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.59 | 0.48 | 0.01 | 479006209.4 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 5.64 | 1.04 | 0.12 | 632215.85 | 10.82 | skipped_fast |
| PYTHUSDT | IDLE | 1.44 | 2.55 | 2.16 | 0.03 | 527717.73 | 9.28 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 9.19 | 1.74 | 0.06 | 142270.34 | 15.4 | skipped_fast |
| EDELUSDT | IDLE | 2.23 | 8.83 | 6.54 | -0.11 | 207966.98 | 41.02 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 2.23 | 1.84 | 0.01 | 170919.28 | 23.19 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.14 | 3.98 | 0.05 | 68227.57 | 14.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.64 | 2.87 | 2.79 | -0.01 | 17661.26 | 17.54 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.66 | 0.25 | 0.0 | 462474.03 | 2.68 | skipped_fast |
| WUSDT | IDLE | 0.63 | 1.15 | 0.83 | 0.04 | 222461.92 | 13.0 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.6 | 1.42 | 0.01 | 69394.08 | 4.0 | skipped_fast |
| REDUSDT | IDLE | 0.96 | 1.93 | 0.0 | 0.02 | 61000.59 | 12.1 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 8.55 | 6.93 | -0.19 | 59865.16 | 80.1 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 2.35 | 1.0 | 0.03 | 34533.12 | 4.9 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 1.82 | 0.82 | -0.01 | 111175.85 | 34.66 | skipped_fast |
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
