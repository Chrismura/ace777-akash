# Hulk DIGEST — 2026-09-12T23:37:54Z

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
| ETHUSDT | IDLE | 0.27 | 0.52 | 0.17 | 0.0 | 205984941.98 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.22 | 0.43 | 0.11 | 0.01 | 14773826.29 | 2.93 | skipped_fast |
| BTCUSDT | IDLE | 0.16 | 0.31 | 0.06 | 0.0 | 322683038.54 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.34 | 22.73 | 16.37 | 0.42 | 92171.99 | 60.38 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 2.59 | 1.95 | 0.08 | 409999.93 | 1.83 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.27 | 3.13 | 0.03 | 174409.1 | 7.07 | skipped_fast |
| EDELUSDT | IDLE | 1.68 | 3.83 | 0.57 | 0.06 | 167309.8 | 8.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.11 | 2.44 | -0.01 | 218628.93 | 19.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.13 | 2.51 | 0.02 | 76368.51 | 14.64 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.25 | 3.0 | -0.0 | 9646.22 | 82.67 | skipped_fast |
| CCUSDT | IDLE | 0.66 | 1.31 | 0.0 | 0.01 | 207570.26 | 8.17 | skipped_fast |
| KITEUSDT | IDLE | 0.91 | 1.75 | 0.41 | -0.01 | 62647.72 | 14.89 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.71 | 1.16 | 0.02 | 56704.02 | 19.2 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.22 | 0.82 | 0.02 | 65535.78 | 3.93 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 1.71 | 1.32 | -0.04 | 89353.9 | 36.39 | skipped_fast |
| HBARUSDT | IDLE | 0.47 | 0.92 | 0.17 | 0.0 | 132397.07 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 1.38 | 1.05 | 0.01 | 35639.15 | 3.14 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 1.34 | 0.91 | 0.02 | 1708.64 | 21.34 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.67 | 0.52 | 0.0 | 53328.98 | 14.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.36 | 0.14 | -0.0 | 27466.26 | 16.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
