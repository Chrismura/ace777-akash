# Hulk DIGEST — 2026-08-22T15:20:41Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.67 | 0.04 | 51484820.73 | 3.96 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.11 | 0.02 | 214775321.89 | 2.09 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.9 | 0.1 | 798839.96 | 7.73 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 2.89 | 2.81 | -0.02 | 1167397.33 | 5.26 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.76 | -0.1 | 614013.75 | 6.83 | skipped_fast |
| WUSDT | IDLE | 0.8 | 3.17 | 2.2 | -0.03 | 555884.17 | 13.96 | skipped_fast |
| KITEUSDT | IDLE | 2.82 | 6.37 | 3.04 | 0.02 | 85165.1 | 9.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.33 | 3.49 | 2.09 | -0.07 | 327274.82 | 13.4 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 6.58 | 5.42 | -0.07 | 221614.01 | 3.33 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.62 | 5.24 | -0.05 | 150635.85 | 13.86 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.52 | 2.23 | -0.05 | 79102.41 | 34.23 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.45 | 0.03 | 46028.23 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.58 | -0.02 | 188382.47 | 4.75 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9873.12 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 2.75 | 1.47 | -0.01 | 139854.47 | 42.62 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 20.23 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.57 | 0.02 | 57273.92 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
