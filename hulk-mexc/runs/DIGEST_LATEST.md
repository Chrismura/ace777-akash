# Hulk DIGEST — 2026-09-12T19:38:07Z

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
| ETHUSDT | IDLE | 0.61 | 1.07 | 1.05 | -0.01 | 243865417.75 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.5 | 0.88 | 0.85 | 0.0 | 18586352.87 | 2.2 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.52 | 0.49 | -0.0 | 364593773.86 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 56.0 | 16.59 | 0.22 | 125635.3 | 102.02 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 7.36 | 6.74 | 0.01 | 75370.93 | 14.7 | skipped_fast |
| EDELUSDT | IDLE | 3.01 | 6.29 | 1.67 | 0.04 | 169960.17 | 25.43 | skipped_fast |
| ZBCNUSDT | IDLE | 2.36 | 5.6 | 4.44 | -0.03 | 215317.68 | 9.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.68 | 4.57 | 1.36 | 0.08 | 368175.26 | 1.82 | skipped_fast |
| WUSDT | IDLE | 2.02 | 4.02 | 0.15 | 0.04 | 128775.24 | 18.83 | skipped_fast |
| CCUSDT | IDLE | 1.01 | 1.76 | 1.7 | -0.01 | 240664.34 | 10.34 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.83 | 0.78 | 0.03 | 60509.45 | 16.06 | skipped_fast |
| RWAINCUSDT | IDLE | 1.72 | 3.16 | 3.07 | -0.03 | 10156.95 | 55.31 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.53 | 1.51 | 0.02 | 71072.85 | 7.87 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 1.47 | 0.83 | -0.02 | 59476.25 | 10.33 | skipped_fast |
| TELUSDT | IDLE | 1.28 | 2.3 | 1.72 | -0.06 | 98106.96 | 42.21 | skipped_fast |
| HBARUSDT | IDLE | 0.54 | 0.94 | 0.93 | -0.0 | 140432.14 | 1.35 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.89 | 0.81 | 0.0 | 52984.19 | 7.44 | skipped_fast |
| QNTUSDT | IDLE | 0.43 | 0.77 | 0.6 | 0.0 | 41482.66 | 6.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.54 | 0.0 | 0.03 | 1375.44 | 22.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.39 | 0.06 | -0.0 | 24620.51 | 36.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
