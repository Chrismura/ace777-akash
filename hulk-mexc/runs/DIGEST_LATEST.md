# Hulk DIGEST — 2026-08-25T22:44:52Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 7.78 | 5.86 | 0.0 | 2228923.89 | 2.0 | skipped_fast |
| XRPUSDT | IDLE | 2.26 | 5.37 | 2.56 | -0.02 | 75691938.46 | 1.38 | skipped_fast |
| HBARUSDT | IDLE | 2.07 | 4.2 | 2.84 | -0.02 | 812686.08 | 1.28 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 4.28 | 1.45 | -0.02 | 534052.19 | 9.13 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 5.18 | 0.8 | -0.01 | 481114.51 | 6.2 | skipped_fast |
| WUSDT | IDLE | 2.28 | 4.36 | 2.54 | -0.02 | 346129.11 | 12.85 | skipped_fast |
| BIOUSDT | IDLE | 3.12 | 5.87 | 2.41 | -0.0 | 115756.83 | 3.43 | skipped_fast |
| RIZEUSDT | IDLE | 3.51 | 7.26 | 3.62 | 0.04 | 51800.51 | 33.16 | skipped_fast |
| REDUSDT | IDLE | 2.97 | 7.38 | 4.83 | -0.0 | 80276.41 | 12.22 | skipped_fast |
| ZBCNUSDT | IDLE | 2.12 | 3.85 | 3.16 | 0.01 | 197063.54 | 13.26 | skipped_fast |
| KITEUSDT | IDLE | 2.63 | 4.98 | 2.58 | -0.02 | 61862.53 | 11.61 | skipped_fast |
| EDELUSDT | IDLE | 0.96 | 13.82 | 10.24 | 0.01 | 164833.09 | 33.76 | skipped_fast |
| QAITUSDT | IDLE | 1.58 | 4.3 | 0.79 | 0.02 | 12536.96 | 26.42 | skipped_fast |
| FLUIDUSDT | IDLE | 2.23 | 4.14 | 2.2 | -0.02 | 2037.2 | 22.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 1.7 | 1.67 | -0.01 | 2546.77 | 50.1 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.62 | 2.01 | -0.01 | 118082.69 | 17.36 | skipped_fast |
| RWAUSDT | IDLE | 1.5 | 2.63 | 2.41 | -0.03 | 56780.03 | 32.84 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 2.52 | 1.2 | -0.03 | 93348.45 | 55.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
