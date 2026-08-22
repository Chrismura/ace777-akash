# Hulk DIGEST — 2026-08-22T07:08:21Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.28 | 0.05 | 21221989.08 | 3.91 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 23.87 | 5.73 | 0.22 | 217070019.88 | 6.87 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 8.43 | 0.06 | 1388471.31 | 5.03 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.35 | -0.1 | 705615.53 | 3.32 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 17.58 | 6.86 | 0.07 | 620516.26 | 8.18 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.07 | -0.03 | 247672.48 | 6.56 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.33 | 0.07 | 160537.92 | 20.76 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 3.31 | 0.19 | 793091.38 | 10.75 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 5.01 | 0.05 | 543608.03 | 12.84 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 13.91 | 7.97 | 0.05 | 199589.12 | 7.67 | skipped_fast |
| KITEUSDT | IDLE | 3.4 | 9.68 | 3.04 | 0.11 | 74298.93 | 21.58 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.92 | -0.03 | 87676.95 | 44.59 | skipped_fast |
| FLUIDUSDT | IDLE | 3.34 | 7.38 | 4.29 | 0.05 | 6989.9 | 21.85 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.02 | 11448.14 | 101.69 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.36 | 3.55 | 0.06 | 196618.36 | 35.83 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3298.33 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.5 | 0.01 | 57007.02 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.29 | 1.75 | 0.04 | 58002.57 | 16.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
