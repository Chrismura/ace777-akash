# Hulk DIGEST — 2026-10-10T21:59:42Z

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
| ETHUSDT | IDLE | 0.32 | 0.58 | 0.39 | 0.01 | 108833679.27 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.28 | 0.51 | 0.27 | 0.01 | 13132186.8 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.12 | 0.22 | 0.14 | 0.01 | 167875594.64 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 3.91 | 33.98 | 4.21 | 0.29 | 231935.18 | 9.03 | skipped_fast |
| WUSDT | IDLE | 1.04 | 3.34 | 1.99 | 0.04 | 1256671.62 | 11.85 | skipped_fast |
| QNTUSDT | IDLE | 1.65 | 2.93 | 2.4 | -0.03 | 1242987.57 | 2.5 | skipped_fast |
| PYTHUSDT | IDLE | 0.9 | 1.65 | 0.97 | -0.02 | 779699.13 | 5.08 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 4.71 | 1.47 | -0.03 | 240193.62 | 2.56 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.54 | 1.47 | -0.02 | 293552.22 | 8.39 | skipped_fast |
| RWAINCUSDT | IDLE | 2.21 | 4.24 | 1.16 | -0.02 | 9523.81 | 29.51 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 3.08 | 0.71 | 0.05 | 88123.96 | 10.16 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 2.55 | 2.34 | 0.07 | 61279.95 | 11.73 | skipped_fast |
| ZBCNUSDT | IDLE | 0.59 | 1.17 | 0.06 | 0.03 | 207632.86 | 35.07 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 3.46 | 1.81 | -0.02 | 137076.88 | 27.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.13 | 2.02 | 1.56 | -0.03 | 33834.26 | 58.33 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 1.1 | 0.46 | 0.03 | 55083.75 | 14.58 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.13 | 0.62 | 0.02 | 313192.23 | 4.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.45 | 0.87 | 0.0 | 8504.7 | 21.35 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.79 | 0.63 | 0.0 | 53508.11 | 7.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.57 | 1.0 | 0.87 | -0.0 | 36524.99 | 59.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
