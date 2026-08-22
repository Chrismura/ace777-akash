# Hulk DIGEST — 2026-08-22T11:37:40Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 7.01 | 0.01 | 51621731.79 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.23 | 0.09 | 216983059.1 | 0.67 | skipped_fast |
| CCUSDT | IDLE | 2.03 | 10.24 | 6.87 | 0.13 | 793701.09 | 6.01 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.4 | 0.01 | 1258665.69 | 6.46 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.75 | 0.02 | 586095.46 | 13.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.35 | -0.03 | 389253.3 | 19.59 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.91 | -0.11 | 636716.47 | 3.37 | skipped_fast |
| EDELUSDT | IDLE | 2.81 | 4.93 | 4.59 | -0.05 | 78920.89 | 22.83 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.48 | -0.04 | 241556.83 | 3.23 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 4.3 | 0.34 | 0.04 | 73483.95 | 9.89 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.75 | 5.86 | -0.03 | 167507.16 | 42.87 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2493.12 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.15 | 0.04 | 155264.47 | 14.36 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10927.57 | 32.68 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.99 | 0.0 | 188523.96 | 9.37 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.92 | -0.03 | 48707.73 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.61 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57651.9 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
