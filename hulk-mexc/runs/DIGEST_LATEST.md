# Hulk DIGEST — 2026-08-19T01:10:55Z

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
| XRPUSDT | IDLE | 0.36 | 0.66 | 0.44 | -0.0 | 11404677.61 | 1.0 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 7.66 | 5.72 | 0.04 | 164283.26 | 23.06 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.85 | 0.67 | -0.03 | 186685.67 | 3.74 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 1.99 | 0.8 | 0.01 | 220608.62 | 8.79 | skipped_fast |
| PYTHUSDT | IDLE | 0.92 | 1.68 | 1.08 | -0.0 | 185765.78 | 2.61 | skipped_fast |
| ZBCNUSDT | IDLE | 0.63 | 1.24 | 0.12 | -0.0 | 149432.19 | 17.77 | skipped_fast |
| WUSDT | IDLE | 0.48 | 0.93 | 0.14 | -0.01 | 131407.29 | 11.12 | skipped_fast |
| RWAINCUSDT | IDLE | 0.92 | 1.92 | 0.82 | -0.02 | 10609.38 | 11.85 | skipped_fast |
| BIOUSDT | IDLE | 0.52 | 1.02 | 0.08 | 0.0 | 64613.34 | 4.05 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 1.73 | 1.48 | -0.04 | 29815.34 | 48.87 | skipped_fast |
| KITEUSDT | IDLE | 0.4 | 0.76 | 0.29 | -0.0 | 65528.0 | 12.0 | skipped_fast |
| EDELUSDT | IDLE | 0.74 | 2.16 | 1.59 | -0.03 | 74178.57 | 94.02 | skipped_fast |
| QAITUSDT | IDLE | 0.36 | 3.05 | 0.9 | -0.16 | 16107.73 | 39.28 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.83 | 0.0 | 0.02 | 121115.09 | 2.97 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.09 | 0.82 | 0.04 | 88084.68 | 20.68 | skipped_fast |
| QNTUSDT | IDLE | 0.32 | 0.61 | 0.25 | -0.02 | 38686.21 | 8.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.45 | 0.79 | 0.77 | -0.01 | 204.36 | 21.96 | skipped_fast |
| RWAUSDT | IDLE | 0.14 | 0.26 | 0.17 | -0.01 | 51497.01 | 17.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
