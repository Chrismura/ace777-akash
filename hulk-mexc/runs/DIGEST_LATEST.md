# Hulk DIGEST — 2026-08-29T17:11:42Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 75.24 | 37.95 | -0.01 | 138465.76 | 35.78 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.62 | 0.69 | 0.0 | 22348257.46 | 2.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.9 | 5.93 | 1.39 | -0.04 | 1035769.46 | 2.43 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 9.82 | 7.03 | 0.04 | 67088.2 | 9.96 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 3.53 | 1.83 | 0.02 | 321216.97 | 2.09 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 3.84 | 0.43 | 0.06 | 212321.03 | 5.13 | skipped_fast |
| RIZEUSDT | IDLE | 2.6 | 5.39 | 2.18 | 0.01 | 33412.58 | 36.18 | skipped_fast |
| REDUSDT | IDLE | 1.96 | 4.67 | 4.06 | 0.04 | 76400.1 | 12.02 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 3.03 | 0.02 | -0.03 | 188936.63 | 6.04 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.81 | 1.02 | 0.0 | 188198.74 | 6.55 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.57 | 0.58 | -0.01 | 64159.31 | 3.62 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.41 | 0.37 | -0.0 | 215003.9 | 1.32 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.12 | 1.11 | -0.04 | 3664.71 | 105.76 | skipped_fast |
| TELUSDT | IDLE | 0.9 | 1.62 | 1.2 | -0.03 | 70408.0 | 40.36 | skipped_fast |
| QNTUSDT | IDLE | 0.73 | 1.4 | 0.45 | 0.0 | 30340.56 | 1.63 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.58 | 0.08 | 0.01 | 53967.86 | 8.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.2 | 0.0 | 0.02 | 2001.2 | 20.68 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
