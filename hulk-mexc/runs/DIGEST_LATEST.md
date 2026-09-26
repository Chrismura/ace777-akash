# Hulk DIGEST — 2026-09-26T05:53:14Z

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
| XRPUSDT | IDLE | 1.22 | 2.16 | 1.87 | 0.01 | 109973908.64 | 1.93 | skipped_fast |
| ETHUSDT | IDLE | 0.3 | 0.54 | 0.37 | 0.0 | 298201597.34 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.41 | 0.23 | -0.0 | 645455039.9 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 3.33 | 2.11 | 0.08 | 1183194.9 | 2.72 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 5.0 | 1.54 | 0.15 | 936450.56 | 9.75 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.29 | 2.18 | 0.01 | 867800.94 | 1.07 | skipped_fast |
| QNTUSDT | IDLE | 2.37 | 7.25 | 4.49 | 0.02 | 523370.39 | 11.94 | skipped_fast |
| WUSDT | IDLE | 1.42 | 2.68 | 1.44 | 0.06 | 463202.25 | 7.3 | skipped_fast |
| CHIPUSDT | IDLE | 2.02 | 5.19 | 4.19 | 0.05 | 148429.81 | 14.43 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 3.39 | 2.4 | 0.02 | 226234.17 | 24.65 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 5.34 | 2.05 | 0.09 | 78293.2 | 10.93 | skipped_fast |
| REDUSDT | IDLE | 1.75 | 3.38 | 2.13 | 0.04 | 59303.77 | 6.41 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 2.78 | 2.2 | 0.06 | 111530.91 | 6.16 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 1.64 | 0.71 | -0.0 | 170749.1 | 3.38 | skipped_fast |
| RWAINCUSDT | IDLE | 1.54 | 3.86 | 0.44 | -0.05 | 12577.41 | 98.38 | skipped_fast |
| RIZEUSDT | IDLE | 0.16 | 2.21 | 0.54 | -0.16 | 76830.45 | 33.62 | skipped_fast |
| TELUSDT | IDLE | 0.77 | 1.35 | 1.27 | 0.01 | 117694.51 | 24.54 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 1.83 | 1.79 | 0.0 | 3437.87 | 21.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.47 | 0.91 | 0.17 | 0.01 | 40929.49 | 8.92 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.89 | 0.74 | -0.01 | 53215.21 | 22.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
