# Hulk DIGEST — 2026-08-17T01:09:55Z

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
| XRPUSDT | IDLE | 0.71 | 1.36 | 0.36 | -0.0 | 7287807.87 | 1.0 | skipped_fast |
| RIZEUSDT | IDLE | 3.53 | 11.51 | 3.54 | 0.06 | 38158.65 | 56.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 7.33 | 6.39 | -0.02 | 296742.07 | 17.98 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.94 | 1.16 | -0.04 | 333125.63 | 11.53 | skipped_fast |
| WUSDT | IDLE | 1.39 | 2.74 | 0.28 | 0.02 | 182740.03 | 11.62 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 2.64 | 0.97 | -0.01 | 150580.0 | 2.57 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 3.05 | 1.29 | 0.03 | 56107.84 | 13.03 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 2.21 | 1.39 | -0.02 | 63048.48 | 8.27 | skipped_fast |
| ZBCNUSDT | IDLE | 0.74 | 1.4 | 0.56 | -0.01 | 188909.2 | 21.65 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.42 | 0.92 | -0.03 | 61698.09 | 18.47 | skipped_fast |
| KITEUSDT | IDLE | 0.5 | 0.92 | 0.57 | -0.02 | 54339.16 | 13.9 | skipped_fast |
| QAITUSDT | IDLE | 0.85 | 2.41 | 0.0 | -0.01 | 2196.8 | 61.3 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 2.94 | 0.48 | -0.01 | 90536.7 | 40.96 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 2.53 | 1.61 | -0.03 | 33569.5 | 5.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 1.31 | 0.34 | 0.04 | 4885.76 | 96.45 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.41 | 0.52 | -0.0 | 91166.15 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.7 | 0.43 | 0.0 | 50517.18 | 17.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.16 | 0.22 | 0.02 | 250.61 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
