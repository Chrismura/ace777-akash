# Hulk DIGEST — 2026-08-19T16:15:42Z

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
| XRPUSDT | IDLE | 3.54 | 6.98 | 0.6 | 0.07 | 21513253.67 | 1.87 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.66 | 19.06 | 1.96 | 0.17 | 114058.14 | 6.88 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 19.8 | 9.62 | 0.07 | 144582.84 | 32.54 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 12.24 | 5.16 | 0.05 | 19664.94 | 39.47 | skipped_fast |
| QAITUSDT | IDLE | 4.21 | 11.42 | 3.94 | 0.02 | 11020.0 | 62.52 | skipped_fast |
| PYTHUSDT | IDLE | 3.13 | 6.05 | 1.41 | 0.04 | 210928.98 | 2.5 | skipped_fast |
| CHIPUSDT | IDLE | 2.86 | 9.02 | 4.4 | 0.03 | 170656.34 | 3.62 | skipped_fast |
| ZBCNUSDT | IDLE | 3.09 | 7.07 | 1.41 | 0.07 | 197005.86 | 21.48 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.99 | 8.27 | 0.75 | 0.05 | 65012.86 | 62.85 | skipped_fast |
| KITEUSDT | IDLE | 3.42 | 6.67 | 1.08 | 0.04 | 56488.38 | 10.45 | skipped_fast |
| WUSDT | IDLE | 2.88 | 5.59 | 1.16 | 0.04 | 147660.3 | 14.19 | skipped_fast |
| CCUSDT | IDLE | 2.11 | 4.02 | 1.37 | 0.01 | 248247.39 | 11.92 | skipped_fast |
| REDUSDT | IDLE | 2.39 | 6.88 | 0.42 | 0.01 | 113352.15 | 24.76 | skipped_fast |
| FLUIDUSDT | IDLE | 3.44 | 7.79 | 2.02 | 0.03 | 1571.31 | 22.57 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 4.12 | 1.67 | -0.05 | 24332.9 | 52.06 | skipped_fast |
| HBARUSDT | IDLE | 1.76 | 3.44 | 0.53 | 0.05 | 197528.85 | 2.88 | skipped_fast |
| QNTUSDT | IDLE | 1.9 | 3.71 | 0.56 | 0.03 | 37979.17 | 13.74 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.58 | 0.43 | -0.0 | 53694.77 | 17.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
