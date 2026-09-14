# Hulk DIGEST — 2026-09-14T19:44:00Z

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
| XRPUSDT | IDLE | 2.39 | 6.3 | 1.51 | 0.08 | 62905181.96 | 2.06 | skipped_fast |
| ETHUSDT | IDLE | 1.14 | 2.23 | 0.36 | 0.01 | 375966982.98 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.76 | 1.48 | 0.29 | 0.02 | 533517351.94 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.02 | 3.8 | 1.57 | -0.02 | 445096.21 | 1.79 | skipped_fast |
| REDUSDT | IDLE | 2.48 | 8.59 | 5.79 | 0.06 | 184813.59 | 9.33 | skipped_fast |
| EDELUSDT | IDLE | 1.75 | 8.78 | 1.29 | 0.13 | 268147.87 | 19.6 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 3.08 | 0.7 | 0.02 | 306164.92 | 6.15 | skipped_fast |
| WUSDT | IDLE | 1.81 | 3.5 | 0.85 | -0.0 | 204218.58 | 6.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 3.15 | 1.0 | 0.02 | 207469.4 | 4.4 | skipped_fast |
| BIOUSDT | IDLE | 2.03 | 3.83 | 1.52 | 0.02 | 91612.35 | 11.57 | skipped_fast |
| TELUSDT | IDLE | 3.18 | 8.53 | 2.43 | 0.07 | 100238.39 | 29.59 | skipped_fast |
| CHIPUSDT | IDLE | 1.69 | 3.17 | 2.28 | -0.04 | 90223.44 | 16.8 | skipped_fast |
| RIZEUSDT | IDLE | 0.94 | 10.63 | 6.52 | -0.01 | 54977.22 | 8.25 | skipped_fast |
| KITEUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.01 | 63058.89 | 12.02 | skipped_fast |
| HBARUSDT | IDLE | 1.56 | 2.99 | 0.83 | 0.02 | 319235.5 | 1.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.84 | 1.08 | 0.02 | 9883.54 | 5.48 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 1.97 | 1.28 | -0.01 | 42733.06 | 4.69 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.54 | 0.09 | 0.03 | 1014.14 | 20.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.81 | 1.55 | 0.5 | 0.0 | 30399.19 | 37.36 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.45 | 0.3 | -0.0 | 55814.05 | 29.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
