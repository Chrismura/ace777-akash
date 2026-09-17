# Hulk DIGEST — 2026-09-17T22:18:09Z

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
| ETHUSDT | IDLE | 0.86 | 1.5 | 1.47 | 0.02 | 298823483.73 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.88 | 1.55 | 1.42 | 0.0 | 38285162.82 | 2.32 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.83 | 0.82 | 0.01 | 430207647.15 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 40.44 | 12.97 | -0.17 | 278102.1 | 13.63 | skipped_fast |
| PYTHUSDT | IDLE | 1.5 | 3.72 | 3.2 | 0.07 | 549011.94 | 1.8 | skipped_fast |
| CCUSDT | IDLE | 1.21 | 2.28 | 0.98 | 0.04 | 559890.92 | 4.99 | skipped_fast |
| WUSDT | IDLE | 1.53 | 4.65 | 1.7 | 0.12 | 326586.02 | 17.13 | skipped_fast |
| HBARUSDT | IDLE | 1.51 | 2.64 | 2.57 | 0.02 | 547016.51 | 1.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 4.34 | 0.04 | 144021.83 | 18.82 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.38 | 1.32 | 0.02 | 199336.06 | 48.36 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 2.17 | 2.12 | 0.01 | 67782.24 | 4.01 | skipped_fast |
| TELUSDT | IDLE | 2.75 | 4.88 | 4.18 | -0.02 | 75352.78 | 63.27 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.02 | 0.83 | 0.01 | 60673.48 | 10.41 | skipped_fast |
| REDUSDT | IDLE | 0.5 | 0.9 | 0.68 | 0.01 | 65543.45 | 16.22 | skipped_fast |
| RWAINCUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.0 | 14461.96 | 23.81 | skipped_fast |
| RIZEUSDT | IDLE | 1.03 | 7.03 | 3.7 | -0.07 | 43474.79 | 135.31 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 1.43 | 1.38 | 0.0 | 40029.78 | 4.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.03 | 146.13 | 21.87 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.6 | 0.15 | 0.0 | 57529.75 | 29.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.03 | 0.02 | 43046.92 | 4.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
