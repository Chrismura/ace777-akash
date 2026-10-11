# Hulk DIGEST — 2026-10-11T03:09:15Z

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
| XRPUSDT | IDLE | 0.42 | 0.75 | 0.54 | -0.0 | 11571137.71 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.22 | 0.42 | 0.14 | 0.01 | 137366672.86 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.25 | 0.12 | 0.01 | 144954770.71 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.15 | 3.66 | 2.28 | 0.03 | 1206060.81 | 5.68 | skipped_fast |
| QNTUSDT | IDLE | 1.19 | 2.14 | 1.62 | -0.05 | 1302154.23 | 0.42 | skipped_fast |
| PYTHUSDT | IDLE | 1.98 | 3.91 | 0.39 | -0.0 | 787128.02 | 3.76 | skipped_fast |
| RIZEUSDT | IDLE | 3.15 | 6.26 | 4.75 | -0.06 | 33286.53 | 39.97 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 9.26 | 5.61 | 0.3 | 279807.26 | 10.3 | skipped_fast |
| EDELUSDT | IDLE | 1.61 | 2.98 | 1.62 | -0.04 | 284218.56 | 13.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.85 | 1.29 | 0.01 | 170503.37 | 13.55 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.18 | 1.86 | 0.0 | 89725.29 | 6.9 | skipped_fast |
| CCUSDT | IDLE | 0.68 | 1.33 | 0.23 | -0.02 | 228015.91 | 10.87 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 1.53 | 1.25 | 0.04 | 75153.89 | 6.31 | skipped_fast |
| REDUSDT | IDLE | 0.77 | 1.34 | 1.3 | -0.01 | 57200.03 | 15.42 | skipped_fast |
| TELUSDT | IDLE | 1.67 | 3.29 | 2.46 | -0.05 | 136642.0 | 22.9 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 1.29 | 0.59 | -0.03 | 13917.41 | 4.94 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.1 | 0.85 | -0.01 | 306205.3 | 4.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.34 | 2.35 | 2.19 | 0.0 | 7833.02 | 4.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.81 | 1.51 | 0.72 | -0.01 | 35549.71 | 57.36 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.0 | 53679.43 | 15.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
