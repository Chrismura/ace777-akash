# Hulk DIGEST — 2026-08-21T20:03:38Z

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
| PYTHUSDT | IDLE | 1.36 | 4.78 | 3.81 | 0.07 | 5461121.83 | 4.26 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.49 | 0.11 | 128891161.27 | 2.92 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.64 | 0.16 | 154369.87 | 13.13 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 10.86 | 8.45 | 0.07 | 481353.51 | 25.78 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.72 | 0.07 | 635080.61 | 13.08 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 3.23 | 3.06 | 0.05 | 793856.38 | 1.32 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 4.81 | 4.29 | 0.09 | 513601.26 | 3.12 | skipped_fast |
| WUSDT | IDLE | 2.18 | 3.92 | 2.95 | 0.05 | 365893.42 | 8.57 | skipped_fast |
| BIOUSDT | IDLE | 2.62 | 5.33 | 4.08 | -0.0 | 189982.27 | 3.2 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 4.29 | 4.01 | -0.05 | 79684.73 | 33.76 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.61 | 0.02 | 56220.06 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.19 | 4.3 | 0.58 | 0.05 | 11066.49 | 37.42 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.41 | 0.09 | 61312.52 | 12.2 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2867.01 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.54 | 0.01 | 183636.44 | 37.99 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.65 | 1.97 | 0.04 | 59921.93 | 4.69 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.16 | 0.82 | 0.04 | 54350.76 | 16.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.14 | 0.07 | 4276.39 | 21.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
