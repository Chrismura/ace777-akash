# Hulk DIGEST — 2026-08-16T12:18:27Z

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
| XRPUSDT | IDLE | 0.29 | 0.54 | 0.32 | -0.0 | 4926693.44 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.23 | 16.8 | 8.33 | 0.22 | 206214.42 | 20.44 | skipped_fast |
| QAITUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.17 | 10.06 | 1.38 | -0.04 | 1783.12 | 3.2 | skipped_fast |
| WUSDT | IDLE | 2.05 | 4.1 | 0.01 | 0.03 | 124843.22 | 13.9 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.36 | 0.93 | 0.02 | 313221.88 | 9.33 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 4.27 | 2.01 | -0.04 | 39212.21 | 72.52 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 4.12 | 0.66 | -0.0 | 67379.6 | 79.47 | skipped_fast |
| ZBCNUSDT | IDLE | 0.39 | 0.74 | 0.2 | -0.01 | 214214.77 | 11.54 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.26 | 0.64 | -0.01 | 66303.4 | 4.05 | skipped_fast |
| PYTHUSDT | IDLE | 0.45 | 0.84 | 0.43 | -0.02 | 91064.81 | 2.54 | skipped_fast |
| KITEUSDT | IDLE | 0.61 | 1.13 | 0.55 | -0.03 | 57904.79 | 11.65 | skipped_fast |
| REDUSDT | IDLE | 0.27 | 2.31 | 1.3 | 0.01 | 92563.03 | 14.78 | skipped_fast |
| TELUSDT | IDLE | 1.78 | 3.3 | 1.7 | -0.03 | 97413.24 | 48.26 | skipped_fast |
| RWAINCUSDT | IDLE | 0.36 | 0.95 | 0.67 | 0.09 | 8587.81 | 33.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.74 | 0.0 | 0.04 | 122.34 | 21.7 | skipped_fast |
| QNTUSDT | IDLE | 0.45 | 0.86 | 0.29 | -0.01 | 32094.22 | 3.48 | skipped_fast |
| HBARUSDT | IDLE | 0.13 | 0.22 | 0.21 | -0.01 | 77199.36 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.53 | 0.17 | -0.01 | 52206.1 | 17.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
