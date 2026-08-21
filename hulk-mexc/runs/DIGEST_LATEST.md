# Hulk DIGEST — 2026-08-21T22:02:37Z

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
| PYTHUSDT | IDLE | 1.26 | 4.74 | 0.45 | 0.1 | 5693847.45 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.11 | 3.73 | 0.95 | 0.11 | 129714850.5 | 2.14 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.74 | 0.08 | 840729.12 | 3.8 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 3.95 | 0.09 | 0.11 | 636402.28 | 6.38 | skipped_fast |
| CHIPUSDT | IDLE | 1.54 | 4.54 | 2.47 | 0.04 | 527326.96 | 3.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 6.19 | 0.1 | 0.12 | 494439.05 | 23.68 | skipped_fast |
| WUSDT | IDLE | 2.11 | 4.19 | 0.18 | 0.07 | 367957.99 | 18.69 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.01 | 1.2 | 0.03 | 185340.83 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.71 | 0.18 | 153862.71 | 10.61 | skipped_fast |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.18 | 0.05 | 189043.68 | 25.99 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 4.12 | 1.1 | -0.04 | 82668.26 | 44.25 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 4.07 | 0.9 | 0.02 | 10204.87 | 53.39 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.89 | 0.11 | 61251.97 | 12.89 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.76 | 0.06 | 56467.5 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 2.49 | 0.26 | 0.04 | 62413.28 | 7.72 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.33 | 0.25 | 0.04 | 54109.07 | 49.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
