# Hulk DIGEST — 2026-08-22T12:36:36Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.3 | 0.11 | 216354377.91 | 2.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 7.83 | 2.21 | 0.04 | 51606130.33 | 1.99 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.41 | 0.02 | 1260580.19 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.63 | 0.15 | 779156.83 | 5.85 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.7 | 0.01 | 577536.27 | 11.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 5.77 | 4.05 | -0.01 | 335405.27 | 23.18 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.85 | -0.1 | 603767.39 | 6.72 | skipped_fast |
| KITEUSDT | IDLE | 2.69 | 6.37 | 0.86 | 0.03 | 84437.18 | 0.88 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 3.89 | 2.21 | -0.02 | 78154.7 | 11.28 | skipped_fast |
| BIOUSDT | IDLE | 0.8 | 5.65 | 2.36 | -0.03 | 238325.09 | 3.22 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.16 | 2.56 | -0.01 | 2404.2 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.35 | 0.0 | 153059.63 | 11.57 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.88 | -0.03 | 163486.01 | 37.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.7 | -0.0 | 188087.59 | 4.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.15 | -0.0 | 46795.44 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.04 | 0.02 | 57829.54 | 8.11 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.02 | 5705.21 | 23.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
