# Hulk DIGEST — 2026-09-25T07:42:55Z

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
| XRPUSDT | IDLE | 1.27 | 2.25 | 2.0 | 0.01 | 71595304.04 | 1.31 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.33 | 1.19 | -0.01 | 731158105.34 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.22 | 1.14 | -0.01 | 356507042.36 | 0.19 | skipped_fast |
| PYTHUSDT | IDLE | 0.8 | 2.72 | 1.68 | 0.06 | 1035936.74 | 2.93 | skipped_fast |
| HBARUSDT | IDLE | 1.66 | 2.91 | 2.77 | 0.0 | 918013.65 | 1.09 | skipped_fast |
| CCUSDT | IDLE | 1.26 | 3.1 | 0.63 | 0.06 | 536363.81 | 9.43 | skipped_fast |
| RIZEUSDT | IDLE | 2.33 | 60.05 | 13.43 | 0.6 | 108540.57 | 421.68 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 18.09 | 4.57 | 0.38 | 474008.04 | 12.07 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 5.4 | 3.92 | 0.07 | 135565.96 | 6.75 | skipped_fast |
| WUSDT | IDLE | 1.37 | 2.4 | 2.3 | -0.0 | 281148.36 | 5.18 | skipped_fast |
| ZBCNUSDT | IDLE | 0.97 | 1.69 | 1.66 | -0.01 | 212715.33 | 17.2 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.1 | 1.67 | -0.05 | 67974.99 | 10.36 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 2.67 | 1.41 | 0.04 | 88296.0 | 13.05 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 5.96 | 3.4 | 0.08 | 191062.9 | 50.79 | skipped_fast |
| CHIPUSDT | IDLE | 0.6 | 3.14 | 2.11 | 0.08 | 105039.68 | 15.22 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 4.71 | 3.23 | 0.14 | 17964.42 | 75.61 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 2.9 | 0.86 | -0.05 | 110403.5 | 49.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 1.01 | 0.49 | 0.01 | 41343.04 | 18.08 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.66 | 0.29 | 0.01 | 58315.38 | 7.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.23 | 0.45 | 0.0 | 0.04 | 1085.23 | 21.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
