# Hulk DIGEST — 2026-09-12T14:36:29Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.35 | 0.67 | 0.18 | -0.03 | 392679014.65 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.33 | 0.62 | 0.31 | -0.02 | 28854991.02 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.26 | 0.03 | -0.02 | 444604841.66 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.5 | 8.33 | 4.98 | -0.02 | 225847.99 | 31.86 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.67 | 6.94 | 5.3 | -0.0 | 12501.07 | 5.49 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 2.42 | 0.02 | 0.02 | 357535.57 | 1.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.39 | 5.05 | 0.91 | 0.04 | 78149.65 | 16.26 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 1.67 | 1.29 | -0.02 | 291090.24 | 6.11 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 3.39 | 1.21 | 0.03 | 162942.47 | 8.71 | skipped_fast |
| RIZEUSDT | IDLE | 0.41 | 18.2 | 2.02 | 0.96 | 169910.87 | 77.19 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.97 | 0.89 | 0.0 | 75259.4 | 7.8 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.12 | 1.16 | 0.02 | 62307.22 | 20.27 | skipped_fast |
| WUSDT | IDLE | 0.61 | 1.15 | 0.45 | -0.0 | 162755.07 | 12.27 | skipped_fast |
| KITEUSDT | IDLE | 0.62 | 1.24 | 0.0 | -0.03 | 60978.43 | 12.13 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.3 | 1.42 | -0.09 | 91813.76 | 23.95 | skipped_fast |
| HBARUSDT | IDLE | 0.33 | 0.63 | 0.25 | -0.02 | 197347.79 | 1.34 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.85 | 1.46 | 0.0 | 54842.34 | 29.56 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.47 | 0.54 | -0.01 | 41281.49 | 7.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.71 | 0.07 | -0.01 | 24177.33 | 5.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.0 | 1329.82 | 22.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
