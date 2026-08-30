# Hulk DIGEST — 2026-08-30T14:13:09Z

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
| XRPUSDT | IDLE | 1.03 | 2.02 | 0.33 | 0.01 | 18783886.29 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.27 | 0.12 | 0.02 | 251651831.77 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.54 | 1.06 | 0.12 | 0.02 | 157685697.45 | 0.28 | skipped_fast |
| CHIPUSDT | IDLE | 3.27 | 6.51 | 0.26 | 0.02 | 584122.42 | 2.41 | skipped_fast |
| PYTHUSDT | IDLE | 3.87 | 7.51 | 1.57 | 0.04 | 413888.33 | 14.16 | skipped_fast |
| ZBCNUSDT | IDLE | 2.58 | 4.6 | 3.8 | -0.02 | 151887.18 | 8.96 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.68 | 0.3 | 0.04 | 206247.16 | 2.11 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.62 | 1.28 | 0.03 | 284511.41 | 8.46 | skipped_fast |
| REDUSDT | IDLE | 1.25 | 2.39 | 0.67 | 0.01 | 60390.21 | 11.76 | skipped_fast |
| EDELUSDT | IDLE | 0.43 | 7.09 | 3.63 | 0.11 | 111877.0 | 16.74 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.36 | 0.25 | -0.0 | 71615.31 | 3.64 | skipped_fast |
| KITEUSDT | IDLE | 0.75 | 1.35 | 0.99 | -0.04 | 69393.93 | 11.73 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 2.75 | 1.03 | -0.06 | 46208.09 | 61.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 2.05 | 0.0 | -0.01 | 1706.2 | 61.13 | skipped_fast |
| TELUSDT | IDLE | 1.33 | 2.59 | 0.53 | -0.02 | 78562.33 | 35.4 | skipped_fast |
| HBARUSDT | IDLE | 0.66 | 1.23 | 0.55 | 0.0 | 142733.35 | 1.33 | skipped_fast |
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
