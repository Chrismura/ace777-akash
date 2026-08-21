# Hulk DIGEST — 2026-08-21T21:46:01Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.62 | 0.1 | 5662338.14 | 4.13 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.36 | 0.11 | 129134688.59 | 2.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.66 | 0.12 | 492027.57 | 11.95 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 5.61 | 3.34 | 0.05 | 522446.61 | 9.27 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 3.75 | 0.16 | 0.1 | 650957.45 | 6.39 | skipped_fast |
| HBARUSDT | IDLE | 1.68 | 3.36 | 0.0 | 0.07 | 819768.85 | 1.27 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.83 | 0.19 | 0.07 | 368989.77 | 11.46 | skipped_fast |
| BIOUSDT | IDLE | 2.4 | 5.2 | 1.72 | 0.02 | 187736.72 | 6.25 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.37 | 0.17 | 154161.62 | 19.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.01 | 0.04 | 55802.28 | 47.31 | skipped_fast |
| QAITUSDT | IDLE | 2.36 | 4.38 | 2.29 | -0.02 | 3819.28 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 4.12 | 0.99 | -0.04 | 83633.97 | 55.59 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.32 | 0.11 | 61151.23 | 12.89 | skipped_fast |
| TELUSDT | IDLE | 1.94 | 4.81 | 1.56 | 0.03 | 183300.8 | 26.49 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.65 | 0.49 | 0.04 | 62656.69 | 4.63 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.49 | 0.03 | 53893.58 | 16.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 38.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
