# Hulk DIGEST — 2026-08-22T08:41:22Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.42 | 0.02 | 31276621.64 | 15.99 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 23.87 | 11.68 | 0.1 | 224562920.68 | 3.33 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.19 | 0.02 | 1336614.9 | 8.97 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.21 | -0.1 | 688025.48 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.22 | 0.02 | 601415.57 | 13.63 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.25 | -0.06 | 257017.96 | 6.45 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.34 | 0.05 | 155501.57 | 22.17 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 11.25 | 3.6 | 0.16 | 805593.4 | 9.12 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 8.47 | 6.57 | -0.01 | 518803.89 | 22.61 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.34 | 0.02 | 192517.15 | 7.78 | skipped_fast |
| KITEUSDT | IDLE | 3.82 | 9.68 | 4.15 | 0.06 | 73677.09 | 11.83 | skipped_fast |
| EDELUSDT | IDLE | 2.32 | 4.52 | 4.0 | -0.05 | 86854.75 | 11.2 | skipped_fast |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6885.76 | 22.16 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11076.52 | 112.63 | skipped_fast |
| TELUSDT | IDLE | 2.33 | 5.85 | 5.48 | -0.02 | 174687.23 | 67.87 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3212.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 3.73 | 1.76 | 0.0 | 52265.54 | 44.83 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.04 | 58383.22 | 8.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
