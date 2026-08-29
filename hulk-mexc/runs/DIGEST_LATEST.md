# Hulk DIGEST — 2026-08-29T13:11:19Z

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
| XRPUSDT | IDLE | 0.42 | 0.78 | 0.41 | -0.03 | 38218623.54 | 1.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.54 | 6.99 | 5.97 | -0.1 | 1145602.88 | 10.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.17 | 2.21 | 0.8 | -0.01 | 409103.02 | 2.12 | skipped_fast |
| CCUSDT | IDLE | 1.75 | 3.39 | 0.76 | 0.02 | 216471.62 | 7.01 | skipped_fast |
| REDUSDT | IDLE | 1.79 | 5.16 | 2.86 | 0.04 | 75704.01 | 21.58 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 2.71 | 1.92 | -0.07 | 182635.7 | 19.56 | skipped_fast |
| QAITUSDT | IDLE | 1.29 | 11.11 | 4.71 | 0.01 | 94483.97 | 75.06 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 5.64 | 1.59 | -0.1 | 97238.7 | 38.1 | skipped_fast |
| WUSDT | IDLE | 0.9 | 1.64 | 1.1 | -0.04 | 217348.92 | 13.27 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 2.5 | 0.6 | 0.01 | 63002.52 | 11.66 | skipped_fast |
| BIOUSDT | IDLE | 0.56 | 0.99 | 0.9 | -0.04 | 82599.09 | 3.65 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.17 | 1.59 | -0.04 | 26423.71 | 58.87 | skipped_fast |
| HBARUSDT | IDLE | 0.28 | 0.52 | 0.28 | -0.04 | 364243.05 | 1.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.53 | 1.0 | 0.39 | -0.04 | 4404.21 | 100.22 | skipped_fast |
| TELUSDT | IDLE | 0.73 | 1.33 | 0.86 | -0.04 | 78203.21 | 46.19 | skipped_fast |
| QNTUSDT | IDLE | 0.54 | 0.97 | 0.75 | -0.02 | 34425.88 | 4.92 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.58 | 0.41 | 0.02 | 56412.47 | 24.72 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 0.69 | 0.0 | -0.03 | 1878.64 | 21.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
