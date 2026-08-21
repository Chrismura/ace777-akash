# Hulk DIGEST — 2026-08-21T20:02:14Z

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
| PYTHUSDT | IDLE | 1.37 | 4.78 | 3.99 | 0.06 | 5458080.27 | 2.13 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 4.21 | 3.71 | 0.11 | 128877092.1 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.85 | 0.16 | 154359.72 | 13.13 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 10.86 | 8.76 | 0.07 | 481552.46 | 26.39 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.77 | 0.07 | 635030.45 | 10.28 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 3.23 | 3.02 | 0.05 | 793928.08 | 1.32 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 4.81 | 4.41 | 0.08 | 514641.43 | 6.24 | skipped_fast |
| WUSDT | IDLE | 2.21 | 3.92 | 3.29 | 0.04 | 365871.23 | 9.67 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 5.33 | 4.51 | -0.0 | 189994.57 | 3.21 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 4.29 | 4.01 | -0.05 | 79709.78 | 33.8 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.44 | 0.02 | 56223.4 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.19 | 4.3 | 0.58 | 0.05 | 11066.49 | 10.71 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.44 | 0.1 | 61351.07 | 11.29 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2867.01 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.54 | 0.01 | 183677.06 | 43.43 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 2.65 | 2.12 | 0.04 | 59922.56 | 6.28 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.08 | 0.99 | 0.04 | 54305.5 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.14 | 0.07 | 4276.39 | 20.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
