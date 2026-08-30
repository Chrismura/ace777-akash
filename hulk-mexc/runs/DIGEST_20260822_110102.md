# Hulk DIGEST — 2026-08-22T11:01:02Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.83 | -0.0 | 51654661.41 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.85 | 0.07 | 218108371.16 | 1.35 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.56 | 0.12 | 818246.27 | 6.05 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.58 | -0.0 | 1248974.41 | 3.89 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.64 | 0.01 | 595569.61 | 13.75 | skipped_fast |
| ZBCNUSDT | IDLE | 1.99 | 5.08 | 4.12 | -0.03 | 424348.11 | 18.0 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.88 | -0.1 | 645982.23 | 3.36 | skipped_fast |
| EDELUSDT | IDLE | 2.77 | 4.93 | 4.04 | -0.04 | 78974.57 | 45.4 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.68 | -0.06 | 240717.57 | 6.51 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 4.3 | 2.06 | 0.03 | 73299.62 | 13.71 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 6.75 | 5.36 | -0.04 | 169061.57 | 48.06 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.01 | 2418.23 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.7 | 0.03 | 154026.56 | 65.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | 0.0 | 11326.93 | 59.83 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.94 | -0.01 | 189149.37 | 7.82 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 1.24 | -0.0 | 49217.23 | 46.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.61 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57437.58 | 32.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
