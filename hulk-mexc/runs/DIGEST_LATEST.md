# Hulk DIGEST — 2026-08-26T01:10:07Z

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
| PYTHUSDT | IDLE | 1.83 | 3.82 | 0.78 | -0.01 | 2185045.47 | 3.95 | skipped_fast |
| XRPUSDT | IDLE | 2.0 | 4.78 | 2.06 | -0.04 | 72235134.55 | 1.38 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 3.39 | 1.04 | -0.03 | 535806.51 | 9.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.82 | 5.18 | 2.19 | -0.02 | 408455.97 | 6.3 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 2.22 | 0.96 | -0.03 | 764788.33 | 2.56 | skipped_fast |
| WUSDT | IDLE | 1.53 | 3.03 | 0.54 | -0.04 | 314940.9 | 9.57 | skipped_fast |
| RIZEUSDT | IDLE | 2.61 | 5.51 | 1.9 | 0.04 | 51090.24 | 25.72 | skipped_fast |
| BIOUSDT | IDLE | 2.14 | 4.18 | 0.68 | -0.02 | 103135.92 | 10.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.58 | 2.8 | 2.37 | -0.01 | 168639.15 | 12.28 | skipped_fast |
| REDUSDT | IDLE | 1.89 | 5.04 | 0.78 | 0.02 | 81575.57 | 9.41 | skipped_fast |
| KITEUSDT | IDLE | 1.74 | 3.51 | 0.23 | -0.03 | 61402.99 | 13.27 | skipped_fast |
| QAITUSDT | IDLE | 1.96 | 5.43 | 0.3 | 0.04 | 12810.35 | 59.59 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 9.23 | 6.68 | -0.02 | 165144.53 | 77.42 | skipped_fast |
| FLUIDUSDT | IDLE | 2.13 | 3.96 | 2.03 | -0.03 | 439.34 | 44.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 2.03 | 1.84 | -0.02 | 2424.02 | 95.94 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.59 | 0.44 | -0.02 | 136169.01 | 1.57 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.13 | 0.66 | -0.03 | 91131.59 | 33.11 | skipped_fast |
| RWAUSDT | IDLE | 0.94 | 1.65 | 1.54 | -0.03 | 56187.66 | 8.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
