# Hulk DIGEST — 2026-08-12T20:07:57Z

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
| XRPUSDT | IDLE | 0.35 | 0.64 | 0.41 | -0.01 | 15561409.08 | 1.98 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 27.36 | 15.44 | 0.13 | 46250.92 | 47.27 | skipped_fast |
| CHIPUSDT | IDLE | 2.87 | 6.56 | 3.84 | 0.05 | 105800.1 | 4.3 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 2.99 | 2.19 | -0.05 | 325173.96 | 7.47 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 8.52 | 5.49 | 0.07 | 68640.43 | 49.71 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 2.15 | 1.43 | -0.02 | 223526.74 | 9.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 2.03 | 1.38 | -0.02 | 194650.16 | 16.42 | skipped_fast |
| REDUSDT | IDLE | 1.63 | 2.9 | 2.34 | -0.01 | 60335.04 | 15.27 | skipped_fast |
| RWAINCUSDT | IDLE | 2.12 | 4.03 | 1.36 | -0.01 | 1707.38 | 52.88 | skipped_fast |
| WUSDT | IDLE | 0.81 | 1.49 | 0.81 | -0.02 | 176842.26 | 11.07 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.9 | 1.42 | -0.03 | 63456.16 | 4.11 | skipped_fast |
| KITEUSDT | IDLE | 1.04 | 2.06 | 0.09 | -0.04 | 60057.91 | 10.86 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 2.77 | 1.99 | 0.01 | 61704.4 | 8.55 | skipped_fast |
| QAITUSDT | IDLE | 0.71 | 2.54 | 2.48 | -0.04 | 4591.18 | 60.7 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 1.8 | 1.01 | 0.03 | 100838.21 | 31.82 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.25 | 0.66 | 0.02 | 51728.53 | 16.61 | skipped_fast |
| HBARUSDT | IDLE | 0.41 | 0.76 | 0.35 | -0.01 | 76754.3 | 1.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.21 | 0.37 | 0.29 | -0.02 | 542.31 | 22.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
