# Hulk DIGEST — 2026-08-22T15:53:36Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.79 | 0.04 | 51487985.79 | 5.94 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.14 | 0.02 | 216020701.59 | 4.18 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 5.65 | 2.24 | 0.09 | 759021.58 | 5.12 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.45 | -0.02 | 1152828.58 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 0.61 | 3.51 | 1.66 | -0.09 | 603608.57 | 3.38 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 1.93 | -0.03 | 554106.55 | 12.85 | skipped_fast |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.69 | 0.03 | 85538.86 | 10.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.88 | -0.05 | 320425.2 | 20.55 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.14 | -0.07 | 219357.76 | 3.33 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.52 | 2.23 | -0.02 | 75064.08 | 11.4 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.52 | -0.16 | 134284.26 | 11.93 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.22 | 0.03 | 56477.75 | 45.5 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.58 | -0.03 | 184222.85 | 4.75 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.0 | 9767.54 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 2.75 | 1.68 | 0.0 | 139048.13 | 42.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.73 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 56603.73 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
