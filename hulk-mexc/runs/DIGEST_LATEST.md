# Hulk DIGEST — 2026-09-22T07:09:00Z

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
| XRPUSDT | IDLE | 0.96 | 2.21 | 0.37 | 0.06 | 119070292.56 | 1.97 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.25 | 0.65 | 0.03 | 710479022.16 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.88 | 0.53 | 0.05 | 1144274228.94 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.91 | 4.44 | 2.04 | 0.08 | 1234261.61 | 1.07 | skipped_fast |
| PYTHUSDT | IDLE | 2.21 | 4.22 | 2.84 | 0.03 | 853326.25 | 4.76 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.51 | 0.21 | 0.05 | 661437.75 | 5.04 | skipped_fast |
| WUSDT | IDLE | 1.58 | 2.97 | 1.31 | -0.0 | 467456.14 | 7.62 | skipped_fast |
| KITEUSDT | IDLE | 3.08 | 6.28 | 0.63 | 0.07 | 82983.27 | 11.13 | skipped_fast |
| EDELUSDT | IDLE | 1.58 | 9.16 | 2.7 | 0.1 | 228620.7 | 9.49 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 3.03 | 1.22 | 0.03 | 272756.32 | 26.46 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.76 | 0.99 | 0.07 | 178636.49 | 16.69 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.56 | 1.54 | 0.02 | 129791.43 | 6.95 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.86 | 0.01 | 0.04 | 97898.06 | 6.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.14 | 21.37 | 5.54 | -0.14 | 51351.89 | 287.91 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 2.18 | 1.26 | 0.07 | 24593.35 | 22.17 | skipped_fast |
| QNTUSDT | IDLE | 1.3 | 2.58 | 0.19 | 0.04 | 121745.46 | 8.84 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 2.5 | 1.77 | 0.06 | 117552.2 | 49.75 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.02 | 0.65 | 0.01 | 56916.98 | 36.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.48 | 0.85 | 0.79 | 0.07 | 12465.48 | 21.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.75 | 0.56 | 0.02 | 41691.49 | 29.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
