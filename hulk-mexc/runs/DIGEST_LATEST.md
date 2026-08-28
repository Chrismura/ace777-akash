# Hulk DIGEST — 2026-08-28T17:08:29Z

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
| XRPUSDT | IDLE | 2.61 | 4.69 | 3.48 | -0.05 | 53338906.37 | 1.44 | skipped_fast |
| CHIPUSDT | IDLE | 2.33 | 14.34 | 9.18 | 0.04 | 955344.02 | 6.97 | skipped_fast |
| PYTHUSDT | IDLE | 2.34 | 5.81 | 3.47 | -0.06 | 954968.21 | 4.27 | skipped_fast |
| QAITUSDT | IDLE | 2.44 | 32.58 | 21.02 | -0.19 | 70698.45 | 67.41 | skipped_fast |
| CCUSDT | IDLE | 2.57 | 4.64 | 3.37 | -0.06 | 382636.69 | 7.29 | skipped_fast |
| WUSDT | IDLE | 2.94 | 6.36 | 4.4 | -0.07 | 218935.87 | 6.58 | skipped_fast |
| ZBCNUSDT | IDLE | 2.97 | 5.24 | 4.68 | -0.08 | 209193.6 | 19.0 | skipped_fast |
| HBARUSDT | IDLE | 3.11 | 5.77 | 3.01 | -0.04 | 435503.43 | 1.32 | skipped_fast |
| BIOUSDT | IDLE | 2.67 | 5.99 | 3.5 | -0.05 | 95691.84 | 3.59 | skipped_fast |
| REDUSDT | IDLE | 2.61 | 6.25 | 3.2 | -0.04 | 68462.36 | 22.94 | skipped_fast |
| KITEUSDT | IDLE | 2.27 | 4.27 | 1.76 | -0.03 | 80721.5 | 8.78 | skipped_fast |
| RWAUSDT | IDLE | 3.31 | 5.99 | 4.22 | 0.0 | 55378.77 | 16.63 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 4.25 | 4.07 | -0.11 | 65374.62 | 17.68 | skipped_fast |
| QNTUSDT | IDLE | 2.64 | 4.72 | 3.69 | -0.04 | 49779.89 | 6.54 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 4.58 | 3.59 | -0.06 | 76484.07 | 28.06 | skipped_fast |
| FLUIDUSDT | IDLE | 2.4 | 4.19 | 4.02 | -0.07 | 4792.01 | 22.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 3.82 | 0.69 | 0.0 | 18818.36 | 64.27 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 4.07 | 3.42 | -0.06 | 125995.76 | 39.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
