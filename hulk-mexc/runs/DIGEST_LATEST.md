# Hulk DIGEST — 2026-08-21T22:31:27Z

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
| PYTHUSDT | IDLE | 1.38 | 5.17 | 0.69 | 0.11 | 5795413.68 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.55 | 5.68 | 0.18 | 0.14 | 134038051.26 | 4.17 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.48 | 0.24 | 0.14 | 657551.7 | 11.58 | skipped_fast |
| HBARUSDT | IDLE | 2.23 | 4.71 | 1.04 | 0.07 | 856852.52 | 3.81 | skipped_fast |
| WUSDT | IDLE | 2.48 | 5.3 | 0.54 | 0.08 | 370779.58 | 12.39 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.6 | 0.06 | 534274.44 | 9.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 6.77 | 0.09 | 0.12 | 503845.25 | 13.26 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.57 | 0.02 | 188030.31 | 15.63 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.28 | 0.18 | 155976.29 | 12.96 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 5.04 | 0.44 | -0.03 | 82607.08 | 10.95 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.07 | 2.43 | 0.02 | 10246.23 | 21.56 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.05 | 187127.61 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.24 | 0.11 | 61413.86 | 12.93 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.81 | 0.06 | 56362.84 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 3.71 | 0.0 | 0.05 | 69559.02 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.25 | 0.04 | 54144.25 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
