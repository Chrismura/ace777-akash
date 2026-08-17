# Hulk DIGEST — 2026-08-17T14:11:54Z

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
| XRPUSDT | IDLE | 0.4 | 0.75 | 0.35 | 0.0 | 11565650.53 | 1.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 26.76 | 12.77 | 0.22 | 68866.57 | 40.85 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 7.6 | 2.82 | 0.03 | 352488.01 | 3.26 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 4.0 | 3.36 | -0.04 | 273357.91 | 17.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.71 | 4.92 | 3.36 | -0.0 | 166697.79 | 31.57 | skipped_fast |
| REDUSDT | IDLE | 2.33 | 4.16 | 3.4 | -0.05 | 57296.83 | 15.67 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 4.11 | 0.37 | 0.07 | 60405.27 | 12.38 | skipped_fast |
| WUSDT | IDLE | 0.68 | 1.21 | 0.94 | -0.03 | 166333.71 | 15.58 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.67 | 1.04 | -0.0 | 74612.55 | 4.06 | skipped_fast |
| PYTHUSDT | IDLE | 0.54 | 0.98 | 0.64 | -0.01 | 149277.99 | 2.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.45 | 2.56 | 2.32 | -0.04 | 2257.9 | 46.4 | skipped_fast |
| KITEUSDT | IDLE | 0.87 | 1.57 | 1.09 | -0.02 | 52955.58 | 16.19 | skipped_fast |
| TELUSDT | IDLE | 2.02 | 3.6 | 3.0 | -0.01 | 94398.44 | 35.08 | skipped_fast |
| QAITUSDT | IDLE | 1.2 | 2.1 | 1.99 | 0.01 | 825.6 | 61.12 | skipped_fast |
| QNTUSDT | IDLE | 1.89 | 3.77 | 0.05 | 0.0 | 35600.67 | 12.15 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.55 | 0.98 | 0.01 | 123418.79 | 1.52 | skipped_fast |
| FLUIDUSDT | IDLE | 1.11 | 2.23 | 0.0 | -0.0 | 903.56 | 22.03 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.61 | 0.09 | 0.01 | 50082.04 | 17.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
