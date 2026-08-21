# Hulk DIGEST — 2026-08-21T22:33:26Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.38 | 5.17 | 0.84 | 0.11 | 5812701.25 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 1.54 | 5.68 | 0.14 | 0.14 | 134311574.96 | 3.48 | skipped_fast |
| HBARUSDT | IDLE | 2.27 | 4.71 | 1.6 | 0.07 | 865599.63 | 2.55 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 6.48 | 0.36 | 0.13 | 657959.66 | 7.11 | skipped_fast |
| WUSDT | IDLE | 2.51 | 5.3 | 0.93 | 0.08 | 370752.96 | 14.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.45 | 0.06 | 533924.04 | 6.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.6 | 6.77 | 0.8 | 0.11 | 502464.24 | 30.61 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.57 | 0.02 | 188362.74 | 3.12 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.2 | 0.18 | 155950.27 | 11.31 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.22 | -0.03 | 82619.41 | 43.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.07 | 2.43 | 0.02 | 10212.45 | 16.17 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.92 | 0.05 | 187182.46 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 3.58 | 1.4 | 0.11 | 61497.8 | 12.93 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.74 | 0.06 | 56376.5 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 3.76 | 0.0 | 0.06 | 72297.93 | 7.6 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.16 | 0.04 | 54122.73 | 24.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
