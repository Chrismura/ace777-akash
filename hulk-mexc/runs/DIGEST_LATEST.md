# Hulk DIGEST — 2026-08-22T16:10:18Z

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
| PYTHUSDT | IDLE | 1.52 | 7.24 | 2.02 | 0.04 | 51458820.29 | 3.97 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 7.64 | 5.42 | 0.04 | 215583317.39 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.15 | -0.01 | 1141769.65 | 3.92 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.49 | 0.09 | 764197.48 | 1.71 | skipped_fast |
| CHIPUSDT | IDLE | 0.58 | 3.36 | 1.26 | -0.09 | 627754.3 | 6.74 | skipped_fast |
| WUSDT | IDLE | 0.65 | 2.58 | 1.73 | -0.02 | 547363.88 | 10.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 1.9 | -0.04 | 318197.8 | 20.6 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.98 | -0.07 | 219071.35 | 13.32 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 4.35 | 1.35 | 0.04 | 85453.35 | 10.66 | skipped_fast |
| EDELUSDT | IDLE | 1.35 | 2.41 | 1.9 | -0.02 | 74668.59 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.16 | -0.13 | 135761.4 | 11.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.31 | 3.23 | 0.02 | 0.03 | 56523.81 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.28 | -0.02 | 183578.93 | 6.32 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.52 | -0.0 | 137305.75 | 48.04 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.06 | 0.49 | 0.02 | 56344.21 | 32.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.04 | 4625.53 | 20.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
