# Hulk DIGEST — 2026-09-06T11:30:44Z

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
| ETHUSDT | IDLE | 0.64 | 1.21 | 0.48 | 0.02 | 230837598.26 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.63 | 1.19 | 0.42 | 0.01 | 25231384.59 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 0.28 | 0.54 | 0.12 | 0.0 | 403347753.62 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.82 | 7.32 | 3.83 | 0.05 | 412128.16 | 10.11 | skipped_fast |
| RWAINCUSDT | IDLE | 3.52 | 7.89 | 2.1 | 0.04 | 7894.41 | 46.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.11 | 2.16 | 0.34 | 0.03 | 440700.92 | 1.8 | skipped_fast |
| WUSDT | IDLE | 2.11 | 4.15 | 0.49 | 0.04 | 191815.37 | 14.5 | skipped_fast |
| RIZEUSDT | IDLE | 2.04 | 11.34 | 8.6 | 0.02 | 91434.71 | 64.75 | skipped_fast |
| REDUSDT | IDLE | 2.39 | 4.59 | 1.32 | 0.02 | 61063.97 | 10.07 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 2.07 | 1.22 | 0.01 | 317934.03 | 9.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 2.76 | 1.33 | 0.0 | 205776.4 | 9.5 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.63 | 1.56 | 0.0 | 69510.44 | 18.62 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.75 | 0.57 | 0.02 | 93931.74 | 3.59 | skipped_fast |
| KITEUSDT | IDLE | 1.03 | 1.84 | 1.43 | -0.03 | 64881.07 | 10.19 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.37 | 0.23 | 0.02 | 422363.43 | 1.23 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 2.56 | 2.01 | 0.03 | 40164.53 | 3.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.61 | 1.15 | 0.45 | 0.02 | 42512.74 | 2.68 | skipped_fast |
| TELUSDT | IDLE | 0.88 | 1.65 | 0.75 | 0.01 | 71711.68 | 52.49 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.0 | 0.71 | -0.0 | 53046.77 | 14.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
