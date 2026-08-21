# Hulk DIGEST — 2026-08-21T22:36:54Z

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
| PYTHUSDT | IDLE | 1.37 | 5.17 | 0.53 | 0.11 | 5828193.29 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.58 | 5.94 | 0.06 | 0.15 | 134723890.1 | 2.08 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 6.75 | 0.05 | 0.14 | 659982.68 | 5.32 | skipped_fast |
| HBARUSDT | IDLE | 2.22 | 4.71 | 0.89 | 0.07 | 869054.55 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.46 | 5.3 | 0.3 | 0.08 | 370907.09 | 12.35 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.54 | 0.05 | 533795.48 | 3.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.58 | 6.77 | 0.26 | 0.11 | 503787.68 | 39.3 | skipped_fast |
| BIOUSDT | IDLE | 2.31 | 5.04 | 1.38 | 0.03 | 188354.66 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 8.04 | 0.18 | 155989.42 | 12.96 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10212.45 | 16.16 | skipped_fast |
| EDELUSDT | IDLE | 2.34 | 5.04 | 0.87 | -0.03 | 82594.39 | 76.97 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.92 | 0.05 | 187034.48 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3825.97 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.09 | 0.11 | 61570.7 | 10.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.77 | 0.06 | 56363.71 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 2.04 | 4.06 | 0.08 | 0.06 | 75137.26 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.08 | 0.04 | 54156.39 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
