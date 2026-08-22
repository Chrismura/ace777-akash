# Hulk DIGEST — 2026-08-22T15:33:17Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.28 | 0.04 | 51502103.87 | 3.94 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.49 | 5.21 | 0.03 | 214962359.52 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 5.65 | 3.91 | 0.08 | 795885.22 | 8.67 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 3.03 | 2.59 | -0.02 | 1159208.64 | 5.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.39 | -0.09 | 604380.91 | 3.41 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.84 | -0.02 | 556381.59 | 13.91 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 6.37 | 1.91 | 0.03 | 85180.19 | 10.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.33 | 3.49 | 2.25 | -0.05 | 321246.13 | 26.29 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.88 | -0.07 | 221231.38 | 3.31 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.04 | 79000.98 | 22.78 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.94 | -0.07 | 147893.0 | 10.14 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.27 | 0.03 | 56483.33 | 23.62 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.25 | -0.02 | 185230.47 | 6.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.01 | 140567.19 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 22.46 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.57 | 0.02 | 57334.85 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
