# Hulk DIGEST — 2026-08-22T02:55:56Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.64 | 11.02 | 1.09 | 0.16 | 7347788.63 | 1.91 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.53 | 13.33 | 0.28 | 0.2 | 158986795.56 | 3.87 | skipped_fast |
| HBARUSDT | IDLE | 2.57 | 6.7 | 0.1 | 0.1 | 990058.34 | 1.22 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 9.53 | 0.07 | 0.18 | 663077.2 | 8.43 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 9.63 | 2.55 | 0.1 | 541339.8 | 49.75 | skipped_fast |
| CHIPUSDT | IDLE | 2.58 | 5.95 | 0.0 | -0.01 | 451132.19 | 5.95 | skipped_fast |
| BIOUSDT | IDLE | 3.21 | 8.18 | 2.17 | 0.08 | 194363.76 | 3.0 | skipped_fast |
| WUSDT | IDLE | 2.04 | 6.23 | 0.05 | 0.11 | 415577.72 | 12.88 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 5.02 | 2.5 | -0.03 | 79929.14 | 33.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.44 | 0.1 | 61384.36 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.76 | 0.2 | 157940.04 | 11.15 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9385.21 | 5.43 | skipped_fast |
| QNTUSDT | IDLE | 2.33 | 5.48 | 0.15 | 0.09 | 172646.92 | 7.44 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.19 | 0.12 | 62425.03 | 8.96 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 5.11 | 0.92 | 0.06 | 173952.01 | 61.98 | skipped_fast |
| RWAUSDT | IDLE | 1.68 | 3.33 | 0.16 | 0.05 | 56227.16 | 24.24 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
