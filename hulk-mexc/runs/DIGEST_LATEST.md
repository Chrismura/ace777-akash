# Hulk DIGEST — 2026-08-22T02:26:31Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 9.45 | 0.98 | 0.15 | 6989361.77 | 11.6 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 10.44 | 0.44 | 0.17 | 154917205.63 | 1.99 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.78 | 0.09 | 542309.28 | 7.74 | skipped_fast |
| HBARUSDT | IDLE | 2.33 | 5.14 | 0.0 | 0.09 | 962869.08 | 6.18 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 6.33 | 0.32 | 0.15 | 654278.72 | 7.85 | skipped_fast |
| CHIPUSDT | IDLE | 2.23 | 5.07 | 0.57 | -0.01 | 474438.78 | 6.03 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.1 | 8.18 | 0.21 | 0.1 | 193329.89 | 5.88 | skipped_fast |
| WUSDT | IDLE | 1.85 | 5.09 | 0.03 | 0.1 | 401768.41 | 4.0 | skipped_fast |
| EDELUSDT | IDLE | 2.48 | 5.02 | 3.04 | -0.03 | 79663.24 | 22.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.92 | 0.11 | 61310.59 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.35 | 0.17 | 157147.28 | 17.03 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 4.09 | 0.84 | 0.12 | 61852.74 | 9.92 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9345.09 | 32.54 | skipped_fast |
| QNTUSDT | IDLE | 2.22 | 4.89 | 0.01 | 0.08 | 171099.52 | 4.48 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.43 | 0.04 | 178535.41 | 62.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.78 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54964.48 | 8.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
