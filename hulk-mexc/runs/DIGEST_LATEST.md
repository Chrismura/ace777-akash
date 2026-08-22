# Hulk DIGEST — 2026-08-22T02:50:39Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.61 | 11.02 | 0.42 | 0.17 | 7283105.63 | 1.9 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 12.56 | 0.31 | 0.19 | 157910396.7 | 1.3 | skipped_fast |
| HBARUSDT | IDLE | 2.54 | 6.38 | 0.27 | 0.1 | 983661.21 | 2.45 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 8.9 | 0.0 | 0.17 | 657476.99 | 10.17 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.99 | 0.11 | 540047.54 | 42.03 | skipped_fast |
| CHIPUSDT | IDLE | 2.41 | 5.57 | 0.0 | -0.02 | 452247.85 | 5.96 | skipped_fast |
| BIOUSDT | IDLE | 3.22 | 8.18 | 2.29 | 0.09 | 193356.29 | 2.99 | skipped_fast |
| WUSDT | IDLE | 1.98 | 5.85 | 0.02 | 0.11 | 414917.15 | 14.9 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 5.02 | 2.61 | -0.03 | 79904.02 | 44.54 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.44 | 0.1 | 61372.52 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.93 | 0.19 | 157863.64 | 17.59 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9400.35 | 5.43 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.25 | 0.08 | 172556.26 | 7.44 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.34 | 0.12 | 62427.57 | 14.36 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.06 | 174222.32 | 36.17 | skipped_fast |
| RWAUSDT | IDLE | 1.51 | 3.0 | 0.16 | 0.05 | 55929.8 | 24.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
