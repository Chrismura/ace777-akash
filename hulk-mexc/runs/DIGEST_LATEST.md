# Hulk DIGEST — 2026-08-21T20:45:17Z

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
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.5 | 0.08 | 5549057.6 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.37 | 0.11 | 128794010.52 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.32 | 0.17 | 153056.54 | 21.84 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.54 | 0.12 | 478647.06 | 15.99 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.24 | 0.09 | 640529.43 | 8.27 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.84 | 0.05 | 811111.92 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.22 | 0.08 | 514375.86 | 6.17 | skipped_fast |
| WUSDT | IDLE | 2.07 | 3.92 | 1.42 | 0.06 | 367707.99 | 10.54 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.33 | 2.61 | 0.0 | 189094.75 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 5.01 | 3.58 | -0.04 | 81444.19 | 33.73 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10858.43 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.42 | 0.02 | 56284.18 | 45.14 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.43 | 0.11 | 61023.14 | 13.96 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.16 | 0.01 | 181651.38 | 21.4 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.71 | 0.03 | 59909.08 | 7.82 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 54013.87 | 8.32 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2795.49 | 264.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
