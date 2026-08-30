# Hulk DIGEST — 2026-08-30T05:07:24Z

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
| XRPUSDT | IDLE | 0.45 | 0.86 | 0.27 | 0.01 | 16189109.96 | 1.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 5.18 | 1.67 | -0.04 | 823751.94 | 4.92 | skipped_fast |
| RIZEUSDT | IDLE | 2.97 | 12.31 | 3.0 | -0.04 | 44861.7 | 60.45 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 3.04 | 1.42 | 0.08 | 300841.56 | 6.7 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 1.88 | 1.12 | 0.0 | 316715.44 | 2.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 2.27 | 0.16 | -0.03 | 186519.8 | 9.9 | skipped_fast |
| WUSDT | IDLE | 1.04 | 1.97 | 0.72 | -0.01 | 191154.14 | 14.15 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.87 | 0.5 | 0.02 | 76846.94 | 9.89 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 1.39 | 0.83 | -0.01 | 68666.65 | 3.63 | skipped_fast |
| KITEUSDT | IDLE | 0.7 | 1.77 | 1.71 | 0.01 | 69353.07 | 7.8 | skipped_fast |
| EDELUSDT | IDLE | 0.27 | 5.05 | 1.37 | 0.08 | 121450.07 | 61.11 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.75 | 1.03 | -0.01 | 142142.49 | 2.67 | skipped_fast |
| TELUSDT | IDLE | 1.21 | 2.35 | 0.47 | -0.04 | 72157.59 | 29.58 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.57 | 1.3 | 0.0 | 54471.58 | 16.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.61 | 1.24 | 0.01 | 1482.06 | 21.49 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.09 | 0.69 | -0.0 | 31584.63 | 8.12 | skipped_fast |
| RWAINCUSDT | IDLE | 0.16 | 0.28 | 0.28 | -0.04 | 1577.44 | 107.37 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
