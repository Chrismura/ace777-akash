# Hulk DIGEST — 2026-08-22T17:01:15Z

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
| PYTHUSDT | IDLE | 1.71 | 8.33 | 0.87 | 0.08 | 49197192.27 | 1.91 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.12 | 0.06 | 214621974.71 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.1 | -0.0 | 1125238.06 | 6.45 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 4.14 | 0.53 | 0.1 | 773424.64 | 10.06 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.7 | -0.1 | 631145.4 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.44 | -0.01 | 544394.22 | 10.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.45 | 1.43 | -0.02 | 312713.87 | 22.51 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.48 | -0.07 | 225790.74 | 3.34 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 3.0 | 2.24 | -0.02 | 74820.32 | 22.86 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 3.22 | 1.15 | 0.03 | 87673.92 | 13.31 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.74 | -0.13 | 125417.58 | 11.83 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.5 | 0.05 | 46170.05 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.99 | -0.01 | 181127.31 | 3.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 91.62 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 2.0 | -0.0 | 136163.96 | 42.94 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.08 | 0.02 | 56307.17 | 8.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
