# Hulk DIGEST — 2026-10-25T04:35:07Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.86 | 1.67 | 0.27 | 0.01 | 26195975.8 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.23 | 0.27 | -0.01 | 121626312.04 | 0.17 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.58 | 0.18 | -0.0 | 242218299.11 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.3 | 2.44 | 1.41 | -0.06 | 772829.82 | 22.95 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.71 | 0.54 | 0.01 | 501266.79 | 1.4 | skipped_fast |
| EDELUSDT | IDLE | 0.83 | 2.01 | 1.02 | -0.06 | 592005.95 | 29.89 | skipped_fast |
| QNTUSDT | IDLE | 2.23 | 4.41 | 0.32 | 0.01 | 372667.37 | 0.54 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 3.23 | 3.11 | -0.05 | 59126.4 | 13.27 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 3.84 | 2.15 | -0.0 | 93226.32 | 7.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 4.52 | 2.44 | 0.04 | 93266.16 | 13.32 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 1.85 | 1.46 | 0.0 | 225981.56 | 12.1 | skipped_fast |
| LAUSDT | IDLE | 2.03 | 11.5 | 6.65 | -0.06 | 107679.79 | 23.12 | skipped_fast |
| CCUSDT | IDLE | 0.69 | 1.26 | 0.76 | -0.02 | 208189.17 | 5.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.19 | 2.25 | 0.91 | -0.0 | 55881.14 | 5.42 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.89 | 1.51 | -0.03 | 66102.86 | 4.39 | skipped_fast |
| WAXLUSDT | IDLE | 2.2 | 5.99 | 2.37 | 0.02 | 56219.27 | 32.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.72 | 2.01 | 0.76 | -0.03 | 41721.04 | 27.77 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.52 | 0.69 | 0.01 | 203192.83 | 12.81 | skipped_fast |
| IOTAUSDT | IDLE | 1.03 | 1.89 | 1.13 | -0.02 | 67677.99 | 29.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.94 | 1.83 | 1.39 | -0.04 | 13034.03 | 21.25 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.64 | 0.16 | -0.0 | 53247.19 | 15.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.43 | -0.01 | 37388.62 | 65.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
