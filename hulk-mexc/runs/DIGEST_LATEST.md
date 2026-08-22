# Hulk DIGEST — 2026-08-22T10:01:42Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.67 | 16.77 | 9.39 | 0.03 | 51561423.48 | 28.23 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 11.85 | 0.06 | 215029489.37 | 4.01 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 15.8 | 10.53 | 0.02 | 1259634.25 | 6.44 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.8 | -0.1 | 664448.18 | 3.38 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 16.84 | 8.92 | 0.02 | 594416.24 | 13.69 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.82 | -0.03 | 237325.93 | 3.2 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.41 | 0.11 | 809777.17 | 9.58 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 37.92 | 10.33 | 0.05 | 153857.08 | 22.28 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 7.87 | 6.53 | -0.01 | 436942.75 | 10.6 | skipped_fast |
| KITEUSDT | IDLE | 4.14 | 9.28 | 4.93 | 0.04 | 73354.5 | 11.05 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.04 | 9.75 | 5.61 | 0.01 | 189367.81 | 7.76 | skipped_fast |
| EDELUSDT | IDLE | 2.68 | 4.76 | 4.0 | -0.03 | 79217.64 | 33.8 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 22.17 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 6.98 | 6.43 | -0.02 | 170968.7 | 37.01 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.63 | -0.0 | 49319.48 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.02 | 57536.07 | 16.17 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.0 | 11462.91 | 86.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
