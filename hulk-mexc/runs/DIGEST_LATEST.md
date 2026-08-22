# Hulk DIGEST — 2026-08-22T03:11:33Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 10.96 | 0.69 | 0.18 | 7589089.09 | 11.26 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 11.43 | 0.77 | 0.2 | 160634279.47 | 5.17 | skipped_fast |
| HBARUSDT | IDLE | 2.17 | 5.29 | 0.57 | 0.1 | 996948.17 | 3.67 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.54 | 0.19 | 671384.47 | 5.88 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.06 | 195715.86 | 3.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 4.28 | 0.36 | -0.0 | 449079.4 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.79 | 5.61 | 0.51 | 0.12 | 417841.23 | 7.91 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 5.16 | 2.66 | 0.12 | 541239.74 | 48.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.46 | 0.1 | 59517.04 | 28.93 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.83 | 3.15 | -0.03 | 80045.98 | 22.4 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.06 | 0.2 | 157974.27 | 12.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 21.62 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 4.4 | 0.24 | 0.13 | 67728.07 | 11.61 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3813.17 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.27 | 0.08 | 173632.91 | 1.49 | skipped_fast |
| RWAUSDT | IDLE | 1.18 | 2.31 | 0.32 | 0.05 | 56154.24 | 8.09 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.36 | 0.07 | 173195.22 | 61.51 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
