# Hulk DIGEST — 2026-09-12T06:17:49Z

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
| XRPUSDT | IDLE | 0.37 | 0.77 | 0.27 | 0.01 | 51316016.92 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 0.15 | 0.32 | 0.23 | 0.02 | 615123505.57 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.15 | 0.26 | 0.22 | -0.0 | 572551084.4 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.21 | 0.55 | 0.01 | 427623.25 | 3.82 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 2.79 | 1.36 | 0.0 | 417329.32 | 4.04 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 4.03 | 3.38 | 0.04 | 65256.24 | 17.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.92 | 3.83 | 1.74 | 0.01 | 15545.41 | 16.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.13 | 2.26 | 0.0 | -0.01 | 187561.33 | 16.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.22 | 3.3 | 2.39 | 0.04 | 115178.0 | 14.77 | skipped_fast |
| EDELUSDT | IDLE | 0.94 | 2.6 | 1.31 | 0.06 | 166898.37 | 17.68 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 2.38 | 2.03 | -0.01 | 58900.62 | 10.29 | skipped_fast |
| WUSDT | IDLE | 0.77 | 1.55 | 0.56 | 0.01 | 194923.2 | 11.24 | skipped_fast |
| RIZEUSDT | IDLE | 0.12 | 7.74 | 4.67 | 0.71 | 186922.27 | 53.88 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.23 | 0.82 | 0.01 | 81021.03 | 7.88 | skipped_fast |
| HBARUSDT | IDLE | 0.47 | 0.82 | 0.74 | -0.02 | 264767.39 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.6 | 1.29 | -0.03 | 94621.14 | 41.46 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.1 | 0.7 | -0.01 | 43704.92 | 6.25 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.74 | 0.07 | 0.03 | 53240.74 | 14.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.4 | 0.01 | 29132.58 | 13.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.01 | 1927.49 | 19.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
