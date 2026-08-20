# Hulk DIGEST — 2026-08-20T00:20:12Z

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
| XRPUSDT | IDLE | 2.05 | 6.78 | 2.39 | 0.11 | 42921113.01 | 1.8 | skipped_fast |
| PYTHUSDT | IDLE | 2.11 | 6.43 | 0.23 | 0.11 | 319386.93 | 4.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.88 | 8.36 | 2.32 | 0.15 | 222341.18 | 23.37 | skipped_fast |
| RIZEUSDT | IDLE | 3.11 | 6.11 | 2.61 | -0.0 | 47543.67 | 51.01 | skipped_fast |
| WUSDT | IDLE | 1.75 | 4.13 | 0.26 | 0.08 | 255086.4 | 12.61 | skipped_fast |
| CCUSDT | IDLE | 1.07 | 3.08 | 1.25 | 0.09 | 342571.59 | 7.06 | skipped_fast |
| HBARUSDT | IDLE | 1.99 | 3.76 | 1.53 | 0.05 | 344820.44 | 1.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 3.54 | 1.78 | 0.06 | 189514.74 | 7.11 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 5.04 | 2.64 | 0.14 | 155617.12 | 3.57 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 9.03 | 0.77 | 0.2 | 83013.81 | 66.89 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 4.7 | 0.79 | 0.06 | 100105.59 | 10.33 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.23 | 0.84 | 0.06 | 58942.35 | 13.46 | skipped_fast |
| FLUIDUSDT | IDLE | 2.26 | 6.09 | 3.68 | 0.06 | 3385.83 | 21.57 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 6.32 | 2.3 | 0.11 | 186328.0 | 24.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.01 | 2.88 | 1.62 | 0.04 | 16859.16 | 39.78 | skipped_fast |
| QNTUSDT | IDLE | 1.57 | 3.03 | 0.79 | 0.05 | 41613.31 | 5.1 | skipped_fast |
| QAITUSDT | IDLE | 0.71 | 2.03 | 0.0 | 0.03 | 10656.03 | 65.85 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.09 | 0.01 | 53800.52 | 8.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
