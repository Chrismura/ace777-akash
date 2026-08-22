# Hulk DIGEST — 2026-08-22T03:17:48Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 10.96 | 0.52 | 0.17 | 7662330.06 | 1.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.26 | 11.43 | 0.15 | 0.2 | 161163052.68 | 0.64 | skipped_fast |
| HBARUSDT | IDLE | 2.25 | 5.87 | 0.23 | 0.11 | 1005877.86 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 8.96 | 1.73 | 0.17 | 679649.14 | 6.81 | skipped_fast |
| BIOUSDT | IDLE | 3.04 | 7.36 | 2.9 | 0.06 | 197937.73 | 3.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 4.28 | 0.68 | -0.01 | 450394.86 | 2.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 5.16 | 2.29 | 0.12 | 539940.49 | 21.61 | skipped_fast |
| WUSDT | IDLE | 1.78 | 5.61 | 0.42 | 0.12 | 417776.72 | 9.88 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 3.83 | 3.04 | -0.03 | 80021.02 | 22.42 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.37 | 0.1 | 59511.67 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.88 | 0.2 | 157977.62 | 18.99 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | 0.01 | 9452.18 | 16.21 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.4 | 0.5 | 0.12 | 67583.83 | 9.85 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.68 | 3.97 | 0.03 | 0.09 | 174148.61 | 8.91 | skipped_fast |
| RWAUSDT | IDLE | 1.3 | 2.56 | 0.24 | 0.05 | 56124.87 | 16.14 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.36 | 0.07 | 173402.21 | 51.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
