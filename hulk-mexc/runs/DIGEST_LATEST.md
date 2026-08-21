# Hulk DIGEST — 2026-08-21T20:35:40Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.7 | 0.08 | 5531990.5 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 4.21 | 3.06 | 0.11 | 129095155.53 | 3.63 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.62 | 0.17 | 154084.16 | 13.81 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 10.86 | 5.15 | 0.12 | 478466.31 | 5.47 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 3.91 | 0.59 | 0.08 | 634144.69 | 8.3 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.81 | 0.05 | 810003.39 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.31 | 0.08 | 514042.76 | 3.08 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.6 | 0.06 | 368361.25 | 4.23 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.79 | 0.02 | 189077.43 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.79 | 5.01 | 4.12 | -0.05 | 80864.85 | 78.78 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10934.71 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.68 | 0.03 | 56298.25 | 47.09 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.5 | 0.1 | 60744.54 | 9.32 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.59 | 0.01 | 183185.08 | 26.83 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.77 | 0.04 | 59936.78 | 4.7 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53842.85 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
