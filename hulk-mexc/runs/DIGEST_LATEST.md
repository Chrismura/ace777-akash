# Hulk DIGEST — 2026-08-16T13:05:10Z

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
| XRPUSDT | IDLE | 0.29 | 0.54 | 0.21 | -0.0 | 4881516.92 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.32 | 15.73 | 10.06 | 0.19 | 217466.35 | 17.53 | skipped_fast |
| QAITUSDT | IDLE | 3.22 | 10.06 | 2.38 | -0.04 | 1743.47 | 54.37 | skipped_fast |
| WUSDT | IDLE | 1.91 | 3.73 | 0.54 | 0.02 | 129211.35 | 11.62 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 2.0 | 0.47 | 0.02 | 319727.64 | 8.29 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 4.27 | 2.34 | -0.04 | 38588.48 | 22.15 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 4.26 | 0.13 | 0.01 | 67339.02 | 39.66 | skipped_fast |
| ZBCNUSDT | IDLE | 0.39 | 0.74 | 0.28 | -0.02 | 211506.13 | 12.2 | skipped_fast |
| BIOUSDT | IDLE | 0.62 | 1.22 | 0.2 | 0.0 | 66326.37 | 4.03 | skipped_fast |
| PYTHUSDT | IDLE | 0.42 | 0.77 | 0.46 | -0.02 | 98615.34 | 5.09 | skipped_fast |
| KITEUSDT | IDLE | 0.48 | 0.9 | 0.39 | -0.03 | 57750.75 | 11.65 | skipped_fast |
| REDUSDT | IDLE | 0.21 | 1.79 | 0.96 | 0.0 | 89784.76 | 17.07 | skipped_fast |
| TELUSDT | IDLE | 1.46 | 2.73 | 1.23 | -0.02 | 96275.72 | 27.64 | skipped_fast |
| RWAINCUSDT | IDLE | 0.24 | 0.67 | 0.22 | 0.1 | 8827.27 | 83.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.74 | 0.0 | 0.04 | 122.34 | 22.38 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.53 | 0.35 | -0.01 | 52013.88 | 8.76 | skipped_fast |
| HBARUSDT | IDLE | 0.12 | 0.22 | 0.11 | -0.01 | 77910.59 | 1.54 | skipped_fast |
| QNTUSDT | IDLE | 0.26 | 0.49 | 0.24 | -0.01 | 32038.03 | 8.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
