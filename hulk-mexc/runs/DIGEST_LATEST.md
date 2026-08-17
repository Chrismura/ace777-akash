# Hulk DIGEST — 2026-08-17T13:08:33Z

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
| XRPUSDT | IDLE | 0.38 | 0.69 | 0.52 | -0.0 | 11076251.1 | 1.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 11.83 | 7.41 | 0.07 | 354649.84 | 6.58 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 25.22 | 12.44 | 0.23 | 75075.19 | 35.94 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 2.87 | 2.5 | -0.03 | 262199.57 | 10.69 | skipped_fast |
| REDUSDT | IDLE | 2.32 | 4.16 | 3.18 | -0.05 | 56048.77 | 15.64 | skipped_fast |
| EDELUSDT | IDLE | 2.38 | 4.66 | 0.62 | 0.06 | 60276.02 | 37.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 2.19 | 2.14 | 0.01 | 157050.28 | 19.78 | skipped_fast |
| PYTHUSDT | IDLE | 0.91 | 1.64 | 1.21 | -0.01 | 149918.5 | 2.56 | skipped_fast |
| WUSDT | IDLE | 0.69 | 1.21 | 1.14 | -0.03 | 174511.84 | 15.54 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.67 | 1.44 | -0.01 | 69875.72 | 4.06 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.73 | 0.88 | -0.02 | 53566.32 | 16.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.44 | 2.56 | 2.15 | -0.04 | 2000.6 | 63.97 | skipped_fast |
| TELUSDT | IDLE | 1.94 | 3.6 | 1.91 | -0.0 | 93386.62 | 34.73 | skipped_fast |
| QAITUSDT | IDLE | 1.18 | 2.1 | 1.68 | -0.0 | 1694.23 | 61.12 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.62 | 0.8 | 0.01 | 119327.63 | 1.52 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.28 | 0.25 | -0.02 | 33128.86 | 21.12 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.85 | 1.14 | -0.02 | 882.14 | 16.15 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.17 | 0.01 | 49530.51 | 17.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
