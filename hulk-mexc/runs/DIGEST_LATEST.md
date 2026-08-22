# Hulk DIGEST — 2026-08-22T03:58:28Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.46 | 0.17 | 9160390.73 | 20.6 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.9 | 0.19 | 166196455.81 | 1.28 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 6.93 | 0.6 | 0.1 | 1033522.23 | 1.21 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.34 | 0.2 | 702572.39 | 6.62 | skipped_fast |
| CHIPUSDT | IDLE | 2.47 | 5.36 | 1.18 | -0.02 | 458779.14 | 2.98 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.26 | 0.07 | 199185.79 | 6.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 5.37 | 1.38 | 0.14 | 537830.58 | 21.4 | skipped_fast |
| WUSDT | IDLE | 1.87 | 6.27 | 0.18 | 0.13 | 425397.96 | 10.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.83 | 7.71 | 4.57 | 0.11 | 59293.3 | 27.3 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80625.51 | 33.69 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.77 | 0.23 | 157628.65 | 10.16 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 5.55 | 0.0 | 0.13 | 67523.09 | 22.07 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 38.1 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 4.68 | 0.34 | 0.1 | 178509.16 | 16.3 | skipped_fast |
| RWAUSDT | IDLE | 1.62 | 3.22 | 0.08 | 0.06 | 56346.06 | 16.01 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.41 | 0.07 | 174164.98 | 35.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 18.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
