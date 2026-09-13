# Hulk DIGEST — 2026-09-13T03:32:36Z

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
| XRPUSDT | IDLE | 0.33 | 0.6 | 0.42 | 0.0 | 14067225.39 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 0.18 | 0.32 | 0.32 | 0.0 | 195081213.56 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.12 | 0.22 | 0.12 | -0.0 | 311515683.62 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.42 | 41.76 | 24.95 | 0.07 | 94476.76 | 34.7 | skipped_fast |
| PYTHUSDT | IDLE | 1.31 | 2.49 | 0.81 | 0.06 | 432598.77 | 1.81 | skipped_fast |
| WUSDT | IDLE | 2.18 | 4.05 | 2.02 | 0.03 | 214526.59 | 15.86 | skipped_fast |
| ZBCNUSDT | IDLE | 1.74 | 5.23 | 1.88 | -0.0 | 225234.79 | 10.09 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.7 | 3.65 | 0.02 | 9864.89 | 5.47 | skipped_fast |
| QNTUSDT | IDLE | 3.32 | 5.95 | 4.62 | 0.0 | 41115.67 | 6.23 | skipped_fast |
| REDUSDT | IDLE | 2.02 | 3.97 | 0.45 | 0.02 | 56193.19 | 16.4 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 3.77 | 0.65 | 0.09 | 171528.84 | 24.32 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.59 | 0.95 | -0.01 | 186870.58 | 6.15 | skipped_fast |
| RWAUSDT | IDLE | 2.68 | 4.77 | 3.98 | 0.0 | 54846.25 | 44.48 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.74 | 0.89 | 0.0 | 70594.9 | 3.91 | skipped_fast |
| CHIPUSDT | IDLE | 0.85 | 1.6 | 1.58 | -0.0 | 77080.7 | 14.76 | skipped_fast |
| KITEUSDT | IDLE | 0.9 | 1.65 | 1.04 | -0.01 | 62896.65 | 12.15 | skipped_fast |
| FLUIDUSDT | IDLE | 2.07 | 4.13 | 0.08 | 0.03 | 536.22 | 21.59 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.97 | 0.35 | 0.01 | 132586.47 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.53 | 1.27 | -0.04 | 90704.43 | 30.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.08 | 0.14 | 0.08 | 0.0 | 29197.88 | 15.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
