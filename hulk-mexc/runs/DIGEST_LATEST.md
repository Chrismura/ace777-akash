# Hulk DIGEST — 2026-09-02T01:30:06Z

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
| XRPUSDT | IDLE | 0.78 | 1.37 | 1.28 | -0.03 | 35880640.14 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.08 | 0.71 | -0.02 | 347405283.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.9 | 0.57 | -0.02 | 522701086.9 | 0.0 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.7 | 8.04 | 1.2 | 0.07 | 746513.96 | 1.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.44 | 6.66 | 5.7 | 0.12 | 763307.39 | 4.62 | skipped_fast |
| WUSDT | IDLE | 2.74 | 4.82 | 4.35 | 0.02 | 420063.3 | 10.51 | skipped_fast |
| ZBCNUSDT | IDLE | 2.83 | 5.2 | 4.78 | -0.03 | 195721.13 | 6.11 | skipped_fast |
| RIZEUSDT | IDLE | 2.67 | 7.87 | 4.96 | -0.06 | 42059.37 | 77.43 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 9.32 | 2.43 | -0.03 | 166768.46 | 17.71 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 3.74 | 3.41 | 0.06 | 119452.46 | 11.57 | skipped_fast |
| CCUSDT | IDLE | 0.53 | 1.21 | 0.67 | -0.06 | 330307.78 | 1.76 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.36 | 0.24 | 0.05 | 68936.9 | 11.26 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.74 | 0.89 | -0.04 | 69610.1 | 3.92 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.59 | 1.54 | -0.0 | 253796.38 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.8 | 0.93 | 0.04 | 47155.17 | 12.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 1.95 | 0.29 | -0.01 | 5787.07 | 98.69 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.32 | 1.08 | -0.03 | 92522.36 | 30.22 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 1.01 | 0.38 | -0.03 | 58403.91 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.7 | 0.33 | -0.02 | 35091.38 | 13.75 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 0.96 | 0.62 | -0.04 | 249.95 | 21.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
