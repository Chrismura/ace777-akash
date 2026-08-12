# Hulk DIGEST — 2026-08-13T01:37:45Z

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
| XRPUSDT | IDLE | 0.54 | 0.99 | 0.61 | -0.02 | 14517462.81 | 1.99 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 20.64 | 15.99 | 0.06 | 83920.83 | 33.33 | skipped_fast |
| RIZEUSDT | IDLE | 2.26 | 18.83 | 5.99 | 0.24 | 56608.45 | 32.68 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.11 | 0.47 | -0.04 | 332587.38 | 4.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.71 | 3.05 | 2.52 | -0.06 | 174338.5 | 17.44 | skipped_fast |
| RWAINCUSDT | IDLE | 2.55 | 4.58 | 3.43 | -0.03 | 2062.5 | 32.82 | skipped_fast |
| QNTUSDT | IDLE | 3.12 | 5.57 | 4.52 | 0.01 | 61110.1 | 5.15 | skipped_fast |
| WUSDT | IDLE | 1.37 | 2.66 | 0.48 | -0.04 | 173813.55 | 12.34 | skipped_fast |
| BIOUSDT | IDLE | 1.74 | 3.22 | 1.76 | -0.05 | 61482.76 | 4.17 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 2.23 | 0.09 | -0.0 | 214231.97 | 10.94 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 2.99 | 0.77 | 0.03 | 105265.12 | 8.59 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.1 | 1.83 | -0.02 | 60020.79 | 11.9 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 1.94 | 1.6 | -0.05 | 54574.86 | 13.87 | skipped_fast |
| QAITUSDT | IDLE | 0.77 | 2.51 | 1.67 | -0.04 | 4081.32 | 60.51 | skipped_fast |
| HBARUSDT | IDLE | 0.38 | 0.72 | 0.29 | -0.01 | 82967.68 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 0.5 | 0.96 | 0.32 | -0.0 | 93077.84 | 50.6 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.25 | 0.01 | 52580.7 | 16.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 0.64 | 0.29 | -0.02 | 569.18 | 16.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
