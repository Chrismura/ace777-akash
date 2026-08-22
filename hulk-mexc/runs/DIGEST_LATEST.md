# Hulk DIGEST — 2026-08-22T02:07:15Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 8.42 | 1.41 | 0.13 | 6892566.91 | 3.92 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 10.03 | 0.58 | 0.16 | 154039335.6 | 3.33 | skipped_fast |
| HBARUSDT | IDLE | 2.31 | 4.9 | 0.51 | 0.07 | 952580.26 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.5 | 9.63 | 3.22 | 0.08 | 547252.79 | 40.36 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.12 | 0.15 | 654324.42 | 7.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.7 | 3.91 | 0.09 | 0.02 | 515104.91 | 3.03 | skipped_fast |
| BIOUSDT | IDLE | 2.93 | 6.4 | 0.33 | 0.08 | 185295.56 | 5.98 | skipped_fast |
| WUSDT | IDLE | 1.74 | 4.41 | 0.53 | 0.08 | 400253.82 | 14.19 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 5.02 | 1.52 | -0.02 | 79596.21 | 44.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.0 | 0.11 | 61105.56 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.24 | 0.17 | 156754.6 | 17.84 | skipped_fast |
| QNTUSDT | IDLE | 2.32 | 4.89 | 1.45 | 0.06 | 171287.12 | 13.64 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.72 | 0.12 | 61317.55 | 9.01 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9241.73 | 69.8 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.38 | 0.04 | 179022.56 | 62.24 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.92 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54622.64 | 8.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
