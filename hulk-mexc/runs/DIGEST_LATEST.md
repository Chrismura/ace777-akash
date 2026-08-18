# Hulk DIGEST — 2026-08-18T19:10:14Z

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
| XRPUSDT | IDLE | 0.51 | 0.94 | 0.52 | -0.0 | 10607779.0 | 1.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 7.03 | 5.95 | -0.03 | 8746.72 | 11.9 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.03 | 6.57 | 6.04 | -0.07 | 34654.27 | 50.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.0 | 3.21 | -0.05 | 218410.7 | 3.73 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 7.76 | 4.91 | 0.09 | 133092.32 | 12.85 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 2.45 | 1.77 | -0.02 | 177035.86 | 14.71 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.58 | 0.03 | 0.01 | 168035.7 | 2.57 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 1.71 | 1.05 | 0.0 | 244956.01 | 8.83 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.84 | 1.08 | -0.0 | 64774.95 | 4.06 | skipped_fast |
| EDELUSDT | IDLE | 1.07 | 3.12 | 2.23 | -0.03 | 74858.73 | 40.3 | skipped_fast |
| WUSDT | IDLE | 0.63 | 1.16 | 0.73 | -0.02 | 134294.85 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 2.12 | 4.2 | 1.78 | 0.02 | 104786.0 | 48.59 | skipped_fast |
| KITEUSDT | IDLE | 0.54 | 1.03 | 0.31 | -0.01 | 64204.4 | 16.33 | skipped_fast |
| QAITUSDT | IDLE | 0.43 | 5.83 | 3.06 | -0.19 | 18432.6 | 56.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.29 | 2.19 | -0.01 | 179.07 | 21.86 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.75 | 0.67 | -0.02 | 34420.38 | 7.14 | skipped_fast |
| HBARUSDT | IDLE | 0.48 | 0.93 | 0.23 | 0.01 | 95778.6 | 3.02 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.7 | 0.52 | -0.01 | 50095.69 | 17.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
