# Hulk DIGEST — 2026-08-18T10:09:18Z

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
| XRPUSDT | IDLE | 0.46 | 0.84 | 0.52 | -0.0 | 11872670.71 | 1.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 11.21 | 7.92 | -0.02 | 82388.99 | 26.11 | skipped_fast |
| RWAINCUSDT | IDLE | 4.34 | 8.85 | 4.96 | -0.02 | 2589.12 | 29.46 | skipped_fast |
| REDUSDT | IDLE | 2.12 | 18.49 | 10.72 | 0.23 | 84110.68 | 13.75 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.05 | 8.07 | 1.73 | -0.03 | 280284.36 | 13.82 | skipped_fast |
| KITEUSDT | IDLE | 2.86 | 5.03 | 4.55 | -0.02 | 61508.71 | 14.33 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.53 | 1.97 | -0.04 | 291814.01 | 6.58 | skipped_fast |
| QAITUSDT | IDLE | 1.64 | 10.79 | 8.14 | -0.05 | 11389.72 | 60.02 | skipped_fast |
| PYTHUSDT | IDLE | 0.8 | 1.51 | 0.58 | -0.03 | 179893.05 | 2.63 | skipped_fast |
| ZBCNUSDT | IDLE | 0.68 | 1.32 | 0.33 | -0.01 | 211338.53 | 19.11 | skipped_fast |
| WUSDT | IDLE | 0.67 | 1.19 | 0.96 | -0.03 | 153320.18 | 9.86 | skipped_fast |
| BIOUSDT | IDLE | 0.71 | 1.29 | 0.86 | -0.02 | 75706.83 | 4.13 | skipped_fast |
| RIZEUSDT | IDLE | 0.28 | 2.04 | 0.0 | -0.18 | 56133.64 | 27.27 | skipped_fast |
| HBARUSDT | IDLE | 0.41 | 0.78 | 0.29 | -0.0 | 123669.09 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 0.69 | 1.44 | 0.43 | -0.03 | 132897.65 | 42.77 | skipped_fast |
| QNTUSDT | IDLE | 0.47 | 0.83 | 0.75 | -0.0 | 36607.23 | 8.96 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.78 | 0.69 | -0.0 | 50144.12 | 17.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.22 | 0.39 | 0.38 | -0.04 | 217.91 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
