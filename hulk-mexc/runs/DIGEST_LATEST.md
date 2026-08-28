# Hulk DIGEST — 2026-08-28T08:06:29Z

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
| PYTHUSDT | IDLE | 1.4 | 2.57 | 1.52 | 0.01 | 12829153.33 | 2.05 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 55.46 | 31.55 | -0.2 | 60409.99 | 49.93 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.34 | 1.02 | -0.0 | 56081877.04 | 1.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 7.0 | 1.04 | 0.08 | 694423.48 | 7.49 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.69 | 1.29 | -0.03 | 474418.75 | 5.34 | skipped_fast |
| REDUSDT | IDLE | 2.07 | 3.68 | 3.12 | -0.02 | 81349.62 | 13.81 | skipped_fast |
| KITEUSDT | IDLE | 2.08 | 3.8 | 2.42 | -0.01 | 72863.42 | 8.59 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 2.15 | 1.29 | 0.02 | 255474.2 | 2.88 | skipped_fast |
| WUSDT | IDLE | 0.94 | 1.72 | 1.11 | -0.01 | 201908.58 | 9.57 | skipped_fast |
| RIZEUSDT | IDLE | 0.87 | 10.92 | 1.51 | -0.16 | 119414.62 | 51.22 | skipped_fast |
| TELUSDT | IDLE | 1.97 | 3.44 | 3.33 | -0.0 | 137787.63 | 5.46 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.34 | 0.45 | -0.0 | 92840.56 | 3.49 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.51 | 0.34 | 0.0 | 306266.69 | 1.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 4.28 | 4.1 | -0.03 | 20682.7 | 132.23 | skipped_fast |
| EDELUSDT | IDLE | 0.47 | 3.22 | 2.44 | 0.09 | 45964.91 | 43.12 | skipped_fast |
| FLUIDUSDT | IDLE | 1.43 | 2.68 | 1.16 | -0.01 | 7663.46 | 21.87 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.26 | 0.0 | -0.0 | 43252.25 | 12.77 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.33 | 0.01 | 54456.86 | 8.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
