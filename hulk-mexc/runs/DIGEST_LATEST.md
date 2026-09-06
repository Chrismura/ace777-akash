# Hulk DIGEST — 2026-09-06T20:31:55Z

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
| ETHUSDT | IDLE | 0.58 | 1.13 | 0.15 | 0.01 | 249785399.98 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.52 | 1.03 | 0.06 | 0.0 | 23541995.12 | 2.12 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.71 | 0.04 | 0.0 | 346918314.49 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.02 | 5.82 | 4.54 | 0.04 | 394170.16 | 7.79 | skipped_fast |
| PYTHUSDT | IDLE | 1.44 | 2.71 | 1.14 | -0.0 | 530708.6 | 1.83 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 3.93 | 0.26 | -0.01 | 416950.12 | 1.71 | skipped_fast |
| RIZEUSDT | IDLE | 2.05 | 14.15 | 7.1 | -0.16 | 71943.79 | 64.9 | skipped_fast |
| RWAINCUSDT | IDLE | 2.37 | 5.16 | 2.7 | 0.02 | 5858.31 | 31.1 | skipped_fast |
| BIOUSDT | IDLE | 1.79 | 3.4 | 1.18 | -0.01 | 89367.72 | 3.61 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.65 | 0.27 | 0.01 | 301990.05 | 10.9 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 2.42 | 2.26 | -0.02 | 59337.04 | 10.42 | skipped_fast |
| ZBCNUSDT | IDLE | 0.76 | 1.46 | 0.41 | 0.01 | 164787.15 | 15.55 | skipped_fast |
| REDUSDT | IDLE | 0.96 | 1.87 | 0.32 | 0.01 | 67460.18 | 12.48 | skipped_fast |
| HBARUSDT | IDLE | 0.44 | 0.87 | 0.11 | -0.0 | 412774.11 | 1.24 | skipped_fast |
| TELUSDT | IDLE | 1.21 | 2.36 | 0.35 | -0.0 | 67758.08 | 34.64 | skipped_fast |
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
