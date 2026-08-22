# Hulk DIGEST — 2026-08-22T05:06:46Z

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
| PYTHUSDT | IDLE | 3.24 | 15.45 | 3.76 | 0.16 | 14007194.48 | 7.44 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 19.3 | 0.9 | 0.28 | 183615557.79 | 2.97 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.59 | 10.33 | 0.79 | 0.15 | 1127578.09 | 1.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.11 | 0.2 | 747646.86 | 7.37 | skipped_fast |
| CHIPUSDT | IDLE | 2.81 | 5.36 | 1.68 | 0.01 | 446693.0 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.22 | 0.84 | 0.15 | 450516.51 | 10.57 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.03 | 9.0 | 0.23 | 0.1 | 203391.22 | 2.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.61 | 4.29 | 2.77 | 0.09 | 538656.09 | 69.41 | skipped_fast |
| QNTUSDT | IDLE | 2.73 | 9.16 | 4.05 | 0.1 | 187008.14 | 5.88 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 7.96 | 6.23 | 0.19 | 158273.49 | 12.96 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 6.62 | 0.38 | 0.15 | 68329.73 | 14.0 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.28 | 1.31 | -0.02 | 80934.21 | 44.3 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.39 | 0.1 | 184031.93 | 24.81 | skipped_fast |
| RIZEUSDT | IDLE | 1.11 | 4.41 | 4.22 | 0.09 | 58679.0 | 44.52 | skipped_fast |
| RWAUSDT | IDLE | 1.7 | 3.38 | 0.08 | 0.07 | 56831.05 | 7.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 21.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
