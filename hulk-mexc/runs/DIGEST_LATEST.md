# Hulk DIGEST — 2026-08-16T22:16:24Z

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
| XRPUSDT | IDLE | 0.68 | 1.26 | 0.69 | -0.01 | 6465846.51 | 1.0 | skipped_fast |
| RIZEUSDT | IDLE | 3.68 | 7.8 | 2.26 | 0.02 | 38015.35 | 59.77 | skipped_fast |
| PYTHUSDT | IDLE | 2.11 | 3.77 | 2.98 | -0.03 | 147121.19 | 2.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 4.9 | 2.23 | 0.05 | 294365.54 | 3.46 | skipped_fast |
| WUSDT | IDLE | 1.71 | 3.24 | 1.19 | 0.01 | 182347.15 | 12.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 2.83 | 2.02 | -0.02 | 193690.17 | 33.75 | skipped_fast |
| BIOUSDT | IDLE | 1.81 | 3.21 | 2.75 | -0.03 | 67764.22 | 4.16 | skipped_fast |
| CCUSDT | IDLE | 0.64 | 1.2 | 1.17 | -0.04 | 332815.52 | 5.27 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.67 | 1.17 | 0.03 | 60526.38 | 65.49 | skipped_fast |
| KITEUSDT | IDLE | 0.86 | 1.5 | 1.41 | -0.03 | 56319.22 | 17.12 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 1.37 | 0.88 | -0.1 | 67097.39 | 14.99 | skipped_fast |
| QAITUSDT | IDLE | 1.25 | 3.83 | 0.0 | -0.01 | 2289.9 | 61.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 3.01 | 0.0 | 0.09 | 9973.17 | 73.38 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.09 | 1.78 | -0.03 | 94227.07 | 34.78 | skipped_fast |
| HBARUSDT | IDLE | 0.66 | 1.24 | 0.57 | -0.01 | 104467.47 | 1.54 | skipped_fast |
| QNTUSDT | IDLE | 0.91 | 1.63 | 1.33 | -0.02 | 33811.62 | 5.3 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.61 | 0.26 | 0.0 | 50789.87 | 17.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 0.62 | 0.11 | 0.02 | 219.43 | 21.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
