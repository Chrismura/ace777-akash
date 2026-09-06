# Hulk DIGEST — 2026-09-06T18:31:54Z

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
| XRPUSDT | IDLE | 0.9 | 1.7 | 0.61 | -0.0 | 25198042.23 | 2.83 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.54 | 0.18 | 0.01 | 243988302.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.97 | 0.07 | -0.0 | 351527182.43 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.4 | 7.14 | 3.19 | 0.06 | 340539.65 | 14.39 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 3.91 | 1.87 | -0.0 | 531050.09 | 3.65 | skipped_fast |
| CHIPUSDT | IDLE | 1.9 | 3.93 | 2.39 | -0.02 | 416688.75 | 1.75 | skipped_fast |
| EDELUSDT | IDLE | 2.72 | 4.95 | 3.33 | -0.01 | 60657.83 | 57.14 | skipped_fast |
| BIOUSDT | IDLE | 1.96 | 3.71 | 1.39 | -0.02 | 90602.66 | 3.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.54 | 11.91 | 7.78 | -0.14 | 73029.75 | 65.12 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.54 | 0.71 | -0.01 | 322853.36 | 9.14 | skipped_fast |
| RWAINCUSDT | IDLE | 1.98 | 4.28 | 2.5 | 0.07 | 6107.61 | 15.38 | skipped_fast |
| ZBCNUSDT | IDLE | 1.09 | 1.97 | 1.4 | 0.03 | 186502.21 | 13.97 | skipped_fast |
| REDUSDT | IDLE | 1.24 | 2.33 | 0.98 | 0.01 | 66846.2 | 10.21 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.38 | 0.78 | -0.01 | 417712.37 | 1.24 | skipped_fast |
| KITEUSDT | IDLE | 0.77 | 1.39 | 1.03 | 0.0 | 60885.05 | 12.67 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.3 | 0.58 | -0.0 | 65798.39 | 28.99 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 1.65 | 0.32 | 0.01 | 35026.08 | 7.6 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.3 | 1.0 | -0.02 | 54023.48 | 14.39 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.36 | 0.19 | 0.02 | 41542.06 | 6.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.63 | 0.63 | 0.02 | 194.56 | 22.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
