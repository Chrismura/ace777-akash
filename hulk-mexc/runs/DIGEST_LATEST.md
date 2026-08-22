# Hulk DIGEST — 2026-08-22T03:51:34Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.52 | 0.17 | 8698071.86 | 3.76 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.36 | 0.2 | 165792103.22 | 3.17 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 6.93 | 0.57 | 0.11 | 1034516.97 | 1.2 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 10.39 | 0.55 | 0.2 | 698572.73 | 13.25 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 5.36 | 1.35 | -0.03 | 459647.07 | 5.96 | skipped_fast |
| BIOUSDT | IDLE | 2.97 | 7.36 | 1.7 | 0.07 | 199253.88 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.82 | 5.98 | 0.0 | 0.13 | 424533.08 | 10.78 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 5.37 | 1.32 | 0.14 | 537415.15 | 33.27 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 3.95 | 3.69 | -0.04 | 80754.48 | 22.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.13 | 0.11 | 59494.3 | 32.22 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 3.05 | 0.22 | 157475.4 | 11.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 43.55 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 4.87 | 0.04 | 0.13 | 67801.54 | 24.74 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.44 | 0.09 | 175143.5 | 2.96 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.57 | 3.14 | 0.0 | 0.06 | 56244.83 | 16.01 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.56 | 0.07 | 173743.97 | 30.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
