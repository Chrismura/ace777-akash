# Hulk DIGEST — 2026-09-07T03:34:08Z

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
| XRPUSDT | IDLE | 1.19 | 2.12 | 1.68 | -0.01 | 28415917.58 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 1.01 | 1.83 | 1.25 | 0.0 | 283905019.45 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.12 | 1.0 | -0.0 | 377912033.91 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.61 | 4.69 | 3.49 | 0.0 | 604817.4 | 1.8 | skipped_fast |
| CHIPUSDT | IDLE | 2.64 | 5.22 | 4.96 | -0.03 | 411030.71 | 15.85 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 3.03 | 2.33 | -0.01 | 391433.2 | 3.65 | skipped_fast |
| WUSDT | IDLE | 1.52 | 2.87 | 1.12 | 0.04 | 407250.66 | 9.54 | skipped_fast |
| EDELUSDT | IDLE | 2.8 | 5.6 | 0.0 | 0.02 | 56566.05 | 18.3 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.53 | 10.32 | 1.94 | 0.14 | 6120.98 | 42.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 3.35 | 1.91 | 0.0 | 135552.8 | 10.22 | skipped_fast |
| REDUSDT | IDLE | 1.89 | 3.35 | 2.83 | -0.0 | 67394.02 | 10.27 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 5.99 | 5.32 | 0.01 | 96320.1 | 57.97 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 2.8 | 2.48 | -0.03 | 79885.76 | 7.36 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.01 | 1.86 | -0.01 | 448634.94 | 1.24 | skipped_fast |
| RIZEUSDT | IDLE | 1.2 | 10.09 | 6.02 | -0.19 | 70483.53 | 65.02 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 1.51 | 0.47 | -0.02 | 57663.61 | 10.23 | skipped_fast |
| QNTUSDT | IDLE | 0.68 | 1.22 | 1.0 | 0.01 | 38295.28 | 3.01 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.7 | 1.27 | 0.0 | 1152.26 | 19.61 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.64 | -0.02 | 53176.4 | 7.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.09 | 0.17 | 0.08 | 0.0 | 40190.65 | 6.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
