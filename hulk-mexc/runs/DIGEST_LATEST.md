# Hulk DIGEST — 2026-09-23T05:16:38Z

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
| XRPUSDT | IDLE | 2.44 | 5.64 | 2.15 | 0.07 | 114414057.19 | 1.85 | skipped_fast |
| PYTHUSDT | IDLE | 1.0 | 4.62 | 2.57 | 0.05 | 1772440.31 | 3.0 | skipped_fast |
| ETHUSDT | IDLE | 0.81 | 1.52 | 0.64 | 0.02 | 406254350.58 | 0.43 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.33 | 0.39 | 0.02 | 878198375.59 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.84 | 1.98 | 0.08 | 1792974.28 | 1.01 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.86 | 9.79 | 1.61 | 0.05 | 220883.34 | 14.35 | skipped_fast |
| WUSDT | IDLE | 1.94 | 3.68 | 1.36 | 0.05 | 318491.99 | 7.32 | skipped_fast |
| CCUSDT | IDLE | 1.4 | 2.72 | 0.58 | -0.02 | 411667.4 | 9.5 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 6.66 | 2.23 | -0.06 | 270715.08 | 13.22 | skipped_fast |
| BIOUSDT | IDLE | 1.75 | 3.38 | 0.85 | 0.05 | 111261.19 | 13.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 2.65 | 0.85 | 0.0 | 199398.04 | 10.68 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 4.42 | 2.62 | 0.14 | 130051.91 | 7.99 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 18.71 | 4.02 | 0.47 | 57462.44 | 93.24 | skipped_fast |
| REDUSDT | IDLE | 1.31 | 2.57 | 0.38 | 0.03 | 59165.01 | 8.1 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.57 | 1.18 | 0.12 | 213605.58 | 5.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.57 | 1.22 | 0.03 | 21135.78 | 10.79 | skipped_fast |
| TELUSDT | IDLE | 0.88 | 3.93 | 0.69 | 0.15 | 109434.4 | 32.19 | skipped_fast |
| FLUIDUSDT | IDLE | 1.23 | 2.42 | 0.33 | 0.03 | 4320.56 | 21.56 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.8 | 0.36 | 0.01 | 53110.91 | 21.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.72 | 0.01 | 0.01 | 39827.53 | 6.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
