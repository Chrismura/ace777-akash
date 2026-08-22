# Hulk DIGEST — 2026-08-22T00:06:25Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.69 | 0.1 | 6263359.38 | 4.1 | skipped_fast |
| XRPUSDT | IDLE | 2.05 | 8.23 | 2.31 | 0.15 | 142661772.35 | 5.55 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.72 | 0.08 | 912059.03 | 3.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.97 | 0.12 | 515205.64 | 30.16 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 7.42 | 0.48 | 0.13 | 644797.84 | 7.96 | skipped_fast |
| WUSDT | IDLE | 2.76 | 6.91 | 1.49 | 0.08 | 379462.17 | 8.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.25 | 0.04 | 543243.14 | 6.16 | skipped_fast |
| BIOUSDT | IDLE | 2.34 | 5.04 | 1.85 | 0.02 | 187304.63 | 3.14 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.41 | -0.01 | 80059.73 | 44.05 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 9.82 | 3.54 | 0.13 | 59036.34 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.51 | 0.06 | 189914.58 | 10.28 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.42 | 0.72 | 0.07 | 166717.76 | 1.5 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 4.91 | 2.8 | 0.17 | 157743.27 | 20.26 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.16 | 0.09 | 61507.07 | 12.98 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54574.33 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 22.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
