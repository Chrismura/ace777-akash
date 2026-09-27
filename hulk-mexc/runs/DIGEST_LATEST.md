# Hulk DIGEST — 2026-09-27T00:04:59Z

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
| QNTUSDT | IDLE | 2.26 | 34.96 | 4.09 | 0.54 | 2065614.23 | 14.3 | skipped_fast |
| XRPUSDT | IDLE | 0.97 | 1.9 | 0.29 | -0.03 | 40499932.1 | 1.97 | skipped_fast |
| ETHUSDT | IDLE | 0.61 | 1.2 | 0.1 | 0.0 | 117225812.5 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.76 | 0.14 | 0.0 | 350375599.88 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.01 | 6.21 | 0.07 | 0.1 | 1118353.41 | 8.59 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 3.73 | 1.38 | 0.04 | 833989.42 | 5.92 | skipped_fast |
| WUSDT | IDLE | 2.52 | 5.22 | 1.37 | 0.06 | 559492.16 | 7.67 | skipped_fast |
| EDELUSDT | IDLE | 3.0 | 5.36 | 4.28 | 0.0 | 170468.73 | 3.36 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 6.5 | 1.29 | 0.14 | 140683.58 | 9.88 | skipped_fast |
| CHIPUSDT | IDLE | 2.07 | 5.11 | 1.57 | -0.02 | 102731.36 | 16.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 2.74 | 1.78 | -0.03 | 192248.22 | 19.17 | skipped_fast |
| RIZEUSDT | IDLE | 2.38 | 6.03 | 0.55 | 0.08 | 47447.08 | 59.87 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 2.02 | 0.52 | -0.02 | 536722.09 | 1.07 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.83 | 0.84 | -0.03 | 109821.1 | 12.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.4 | 4.65 | 4.44 | 0.03 | 10088.3 | 68.23 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 1.89 | 0.02 | -0.02 | 58745.11 | 13.6 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 3.72 | 0.12 | 0.02 | 124718.41 | 47.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.25 | 2.29 | 1.45 | -0.0 | 693.01 | 17.38 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 1.01 | 0.21 | 0.03 | 55762.97 | 7.15 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.11 | -0.0 | 38613.44 | 31.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
