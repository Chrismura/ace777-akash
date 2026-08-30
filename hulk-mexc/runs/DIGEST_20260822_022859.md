# Hulk DIGEST — 2026-08-22T02:28:59Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 9.64 | 0.02 | 0.16 | 7022297.87 | 1.91 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 10.52 | 0.07 | 0.17 | 154965141.06 | 2.64 | skipped_fast |
| HBARUSDT | IDLE | 2.36 | 5.35 | 0.0 | 0.09 | 966863.26 | 2.47 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 9.63 | 1.9 | 0.09 | 545834.01 | 30.21 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 6.33 | 0.03 | 0.15 | 652470.42 | 9.57 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 5.07 | 0.42 | -0.01 | 470128.0 | 3.01 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.13 | 8.18 | 0.79 | 0.1 | 193214.4 | 5.91 | skipped_fast |
| WUSDT | IDLE | 1.86 | 5.2 | 0.0 | 0.1 | 401936.43 | 17.01 | skipped_fast |
| EDELUSDT | IDLE | 2.48 | 5.02 | 3.04 | -0.03 | 79648.04 | 22.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.89 | 0.11 | 61353.83 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.26 | 0.17 | 157874.68 | 20.27 | skipped_fast |
| QNTUSDT | IDLE | 2.25 | 5.06 | 0.0 | 0.08 | 171093.29 | 1.49 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 4.09 | 0.89 | 0.11 | 61906.56 | 21.53 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.28 | 0.04 | 178548.78 | 20.7 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9345.09 | 54.17 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.75 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 2.08 | 0.0 | 0.04 | 54965.66 | 24.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
