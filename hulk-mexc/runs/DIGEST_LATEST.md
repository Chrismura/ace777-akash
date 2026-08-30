# Hulk DIGEST — 2026-08-30T09:13:32Z

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
| XRPUSDT | IDLE | 0.67 | 1.21 | 0.89 | 0.01 | 15863973.91 | 2.16 | skipped_fast |
| CHIPUSDT | IDLE | 2.47 | 4.43 | 3.4 | -0.04 | 659781.59 | 2.51 | skipped_fast |
| ZBCNUSDT | IDLE | 2.04 | 3.86 | 1.46 | -0.01 | 168232.47 | 12.86 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 2.0 | 1.42 | 0.05 | 295962.08 | 5.89 | skipped_fast |
| PYTHUSDT | IDLE | 0.79 | 1.48 | 0.71 | 0.02 | 308181.87 | 2.11 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 2.99 | 2.6 | -0.01 | 75152.84 | 10.11 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.59 | 1.26 | -0.01 | 67487.53 | 3.66 | skipped_fast |
| WUSDT | IDLE | 0.79 | 1.43 | 0.97 | 0.01 | 196819.16 | 11.99 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 1.89 | 1.17 | 0.01 | 70442.82 | 10.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.47 | 1.83 | -0.05 | 45496.13 | 59.09 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.59 | 1.57 | -0.03 | 1551.94 | 56.59 | skipped_fast |
| EDELUSDT | IDLE | 0.26 | 5.09 | 0.25 | 0.15 | 123011.35 | 84.03 | skipped_fast |
| HBARUSDT | IDLE | 0.56 | 1.08 | 0.31 | 0.0 | 143730.92 | 1.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 2.3 | 0.07 | 0.03 | 2963.27 | 21.82 | skipped_fast |
| TELUSDT | IDLE | 0.66 | 1.19 | 0.82 | -0.03 | 74141.93 | 11.88 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.32 | 0.24 | 0.01 | 52650.48 | 8.17 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.93 | 0.62 | 0.01 | 36836.55 | 4.88 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
