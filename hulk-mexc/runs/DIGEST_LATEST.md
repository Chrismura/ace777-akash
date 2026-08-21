# Hulk DIGEST — 2026-08-21T22:38:36Z

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
| PYTHUSDT | IDLE | 1.37 | 5.17 | 0.39 | 0.11 | 5833067.59 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.59 | 5.94 | 0.28 | 0.15 | 134948297.57 | 2.08 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 6.86 | 0.0 | 0.14 | 659996.12 | 7.08 | skipped_fast |
| HBARUSDT | IDLE | 2.22 | 4.71 | 0.8 | 0.08 | 873809.3 | 2.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 6.77 | 0.07 | 0.11 | 504558.65 | 2.45 | skipped_fast |
| WUSDT | IDLE | 2.46 | 5.3 | 0.24 | 0.08 | 371192.55 | 14.38 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.57 | 0.05 | 533668.3 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 0.98 | 0.03 | 188311.77 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.29 | 0.18 | 156025.34 | 20.26 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.22 | -0.03 | 82605.41 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10279.27 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.05 | 186935.64 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3825.97 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 1.02 | 0.11 | 61480.86 | 13.81 | skipped_fast |
| QNTUSDT | IDLE | 2.09 | 4.18 | 0.0 | 0.06 | 78853.02 | 1.52 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.79 | 0.06 | 56376.48 | 45.14 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.0 | 0.04 | 54146.88 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 8.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
