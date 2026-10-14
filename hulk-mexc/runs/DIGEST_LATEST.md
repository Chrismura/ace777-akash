# Hulk DIGEST — 2026-10-14T02:18:17Z

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
| WUSDT | IDLE | 1.2 | 6.93 | 6.38 | -0.18 | 4002109.36 | 7.22 | skipped_fast |
| PYTHUSDT | IDLE | 1.12 | 3.72 | 1.1 | -0.04 | 1916670.89 | 1.26 | skipped_fast |
| XRPUSDT | IDLE | 0.59 | 1.08 | 0.73 | 0.01 | 29160375.8 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 0.49 | 0.9 | 0.55 | 0.01 | 160792891.55 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.67 | 0.43 | 0.01 | 356765989.19 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.01 | 3.62 | 1.34 | -0.06 | 1747725.07 | 3.75 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 3.34 | 2.85 | 0.02 | 583716.93 | 4.01 | skipped_fast |
| RWAINCUSDT | IDLE | 3.21 | 6.02 | 4.75 | -0.03 | 31591.85 | 5.09 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.57 | 1.47 | 0.04 | 222089.47 | 11.68 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 3.19 | 2.14 | -0.02 | 97323.83 | 13.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 2.0 | 0.46 | -0.01 | 216903.1 | 5.27 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.54 | 1.24 | 0.01 | 118265.43 | 15.32 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 2.85 | 1.69 | 0.05 | 57963.39 | 10.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 4.26 | 2.94 | 0.0 | 52653.23 | 61.33 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 1.63 | 1.04 | 0.01 | 71078.65 | 3.61 | skipped_fast |
| FLUIDUSDT | IDLE | 2.23 | 4.24 | 1.63 | 0.06 | 19565.85 | 21.65 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.43 | 0.93 | -0.0 | 244503.93 | 6.87 | skipped_fast |
| TELUSDT | IDLE | 1.41 | 2.77 | 0.27 | 0.05 | 117088.84 | 27.54 | skipped_fast |
| RWAUSDT | IDLE | 0.16 | 0.31 | 0.08 | 0.01 | 51796.48 | 7.73 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.39 | 0.1 | 0.0 | 37952.38 | 5.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
