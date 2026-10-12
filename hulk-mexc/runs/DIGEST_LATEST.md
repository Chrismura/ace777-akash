# Hulk DIGEST — 2026-10-12T09:26:35Z

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
| WUSDT | IDLE | 0.67 | 13.08 | 2.57 | 0.74 | 13311003.09 | 9.95 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.78 | 8.1 | 0.6 | 0.09 | 1377010.85 | 3.55 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.43 | 1.05 | 0.02 | 235597330.12 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.25 | 1.15 | 0.01 | 23146004.54 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.08 | 1.07 | 0.01 | 228459141.78 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.17 | 3.95 | 2.65 | -0.01 | 838325.7 | 3.38 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 7.86 | 5.93 | -0.01 | 220598.91 | 14.2 | skipped_fast |
| REDUSDT | IDLE | 2.91 | 7.41 | 0.68 | 0.08 | 75861.77 | 11.15 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 14.29 | 5.37 | 0.14 | 46446.56 | 38.5 | skipped_fast |
| EDELUSDT | IDLE | 1.69 | 2.98 | 2.64 | -0.04 | 253070.2 | 10.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 2.67 | 2.08 | 0.05 | 280133.56 | 8.38 | skipped_fast |
| CCUSDT | IDLE | 0.9 | 1.61 | 1.24 | 0.03 | 395843.01 | 9.56 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 1.83 | 1.8 | 0.02 | 461683.41 | 2.14 | skipped_fast |
| BIOUSDT | IDLE | 1.32 | 2.31 | 2.26 | -0.01 | 100679.76 | 6.79 | skipped_fast |
| TELUSDT | IDLE | 2.12 | 3.97 | 1.74 | 0.0 | 185898.31 | 28.61 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.14 | 0.86 | 0.02 | 63428.94 | 10.1 | skipped_fast |
| RWAINCUSDT | IDLE | 0.75 | 2.14 | 1.4 | -0.01 | 20364.59 | 20.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.78 | 1.37 | 1.25 | 0.01 | 37385.18 | 5.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 3.47 | 0.12 | 0.05 | 63363.97 | 21.23 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.54 | 0.23 | 0.03 | 52630.93 | 15.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
