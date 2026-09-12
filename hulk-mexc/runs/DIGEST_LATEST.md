# Hulk DIGEST — 2026-09-12T08:22:32Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.33 | 0.78 | 0.01 | 0.02 | 615419967.07 | 0.24 | skipped_fast |
| XRPUSDT | IDLE | 0.3 | 0.63 | 0.16 | 0.01 | 51445132.51 | 1.46 | skipped_fast |
| BTCUSDT | IDLE | 0.12 | 0.23 | 0.04 | 0.0 | 563471547.85 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.04 | 2.09 | 0.51 | 0.02 | 420158.0 | 1.91 | skipped_fast |
| CCUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.0 | 396417.54 | 8.08 | skipped_fast |
| REDUSDT | IDLE | 1.64 | 4.1 | 3.37 | 0.05 | 64521.07 | 18.87 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 2.99 | 2.09 | -0.02 | 59871.48 | 10.37 | skipped_fast |
| EDELUSDT | IDLE | 0.93 | 2.5 | 1.92 | 0.07 | 166703.9 | 17.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.93 | 3.83 | 1.9 | 0.0 | 15715.66 | 55.04 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.5 | 0.33 | -0.01 | 195942.61 | 16.63 | skipped_fast |
| WUSDT | IDLE | 0.65 | 1.31 | 0.4 | 0.02 | 199962.2 | 14.25 | skipped_fast |
| CHIPUSDT | IDLE | 0.92 | 2.77 | 0.06 | 0.06 | 90449.01 | 16.57 | skipped_fast |
| BIOUSDT | IDLE | 0.64 | 1.23 | 0.35 | 0.02 | 80061.4 | 3.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.11 | 7.74 | 2.87 | 0.87 | 185363.28 | 126.12 | skipped_fast |
| HBARUSDT | IDLE | 0.42 | 0.82 | 0.12 | 0.0 | 252880.14 | 2.68 | skipped_fast |
| TELUSDT | IDLE | 0.7 | 1.73 | 0.76 | -0.03 | 98659.51 | 29.54 | skipped_fast |
| QNTUSDT | IDLE | 0.47 | 0.83 | 0.7 | -0.01 | 44986.1 | 4.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.12 | 0.89 | -0.0 | 27225.44 | 37.78 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.59 | 0.07 | 0.03 | 53458.77 | 14.79 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.03 | 1625.5 | 22.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
