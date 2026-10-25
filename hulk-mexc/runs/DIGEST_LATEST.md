# Hulk DIGEST — 2026-10-25T01:33:25Z

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
| XRPUSDT | IDLE | 0.72 | 1.38 | 0.35 | 0.01 | 25295150.56 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.23 | 0.25 | -0.01 | 121256181.43 | 0.13 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.77 | 0.17 | 0.0 | 246605086.76 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.22 | 2.79 | 0.92 | -0.03 | 775484.35 | 36.81 | skipped_fast |
| PYTHUSDT | IDLE | 1.79 | 3.36 | 1.43 | 0.02 | 523032.48 | 1.41 | skipped_fast |
| EDELUSDT | IDLE | 1.3 | 3.24 | 1.18 | -0.06 | 586206.04 | 19.89 | skipped_fast |
| ZBCNUSDT | IDLE | 2.41 | 5.28 | 4.48 | 0.01 | 224237.26 | 15.8 | skipped_fast |
| RIZEUSDT | IDLE | 3.1 | 8.8 | 2.18 | -0.01 | 42256.94 | 60.47 | skipped_fast |
| CHIPUSDT | IDLE | 2.35 | 7.21 | 2.12 | 0.05 | 87163.99 | 15.46 | skipped_fast |
| QNTUSDT | IDLE | 1.6 | 3.11 | 0.63 | 0.0 | 369035.61 | 0.55 | skipped_fast |
| KITEUSDT | IDLE | 1.48 | 2.86 | 0.68 | -0.02 | 60661.53 | 12.95 | skipped_fast |
| CCUSDT | IDLE | 0.65 | 1.19 | 0.76 | -0.02 | 222508.88 | 8.9 | skipped_fast |
| REDUSDT | IDLE | 1.13 | 2.74 | 1.94 | 0.02 | 99207.59 | 16.11 | skipped_fast |
| BIOUSDT | IDLE | 1.22 | 2.25 | 1.21 | -0.02 | 66274.63 | 4.37 | skipped_fast |
| RWAINCUSDT | IDLE | 0.75 | 1.49 | 0.11 | -0.0 | 53901.18 | 5.45 | skipped_fast |
| FLUIDUSDT | IDLE | 1.73 | 3.56 | 1.39 | -0.05 | 13084.07 | 21.7 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.14 | 0.28 | 0.01 | 198073.02 | 6.42 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.56 | 0.32 | -0.0 | 54290.8 | 15.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.65 | -0.01 | 37597.08 | 77.07 | skipped_fast |
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
