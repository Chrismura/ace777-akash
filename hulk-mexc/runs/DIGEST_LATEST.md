# Hulk DIGEST — 2026-09-21T21:07:26Z

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
| XRPUSDT | IDLE | 1.57 | 3.86 | 0.57 | 0.09 | 96647662.8 | 3.27 | skipped_fast |
| ETHUSDT | IDLE | 1.42 | 2.66 | 1.25 | 0.06 | 730914809.72 | 0.22 | skipped_fast |
| BTCUSDT | IDLE | 1.07 | 2.06 | 0.76 | 0.07 | 1026085586.86 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.37 | 5.49 | 4.4 | 0.03 | 671678.14 | 6.29 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 3.42 | 1.54 | 0.08 | 1139115.4 | 1.09 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 3.27 | 1.42 | 0.09 | 588364.09 | 9.42 | skipped_fast |
| WUSDT | IDLE | 1.2 | 2.71 | 1.27 | 0.02 | 582311.46 | 5.97 | skipped_fast |
| ZBCNUSDT | IDLE | 2.27 | 6.77 | 3.4 | 0.08 | 255646.42 | 19.4 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 6.6 | 4.6 | 0.19 | 230869.87 | 23.36 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.87 | 2.52 | -0.0 | 104635.85 | 14.64 | skipped_fast |
| RWAINCUSDT | IDLE | 2.45 | 6.59 | 0.43 | 0.09 | 18804.66 | 82.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.08 | 5.1 | 3.23 | 0.09 | 142483.47 | 19.59 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.5 | 1.65 | 0.04 | 103407.03 | 13.95 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 2.46 | 1.53 | 0.03 | 81406.27 | 9.29 | skipped_fast |
| TELUSDT | IDLE | 1.67 | 4.98 | 2.07 | 0.09 | 107707.36 | 42.33 | skipped_fast |
| QNTUSDT | IDLE | 1.3 | 2.56 | 0.22 | 0.05 | 107834.24 | 10.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.22 | 2.88 | 1.15 | 0.09 | 10708.11 | 23.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 6.2 | 1.38 | -0.11 | 48424.48 | 203.39 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.16 | 0.79 | 0.01 | 56669.76 | 21.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.17 | 0.03 | 42362.82 | 14.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
