# Hulk DIGEST — 2026-08-29T02:10:15Z

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
| XRPUSDT | IDLE | 0.74 | 1.42 | 0.36 | -0.04 | 48950155.76 | 2.89 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 6.52 | 2.38 | 0.02 | 1191544.9 | 4.8 | skipped_fast |
| QAITUSDT | IDLE | 2.08 | 27.55 | 20.0 | -0.02 | 82499.69 | 71.94 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.06 | 0.73 | -0.03 | 589358.69 | 2.1 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 6.84 | 6.26 | -0.08 | 34970.07 | 55.32 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.88 | 1.19 | -0.02 | 266810.04 | 9.03 | skipped_fast |
| KITEUSDT | IDLE | 1.48 | 2.67 | 1.92 | -0.03 | 79043.09 | 8.67 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.79 | 1.65 | -0.04 | 469382.45 | 1.33 | skipped_fast |
| WUSDT | IDLE | 0.8 | 1.54 | 0.39 | -0.06 | 218944.01 | 16.4 | skipped_fast |
| ZBCNUSDT | IDLE | 0.68 | 1.76 | 0.92 | -0.08 | 171671.78 | 8.71 | skipped_fast |
| EDELUSDT | IDLE | 1.0 | 4.26 | 0.76 | -0.12 | 92515.32 | 19.14 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.76 | 1.54 | -0.04 | 61994.11 | 10.26 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.3 | 0.43 | -0.04 | 85921.54 | 3.59 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 2.28 | 0.0 | -0.02 | 3438.94 | 109.35 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.12 | 0.34 | -0.06 | 99517.86 | 45.02 | skipped_fast |
| FLUIDUSDT | IDLE | 0.86 | 1.52 | 1.32 | -0.07 | 4375.18 | 20.77 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 1.0 | 0.16 | 0.0 | 54212.33 | 16.5 | skipped_fast |
| QNTUSDT | IDLE | 0.37 | 0.74 | 0.03 | -0.03 | 41937.0 | 3.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
