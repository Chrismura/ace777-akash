# Hulk DIGEST — 2026-08-22T16:24:30Z

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
| PYTHUSDT | IDLE | 1.47 | 7.24 | 0.35 | 0.06 | 51442290.77 | 3.91 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.64 | 4.31 | 0.05 | 215590340.84 | 3.42 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.18 | -0.0 | 1138556.59 | 6.47 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.4 | 0.1 | 767398.52 | 11.09 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.7 | -0.1 | 627823.65 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.98 | -0.01 | 544389.98 | 10.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 1.91 | -0.04 | 316050.55 | 23.64 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.29 | -0.07 | 219669.73 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.48 | 0.03 | 85462.05 | 8.89 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.52 | 2.24 | -0.03 | 74831.15 | 22.86 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.95 | -0.12 | 133501.6 | 20.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.2 | 0.03 | 56568.86 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.07 | -0.01 | 184071.71 | 6.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 8652.8 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.16 | 0.01 | 137700.1 | 42.6 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.32 | 0.02 | 56326.5 | 8.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 22.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
