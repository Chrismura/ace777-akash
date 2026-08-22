# Hulk DIGEST — 2026-08-22T08:37:02Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 19.14 | 11.27 | 0.01 | 30252371.3 | 14.13 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 23.87 | 11.28 | 0.1 | 224592273.19 | 1.99 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.08 | 0.02 | 1341326.08 | 3.84 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 12.97 | -0.1 | 688173.57 | 3.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 17.58 | 9.48 | 0.02 | 601255.86 | 12.64 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.48 | -0.06 | 253280.43 | 9.68 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.35 | 0.06 | 155434.57 | 9.75 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.78 | 0.17 | 815222.57 | 9.13 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 8.47 | 6.24 | -0.0 | 526951.92 | 25.54 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.1 | 0.02 | 194056.98 | 10.88 | skipped_fast |
| KITEUSDT | IDLE | 3.83 | 9.68 | 4.32 | 0.06 | 73510.88 | 11.85 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.03 | 6716.59 | 21.18 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 4.52 | 3.78 | -0.04 | 86959.68 | 56.02 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11076.52 | 112.63 | skipped_fast |
| TELUSDT | IDLE | 2.05 | 5.14 | 4.84 | -0.01 | 173916.78 | 41.6 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.66 | 0.01 | 52255.32 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.51 | 0.04 | 58329.81 | 16.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
