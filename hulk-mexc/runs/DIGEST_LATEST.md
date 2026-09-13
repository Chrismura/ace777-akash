# Hulk DIGEST — 2026-09-13T11:39:44Z

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
| ETHUSDT | IDLE | 1.26 | 2.26 | 1.78 | -0.02 | 231428652.31 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 2.26 | 1.81 | -0.02 | 14002388.36 | 2.98 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.07 | 0.74 | -0.01 | 304511857.75 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 14.26 | 12.34 | 0.05 | 203973.26 | 24.95 | skipped_fast |
| PYTHUSDT | IDLE | 2.21 | 3.92 | 3.28 | 0.0 | 440639.51 | 1.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 29.19 | 15.0 | 0.15 | 102881.97 | 68.35 | skipped_fast |
| CCUSDT | IDLE | 2.35 | 4.17 | 3.59 | -0.04 | 289659.04 | 8.43 | skipped_fast |
| WUSDT | IDLE | 1.63 | 2.92 | 2.29 | 0.01 | 244105.1 | 8.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 4.67 | 4.04 | -0.04 | 79279.56 | 15.28 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 2.53 | 2.26 | -0.07 | 195571.3 | 9.12 | skipped_fast |
| BIOUSDT | IDLE | 1.35 | 2.42 | 1.82 | -0.01 | 69777.51 | 3.95 | skipped_fast |
| KITEUSDT | IDLE | 1.48 | 2.69 | 1.83 | 0.02 | 63464.02 | 21.14 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.44 | 1.84 | 0.01 | 56900.01 | 18.39 | skipped_fast |
| TELUSDT | IDLE | 2.11 | 3.9 | 2.09 | -0.05 | 84825.71 | 12.57 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 1.56 | 1.54 | -0.04 | 7173.52 | 5.59 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.57 | 0.77 | 0.01 | 152229.13 | 1.33 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 1.89 | 1.85 | -0.02 | 55057.1 | 30.14 | skipped_fast |
| QNTUSDT | IDLE | 0.68 | 1.31 | 0.34 | -0.0 | 36640.67 | 9.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.14 | -0.0 | 32815.43 | 22.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.47 | 0.44 | 0.01 | 1217.06 | 21.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
