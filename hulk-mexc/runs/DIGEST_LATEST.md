# Hulk DIGEST — 2026-09-05T22:30:17Z

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
| XRPUSDT | IDLE | 0.62 | 1.08 | 1.02 | 0.01 | 22106416.04 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.88 | 0.55 | 0.01 | 158798491.69 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.6 | 0.49 | 0.0 | 345179560.52 | 0.08 | skipped_fast |
| CHIPUSDT | IDLE | 2.29 | 5.81 | 3.18 | 0.06 | 442952.63 | 3.44 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.96 | 18.34 | 12.93 | -0.0 | 137399.78 | 61.54 | skipped_fast |
| ZBCNUSDT | IDLE | 2.41 | 4.55 | 1.77 | -0.0 | 205540.2 | 19.39 | skipped_fast |
| RWAINCUSDT | IDLE | 2.94 | 5.2 | 4.48 | -0.01 | 7951.12 | 54.35 | skipped_fast |
| PYTHUSDT | IDLE | 1.06 | 1.91 | 1.39 | -0.0 | 337437.76 | 12.79 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.66 | 1.63 | 0.02 | 301936.48 | 5.51 | skipped_fast |
| WUSDT | IDLE | 1.01 | 1.95 | 0.41 | 0.05 | 140683.33 | 7.0 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.62 | 1.38 | 0.03 | 82417.87 | 3.59 | skipped_fast |
| EDELUSDT | IDLE | 0.13 | 2.58 | 0.0 | -0.0 | 166711.95 | 9.33 | skipped_fast |
| HBARUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 337780.17 | 1.25 | skipped_fast |
| KITEUSDT | IDLE | 0.49 | 1.21 | 0.38 | -0.06 | 63204.5 | 8.7 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.96 | 0.2 | 0.05 | 60611.82 | 73.85 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 1.9 | 1.21 | 0.02 | 36683.69 | 4.63 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 1.46 | 1.09 | 0.0 | 66340.56 | 34.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.49 | 0.5 | 0.02 | 528.79 | 22.43 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.99 | 0.35 | 0.03 | 52101.27 | 20.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.26 | 0.05 | 0.0 | 38141.62 | 21.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
