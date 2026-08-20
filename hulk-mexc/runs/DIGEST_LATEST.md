# Hulk DIGEST — 2026-08-20T19:27:46Z

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
| XRPUSDT | IDLE | 1.83 | 10.64 | 8.11 | 0.16 | 104623032.21 | 0.81 | skipped_fast |
| PYTHUSDT | IDLE | 1.17 | 2.65 | 0.99 | 0.09 | 1310519.09 | 2.27 | skipped_fast |
| ZBCNUSDT | IDLE | 4.19 | 12.78 | 4.17 | 0.07 | 283730.69 | 23.42 | skipped_fast |
| CCUSDT | IDLE | 2.4 | 4.21 | 3.92 | 0.02 | 488190.14 | 10.96 | skipped_fast |
| CHIPUSDT | IDLE | 2.42 | 6.82 | 5.55 | 0.05 | 292005.37 | 10.21 | skipped_fast |
| HBARUSDT | IDLE | 2.14 | 3.82 | 3.02 | 0.04 | 507994.89 | 1.39 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.08 | 1.25 | 0.06 | 314653.33 | 12.3 | skipped_fast |
| TELUSDT | IDLE | 2.25 | 13.63 | 6.74 | 0.16 | 190548.69 | 27.39 | skipped_fast |
| KITEUSDT | IDLE | 2.12 | 3.89 | 2.35 | 0.01 | 64572.1 | 15.39 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 4.08 | 3.16 | 0.02 | 6955.74 | 22.46 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 4.64 | 0.63 | 0.13 | 235122.76 | 3.19 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 4.44 | 2.92 | 0.12 | 185362.72 | 12.43 | skipped_fast |
| EDELUSDT | IDLE | 1.14 | 5.19 | 0.32 | 0.07 | 93604.01 | 21.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.13 | 5.87 | 3.92 | 0.07 | 50208.07 | 48.33 | skipped_fast |
| QAITUSDT | IDLE | 1.69 | 3.24 | 0.88 | 0.0 | 5271.64 | 65.85 | skipped_fast |
| QNTUSDT | IDLE | 1.89 | 4.04 | 3.68 | 0.06 | 65001.39 | 3.25 | skipped_fast |
| RWAUSDT | IDLE | 0.99 | 1.83 | 0.94 | 0.01 | 54131.67 | 17.24 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.55 | 0.0 | 0.09 | 1810.99 | 22.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
