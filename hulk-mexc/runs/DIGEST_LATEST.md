# Hulk DIGEST — 2026-10-16T03:22:17Z

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
| WUSDT | IDLE | 1.74 | 4.31 | 0.57 | 0.0 | 2290589.35 | 12.06 | skipped_fast |
| PYTHUSDT | IDLE | 0.72 | 4.3 | 1.33 | 0.12 | 4298147.1 | 10.53 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.46 | 0.98 | 0.03 | 258446929.69 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.56 | 1.04 | 0.49 | 0.02 | 41328482.06 | 2.99 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.71 | 0.52 | 0.01 | 458634220.48 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 3.28 | 0.91 | 0.05 | 1177523.41 | 1.93 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 3.28 | 1.92 | -0.04 | 450369.11 | 7.54 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.0 | 11.09 | 1.82 | 0.08 | 163997.53 | 9.76 | skipped_fast |
| REDUSDT | IDLE | 1.78 | 5.18 | 4.8 | -0.04 | 91705.76 | 0.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.68 | 3.16 | 2.39 | 0.05 | 190630.44 | 19.9 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 3.05 | 2.42 | -0.1 | 218642.44 | 24.12 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.01 | 1.97 | 0.0 | 67957.29 | 8.98 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 2.43 | 1.23 | 0.02 | 29153.19 | 5.01 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.57 | 0.96 | 0.03 | 76545.72 | 3.89 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.72 | 1.01 | 0.04 | 223064.79 | 7.02 | skipped_fast |
| RIZEUSDT | IDLE | 0.63 | 1.73 | 0.91 | 0.09 | 73770.94 | 57.14 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 1.53 | 1.0 | 0.03 | 84392.06 | 28.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.84 | 1.54 | 1.52 | -0.03 | 9309.29 | 21.53 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.56 | 0.32 | 0.01 | 53125.66 | 7.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.37 | 0.18 | 0.01 | 37672.81 | 25.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
