# Hulk DIGEST — 2026-09-14T01:41:07Z

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
| XRPUSDT | IDLE | 1.16 | 2.12 | 1.36 | -0.02 | 19478963.56 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 1.13 | 2.06 | 1.33 | -0.02 | 287910546.48 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.39 | 0.76 | -0.01 | 297176400.09 | 0.01 | skipped_fast |
| PYTHUSDT | IDLE | 2.26 | 4.44 | 2.13 | 0.03 | 449975.98 | 3.53 | skipped_fast |
| WUSDT | IDLE | 2.27 | 4.21 | 2.15 | -0.03 | 210314.44 | 9.08 | skipped_fast |
| EDELUSDT | IDLE | 1.97 | 6.54 | 3.36 | 0.09 | 213773.02 | 30.33 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.17 | 0.93 | -0.02 | 315198.12 | 3.14 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 3.32 | 2.14 | -0.0 | 200977.36 | 32.24 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.46 | 3.64 | -0.01 | 9280.28 | 21.94 | skipped_fast |
| BIOUSDT | IDLE | 2.02 | 3.72 | 2.07 | -0.01 | 70775.79 | 3.98 | skipped_fast |
| REDUSDT | IDLE | 2.03 | 4.06 | 0.0 | 0.01 | 88752.43 | 16.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 6.25 | 4.46 | -0.13 | 95901.25 | 19.25 | skipped_fast |
| HBARUSDT | IDLE | 2.0 | 3.62 | 2.58 | 0.01 | 255440.64 | 1.32 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.76 | 1.03 | -0.0 | 60283.44 | 12.18 | skipped_fast |
| RIZEUSDT | IDLE | 0.6 | 8.56 | 6.57 | -0.03 | 65380.28 | 72.36 | skipped_fast |
| QNTUSDT | IDLE | 1.97 | 3.53 | 2.76 | -0.02 | 38097.18 | 7.96 | skipped_fast |
| TELUSDT | IDLE | 1.25 | 2.25 | 1.63 | -0.05 | 83755.85 | 31.98 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.0 | 1.96 | -0.01 | 1325.28 | 22.1 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.67 | 0.44 | 0.0 | 54630.64 | 7.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.47 | 0.36 | -0.0 | 30084.26 | 4.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
