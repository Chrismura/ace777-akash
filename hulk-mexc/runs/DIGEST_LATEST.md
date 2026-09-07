# Hulk DIGEST — 2026-09-07T23:47:48Z

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
| XRPUSDT | IDLE | 0.76 | 1.45 | 0.46 | -0.02 | 36439959.48 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.87 | 0.27 | -0.01 | 327450252.91 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.79 | 0.39 | -0.02 | 434095260.24 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.37 | 2.5 | 1.6 | -0.04 | 504224.97 | 1.85 | skipped_fast |
| CCUSDT | IDLE | 1.57 | 2.99 | 1.68 | -0.05 | 438510.41 | 9.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 6.28 | 2.41 | -0.08 | 220016.17 | 13.0 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.83 | 1.29 | 0.01 | 573255.67 | 1.22 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 6.87 | 5.29 | -0.08 | 4654.4 | 83.16 | skipped_fast |
| WUSDT | IDLE | 0.98 | 1.83 | 0.92 | -0.01 | 240969.22 | 12.67 | skipped_fast |
| ZBCNUSDT | IDLE | 0.94 | 2.52 | 1.35 | -0.04 | 217689.77 | 12.3 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 5.58 | 2.64 | -0.03 | 54847.12 | 66.79 | skipped_fast |
| REDUSDT | IDLE | 1.27 | 2.37 | 1.13 | 0.04 | 57915.16 | 9.11 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.97 | 0.76 | -0.02 | 66759.0 | 3.67 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 2.03 | 0.63 | -0.06 | 61981.48 | 11.73 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.01 | 0.99 | -0.02 | 82081.63 | 35.17 | skipped_fast |
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
