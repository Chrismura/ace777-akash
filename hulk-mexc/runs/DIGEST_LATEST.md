# Hulk DIGEST — 2026-08-19T15:14:41Z

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
| XRPUSDT | IDLE | 2.09 | 4.16 | 0.16 | 0.04 | 14427933.58 | 0.96 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.04 | 11.52 | 0.81 | 0.06 | 167909.54 | 3.56 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 12.24 | 5.53 | 0.06 | 19393.1 | 39.36 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 11.42 | 5.74 | -0.01 | 9990.76 | 64.05 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.37 | 10.21 | 0.15 | 0.11 | 77912.74 | 7.3 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 4.94 | 0.23 | 0.05 | 180486.82 | 25.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.96 | 3.89 | 0.15 | 0.03 | 183057.32 | 5.07 | skipped_fast |
| KITEUSDT | IDLE | 2.31 | 4.57 | 0.36 | 0.02 | 55810.58 | 15.91 | skipped_fast |
| WUSDT | IDLE | 1.9 | 3.8 | 0.01 | 0.03 | 116885.52 | 14.35 | skipped_fast |
| EDELUSDT | IDLE | 2.32 | 4.61 | 0.26 | 0.03 | 62709.91 | 38.94 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 2.07 | 0.09 | 0.01 | 245165.69 | 7.63 | skipped_fast |
| RIZEUSDT | IDLE | 2.06 | 4.44 | 3.55 | -0.08 | 34517.26 | 52.87 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 3.9 | 0.08 | -0.04 | 121937.82 | 22.14 | skipped_fast |
| TELUSDT | IDLE | 1.83 | 3.61 | 0.27 | 0.03 | 84148.64 | 34.23 | skipped_fast |
| FLUIDUSDT | IDLE | 2.15 | 4.31 | 0.0 | 0.03 | 1235.33 | 34.52 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.93 | 0.07 | 0.04 | 167422.48 | 1.46 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 2.34 | 0.0 | 0.03 | 36912.45 | 8.67 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.97 | 0.35 | -0.0 | 53266.65 | 17.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
