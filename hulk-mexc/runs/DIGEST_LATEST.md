# Hulk DIGEST — 2026-09-26T11:29:54Z

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
| XRPUSDT | IDLE | 0.69 | 1.3 | 0.49 | -0.02 | 99649744.94 | 1.29 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.66 | 0.34 | -0.01 | 234477136.26 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.51 | 0.2 | -0.01 | 512948826.37 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.09 | 5.46 | 0.0 | 0.08 | 1175395.93 | 2.59 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 5.09 | 3.51 | 0.1 | 1007685.64 | 10.41 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 10.52 | 4.94 | 0.07 | 771546.57 | 4.79 | skipped_fast |
| WUSDT | IDLE | 2.11 | 5.79 | 0.02 | 0.08 | 486509.5 | 10.78 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.5 | 0.32 | -0.01 | 770741.42 | 1.06 | skipped_fast |
| RWAINCUSDT | IDLE | 2.58 | 4.93 | 3.56 | 0.02 | 5984.05 | 58.88 | skipped_fast |
| EDELUSDT | IDLE | 1.53 | 3.07 | 0.0 | 0.02 | 177092.89 | 13.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 2.28 | 0.16 | -0.02 | 228450.46 | 6.09 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 2.89 | 1.17 | 0.0 | 143073.22 | 14.31 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 3.25 | 0.96 | 0.04 | 125858.86 | 6.04 | skipped_fast |
| RIZEUSDT | IDLE | 1.29 | 9.26 | 4.44 | -0.21 | 52156.13 | 59.96 | skipped_fast |
| RWAUSDT | IDLE | 2.36 | 4.31 | 2.71 | -0.0 | 55722.25 | 7.32 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 2.24 | 0.71 | 0.03 | 75425.23 | 8.08 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.78 | 1.47 | -0.0 | 59428.57 | 12.96 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.06 | 1.96 | -0.05 | 121118.43 | 6.25 | skipped_fast |
| FLUIDUSDT | IDLE | 1.21 | 2.4 | 0.17 | -0.01 | 3407.89 | 22.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.06 | 0.0 | 38875.98 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
