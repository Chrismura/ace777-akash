# Hulk DIGEST — 2026-10-10T19:42:28Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.71 | 8.42 | 6.99 | 0.03 | 1238843.87 | 7.38 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.88 | 0.07 | 0.02 | 96258923.9 | 0.2 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.7 | 0.41 | 0.02 | 14066965.79 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.46 | 0.08 | 0.01 | 174001895.58 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.87 | 5.17 | 3.83 | -0.0 | 1174041.77 | 0.41 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.44 | 29.34 | 1.98 | 0.31 | 177800.87 | 16.8 | skipped_fast |
| PYTHUSDT | IDLE | 1.28 | 2.34 | 1.43 | -0.01 | 798045.36 | 3.83 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.64 | 1.68 | -0.03 | 323005.3 | 5.88 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 3.54 | 0.69 | -0.04 | 225303.74 | 35.93 | skipped_fast |
| BIOUSDT | IDLE | 1.57 | 2.95 | 1.32 | 0.05 | 88178.92 | 6.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.04 | 1.96 | 0.74 | 0.01 | 199942.74 | 15.25 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 4.24 | 2.18 | -0.03 | 9650.09 | 78.9 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 3.16 | 2.76 | 0.08 | 71477.82 | 19.47 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.69 | 1.22 | 0.03 | 328416.88 | 4.32 | skipped_fast |
| TELUSDT | IDLE | 2.02 | 3.63 | 2.68 | -0.03 | 133092.95 | 45.02 | skipped_fast |
| REDUSDT | IDLE | 0.61 | 1.21 | 0.06 | 0.04 | 54553.12 | 15.17 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 1.1 | 0.69 | -0.02 | 43370.94 | 31.87 | skipped_fast |
| FLUIDUSDT | IDLE | 1.61 | 3.1 | 0.83 | 0.02 | 14854.75 | 21.42 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.79 | 0.47 | 0.01 | 54156.38 | 7.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.12 | 0.0 | 37918.88 | 13.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
