# Hulk DIGEST — 2026-10-15T08:27:23Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.0 | 9.59 | 1.36 | 0.06 | 2773098.12 | 2.28 | skipped_fast |
| WUSDT | IDLE | 2.01 | 6.13 | 4.91 | -0.11 | 2738084.43 | 18.42 | skipped_fast |
| XRPUSDT | IDLE | 1.43 | 2.73 | 0.9 | -0.05 | 61302796.77 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.93 | 1.9 | 0.57 | -0.06 | 346530292.58 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.5 | 0.53 | -0.03 | 542675322.81 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.67 | 4.53 | 0.97 | -0.07 | 1176057.71 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 16.03 | 8.9 | -0.04 | 65256.85 | 36.14 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.67 | 3.49 | -0.12 | 453648.04 | 5.6 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 4.59 | 3.05 | -0.07 | 204458.22 | 18.86 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 2.82 | 0.99 | -0.06 | 602278.31 | 1.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.25 | 8.26 | 6.33 | -0.21 | 122158.42 | 15.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.04 | 2.84 | 0.67 | -0.06 | 219792.38 | 20.02 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 3.98 | 2.21 | -0.1 | 84069.39 | 8.08 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.27 | 0.35 | 0.01 | 67156.73 | 8.19 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 3.59 | 1.52 | -0.14 | 68868.43 | 10.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.08 | 2.37 | 1.11 | 0.01 | 26501.46 | 25.49 | skipped_fast |
| FLUIDUSDT | IDLE | 1.99 | 5.96 | 4.12 | -0.05 | 20373.19 | 17.22 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.0 | 1.04 | -0.05 | 100279.16 | 35.05 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.73 | 0.48 | -0.03 | 55089.79 | 8.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.14 | 1.13 | -0.02 | 31215.35 | 71.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
