# Hulk DIGEST — 2026-10-11T11:53:47Z

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
| XRPUSDT | IDLE | 0.39 | 0.74 | 0.29 | -0.01 | 10047995.37 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.21 | 0.41 | 0.08 | 0.0 | 177538577.67 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.16 | 0.3 | 0.11 | 0.0 | 123266753.21 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.23 | 3.27 | 1.88 | 0.01 | 1187051.9 | 12.03 | skipped_fast |
| QNTUSDT | IDLE | 1.94 | 3.91 | 0.62 | -0.02 | 1077875.07 | 0.41 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 31.62 | 15.5 | 0.06 | 55918.37 | 21.45 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.76 | 1.96 | -0.02 | 717469.83 | 2.61 | skipped_fast |
| RIZEUSDT | IDLE | 3.28 | 9.17 | 4.41 | -0.06 | 35842.83 | 38.02 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 10.39 | 3.09 | 0.28 | 365731.04 | 11.99 | skipped_fast |
| EDELUSDT | IDLE | 1.91 | 3.43 | 2.59 | -0.02 | 372168.68 | 46.24 | skipped_fast |
| CCUSDT | IDLE | 1.82 | 3.44 | 1.33 | 0.0 | 251738.62 | 7.46 | skipped_fast |
| BIOUSDT | IDLE | 2.0 | 3.67 | 2.24 | 0.02 | 74655.96 | 6.83 | skipped_fast |
| TELUSDT | IDLE | 3.03 | 5.34 | 4.85 | -0.08 | 143698.49 | 35.19 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 1.71 | 0.88 | -0.01 | 154159.61 | 8.39 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.2 | 1.72 | -0.01 | 58339.69 | 9.44 | skipped_fast |
| KITEUSDT | IDLE | 0.68 | 1.24 | 0.81 | -0.0 | 74233.02 | 10.32 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.26 | 0.89 | -0.02 | 19203.61 | 20.08 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.74 | 0.85 | -0.01 | 222795.77 | 6.55 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.64 | 0.32 | -0.01 | 52662.58 | 23.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.33 | 0.0 | -0.01 | 32148.71 | 4.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
