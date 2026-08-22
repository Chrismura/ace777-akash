# Hulk DIGEST — 2026-08-22T03:16:02Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 10.96 | 0.48 | 0.17 | 7645703.63 | 3.75 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 11.43 | 0.85 | 0.2 | 160944082.99 | 4.53 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 5.74 | 0.0 | 0.11 | 1004158.92 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 8.96 | 1.59 | 0.17 | 679684.76 | 7.65 | skipped_fast |
| BIOUSDT | IDLE | 3.06 | 7.36 | 3.19 | 0.06 | 197914.17 | 3.02 | skipped_fast |
| ZBCNUSDT | IDLE | 1.47 | 5.16 | 2.85 | 0.12 | 540694.14 | 16.94 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 4.28 | 0.33 | -0.01 | 448752.44 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.79 | 5.61 | 0.59 | 0.12 | 417915.22 | 12.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.42 | 0.1 | 59519.73 | 25.49 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.83 | 3.26 | -0.04 | 80045.99 | 22.42 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.8 | 0.2 | 158029.03 | 10.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 16.21 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.4 | 0.47 | 0.12 | 67612.76 | 9.85 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.27 | 0.09 | 174122.44 | 8.92 | skipped_fast |
| RWAUSDT | IDLE | 1.32 | 2.56 | 0.48 | 0.05 | 56244.77 | 24.2 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.31 | 0.07 | 173435.05 | 56.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
