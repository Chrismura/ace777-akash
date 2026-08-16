# Hulk DIGEST — 2026-08-16T19:04:24Z

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
| XRPUSDT | IDLE | 0.32 | 0.58 | 0.39 | -0.0 | 5477339.49 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 10.74 | 7.12 | 0.12 | 284824.76 | 13.88 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.74 | 2.02 | -0.03 | 347058.84 | 10.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 2.89 | 2.28 | -0.0 | 192887.77 | 12.15 | skipped_fast |
| WUSDT | IDLE | 1.41 | 2.46 | 2.38 | 0.01 | 170179.72 | 16.46 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 1.79 | 1.71 | -0.02 | 125853.61 | 2.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 3.52 | 1.22 | -0.0 | 35967.91 | 64.0 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.84 | 1.65 | -0.01 | 63346.13 | 4.09 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 2.4 | 0.91 | 0.01 | 59983.51 | 26.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.45 | 3.88 | 1.51 | 0.09 | 9820.04 | 73.72 | skipped_fast |
| KITEUSDT | IDLE | 0.52 | 0.9 | 0.87 | -0.03 | 56110.02 | 11.7 | skipped_fast |
| QAITUSDT | IDLE | 0.99 | 3.07 | 0.96 | -0.04 | 2632.88 | 61.66 | skipped_fast |
| REDUSDT | IDLE | 0.16 | 1.36 | 1.12 | -0.05 | 88713.36 | 16.08 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 1.81 | 0.55 | -0.03 | 94073.71 | 34.42 | skipped_fast |
| QNTUSDT | IDLE | 0.49 | 0.89 | 0.59 | -0.01 | 32628.45 | 3.5 | skipped_fast |
| HBARUSDT | IDLE | 0.29 | 0.51 | 0.43 | -0.01 | 75365.88 | 1.53 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.61 | 0.09 | -0.0 | 52508.98 | 17.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.49 | 0.92 | 0.4 | 0.02 | 219.43 | 21.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
