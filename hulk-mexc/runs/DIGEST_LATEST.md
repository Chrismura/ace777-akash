# Hulk DIGEST — 2026-10-06T01:39:37Z

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
| QNTUSDT | IDLE | 3.1 | 6.49 | 2.26 | 0.04 | 2748796.49 | 8.07 | skipped_fast |
| XRPUSDT | IDLE | 0.5 | 0.9 | 0.61 | -0.01 | 31988845.08 | 1.99 | skipped_fast |
| ETHUSDT | IDLE | 0.33 | 0.61 | 0.38 | -0.0 | 352960701.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.55 | 0.35 | -0.01 | 611680398.52 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.29 | 4.03 | 3.73 | -0.01 | 687531.63 | 2.6 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 32.47 | 20.53 | 0.19 | 94027.16 | 127.87 | skipped_fast |
| WUSDT | IDLE | 2.57 | 4.5 | 4.21 | -0.01 | 403880.59 | 7.77 | skipped_fast |
| EDELUSDT | IDLE | 2.41 | 5.32 | 3.46 | 0.03 | 314520.75 | 29.39 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 6.62 | 6.15 | 0.03 | 112349.06 | 6.32 | skipped_fast |
| ZBCNUSDT | IDLE | 2.09 | 3.99 | 1.31 | 0.01 | 282370.31 | 20.73 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 1.97 | 1.37 | -0.02 | 428714.43 | 7.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 6.5 | 0.0 | 0.08 | 137628.08 | 13.07 | skipped_fast |
| MNSRYUSDT | IDLE | 3.24 | 5.85 | 4.16 | 0.0 | 45128.03 | 6.41 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.8 | 1.65 | -0.03 | 489510.14 | 2.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.66 | 3.82 | 3.68 | -0.03 | 18044.58 | 25.01 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 2.44 | 2.3 | -0.05 | 76816.17 | 8.29 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.78 | 1.57 | -0.05 | 68502.26 | 7.88 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 3.02 | 1.85 | -0.03 | 135298.93 | 31.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.36 | 9.31 | 0.66 | 0.26 | 79997.91 | 16.76 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.74 | 0.37 | -0.01 | 51245.64 | 14.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
