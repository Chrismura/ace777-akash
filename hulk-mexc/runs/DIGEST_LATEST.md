# Hulk DIGEST — 2026-08-22T15:26:36Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.65 | 0.04 | 51499120.67 | 3.96 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.71 | 0.02 | 214886339.74 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 5.65 | 3.4 | 0.09 | 796630.05 | 5.18 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 3.03 | 2.85 | -0.02 | 1170881.84 | 6.57 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.69 | -0.09 | 606672.5 | 3.41 | skipped_fast |
| KITEUSDT | IDLE | 2.8 | 6.37 | 2.76 | 0.02 | 85192.72 | 6.32 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 2.04 | -0.03 | 554354.94 | 12.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 3.49 | 2.39 | -0.06 | 324474.1 | 25.33 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.85 | -0.07 | 221633.14 | 3.31 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.08 | -0.06 | 147942.43 | 9.22 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.05 | 79127.41 | 34.23 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.44 | 0.03 | 56431.73 | 23.62 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.24 | -0.02 | 188323.56 | 6.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9839.83 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.63 | -0.01 | 140345.55 | 42.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.75 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.57 | 0.02 | 57263.64 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
