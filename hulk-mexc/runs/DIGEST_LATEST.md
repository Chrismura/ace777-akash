# Hulk DIGEST — 2026-08-21T20:28:20Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.81 | 0.08 | 5516940.05 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.16 | 0.11 | 129074074.86 | 1.45 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.37 | 0.16 | 153392.06 | 20.19 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.62 | 0.11 | 478233.22 | 20.48 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 3.91 | 1.17 | 0.08 | 632407.85 | 6.5 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.23 | 1.94 | 0.05 | 800792.65 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.61 | 0.08 | 509811.44 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.1 | 3.92 | 1.89 | 0.06 | 365060.52 | 11.65 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.39 | 0.02 | 189698.6 | 6.29 | skipped_fast |
| EDELUSDT | IDLE | 2.79 | 4.89 | 4.66 | -0.06 | 80391.28 | 34.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.61 | 0.01 | 56216.92 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10983.46 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.52 | 0.1 | 60981.11 | 12.11 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.59 | 0.01 | 183841.27 | 16.13 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 2.65 | 2.03 | 0.03 | 59966.17 | 23.51 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54215.04 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
