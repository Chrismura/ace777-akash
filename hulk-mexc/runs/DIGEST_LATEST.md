# Hulk DIGEST — 2026-08-22T12:39:18Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.05 | 0.11 | 216438988.59 | 2.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 7.83 | 1.55 | 0.04 | 51600836.69 | 11.84 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.22 | 0.02 | 1259749.62 | 5.14 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.7 | 0.15 | 778871.62 | 10.02 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.68 | 0.0 | 576781.86 | 10.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.23 | 5.77 | 4.14 | -0.01 | 335479.91 | 20.07 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.78 | -0.1 | 603790.54 | 6.72 | skipped_fast |
| KITEUSDT | IDLE | 2.69 | 6.37 | 0.88 | 0.03 | 84469.52 | 0.88 | skipped_fast |
| EDELUSDT | IDLE | 2.09 | 3.89 | 1.98 | -0.02 | 78154.75 | 33.84 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.61 | -0.03 | 237970.09 | 3.23 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2406.2 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.48 | 0.0 | 153350.6 | 14.29 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.83 | -0.03 | 163496.1 | 42.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.68 | -0.0 | 187760.96 | 6.23 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.19 | -0.0 | 46768.79 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57855.87 | 8.14 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.02 | 5705.21 | 22.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
