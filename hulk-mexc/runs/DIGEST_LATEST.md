# Hulk DIGEST — 2026-10-16T20:05:35Z

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
| PYTHUSDT | IDLE | 1.93 | 6.8 | 5.39 | -0.12 | 2036536.2 | 3.57 | skipped_fast |
| WUSDT | IDLE | 2.44 | 6.06 | 4.64 | -0.04 | 1736951.27 | 16.27 | skipped_fast |
| XRPUSDT | IDLE | 1.69 | 3.07 | 2.08 | -0.03 | 28492344.13 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 1.54 | 2.78 | 1.96 | -0.02 | 212536307.63 | 0.17 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.43 | 0.43 | -0.01 | 359969938.42 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 3.33 | 2.47 | -0.04 | 784914.94 | 1.49 | skipped_fast |
| EDELUSDT | IDLE | 3.07 | 5.45 | 4.65 | 0.0 | 189524.74 | 54.4 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 6.9 | 6.46 | -0.1 | 97092.52 | 11.27 | skipped_fast |
| ZBCNUSDT | IDLE | 2.37 | 4.27 | 3.08 | -0.04 | 201380.2 | 23.84 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.49 | 1.42 | -0.04 | 385203.3 | 10.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.98 | 9.03 | 8.28 | -0.13 | 26035.15 | 5.79 | skipped_fast |
| HBARUSDT | IDLE | 2.35 | 4.2 | 3.32 | -0.03 | 306536.85 | 9.66 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 5.31 | 4.5 | -0.02 | 152380.37 | 13.25 | skipped_fast |
| BIOUSDT | IDLE | 1.92 | 3.52 | 2.19 | -0.03 | 61989.73 | 3.99 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.52 | 2.3 | -0.04 | 56304.65 | 12.56 | skipped_fast |
| RWAUSDT | IDLE | 2.08 | 3.9 | 1.8 | -0.0 | 53153.89 | 15.91 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 2.25 | 0.32 | -0.0 | 46287.29 | 36.48 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 3.33 | 3.0 | -0.02 | 94374.0 | 40.1 | skipped_fast |
| FLUIDUSDT | IDLE | 1.71 | 3.4 | 0.2 | -0.0 | 6555.69 | 19.14 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 0.88 | 0.88 | -0.01 | 34714.83 | 55.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
