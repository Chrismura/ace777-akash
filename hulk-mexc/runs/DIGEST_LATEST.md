# Hulk DIGEST — 2026-09-08T02:48:20Z

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
| XRPUSDT | IDLE | 0.9 | 1.71 | 0.63 | -0.02 | 33781513.88 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.27 | 0.59 | -0.01 | 306100326.08 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.85 | 0.43 | -0.01 | 430679650.24 | 0.06 | skipped_fast |
| CCUSDT | IDLE | 1.87 | 3.52 | 1.41 | -0.04 | 445594.43 | 8.5 | skipped_fast |
| RIZEUSDT | IDLE | 3.62 | 11.02 | 3.67 | 0.03 | 53375.81 | 63.52 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.29 | 1.95 | -0.06 | 414374.88 | 1.86 | skipped_fast |
| WUSDT | IDLE | 1.88 | 3.5 | 1.75 | -0.02 | 245073.94 | 10.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 4.84 | 4.34 | -0.11 | 204872.33 | 15.37 | skipped_fast |
| KITEUSDT | IDLE | 2.34 | 4.48 | 1.64 | -0.05 | 62476.4 | 10.75 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 9.19 | 3.92 | -0.07 | 109186.66 | 89.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 3.04 | 1.86 | -0.05 | 241091.76 | 8.43 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.83 | 0.9 | 0.0 | 501390.48 | 1.21 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.56 | 1.41 | -0.01 | 64568.6 | 7.34 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.09 | 1.53 | 0.03 | 58241.33 | 17.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.24 | 3.65 | 1.48 | -0.08 | 3843.49 | 30.99 | skipped_fast |
| QNTUSDT | IDLE | 0.84 | 1.52 | 1.06 | -0.01 | 60529.47 | 6.04 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.95 | 0.7 | -0.02 | 80743.18 | 40.95 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.36 | -0.01 | 53126.74 | 7.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.62 | -0.02 | 37537.34 | 15.02 | skipped_fast |
| FLUIDUSDT | IDLE | 0.03 | 0.05 | 0.0 | 0.01 | 1037.8 | 22.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
