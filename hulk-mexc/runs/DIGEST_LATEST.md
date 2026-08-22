# Hulk DIGEST — 2026-08-22T03:04:26Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 9.55 | 0.87 | 0.15 | 7448924.09 | 1.9 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 11.15 | 0.39 | 0.2 | 159854416.86 | 3.87 | skipped_fast |
| HBARUSDT | IDLE | 2.15 | 5.29 | 0.36 | 0.1 | 995121.09 | 1.22 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.3 | 0.19 | 666008.55 | 7.55 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.2 | 0.07 | 194689.3 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 4.28 | 0.3 | -0.01 | 449200.53 | 2.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 5.16 | 1.83 | 0.13 | 539448.04 | 33.04 | skipped_fast |
| WUSDT | IDLE | 1.76 | 5.57 | 0.0 | 0.12 | 417338.71 | 9.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.41 | 0.09 | 61387.16 | 27.19 | skipped_fast |
| EDELUSDT | IDLE | 1.89 | 3.83 | 2.28 | -0.03 | 79897.61 | 22.25 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.26 | 0.2 | 157929.48 | 11.12 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 21.69 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 4.03 | 0.03 | 0.12 | 62519.31 | 10.74 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3931.36 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.31 | 0.08 | 172771.33 | 2.98 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 1.88 | 0.77 | 0.06 | 172999.94 | 36.07 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.31 | 0.24 | 0.05 | 56079.32 | 24.26 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
