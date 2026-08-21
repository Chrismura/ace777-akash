# Hulk DIGEST — 2026-08-21T21:20:22Z

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
| PYTHUSDT | IDLE | 1.19 | 4.51 | 1.01 | 0.09 | 5615375.68 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 2.12 | 0.1 | 128764330.2 | 1.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.92 | 5.61 | 4.53 | 0.06 | 515699.27 | 6.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.17 | 0.1 | 484279.06 | 31.81 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.43 | 0.1 | 645140.42 | 3.69 | skipped_fast |
| HBARUSDT | IDLE | 1.58 | 3.04 | 0.83 | 0.07 | 809423.58 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.97 | 3.83 | 0.69 | 0.06 | 366555.77 | 10.47 | skipped_fast |
| BIOUSDT | IDLE | 2.45 | 5.2 | 2.4 | 0.0 | 187216.9 | 6.29 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.47 | 0.16 | 153616.35 | 10.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.32 | 0.02 | 56199.26 | 7.03 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 10.75 | skipped_fast |
| QAITUSDT | IDLE | 2.5 | 4.38 | 4.2 | -0.04 | 3753.25 | 103.88 | skipped_fast |
| EDELUSDT | IDLE | 2.05 | 4.12 | 2.75 | -0.05 | 82616.67 | 90.09 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.13 | 0.11 | 61033.04 | 12.99 | skipped_fast |
| TELUSDT | IDLE | 1.36 | 3.39 | 1.06 | 0.01 | 179561.41 | 5.34 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.69 | 0.03 | 60547.15 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.17 | 0.74 | 0.03 | 53794.89 | 33.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 21.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
