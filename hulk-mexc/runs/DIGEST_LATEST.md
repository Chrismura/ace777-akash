# Hulk DIGEST — 2026-08-22T17:26:57Z

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
| PYTHUSDT | IDLE | 1.74 | 8.48 | 1.0 | 0.12 | 49119854.7 | 1.91 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.5 | 0.07 | 213692553.01 | 2.71 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 4.25 | 0.67 | 0.11 | 769018.65 | 7.54 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.97 | 0.01 | 1095054.82 | 3.87 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.9 | -0.09 | 631358.28 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.59 | 2.58 | 0.19 | 0.0 | 533143.71 | 13.68 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 7.96 | 6.33 | -0.07 | 228232.84 | 3.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.45 | 1.42 | -0.02 | 306381.91 | 24.57 | skipped_fast |
| EDELUSDT | IDLE | 1.75 | 3.11 | 2.57 | -0.02 | 74935.26 | 22.96 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 3.22 | 0.9 | 0.04 | 89163.93 | 7.08 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 1.7 | -0.13 | 122116.35 | 2.67 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 2.63 | 0.79 | 0.04 | 46146.59 | 45.71 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.97 | -0.01 | 181229.96 | 1.57 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.79 | -0.0 | 131883.13 | 42.83 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.08 | 0.02 | 56237.61 | 8.08 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 17.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
