# Hulk DIGEST — 2026-08-22T15:56:26Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.38 | 0.05 | 51485607.75 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 5.98 | 0.02 | 216039353.9 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 5.65 | 2.43 | 0.09 | 759709.33 | 5.98 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.53 | -0.02 | 1152917.02 | 5.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 2.03 | -0.1 | 604141.65 | 3.39 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.82 | -0.02 | 553097.84 | 14.98 | skipped_fast |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.72 | 0.03 | 85522.95 | 8.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 1.96 | -0.05 | 320419.87 | 30.84 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.95 | -0.06 | 218933.74 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.03 | 75112.93 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.48 | -0.15 | 134302.6 | 11.91 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.13 | 0.03 | 56487.34 | 45.5 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 2.69 | 2.62 | -0.03 | 184546.76 | 4.75 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.63 | -0.0 | 139050.74 | 42.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | -0.01 | 9555.35 | 86.02 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 56521.67 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
