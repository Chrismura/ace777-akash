# Hulk DIGEST — 2026-08-20T22:28:02Z

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
| XRPUSDT | IDLE | 1.87 | 10.14 | 6.0 | 0.12 | 102446397.5 | 1.58 | skipped_fast |
| PYTHUSDT | IDLE | 1.34 | 2.51 | 1.19 | 0.05 | 1361338.59 | 2.27 | skipped_fast |
| CCUSDT | IDLE | 2.45 | 4.38 | 3.53 | -0.01 | 479398.22 | 8.07 | skipped_fast |
| ZBCNUSDT | IDLE | 2.71 | 8.01 | 4.52 | 0.02 | 273233.13 | 1.09 | skipped_fast |
| CHIPUSDT | IDLE | 2.05 | 6.48 | 0.03 | 0.11 | 292553.76 | 6.45 | skipped_fast |
| HBARUSDT | IDLE | 2.04 | 3.82 | 1.71 | 0.03 | 470325.72 | 1.37 | skipped_fast |
| RWAINCUSDT | IDLE | 2.15 | 4.08 | 1.52 | 0.02 | 7460.21 | 11.03 | skipped_fast |
| WUSDT | IDLE | 1.07 | 2.05 | 0.55 | 0.05 | 260559.15 | 13.34 | skipped_fast |
| QAITUSDT | IDLE | 2.51 | 6.4 | 1.2 | -0.0 | 6010.2 | 66.45 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 4.51 | 0.98 | 0.14 | 235085.4 | 3.19 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 3.0 | 1.91 | 0.02 | 62890.46 | 16.35 | skipped_fast |
| EDELUSDT | IDLE | 1.13 | 3.28 | 0.42 | 0.04 | 88396.43 | 31.9 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 8.29 | 6.43 | 0.14 | 181811.43 | 54.59 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 4.47 | 3.8 | 0.02 | 48599.67 | 23.93 | skipped_fast |
| REDUSDT | IDLE | 0.33 | 2.17 | 1.22 | 0.09 | 186893.41 | 10.53 | skipped_fast |
| RWAUSDT | IDLE | 1.14 | 2.26 | 0.09 | 0.01 | 54861.62 | 17.02 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 1.71 | 0.08 | 0.07 | 64459.27 | 6.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.07 | 0.94 | 0.03 | 1933.85 | 20.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
