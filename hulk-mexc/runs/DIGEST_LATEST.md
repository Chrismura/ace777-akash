# Hulk DIGEST — 2026-09-07T02:47:12Z

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
| XRPUSDT | IDLE | 1.1 | 2.12 | 0.49 | 0.0 | 27273135.1 | 2.11 | skipped_fast |
| ETHUSDT | IDLE | 0.94 | 1.83 | 0.38 | 0.01 | 275181950.6 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.12 | 0.38 | 0.0 | 372129359.2 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.42 | 4.69 | 0.99 | 0.05 | 603998.94 | 1.75 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 3.59 | 2.4 | -0.02 | 399374.49 | 1.72 | skipped_fast |
| WUSDT | IDLE | 1.61 | 3.21 | 0.04 | 0.04 | 402874.83 | 10.41 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 3.03 | 1.34 | -0.0 | 379631.97 | 7.23 | skipped_fast |
| RWAINCUSDT | IDLE | 2.55 | 10.32 | 2.64 | 0.13 | 6211.98 | 43.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.78 | 3.35 | 1.37 | 0.01 | 136391.54 | 18.74 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.35 | 2.46 | 0.01 | 67407.74 | 10.24 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.16 | 0.0 | 0.01 | 51623.21 | 18.55 | skipped_fast |
| TELUSDT | IDLE | 3.08 | 5.56 | 4.06 | 0.02 | 95172.32 | 51.44 | skipped_fast |
| BIOUSDT | IDLE | 1.57 | 2.95 | 1.25 | -0.02 | 79729.66 | 10.88 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 2.01 | 0.41 | 0.01 | 455943.13 | 1.22 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 2.01 | 0.2 | -0.01 | 58105.76 | 10.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.31 | 11.02 | 6.57 | -0.19 | 69387.68 | 154.81 | skipped_fast |
| FLUIDUSDT | IDLE | 0.89 | 1.7 | 0.55 | 0.01 | 933.23 | 16.43 | skipped_fast |
| QNTUSDT | IDLE | 0.62 | 1.22 | 0.1 | 0.02 | 38233.8 | 7.46 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.64 | -0.01 | 53487.29 | 14.4 | skipped_fast |
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
