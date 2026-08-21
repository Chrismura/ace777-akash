# Hulk DIGEST — 2026-08-21T21:30:17Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.84 | 0.1 | 5633056.9 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.13 | 3.73 | 1.52 | 0.11 | 129126200.62 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 4.03 | 0.05 | 517577.37 | 3.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.25 | 0.1 | 485693.94 | 40.43 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.14 | 0.13 | 0.1 | 644964.1 | 4.59 | skipped_fast |
| HBARUSDT | IDLE | 1.55 | 3.04 | 0.42 | 0.07 | 813157.07 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.83 | 0.41 | 0.07 | 367525.02 | 10.45 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.93 | 0.02 | 187009.47 | 6.27 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.28 | 0.17 | 153988.42 | 21.3 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.12 | 1.98 | -0.05 | 83341.62 | 22.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.47 | 0.02 | 56019.0 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.59 | 0.04 | 10203.58 | 37.62 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 1.53 | 0.12 | 61087.36 | 9.22 | skipped_fast |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3782.1 | 139.58 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.39 | 0.63 | 0.02 | 178689.91 | 53.25 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.65 | 0.75 | 0.04 | 63280.39 | 1.55 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.17 | 0.33 | 0.03 | 53842.32 | 16.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
