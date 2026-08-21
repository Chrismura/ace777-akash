# Hulk DIGEST — 2026-08-21T21:03:08Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.54 | 0.09 | 5577562.24 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.18 | 3.73 | 2.71 | 0.1 | 128135133.86 | 1.45 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 8.19 | 5.95 | 0.08 | 480070.93 | 43.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.62 | 3.73 | 0.08 | 514380.49 | 3.1 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.43 | 0.1 | 641716.75 | 7.37 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.04 | 1.53 | 0.06 | 807827.8 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.83 | 0.88 | 0.07 | 367936.94 | 10.5 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.2 | 2.7 | 0.01 | 187767.94 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.26 | 0.17 | 152868.82 | 13.11 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.12 | 2.97 | -0.05 | 82298.73 | 22.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.39 | 0.02 | 56241.9 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.04 | 10893.0 | 64.31 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.13 | 0.11 | 61231.63 | 12.07 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.64 | 0.01 | 181023.26 | 21.49 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60167.27 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 206.51 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.08 | 0.99 | 0.03 | 53789.78 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
