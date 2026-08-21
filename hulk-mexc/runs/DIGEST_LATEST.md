# Hulk DIGEST — 2026-08-21T23:28:41Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.75 | 0.11 | 6075896.91 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.64 | 0.15 | 140248119.55 | 3.41 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 11.25 | 1.22 | 0.13 | 512882.79 | 9.53 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.29 | 0.51 | 0.09 | 901377.36 | 3.74 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.92 | 0.13 | 645399.58 | 8.0 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.35 | 0.08 | 378635.49 | 14.36 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.09 | 0.04 | 548489.42 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.8 | 0.02 | 187628.12 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 5.5 | 0.43 | -0.03 | 82465.43 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.16 | 9.82 | 3.3 | 0.16 | 58902.41 | 45.4 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.21 | 0.07 | 185884.11 | 20.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.01 | 10164.7 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.11 | 0.18 | 157591.38 | 12.96 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.63 | 0.03 | 0.07 | 119862.34 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.25 | 0.09 | 61411.38 | 12.07 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54492.48 | 40.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 22.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
