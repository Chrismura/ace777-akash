# Hulk DIGEST — 2026-10-22T12:31:08Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 0.82 | 3.67 | 3.54 | -0.06 | 3246643.74 | 17.87 | skipped_fast |
| ETHUSDT | IDLE | 0.9 | 1.62 | 1.25 | -0.03 | 223775164.34 | 0.17 | skipped_fast |
| XRPUSDT | IDLE | 0.88 | 1.58 | 1.16 | -0.02 | 32821341.16 | 1.51 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.06 | 0.86 | -0.02 | 530554509.56 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 1.94 | 1.33 | -0.05 | 1374053.71 | 6.2 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 2.2 | 2.13 | -0.03 | 1285261.17 | 1.03 | skipped_fast |
| EDELUSDT | IDLE | 2.73 | 4.87 | 3.95 | -0.05 | 564380.07 | 9.12 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 2.84 | 1.51 | -0.07 | 629018.81 | 4.02 | skipped_fast |
| ZBCNUSDT | IDLE | 2.23 | 6.18 | 1.99 | -0.05 | 223655.26 | 22.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.15 | 4.83 | 2.32 | -0.03 | 338217.59 | 15.86 | skipped_fast |
| CCUSDT | IDLE | 0.81 | 2.43 | 2.01 | -0.04 | 396717.47 | 9.71 | skipped_fast |
| RWAINCUSDT | IDLE | 1.85 | 3.51 | 1.22 | 0.0 | 65009.75 | 5.63 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 1.96 | 1.5 | -0.03 | 85617.38 | 17.62 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.81 | 0.83 | -0.04 | 77533.05 | 8.35 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 1.83 | 0.46 | -0.02 | 60173.79 | 12.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.0 | 0.6 | 0.04 | 43723.42 | 58.68 | skipped_fast |
| IOTAUSDT | IDLE | 0.95 | 1.85 | 1.23 | -0.04 | 78056.12 | 8.87 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 3.67 | 3.26 | -0.03 | 19562.57 | 21.35 | skipped_fast |
| LAUSDT | IDLE | 0.71 | 1.91 | 0.81 | -0.03 | 58261.33 | 25.25 | skipped_fast |
| WAXLUSDT | IDLE | 0.9 | 3.18 | 1.65 | -0.09 | 58528.73 | 63.53 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.95 | 0.55 | -0.01 | 52767.68 | 15.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.57 | 0.21 | 0.0 | 40207.65 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
