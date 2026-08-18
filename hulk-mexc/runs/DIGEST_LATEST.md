# Hulk DIGEST — 2026-08-18T17:42:53Z

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
| XRPUSDT | IDLE | 0.57 | 1.05 | 0.54 | -0.0 | 10810262.52 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.64 | 7.28 | 2.93 | -0.05 | 233385.21 | 3.64 | skipped_fast |
| QAITUSDT | IDLE | 1.83 | 24.5 | 14.96 | -0.17 | 18608.8 | 39.86 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 9.96 | 8.38 | 0.06 | 125299.31 | 26.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.39 | 4.63 | 2.82 | -0.03 | 34553.46 | 48.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.19 | 1.86 | -0.02 | 190785.23 | 15.34 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.65 | 1.52 | -0.01 | 239089.36 | 6.6 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 2.35 | 0.44 | -0.01 | 173421.47 | 2.59 | skipped_fast |
| BIOUSDT | IDLE | 1.22 | 2.3 | 0.96 | 0.0 | 74912.85 | 4.05 | skipped_fast |
| EDELUSDT | IDLE | 1.32 | 3.93 | 2.09 | -0.04 | 75183.93 | 40.03 | skipped_fast |
| WUSDT | IDLE | 0.64 | 1.16 | 0.75 | -0.03 | 139832.99 | 14.8 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 4.27 | 2.12 | 0.02 | 115336.98 | 48.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.01 | 2.1 | 0.82 | -0.02 | 5159.03 | 17.77 | skipped_fast |
| KITEUSDT | IDLE | 0.68 | 1.28 | 0.55 | -0.01 | 64084.12 | 16.33 | skipped_fast |
| QNTUSDT | IDLE | 0.91 | 1.75 | 0.51 | -0.02 | 35328.31 | 3.56 | skipped_fast |
| HBARUSDT | IDLE | 0.52 | 0.96 | 0.5 | 0.0 | 108292.85 | 1.51 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.29 | 0.0 | 0.01 | 177.93 | 22.69 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.96 | 0.52 | -0.01 | 50442.28 | 17.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
