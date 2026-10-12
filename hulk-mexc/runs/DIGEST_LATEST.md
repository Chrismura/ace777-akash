# Hulk DIGEST — 2026-10-12T01:29:53Z

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
| WUSDT | IDLE | 2.0 | 17.91 | 4.88 | 0.27 | 5031817.25 | 17.11 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.37 | 0.37 | 0.01 | 199497684.82 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.58 | 1.07 | 0.58 | 0.0 | 16913498.98 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.88 | 0.29 | 0.01 | 160793878.98 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.17 | 3.94 | 2.66 | -0.0 | 898541.31 | 1.28 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.48 | 1.44 | -0.0 | 732464.87 | 1.67 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 3.19 | 1.43 | 0.06 | 368438.91 | 6.36 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 2.86 | 0.74 | -0.02 | 352617.89 | 26.5 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 4.84 | 4.53 | -0.05 | 253325.56 | 15.0 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.54 | 2.11 | 0.02 | 96520.09 | 6.75 | skipped_fast |
| ZBCNUSDT | IDLE | 0.95 | 1.76 | 0.94 | -0.0 | 227851.93 | 20.0 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.26 | 1.45 | -0.0 | 62610.38 | 11.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 2.64 | 2.28 | -0.0 | 26785.81 | 4.97 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.64 | 1.62 | -0.0 | 55596.41 | 14.72 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.78 | 0.78 | 0.01 | 284905.64 | 4.26 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 2.48 | 1.84 | -0.02 | 171070.18 | 29.32 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 3.69 | 3.0 | 0.06 | 38094.68 | 58.33 | skipped_fast |
| FLUIDUSDT | IDLE | 0.47 | 3.21 | 3.11 | 0.03 | 67168.62 | 20.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.68 | 1.24 | 0.77 | -0.0 | 33856.63 | 12.29 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.54 | 0.23 | 0.02 | 52549.5 | 23.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
