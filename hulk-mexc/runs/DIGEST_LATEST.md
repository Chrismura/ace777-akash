# Hulk DIGEST — 2026-08-22T03:49:25Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.52 | 0.17 | 8572512.57 | 3.76 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.52 | 0.2 | 165662848.74 | 2.54 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 6.93 | 0.55 | 0.11 | 1034274.57 | 9.63 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 10.39 | 0.08 | 0.2 | 697353.53 | 7.44 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 5.36 | 1.56 | -0.03 | 455675.07 | 2.99 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.93 | 0.08 | 199190.97 | 5.97 | skipped_fast |
| WUSDT | IDLE | 1.8 | 5.83 | 0.06 | 0.12 | 424138.85 | 13.75 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 5.37 | 0.69 | 0.14 | 537436.64 | 53.34 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.02 | 0.11 | 59490.29 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.2 | 0.22 | 157908.96 | 10.19 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 3.95 | 3.69 | -0.03 | 80779.53 | 78.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 43.55 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 4.86 | 0.12 | 0.12 | 67683.67 | 13.31 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.41 | 0.09 | 175127.28 | 7.41 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.53 | 3.05 | 0.08 | 0.06 | 56285.89 | 8.01 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.61 | 0.07 | 173779.6 | 30.67 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
