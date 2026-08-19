# Hulk DIGEST — 2026-08-19T03:45:12Z

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
| XRPUSDT | IDLE | 0.35 | 0.66 | 0.27 | 0.01 | 10292447.52 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 5.6 | 3.6 | -0.08 | 184737.63 | 3.85 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 2.99 | 0.28 | 0.04 | 177045.76 | 5.1 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 2.0 | 1.87 | -0.01 | 221618.86 | 8.89 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 5.83 | 4.81 | 0.01 | 166789.96 | 14.48 | skipped_fast |
| ZBCNUSDT | IDLE | 0.63 | 1.1 | 1.09 | 0.0 | 156148.44 | 7.06 | skipped_fast |
| EDELUSDT | IDLE | 0.79 | 2.29 | 1.72 | -0.02 | 73721.07 | 13.41 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.68 | 0.16 | 0.02 | 63187.31 | 8.06 | skipped_fast |
| WUSDT | IDLE | 0.6 | 1.12 | 0.49 | -0.01 | 126523.44 | 16.1 | skipped_fast |
| KITEUSDT | IDLE | 0.74 | 1.29 | 1.25 | -0.02 | 65423.65 | 14.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.79 | 1.74 | 0.06 | -0.0 | 10844.96 | 11.82 | skipped_fast |
| QAITUSDT | IDLE | 0.5 | 3.92 | 3.58 | -0.18 | 12361.78 | 67.05 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.56 | 0.1 | 0.04 | 111513.88 | 1.48 | skipped_fast |
| RIZEUSDT | IDLE | 1.7 | 4.37 | 3.2 | -0.06 | 28020.54 | 257.67 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 1.88 | 0.82 | 0.05 | 84325.23 | 41.32 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.38 | 0.41 | 0.0 | 38882.28 | 3.56 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.44 | 0.26 | -0.01 | 51649.68 | 17.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.45 | 0.79 | 0.78 | -0.01 | 185.56 | 21.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
