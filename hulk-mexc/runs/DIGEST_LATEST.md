# Hulk DIGEST — 2026-09-02T11:27:27Z

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
| XRPUSDT | IDLE | 1.83 | 3.25 | 2.73 | -0.05 | 40289645.82 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 1.7 | 3.04 | 2.42 | -0.03 | 405461207.9 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.1 | 1.94 | 1.77 | -0.02 | 526611688.87 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 8.6 | 5.57 | 0.13 | 977585.69 | 2.27 | skipped_fast |
| PYTHUSDT | IDLE | 1.69 | 5.35 | 4.35 | 0.06 | 864024.64 | 1.86 | skipped_fast |
| WUSDT | IDLE | 2.38 | 4.28 | 3.22 | -0.01 | 408377.99 | 12.64 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 14.74 | 7.62 | 0.05 | 171330.28 | 49.96 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 2.6 | 2.5 | -0.07 | 356195.88 | 9.87 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.62 | 8.17 | 0.95 | 0.09 | 10823.17 | 26.62 | skipped_fast |
| QNTUSDT | IDLE | 3.19 | 6.19 | 4.71 | 0.04 | 71355.45 | 3.13 | skipped_fast |
| RIZEUSDT | IDLE | 2.1 | 7.95 | 6.49 | -0.13 | 40542.05 | 82.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 2.04 | 1.56 | -0.03 | 234902.63 | 17.65 | skipped_fast |
| BIOUSDT | IDLE | 1.56 | 2.8 | 2.18 | -0.04 | 76272.11 | 3.98 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 4.2 | 3.12 | 0.12 | 82846.32 | 9.76 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.83 | 0.79 | 0.02 | 152568.83 | 14.36 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 1.99 | 1.71 | -0.02 | 240764.56 | 1.37 | skipped_fast |
| TELUSDT | IDLE | 1.68 | 3.02 | 2.22 | -0.03 | 85617.06 | 59.88 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.52 | 1.49 | -0.04 | 328.21 | 22.17 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.77 | 0.54 | 0.0 | 50498.64 | 7.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.75 | 0.74 | -0.02 | 36285.13 | 37.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
