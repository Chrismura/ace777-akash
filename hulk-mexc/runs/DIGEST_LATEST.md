# Hulk DIGEST — 2026-10-28T07:27:26Z

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
| XRPUSDT | IDLE | 0.85 | 1.48 | 1.45 | 0.02 | 19555896.97 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.44 | 0.78 | 0.66 | 0.02 | 242604995.69 | 0.21 | skipped_fast |
| BTCUSDT | IDLE | 0.25 | 0.44 | 0.34 | 0.02 | 295690008.64 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 2.87 | 2.64 | -0.02 | 365307.59 | 1.39 | skipped_fast |
| WUSDT | IDLE | 0.68 | 1.32 | 1.08 | 0.02 | 616299.07 | 18.78 | skipped_fast |
| EDELUSDT | IDLE | 1.54 | 2.75 | 2.14 | 0.02 | 350987.71 | 24.55 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 3.51 | 2.49 | -0.04 | 205872.08 | 20.6 | skipped_fast |
| RWAINCUSDT | IDLE | 2.03 | 4.04 | 3.69 | -0.08 | 57495.96 | 34.16 | skipped_fast |
| RIZEUSDT | IDLE | 2.43 | 4.52 | 2.24 | 0.03 | 36177.13 | 61.36 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 1.86 | 1.66 | 0.01 | 239612.44 | 8.1 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.01 | 1.82 | 0.07 | 119118.4 | 14.67 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.79 | 1.72 | -0.01 | 372626.67 | 9.21 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.75 | 1.52 | 0.03 | 60306.11 | 13.72 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 1.55 | 1.53 | 0.02 | 81929.09 | 17.69 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 1.64 | 1.34 | 0.04 | 58153.72 | 14.39 | skipped_fast |
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
