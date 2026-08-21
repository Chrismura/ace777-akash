# Hulk DIGEST — 2026-08-21T23:19:32Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.52 | 0.12 | 6035046.04 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.79 | 7.09 | 0.34 | 0.15 | 138948954.05 | 2.75 | skipped_fast |
| HBARUSDT | IDLE | 2.53 | 6.15 | 0.0 | 0.1 | 893607.74 | 1.24 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 11.25 | 0.4 | 0.16 | 512542.79 | 30.68 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.18 | 0.13 | 645066.05 | 9.79 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.18 | 0.09 | 377720.15 | 9.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.37 | 0.04 | 547955.39 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.05 | 0.03 | 187899.57 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82514.64 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.14 | 9.82 | 2.44 | 0.11 | 59624.05 | 44.9 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 32.38 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.15 | 0.07 | 184975.16 | 35.96 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.68 | 0.19 | 157515.51 | 17.73 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.27 | 0.06 | 0.07 | 118730.56 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.19 | 0.09 | 61628.4 | 10.2 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 2.08 | 0.0 | 0.04 | 54467.54 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
