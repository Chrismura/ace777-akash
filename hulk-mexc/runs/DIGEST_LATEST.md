# Hulk DIGEST — 2026-09-23T12:18:31Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 2.48 | 4.4 | 4.08 | 0.02 | 122436050.46 | 2.56 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 4.33 | 3.05 | 0.06 | 1940625.19 | 12.04 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 5.48 | 5.05 | 0.01 | 1674617.86 | 5.27 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.34 | 1.28 | -0.01 | 417148305.9 | 0.33 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.29 | 1.27 | -0.01 | 849167814.77 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.76 | 3.15 | 2.45 | 0.03 | 399749.28 | 5.77 | skipped_fast |
| CCUSDT | IDLE | 1.57 | 2.88 | 1.68 | -0.05 | 435826.71 | 9.74 | skipped_fast |
| ZBCNUSDT | IDLE | 2.11 | 4.9 | 3.91 | 0.03 | 232356.47 | 24.53 | skipped_fast |
| CHIPUSDT | IDLE | 2.0 | 3.74 | 1.76 | 0.0 | 191840.23 | 19.68 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 3.47 | 1.43 | 0.03 | 137387.03 | 16.12 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 2.73 | 1.64 | 0.06 | 118334.07 | 13.33 | skipped_fast |
| EDELUSDT | IDLE | 0.7 | 3.23 | 2.61 | -0.09 | 230789.51 | 36.77 | skipped_fast |
| REDUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.05 | 59855.51 | 30.95 | skipped_fast |
| QNTUSDT | IDLE | 1.72 | 3.04 | 2.62 | 0.04 | 212253.66 | 5.42 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 6.96 | 5.56 | 0.09 | 152680.71 | 67.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 2.23 | 1.22 | 0.02 | 20078.82 | 5.38 | skipped_fast |
| RIZEUSDT | IDLE | 0.29 | 6.15 | 1.72 | 0.5 | 64315.02 | 89.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.0 | 1.74 | 1.71 | 0.01 | 3866.64 | 21.26 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.58 | 0.01 | 54657.07 | 14.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.73 | 0.36 | 0.0 | 40397.68 | 45.0 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
