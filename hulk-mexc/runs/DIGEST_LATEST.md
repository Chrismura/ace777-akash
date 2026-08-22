# Hulk DIGEST — 2026-08-22T15:45:41Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.5 | 0.04 | 51498788.0 | 5.92 | skipped_fast |
| XRPUSDT | IDLE | 1.38 | 7.64 | 5.78 | 0.02 | 216007870.3 | 1.39 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 5.65 | 3.01 | 0.08 | 790186.55 | 10.3 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.3 | -0.02 | 1155307.47 | 5.23 | skipped_fast |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 2.16 | -0.09 | 604907.4 | 3.4 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.59 | -0.02 | 553086.6 | 11.73 | skipped_fast |
| KITEUSDT | IDLE | 2.76 | 6.37 | 2.01 | 0.03 | 85461.16 | 8.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.87 | -0.05 | 320017.84 | 34.95 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.07 | -0.06 | 221540.77 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.05 | 78977.51 | 22.78 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.21 | -0.22 | 139980.37 | 12.0 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.3 | 0.03 | 56465.76 | 45.5 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.08 | -0.02 | 184188.54 | 4.73 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.52 | -0.01 | 140605.69 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.71 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 57433.65 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
