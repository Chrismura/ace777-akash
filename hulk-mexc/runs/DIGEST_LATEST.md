# Hulk DIGEST — 2026-09-05T22:28:42Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.61 | 1.08 | 0.99 | 0.01 | 22109462.68 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.88 | 0.51 | 0.01 | 158796166.12 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.6 | 0.44 | 0.0 | 347975189.89 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.96 | 18.34 | 13.21 | -0.01 | 137434.2 | 61.54 | skipped_fast |
| CHIPUSDT | IDLE | 2.28 | 5.81 | 3.05 | 0.06 | 443005.32 | 3.44 | skipped_fast |
| ZBCNUSDT | IDLE | 2.39 | 4.55 | 1.51 | 0.0 | 205511.26 | 15.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.94 | 5.2 | 4.48 | -0.01 | 7951.12 | 54.35 | skipped_fast |
| PYTHUSDT | IDLE | 0.8 | 1.46 | 0.96 | 0.0 | 332730.68 | 1.82 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.61 | 1.53 | 0.03 | 301926.74 | 7.35 | skipped_fast |
| WUSDT | IDLE | 1.0 | 1.95 | 0.37 | 0.04 | 140634.41 | 10.99 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.62 | 1.24 | 0.03 | 82807.29 | 3.59 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.96 | 0.16 | 0.05 | 60680.64 | 17.28 | skipped_fast |
| EDELUSDT | IDLE | 0.13 | 2.39 | 0.37 | -0.01 | 166013.46 | 18.73 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.13 | 1.11 | 0.03 | 337733.83 | 1.25 | skipped_fast |
| KITEUSDT | IDLE | 0.49 | 1.21 | 0.38 | -0.06 | 63177.86 | 10.27 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 1.9 | 1.08 | 0.02 | 36649.95 | 4.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.49 | 0.24 | 0.02 | 487.62 | 4.81 | skipped_fast |
| TELUSDT | IDLE | 0.76 | 1.46 | 0.4 | 0.01 | 66338.2 | 40.52 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.99 | 0.35 | 0.03 | 52135.77 | 20.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.26 | 0.22 | -0.0 | 38162.98 | 21.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
