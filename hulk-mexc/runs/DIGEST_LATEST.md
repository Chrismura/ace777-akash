# Hulk DIGEST — 2026-08-21T20:39:25Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.74 | 0.08 | 5540697.47 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.62 | 0.1 | 128885549.73 | 0.73 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.4 | 0.17 | 153963.69 | 8.9 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.83 | 0.11 | 478690.18 | 42.62 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.48 | 0.09 | 638701.4 | 5.54 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.23 | 1.96 | 0.05 | 808302.02 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.58 | 0.08 | 515056.09 | 6.17 | skipped_fast |
| WUSDT | IDLE | 2.09 | 3.92 | 1.74 | 0.06 | 368021.71 | 13.75 | skipped_fast |
| BIOUSDT | IDLE | 2.55 | 5.33 | 3.07 | 0.01 | 189619.16 | 6.33 | skipped_fast |
| EDELUSDT | IDLE | 2.82 | 5.01 | 4.55 | -0.05 | 81444.04 | 22.68 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10892.53 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.5 | 0.03 | 56280.38 | 47.09 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.57 | 0.1 | 60870.96 | 9.32 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 183242.76 | 26.83 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.65 | 1.91 | 0.03 | 59944.6 | 7.83 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53924.55 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 46.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
