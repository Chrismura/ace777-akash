# Hulk DIGEST — 2026-08-22T12:52:40Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.37 | 0.09 | 215987062.97 | 1.99 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 7.83 | 1.5 | 0.04 | 51593401.54 | 1.97 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.39 | 0.01 | 1252442.91 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.2 | 0.13 | 775454.84 | 4.24 | skipped_fast |
| WUSDT | IDLE | 1.57 | 6.27 | 4.03 | -0.0 | 572178.74 | 13.81 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.57 | -0.01 | 335163.8 | 16.39 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.28 | -0.1 | 605925.18 | 3.38 | skipped_fast |
| KITEUSDT | IDLE | 2.69 | 6.37 | 0.89 | 0.04 | 84819.19 | 10.62 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.86 | -0.05 | 238192.2 | 3.24 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 3.89 | 2.87 | -0.03 | 78225.98 | 56.59 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2384.58 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.6 | 0.02 | 152643.63 | 19.62 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.61 | 3.32 | -0.02 | 163207.13 | 100.4 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.52 | -0.01 | 187585.91 | 6.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 2.03 | 0.34 | 0.0 | 46773.42 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.12 | 0.02 | 57463.36 | 16.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.04 | 5072.55 | 23.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
