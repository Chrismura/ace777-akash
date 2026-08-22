# Hulk DIGEST — 2026-08-22T09:25:13Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.19 | 0.05 | 40266072.03 | 5.99 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 23.87 | 10.76 | 0.11 | 219484310.62 | 3.3 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 15.8 | 9.62 | 0.04 | 1300753.33 | 7.65 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 23.96 | 11.85 | -0.08 | 667838.68 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.35 | 0.05 | 595244.72 | 14.56 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.54 | -0.02 | 237829.22 | 3.23 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.78 | 0.05 | 154672.56 | 11.49 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.25 | 7.21 | 0.13 | 795189.8 | 8.61 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.58 | -0.01 | 464125.96 | 21.7 | skipped_fast |
| KITEUSDT | IDLE | 4.27 | 9.68 | 4.29 | 0.05 | 73088.81 | 12.76 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.73 | 0.03 | 193206.01 | 7.73 | skipped_fast |
| EDELUSDT | IDLE | 2.54 | 4.52 | 3.78 | -0.03 | 79310.93 | 22.47 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.02 | 6973.73 | 20.42 | skipped_fast |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.02 | 11490.86 | 15.99 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.69 | 5.87 | -0.01 | 171159.83 | 31.51 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.82 | -0.02 | 50332.64 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.59 | 0.03 | 57704.7 | 24.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
