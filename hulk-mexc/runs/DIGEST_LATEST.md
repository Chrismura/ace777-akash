# Hulk DIGEST — 2026-08-22T16:41:05Z

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
| PYTHUSDT | IDLE | 1.99 | 9.83 | 0.02 | 0.09 | 51311764.73 | 1.9 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.84 | 0.05 | 214789197.51 | 3.4 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.35 | 0.08 | 760199.92 | 2.56 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.89 | -0.0 | 1125098.17 | 2.58 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.66 | -0.11 | 626901.78 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.83 | -0.01 | 543555.3 | 8.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.53 | -0.03 | 314785.93 | 23.53 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.58 | 3.78 | -0.06 | 219657.93 | 3.27 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 4.35 | 1.96 | 0.02 | 85058.43 | 8.05 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.03 | 74871.0 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.69 | -0.13 | 129087.34 | 10.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.17 | 0.09 | 47774.77 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.11 | -0.02 | 181907.31 | 6.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 7676.54 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.94 | -0.0 | 136852.41 | 48.24 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.16 | 0.02 | 56486.5 | 24.34 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 21.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
