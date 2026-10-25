# Hulk DIGEST — 2026-10-25T02:57:04Z

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
| XRPUSDT | IDLE | 0.91 | 1.82 | 0.01 | 0.02 | 25743902.19 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.81 | 1.59 | 0.19 | -0.01 | 123034485.16 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.84 | 0.08 | -0.0 | 250067658.03 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.3 | 2.79 | 2.18 | -0.06 | 778573.56 | 66.9 | skipped_fast |
| PYTHUSDT | IDLE | 1.77 | 3.36 | 1.24 | 0.0 | 519593.59 | 2.81 | skipped_fast |
| ZBCNUSDT | IDLE | 2.37 | 5.28 | 3.88 | 0.01 | 228347.59 | 14.79 | skipped_fast |
| EDELUSDT | IDLE | 0.82 | 2.08 | 0.49 | -0.06 | 591746.96 | 13.21 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.08 | 8.8 | 1.79 | -0.01 | 42248.04 | 43.94 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.62 | 3.2 | 0.02 | 87430.19 | 17.87 | skipped_fast |
| QNTUSDT | IDLE | 1.83 | 3.56 | 0.71 | -0.0 | 364493.69 | 0.55 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 3.84 | 3.29 | -0.0 | 99434.39 | 15.68 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.0 | 2.83 | -0.05 | 60276.16 | 13.22 | skipped_fast |
| LAUSDT | IDLE | 2.06 | 11.5 | 7.6 | -0.04 | 107421.98 | 21.61 | skipped_fast |
| CCUSDT | IDLE | 0.7 | 1.26 | 0.9 | -0.02 | 219650.84 | 6.93 | skipped_fast |
| BIOUSDT | IDLE | 1.25 | 2.25 | 1.64 | -0.03 | 66438.63 | 4.39 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.71 | 0.7 | -0.0 | 54418.53 | 5.44 | skipped_fast |
| WAXLUSDT | IDLE | 2.3 | 5.99 | 4.24 | -0.01 | 57024.57 | 51.17 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.22 | 0.1 | -0.0 | 200503.66 | 11.52 | skipped_fast |
| FLUIDUSDT | IDLE | 1.38 | 2.8 | 1.39 | -0.04 | 13054.05 | 21.26 | skipped_fast |
| IOTAUSDT | IDLE | 1.13 | 2.01 | 1.63 | -0.03 | 68001.28 | 25.26 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.64 | 0.24 | -0.0 | 53850.06 | 15.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.14 | -0.01 | 37652.65 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
