# Hulk DIGEST — 2026-10-11T20:27:06Z

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
| WUSDT | IDLE | 3.63 | 33.42 | 3.12 | 0.28 | 3325445.53 | 20.34 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 1.97 | 1.36 | 0.0 | 14969798.26 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 1.03 | 1.95 | 0.74 | 0.01 | 206560837.66 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.27 | 0.61 | 0.01 | 154731762.49 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.41 | 4.5 | 2.08 | -0.0 | 879098.11 | 1.27 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 21.91 | 11.7 | 0.01 | 40595.0 | 47.35 | skipped_fast |
| EDELUSDT | IDLE | 2.76 | 4.96 | 3.69 | -0.03 | 406906.44 | 15.83 | skipped_fast |
| ZBCNUSDT | IDLE | 2.93 | 5.28 | 3.83 | 0.0 | 200112.95 | 13.49 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.0 | 1.77 | 0.0 | 786285.24 | 0.41 | skipped_fast |
| TELUSDT | IDLE | 4.04 | 7.35 | 4.81 | -0.05 | 179074.28 | 52.07 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.76 | 2.25 | 0.05 | 337190.83 | 6.4 | skipped_fast |
| CHIPUSDT | IDLE | 1.3 | 5.39 | 1.33 | 0.06 | 321252.52 | 14.36 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 4.08 | 2.63 | 0.0 | 28763.53 | 4.91 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.09 | 1.23 | 0.01 | 58000.89 | 13.84 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.68 | 0.5 | 0.02 | 88465.44 | 9.95 | skipped_fast |
| KITEUSDT | IDLE | 0.69 | 1.28 | 0.61 | -0.0 | 73083.99 | 8.62 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.76 | 0.22 | 0.02 | 284648.23 | 6.4 | skipped_fast |
| RWAUSDT | IDLE | 1.7 | 3.13 | 1.82 | 0.02 | 52573.21 | 23.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.33 | 2.54 | 0.61 | 0.07 | 59627.59 | 21.15 | skipped_fast |
| MNSRYUSDT | IDLE | 0.97 | 1.79 | 1.06 | -0.01 | 31783.89 | 68.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
