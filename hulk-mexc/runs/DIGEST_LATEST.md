# Hulk DIGEST — 2026-09-15T12:45:40Z

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
| XRPUSDT | IDLE | 0.86 | 1.68 | 0.23 | 0.0 | 72005843.53 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.89 | 0.46 | -0.01 | 456563968.35 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.78 | 0.47 | -0.01 | 555139739.33 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 4.56 | 2.38 | 0.03 | 212216.46 | 12.64 | skipped_fast |
| EDELUSDT | IDLE | 0.79 | 10.5 | 5.38 | 0.31 | 427481.46 | 31.75 | skipped_fast |
| PYTHUSDT | IDLE | 1.75 | 3.12 | 2.59 | -0.02 | 275041.61 | 1.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 4.44 | 3.51 | -0.06 | 86220.42 | 14.92 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 21.18 | 0.91 | -0.01 | 52268.14 | 96.4 | skipped_fast |
| CCUSDT | IDLE | 0.72 | 1.35 | 0.58 | -0.01 | 364053.31 | 1.05 | skipped_fast |
| HBARUSDT | IDLE | 1.57 | 3.13 | 0.04 | 0.02 | 382259.8 | 1.27 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 6.23 | 1.87 | -0.02 | 122245.98 | 15.18 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.73 | 1.8 | -0.02 | 88454.54 | 7.96 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.29 | 1.34 | -0.03 | 140058.69 | 14.52 | skipped_fast |
| RWAINCUSDT | IDLE | 1.63 | 2.85 | 2.77 | -0.02 | 8064.67 | 5.58 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.39 | 0.28 | 0.01 | 61366.0 | 14.95 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.91 | 2.7 | -0.03 | 93728.8 | 12.91 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.18 | 1.83 | -0.02 | 45102.99 | 7.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.47 | 2.57 | 2.5 | -0.03 | 2102.59 | 21.62 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 0.98 | 0.97 | -0.02 | 52939.43 | 7.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.43 | 0.01 | 31243.02 | 22.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
