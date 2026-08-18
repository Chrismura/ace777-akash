# Hulk DIGEST — 2026-08-18T18:43:54Z

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
| XRPUSDT | IDLE | 0.56 | 1.05 | 0.51 | -0.0 | 10642927.68 | 2.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 7.03 | 5.95 | -0.03 | 8746.72 | 11.9 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 5.91 | 3.11 | -0.05 | 223782.58 | 3.69 | skipped_fast |
| RIZEUSDT | IDLE | 2.9 | 5.38 | 4.86 | -0.05 | 34624.46 | 49.76 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 2.36 | 2.17 | -0.0 | 241427.03 | 6.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 2.45 | 2.35 | -0.03 | 178500.69 | 11.57 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 7.97 | 4.65 | 0.09 | 131530.42 | 16.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.23 | 2.35 | 0.75 | -0.01 | 169694.52 | 2.6 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.92 | 1.16 | 0.0 | 75410.0 | 4.06 | skipped_fast |
| EDELUSDT | IDLE | 1.15 | 3.39 | 2.1 | -0.04 | 75183.44 | 40.13 | skipped_fast |
| WUSDT | IDLE | 0.64 | 1.16 | 0.8 | -0.02 | 137354.8 | 17.27 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 4.27 | 1.71 | 0.02 | 104588.93 | 41.7 | skipped_fast |
| KITEUSDT | IDLE | 0.68 | 1.28 | 0.55 | -0.01 | 63854.47 | 16.33 | skipped_fast |
| QAITUSDT | IDLE | 0.51 | 6.65 | 5.04 | -0.19 | 18749.7 | 68.26 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.29 | 2.19 | -0.01 | 179.07 | 21.01 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.75 | 0.78 | -0.02 | 34333.96 | 5.35 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.96 | 0.44 | 0.0 | 96361.12 | 1.51 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.69 | -0.01 | 50530.48 | 26.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
