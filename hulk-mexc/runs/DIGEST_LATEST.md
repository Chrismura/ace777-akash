# Hulk DIGEST — 2026-08-22T16:07:58Z

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
| PYTHUSDT | IDLE | 1.51 | 7.24 | 1.71 | 0.04 | 51461447.28 | 1.98 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 7.64 | 5.28 | 0.04 | 215551801.81 | 3.45 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.19 | -0.01 | 1141780.96 | 3.91 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.06 | 0.1 | 763788.48 | 5.11 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.0 | -0.09 | 627828.57 | 6.71 | skipped_fast |
| WUSDT | IDLE | 0.65 | 2.58 | 1.71 | -0.02 | 547976.2 | 6.41 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 2.07 | -0.05 | 319031.41 | 21.11 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.66 | -0.07 | 218600.18 | 3.31 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.55 | 0.03 | 85459.76 | 10.68 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 2.41 | 2.01 | -0.02 | 74900.29 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.95 | -0.14 | 135142.74 | 11.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.3 | 3.21 | 0.0 | 0.03 | 56523.53 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.17 | -0.02 | 183601.79 | 6.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 2.37 | 1.42 | -0.0 | 138520.24 | 48.01 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.06 | 0.4 | 0.02 | 56341.06 | 32.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.04 | 4625.53 | 20.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
