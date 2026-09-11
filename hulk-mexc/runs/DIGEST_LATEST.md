# Hulk DIGEST — 2026-09-11T00:17:14Z

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
| XRPUSDT | IDLE | 1.2 | 2.22 | 1.16 | -0.04 | 42426514.91 | 2.98 | skipped_fast |
| ETHUSDT | IDLE | 0.84 | 1.55 | 0.88 | -0.01 | 423961612.15 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.11 | 0.66 | -0.02 | 539726445.38 | 0.13 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 10.01 | 7.79 | -0.09 | 100080.67 | 15.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 2.94 | 2.27 | -0.01 | 431109.23 | 3.9 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 2.52 | 1.36 | -0.06 | 477282.59 | 6.09 | skipped_fast |
| ZBCNUSDT | IDLE | 2.28 | 4.05 | 3.35 | -0.03 | 204502.07 | 18.49 | skipped_fast |
| RIZEUSDT | IDLE | 0.61 | 34.58 | 3.79 | -0.44 | 136810.34 | 87.95 | skipped_fast |
| BIOUSDT | IDLE | 1.63 | 2.97 | 1.89 | -0.04 | 77750.47 | 8.05 | skipped_fast |
| WUSDT | IDLE | 1.18 | 2.17 | 1.25 | -0.05 | 169148.29 | 14.67 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.62 | 2.15 | -0.05 | 56851.98 | 13.86 | skipped_fast |
| REDUSDT | IDLE | 0.69 | 1.33 | 0.82 | -0.07 | 66921.83 | 18.99 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 2.5 | 1.88 | -0.01 | 86007.05 | 5.64 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.67 | 0.97 | -0.02 | 193549.48 | 1.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.24 | 0.28 | 0.01 | 4454.55 | 39.14 | skipped_fast |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
