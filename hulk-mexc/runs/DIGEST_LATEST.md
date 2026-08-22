# Hulk DIGEST — 2026-08-22T03:23:09Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 10.96 | 0.43 | 0.18 | 7715834.29 | 1.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 14.16 | 0.37 | 0.23 | 163132505.39 | 8.17 | skipped_fast |
| HBARUSDT | IDLE | 2.27 | 6.16 | 0.01 | 0.11 | 1007769.47 | 6.04 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 8.96 | 1.46 | 0.17 | 680886.12 | 9.33 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.17 | 0.07 | 197362.37 | 5.98 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 4.28 | 0.03 | -0.01 | 450406.12 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 5.16 | 1.74 | 0.13 | 539059.57 | 22.01 | skipped_fast |
| WUSDT | IDLE | 1.77 | 5.61 | 0.07 | 0.13 | 416771.81 | 9.84 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 3.83 | 3.37 | -0.04 | 79996.15 | 22.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.37 | 0.1 | 59523.63 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.32 | 0.21 | 157946.79 | 18.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | 0.01 | 9365.24 | 32.45 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.4 | 0.42 | 0.12 | 67722.76 | 13.41 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 4.05 | 0.0 | 0.09 | 174177.49 | 2.97 | skipped_fast |
| RWAUSDT | IDLE | 1.3 | 2.56 | 0.24 | 0.05 | 56266.27 | 16.12 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.36 | 0.07 | 173235.57 | 51.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
