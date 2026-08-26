# Hulk DIGEST — 2026-08-26T02:45:25Z

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
| PYTHUSDT | IDLE | 2.54 | 5.38 | 0.54 | -0.0 | 2100416.7 | 3.87 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.0 | 77.68 | 38.49 | 0.09 | 57872.17 | 39.04 | skipped_fast |
| XRPUSDT | IDLE | 1.51 | 3.31 | 0.53 | -0.06 | 65699667.1 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 3.39 | 2.14 | -0.05 | 534302.14 | 5.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.78 | 5.38 | 0.06 | -0.0 | 404517.15 | 6.17 | skipped_fast |
| WUSDT | IDLE | 1.9 | 3.84 | 0.18 | -0.02 | 300588.7 | 11.56 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.84 | 0.06 | -0.04 | 693331.88 | 1.27 | skipped_fast |
| REDUSDT | IDLE | 2.1 | 5.58 | 0.99 | 0.01 | 81146.08 | 11.1 | skipped_fast |
| BIOUSDT | IDLE | 2.12 | 4.21 | 0.24 | -0.01 | 94648.44 | 6.81 | skipped_fast |
| KITEUSDT | IDLE | 2.11 | 4.17 | 0.35 | -0.04 | 60815.42 | 9.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 2.39 | 0.69 | -0.01 | 163261.02 | 16.36 | skipped_fast |
| EDELUSDT | IDLE | 0.57 | 8.27 | 5.77 | 0.06 | 154415.44 | 25.9 | skipped_fast |
| QAITUSDT | IDLE | 1.61 | 4.29 | 1.48 | 0.03 | 12825.21 | 30.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.05 | 1.88 | 1.49 | -0.02 | 2581.87 | 30.4 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.18 | 0.22 | -0.04 | 97432.65 | 32.93 | skipped_fast |
| RWAUSDT | IDLE | 0.99 | 1.74 | 1.63 | -0.04 | 55334.08 | 8.3 | skipped_fast |
| QNTUSDT | IDLE | 0.61 | 1.19 | 0.2 | -0.03 | 134169.31 | 4.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.85 | 0.0 | -0.03 | 289.45 | 22.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
