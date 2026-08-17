# Hulk DIGEST — 2026-08-17T06:10:54Z

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
| XRPUSDT | IDLE | 0.6 | 1.18 | 0.2 | 0.0 | 8893951.34 | 1.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.35 | 25.44 | 16.36 | 0.08 | 45065.12 | 56.39 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 8.67 | 0.94 | 0.08 | 307861.46 | 3.39 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.57 | 1.27 | -0.01 | 276042.42 | 5.26 | skipped_fast |
| WUSDT | IDLE | 1.22 | 2.14 | 1.97 | 0.02 | 189270.6 | 15.34 | skipped_fast |
| REDUSDT | IDLE | 1.78 | 3.13 | 2.87 | -0.05 | 58574.43 | 18.99 | skipped_fast |
| PYTHUSDT | IDLE | 0.94 | 1.84 | 0.31 | -0.0 | 162298.27 | 2.56 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 2.54 | 1.81 | -0.0 | 54418.23 | 13.84 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 3.17 | 1.15 | 0.04 | 55375.58 | 64.56 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.25 | 0.04 | 0.0 | 62976.04 | 4.07 | skipped_fast |
| ZBCNUSDT | IDLE | 0.56 | 1.03 | 0.58 | 0.0 | 198897.22 | 15.29 | skipped_fast |
| QAITUSDT | IDLE | 1.08 | 2.41 | 2.0 | -0.03 | 2151.91 | 61.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.58 | 1.02 | 0.9 | -0.01 | 2325.58 | 51.06 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 1.53 | 1.08 | -0.02 | 34017.3 | 7.17 | skipped_fast |
| TELUSDT | IDLE | 0.78 | 1.44 | 0.81 | -0.0 | 87023.17 | 34.09 | skipped_fast |
| HBARUSDT | IDLE | 0.39 | 0.74 | 0.22 | -0.0 | 89883.72 | 1.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.89 | 1.69 | 0.65 | 0.02 | 426.99 | 22.53 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.05 | 0.09 | 0.01 | 49672.46 | 17.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
