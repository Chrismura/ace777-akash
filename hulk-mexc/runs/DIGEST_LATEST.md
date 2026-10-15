# Hulk DIGEST — 2026-10-15T22:05:33Z

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
| WUSDT | IDLE | 1.26 | 3.68 | 1.2 | -0.03 | 2894616.68 | 17.52 | skipped_fast |
| PYTHUSDT | IDLE | 0.86 | 5.32 | 0.58 | 0.11 | 4459006.99 | 1.04 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.59 | 0.09 | 0.01 | 503037019.79 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.47 | 0.1 | 0.02 | 314086912.85 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.5 | 0.95 | 0.33 | 0.01 | 48024624.43 | 1.49 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 3.97 | 2.99 | 0.0 | 1359031.57 | 4.34 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.81 | 10.86 | 8.6 | -0.13 | 237300.24 | 24.08 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 2.98 | 1.63 | -0.07 | 465155.42 | 6.53 | skipped_fast |
| ZBCNUSDT | IDLE | 1.63 | 3.22 | 2.5 | 0.01 | 216134.86 | 31.95 | skipped_fast |
| RIZEUSDT | IDLE | 2.03 | 8.01 | 2.32 | 0.04 | 82736.14 | 51.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.84 | 3.81 | 2.8 | 0.01 | 28483.31 | 19.89 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.2 | 1.69 | -0.03 | 68957.63 | 9.68 | skipped_fast |
| HBARUSDT | IDLE | 1.49 | 2.88 | 0.72 | 0.0 | 300022.53 | 8.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.66 | 3.46 | 0.0 | -0.1 | 152799.93 | 12.64 | skipped_fast |
| REDUSDT | IDLE | 0.73 | 2.14 | 1.84 | -0.01 | 72472.75 | 9.55 | skipped_fast |
| BIOUSDT | IDLE | 0.56 | 1.33 | 0.42 | -0.03 | 85454.42 | 11.6 | skipped_fast |
| RWAUSDT | IDLE | 0.96 | 1.76 | 1.1 | 0.0 | 55252.86 | 7.93 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 1.94 | 0.34 | 0.01 | 91628.5 | 33.65 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 2.38 | 0.85 | -0.04 | 8931.11 | 21.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.15 | 0.0 | 34565.96 | 8.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
