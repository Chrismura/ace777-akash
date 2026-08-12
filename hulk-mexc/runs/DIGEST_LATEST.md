# Hulk DIGEST — 2026-08-12T23:08:34Z

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
| XRPUSDT | IDLE | 0.61 | 1.06 | 1.03 | -0.02 | 14542469.88 | 1.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 5.46 | 5.18 | -0.04 | 2019.97 | 44.1 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.42 | 1.47 | -0.04 | 328901.55 | 2.49 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 17.24 | 0.43 | 0.25 | 51306.46 | 41.35 | skipped_fast |
| BIOUSDT | IDLE | 2.21 | 3.94 | 3.22 | -0.05 | 62444.48 | 4.21 | skipped_fast |
| WUSDT | IDLE | 1.76 | 3.2 | 2.16 | -0.04 | 176147.83 | 13.72 | skipped_fast |
| EDELUSDT | IDLE | 2.32 | 8.33 | 5.49 | 0.08 | 71904.61 | 99.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.55 | 2.73 | 2.52 | -0.04 | 185833.16 | 24.37 | skipped_fast |
| QNTUSDT | IDLE | 3.12 | 5.57 | 4.41 | 0.01 | 60196.35 | 6.86 | skipped_fast |
| KITEUSDT | IDLE | 1.54 | 2.85 | 1.5 | -0.04 | 60142.33 | 12.85 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 2.39 | 1.79 | -0.01 | 60412.71 | 18.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 2.4 | 1.02 | 0.04 | 104153.94 | 8.62 | skipped_fast |
| CCUSDT | IDLE | 0.47 | 0.86 | 0.58 | -0.02 | 212280.79 | 5.06 | skipped_fast |
| QAITUSDT | IDLE | 0.77 | 2.51 | 1.67 | -0.05 | 4222.39 | 60.51 | skipped_fast |
| HBARUSDT | IDLE | 0.41 | 0.75 | 0.45 | -0.01 | 79579.68 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 0.58 | 1.08 | 0.5 | 0.02 | 95558.81 | 31.66 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.0 | 0.66 | 0.02 | 51999.81 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 0.64 | 0.23 | -0.02 | 557.16 | 22.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
