# Hulk DIGEST — 2026-08-31T14:09:55Z

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
| XRPUSDT | IDLE | 1.05 | 1.91 | 1.3 | -0.03 | 40554305.29 | 2.2 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.43 | 1.02 | -0.01 | 550546928.45 | 0.14 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.1 | 0.73 | -0.01 | 445764691.75 | 0.12 | skipped_fast |
| CHIPUSDT | IDLE | 2.36 | 6.29 | 4.61 | -0.03 | 567862.23 | 2.5 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.74 | 2.08 | -0.05 | 452840.05 | 2.13 | skipped_fast |
| WUSDT | IDLE | 1.84 | 3.36 | 2.68 | -0.04 | 233714.94 | 6.58 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 2.82 | 2.61 | -0.01 | 242866.47 | 9.37 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.74 | 2.43 | -0.03 | 70697.48 | 12.13 | skipped_fast |
| RWAINCUSDT | IDLE | 1.88 | 3.35 | 2.69 | -0.03 | 2116.72 | 23.04 | skipped_fast |
| ZBCNUSDT | IDLE | 0.87 | 2.11 | 0.39 | -0.05 | 230722.7 | 19.4 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.3 | 2.13 | -0.05 | 82824.41 | 3.82 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 2.92 | 2.68 | -0.08 | 100286.69 | 10.99 | skipped_fast |
| EDELUSDT | IDLE | 0.55 | 3.51 | 1.62 | 0.02 | 122889.56 | 16.45 | skipped_fast |
| QNTUSDT | IDLE | 2.12 | 3.9 | 2.21 | -0.01 | 49424.78 | 8.17 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 1.98 | 1.39 | -0.02 | 261458.73 | 1.36 | skipped_fast |
| RWAUSDT | IDLE | 2.2 | 4.35 | 0.39 | 0.05 | 54526.71 | 23.26 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 1.99 | 0.68 | -0.01 | 34109.02 | 61.74 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 3.33 | 2.53 | -0.0 | 90715.45 | 65.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.54 | 0.13 | 0.01 | 2017.96 | 22.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.05 | -0.01 | 25489.17 | 4.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
