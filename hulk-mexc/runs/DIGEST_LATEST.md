# Hulk DIGEST — 2026-08-22T11:35:33Z

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
| PYTHUSDT | IDLE | 2.18 | 9.66 | 7.43 | 0.01 | 51625507.88 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.26 | 0.08 | 217333300.0 | 2.01 | skipped_fast |
| CCUSDT | IDLE | 2.03 | 10.24 | 7.05 | 0.13 | 807968.18 | 6.01 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.27 | 0.01 | 1259616.51 | 6.46 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.81 | 0.02 | 587919.15 | 13.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.35 | -0.03 | 392377.34 | 27.32 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.85 | -0.1 | 636945.41 | 10.11 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.26 | -0.05 | 78957.29 | 22.83 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 6.64 | 2.61 | -0.04 | 237598.35 | 6.46 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 4.3 | 0.37 | 0.04 | 73525.29 | 11.67 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.61 | -0.03 | 167677.15 | 42.87 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2500.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.8 | 0.05 | 155311.43 | 15.2 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | 0.0 | 11178.17 | 32.68 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 1.04 | -0.03 | 48709.49 | 36.1 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.96 | 0.01 | 188514.31 | 7.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.31 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57598.4 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
