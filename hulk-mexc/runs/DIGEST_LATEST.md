# Hulk DIGEST — 2026-09-01T15:25:44Z

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
| XRPUSDT | IDLE | 1.14 | 2.1 | 1.17 | 0.0 | 30131362.3 | 2.92 | skipped_fast |
| ETHUSDT | IDLE | 0.84 | 1.54 | 0.94 | -0.01 | 291397602.52 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.15 | 0.7 | -0.01 | 528639363.09 | 0.26 | skipped_fast |
| CHIPUSDT | IDLE | 3.57 | 14.71 | 2.59 | 0.1 | 465894.05 | 2.31 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 3.4 | 1.92 | 0.06 | 598670.01 | 2.0 | skipped_fast |
| CCUSDT | IDLE | 2.45 | 4.32 | 3.83 | -0.01 | 388336.79 | 11.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.59 | 4.82 | 2.43 | 0.03 | 225170.69 | 10.19 | skipped_fast |
| WUSDT | IDLE | 2.25 | 4.35 | 0.96 | 0.06 | 256808.17 | 12.4 | skipped_fast |
| KITEUSDT | IDLE | 2.91 | 5.66 | 1.0 | 0.03 | 60984.05 | 10.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 4.79 | 3.03 | -0.07 | 43724.3 | 20.18 | skipped_fast |
| REDUSDT | IDLE | 1.9 | 3.77 | 0.14 | 0.05 | 65590.34 | 14.25 | skipped_fast |
| EDELUSDT | IDLE | 0.93 | 6.17 | 4.21 | -0.08 | 175472.61 | 17.56 | skipped_fast |
| BIOUSDT | IDLE | 1.22 | 2.26 | 1.18 | -0.01 | 66749.83 | 3.85 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.83 | 1.63 | 0.01 | 231852.84 | 1.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 1.95 | 1.56 | -0.01 | 5633.26 | 47.09 | skipped_fast |
| QNTUSDT | IDLE | 1.81 | 3.58 | 0.33 | 0.03 | 36685.49 | 1.58 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.18 | 2.02 | 0.01 | 97130.71 | 11.78 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.57 | 1.44 | -0.0 | 62532.23 | 15.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.13 | 0.86 | -0.01 | 32707.88 | 13.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 396.53 | 21.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
