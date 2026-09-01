# Hulk DIGEST — 2026-09-01T13:24:24Z

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
| XRPUSDT | IDLE | 1.16 | 2.1 | 1.52 | 0.0 | 30379524.79 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 1.93 | 1.36 | -0.0 | 300621080.48 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.45 | 1.12 | -0.0 | 550090395.12 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.45 | 5.52 | 2.21 | 0.07 | 590770.61 | 4.0 | skipped_fast |
| CHIPUSDT | IDLE | 3.05 | 6.55 | 0.19 | 0.03 | 385662.43 | 4.86 | skipped_fast |
| CCUSDT | IDLE | 2.64 | 4.64 | 4.25 | -0.02 | 403929.25 | 7.72 | skipped_fast |
| ZBCNUSDT | IDLE | 2.16 | 3.87 | 2.96 | 0.02 | 204404.23 | 10.88 | skipped_fast |
| WUSDT | IDLE | 1.66 | 3.1 | 1.5 | 0.04 | 237400.16 | 9.47 | skipped_fast |
| REDUSDT | IDLE | 2.14 | 3.89 | 2.63 | 0.02 | 63667.29 | 13.7 | skipped_fast |
| KITEUSDT | IDLE | 2.08 | 3.97 | 1.21 | -0.0 | 61072.63 | 10.84 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 5.64 | 4.67 | -0.06 | 177569.13 | 26.3 | skipped_fast |
| BIOUSDT | IDLE | 1.55 | 2.84 | 1.78 | -0.01 | 64630.39 | 3.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.49 | 4.79 | 2.54 | -0.09 | 38079.4 | 72.93 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 2.41 | 0.75 | 0.01 | 246617.99 | 1.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.97 | 1.95 | 0.0 | -0.01 | 4940.4 | 11.61 | skipped_fast |
| QNTUSDT | IDLE | 1.96 | 3.83 | 0.59 | 0.02 | 38822.5 | 1.59 | skipped_fast |
| RWAUSDT | IDLE | 1.48 | 3.5 | 1.88 | 0.02 | 63395.17 | 7.67 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 1.76 | 1.27 | 0.0 | 85551.98 | 40.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.56 | 0.42 | -0.0 | 32176.02 | 4.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.0 | 1002.5 | 21.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
