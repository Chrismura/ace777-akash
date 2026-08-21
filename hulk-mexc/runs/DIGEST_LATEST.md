# Hulk DIGEST — 2026-08-21T21:21:06Z

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
| PYTHUSDT | IDLE | 1.19 | 4.51 | 1.07 | 0.09 | 5615952.39 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.16 | 3.73 | 2.18 | 0.1 | 128697327.59 | 2.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.09 | 0.1 | 484455.64 | 11.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.92 | 5.61 | 4.68 | 0.06 | 515658.19 | 9.39 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.4 | 0.1 | 645098.91 | 6.45 | skipped_fast |
| HBARUSDT | IDLE | 1.59 | 3.04 | 0.92 | 0.07 | 809408.32 | 3.87 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.83 | 0.59 | 0.06 | 366544.41 | 9.42 | skipped_fast |
| BIOUSDT | IDLE | 2.45 | 5.2 | 2.43 | 0.0 | 187159.63 | 3.15 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.66 | 0.16 | 153609.02 | 9.04 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 10.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.41 | 0.01 | 56204.28 | 45.77 | skipped_fast |
| QAITUSDT | IDLE | 2.5 | 4.38 | 4.2 | -0.04 | 3753.25 | 95.92 | skipped_fast |
| EDELUSDT | IDLE | 2.05 | 4.12 | 2.75 | -0.05 | 82591.56 | 90.09 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.06 | 0.11 | 61021.3 | 12.98 | skipped_fast |
| TELUSDT | IDLE | 1.36 | 3.39 | 0.9 | 0.02 | 179588.66 | 5.34 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60551.97 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.17 | 0.99 | 0.03 | 53823.44 | 41.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 21.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
