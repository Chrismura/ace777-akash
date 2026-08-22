# Hulk DIGEST — 2026-08-22T08:38:47Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 19.14 | 11.11 | 0.02 | 30636463.0 | 10.08 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 23.87 | 11.65 | 0.1 | 224466328.77 | 5.34 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 15.8 | 10.29 | 0.02 | 1337789.18 | 8.98 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 12.85 | -0.1 | 688155.61 | 3.38 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 17.58 | 9.43 | 0.02 | 601361.52 | 14.74 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.48 | -0.06 | 256258.24 | 3.22 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.57 | 0.05 | 155496.92 | 11.55 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.72 | 0.16 | 807252.5 | 8.3 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 8.47 | 6.71 | -0.01 | 520684.87 | 23.65 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.22 | 0.02 | 193443.12 | 6.22 | skipped_fast |
| KITEUSDT | IDLE | 3.83 | 9.68 | 4.39 | 0.05 | 73561.97 | 9.12 | skipped_fast |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6715.48 | 22.18 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 4.52 | 3.89 | -0.03 | 86961.87 | 44.89 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11076.52 | 112.63 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.41 | 4.94 | -0.01 | 174444.01 | 36.41 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 3.73 | 1.95 | 0.01 | 52241.11 | 44.83 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.04 | 58358.99 | 8.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
