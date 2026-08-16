# Hulk DIGEST — 2026-08-16T12:04:59Z

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
| XRPUSDT | IDLE | 0.29 | 0.54 | 0.26 | -0.0 | 4948084.42 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 16.8 | 5.68 | 0.25 | 203195.64 | 23.41 | skipped_fast |
| QAITUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.17 | 10.06 | 1.38 | -0.04 | 1783.12 | 60.93 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.36 | 0.95 | 0.01 | 314662.74 | 5.19 | skipped_fast |
| WUSDT | IDLE | 2.05 | 4.1 | 0.03 | 0.03 | 122537.03 | 12.74 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 4.27 | 3.19 | -0.05 | 39206.19 | 48.72 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 3.98 | 1.06 | -0.01 | 67304.36 | 53.26 | skipped_fast |
| ZBCNUSDT | IDLE | 0.38 | 0.73 | 0.24 | -0.01 | 217169.22 | 19.9 | skipped_fast |
| BIOUSDT | IDLE | 0.66 | 1.26 | 0.4 | -0.01 | 66266.76 | 8.08 | skipped_fast |
| PYTHUSDT | IDLE | 0.45 | 0.84 | 0.43 | -0.02 | 90801.83 | 2.54 | skipped_fast |
| KITEUSDT | IDLE | 0.61 | 1.13 | 0.66 | -0.03 | 57895.09 | 14.84 | skipped_fast |
| REDUSDT | IDLE | 0.28 | 2.31 | 1.8 | 0.0 | 92742.09 | 24.0 | skipped_fast |
| RWAINCUSDT | IDLE | 0.36 | 0.95 | 0.67 | 0.09 | 8587.81 | 44.72 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.08 | 2.04 | -0.04 | 90755.28 | 41.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.74 | 0.0 | 0.04 | 122.34 | 22.64 | skipped_fast |
| QNTUSDT | IDLE | 0.45 | 0.86 | 0.28 | -0.02 | 31943.25 | 5.22 | skipped_fast |
| HBARUSDT | IDLE | 0.12 | 0.22 | 0.12 | -0.01 | 76997.0 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.53 | 0.17 | -0.01 | 52367.68 | 17.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
