# Hulk DIGEST — 2026-08-26T00:52:53Z

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
| PYTHUSDT | IDLE | 2.87 | 5.77 | 2.71 | -0.01 | 2195262.1 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 2.18 | 5.12 | 2.99 | -0.05 | 72853476.58 | 2.09 | skipped_fast |
| CCUSDT | IDLE | 1.75 | 3.62 | 1.36 | -0.04 | 535570.21 | 5.84 | skipped_fast |
| HBARUSDT | IDLE | 1.75 | 3.52 | 2.74 | -0.03 | 768228.62 | 1.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.84 | 5.18 | 2.65 | -0.02 | 414562.63 | 9.49 | skipped_fast |
| WUSDT | IDLE | 2.31 | 4.36 | 2.14 | -0.05 | 318301.35 | 7.47 | skipped_fast |
| BIOUSDT | IDLE | 2.63 | 5.06 | 1.35 | -0.02 | 109935.13 | 6.83 | skipped_fast |
| EDELUSDT | IDLE | 1.12 | 15.92 | 13.2 | -0.03 | 164856.83 | 26.19 | skipped_fast |
| ZBCNUSDT | IDLE | 2.26 | 4.02 | 3.39 | -0.01 | 172116.75 | 22.37 | skipped_fast |
| RIZEUSDT | IDLE | 2.64 | 5.62 | 1.65 | 0.04 | 51112.51 | 22.29 | skipped_fast |
| REDUSDT | IDLE | 2.14 | 5.55 | 1.91 | 0.01 | 81690.57 | 9.48 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 3.71 | 0.86 | -0.03 | 61440.86 | 9.78 | skipped_fast |
| QAITUSDT | IDLE | 2.07 | 5.67 | 0.85 | 0.04 | 12802.86 | 59.59 | skipped_fast |
| FLUIDUSDT | IDLE | 2.13 | 3.96 | 2.03 | -0.03 | 439.34 | 22.09 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.13 | 1.26 | -0.02 | 136216.99 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 2.03 | 1.84 | -0.02 | 2424.02 | 101.01 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.13 | 0.66 | -0.03 | 91687.4 | 33.11 | skipped_fast |
| RWAUSDT | IDLE | 0.93 | 1.65 | 1.38 | -0.03 | 56511.7 | 8.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
