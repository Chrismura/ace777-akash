# Hulk DIGEST — 2026-08-20T09:22:12Z

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
| XRPUSDT | IDLE | 1.63 | 6.44 | 0.45 | 0.15 | 52340558.24 | 2.59 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 23.55 | 9.6 | 0.24 | 183062.36 | 10.01 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 18.86 | 1.28 | 0.33 | 237569.93 | 18.03 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 5.36 | 0.37 | 0.16 | 409242.04 | 3.82 | skipped_fast |
| PYTHUSDT | IDLE | 1.3 | 5.51 | 0.47 | 0.14 | 358628.33 | 4.51 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 5.84 | 4.96 | 0.12 | 237928.93 | 6.99 | skipped_fast |
| WUSDT | IDLE | 1.49 | 3.5 | 0.05 | 0.09 | 300652.3 | 11.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.68 | 11.04 | 7.89 | 0.11 | 69041.59 | 44.52 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 4.84 | 0.41 | 0.16 | 239043.18 | 18.54 | skipped_fast |
| HBARUSDT | IDLE | 1.52 | 3.0 | 0.3 | 0.07 | 407965.33 | 1.38 | skipped_fast |
| QAITUSDT | IDLE | 2.02 | 5.78 | 3.83 | 0.01 | 10357.01 | 65.65 | skipped_fast |
| KITEUSDT | IDLE | 0.85 | 1.69 | 0.08 | 0.07 | 60424.78 | 13.41 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 4.3 | 1.74 | 0.21 | 102792.4 | 33.24 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 4.25 | 0.0 | 0.09 | 40052.63 | 6.51 | skipped_fast |
| FLUIDUSDT | IDLE | 2.07 | 5.66 | 0.65 | 0.1 | 2871.92 | 22.17 | skipped_fast |
| TELUSDT | IDLE | 0.74 | 3.56 | 0.54 | 0.14 | 197211.65 | 66.57 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.88 | 0.56 | 0.06 | 17324.42 | 112.8 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.69 | 0.43 | 0.02 | 52700.45 | 8.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
