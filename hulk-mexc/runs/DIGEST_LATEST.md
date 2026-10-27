# Hulk DIGEST — 2026-10-27T11:10:09Z

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
| XRPUSDT | IDLE | 0.7 | 1.37 | 0.14 | 0.02 | 21322231.66 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.17 | 0.17 | -0.0 | 143152365.38 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.8 | 0.1 | -0.0 | 354867549.92 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.17 | 6.93 | 3.27 | -0.03 | 1165062.13 | 4.38 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.6 | 1.11 | -0.03 | 567178.93 | 6.84 | skipped_fast |
| WUSDT | IDLE | 1.3 | 2.42 | 1.18 | 0.06 | 515371.74 | 19.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.14 | 5.75 | 0.38 | 0.13 | 312385.21 | 15.25 | skipped_fast |
| RWAINCUSDT | IDLE | 2.15 | 8.54 | 6.8 | -0.12 | 54278.44 | 40.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.19 | 3.29 | 2.2 | 0.01 | 261780.69 | 24.59 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.42 | 1.12 | -0.04 | 230446.45 | 7.21 | skipped_fast |
| EDELUSDT | IDLE | 0.75 | 1.38 | 0.8 | 0.0 | 334145.25 | 12.45 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.85 | 0.69 | 0.0 | 62522.59 | 15.63 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.62 | 1.08 | 0.0 | 56044.8 | 4.53 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.93 | 0.18 | 0.02 | 53454.91 | 9.64 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.89 | 0.96 | -0.01 | 201662.61 | 9.19 | skipped_fast |
| RIZEUSDT | IDLE | 0.61 | 1.1 | 0.84 | -0.02 | 42927.67 | 37.41 | skipped_fast |
| WAXLUSDT | IDLE | 1.8 | 3.31 | 1.97 | 0.02 | 55066.2 | 51.67 | skipped_fast |
| LAUSDT | IDLE | 1.34 | 2.49 | 1.32 | -0.0 | 62327.82 | 24.41 | skipped_fast |
| IOTAUSDT | IDLE | 1.01 | 2.0 | 0.17 | -0.0 | 95311.7 | 14.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.16 | 1.38 | 0.04 | 3147.46 | 21.41 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.22 | 0.32 | -0.01 | 56146.08 | 8.04 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.77 | 0.66 | 0.0 | 37548.74 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
