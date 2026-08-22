# Hulk DIGEST — 2026-08-22T10:50:56Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.64 | 0.0 | 51651247.48 | 4.14 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.35 | 0.08 | 218245809.2 | 2.69 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.21 | 0.0 | 1250399.3 | 5.19 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 22.93 | 11.89 | -0.11 | 664235.3 | 6.76 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.7 | 0.01 | 596509.64 | 13.81 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.75 | -0.06 | 240523.62 | 3.27 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 11.25 | 8.15 | 0.12 | 817710.43 | 10.42 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.35 | 0.03 | 154237.58 | 9.92 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 9.72 | 7.85 | -0.04 | 423629.34 | 22.03 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 9.28 | 5.02 | 0.03 | 73433.57 | 11.98 | skipped_fast |
| EDELUSDT | IDLE | 3.33 | 5.96 | 4.65 | -0.04 | 78926.58 | 22.7 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.59 | 9.12 | 7.62 | -0.04 | 168673.74 | 42.9 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 9.75 | 6.26 | -0.0 | 189255.79 | 7.82 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 19.39 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.02 | 2603.82 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 54.35 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.45 | -0.0 | 49236.48 | 22.44 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.31 | 0.01 | 57382.35 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
