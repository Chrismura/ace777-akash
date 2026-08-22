# Hulk DIGEST — 2026-08-22T12:21:28Z

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
| PYTHUSDT | IDLE | 1.68 | 7.83 | 3.17 | 0.04 | 51609574.17 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.46 | 14.26 | 6.1 | 0.12 | 215597788.16 | 5.89 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 4.63 | 1.72 | 0.03 | 1260130.73 | 6.39 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 8.38 | 3.27 | 0.14 | 774586.44 | 10.09 | skipped_fast |
| WUSDT | IDLE | 1.53 | 6.27 | 3.12 | 0.02 | 578517.35 | 13.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 5.77 | 3.86 | -0.03 | 370961.15 | 23.55 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 0.86 | -0.1 | 612246.2 | 3.33 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.32 | 0.04 | 83340.78 | 2.64 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 3.89 | 2.65 | -0.02 | 78154.0 | 56.47 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 5.65 | 1.01 | -0.02 | 240908.04 | 6.36 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.24 | 0.03 | 153121.21 | 11.41 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.88 | -0.03 | 164378.66 | 47.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10190.25 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 3.47 | 0.8 | 0.01 | 187889.96 | 4.63 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.27 | -0.04 | 48018.52 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57733.36 | 16.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 19.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
