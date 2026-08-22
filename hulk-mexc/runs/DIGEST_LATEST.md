# Hulk DIGEST — 2026-08-22T03:50:18Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.7 | 0.17 | 8633238.47 | 13.18 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.4 | 0.2 | 165719138.37 | 2.54 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 6.93 | 0.55 | 0.11 | 1034415.48 | 1.2 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.35 | 0.2 | 699652.49 | 7.45 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 5.36 | 1.53 | -0.03 | 455506.67 | 2.99 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.91 | 0.08 | 199142.18 | 2.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 5.37 | 0.89 | 0.14 | 537539.38 | 21.34 | skipped_fast |
| WUSDT | IDLE | 1.81 | 5.86 | 0.06 | 0.13 | 424232.77 | 8.83 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.26 | 0.11 | 59493.18 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 3.04 | 0.22 | 157490.34 | 11.75 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 3.95 | 3.04 | -0.04 | 80754.46 | 67.42 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 4.86 | 0.06 | 0.13 | 67698.81 | 13.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 49.01 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.52 | 0.09 | 175124.53 | 7.41 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.06 | 56265.68 | 8.0 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.51 | 0.07 | 173759.85 | 30.67 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
