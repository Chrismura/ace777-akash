# Hulk DIGEST — 2026-10-10T06:50:12Z

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
| WUSDT | IDLE | 2.34 | 6.03 | 3.98 | -0.03 | 1950442.04 | 7.6 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 4.61 | 3.44 | -0.06 | 1478560.39 | 1.26 | skipped_fast |
| XRPUSDT | IDLE | 0.53 | 1.02 | 0.27 | 0.0 | 24160450.11 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.22 | 0.42 | 0.15 | -0.0 | 139640294.51 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.06 | 0.0 | 240243549.52 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 2.09 | 2.04 | -0.01 | 1211477.92 | 2.45 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 2.33 | 1.44 | 0.03 | 574391.68 | 8.22 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 2.42 | 0.94 | -0.09 | 264535.03 | 13.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.15 | 3.92 | 0.26 | 0.08 | 88498.8 | 7.45 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.59 | 0.96 | 0.02 | 61806.19 | 10.35 | skipped_fast |
| EDELUSDT | IDLE | 0.62 | 2.37 | 1.53 | 0.13 | 207211.41 | 12.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 5.68 | 5.09 | 0.05 | 67084.69 | 31.9 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 2.16 | 1.33 | 0.01 | 57961.95 | 7.35 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 2.04 | 0.77 | -0.03 | 75894.89 | 10.64 | skipped_fast |
| RWAINCUSDT | IDLE | 1.16 | 2.29 | 0.14 | 0.04 | 8509.11 | 38.06 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.52 | 0.39 | 0.0 | 304134.95 | 4.31 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.08 | 2.68 | -0.01 | 52051.67 | 15.74 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 2.61 | 0.05 | 0.01 | 112347.47 | 31.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.42 | 0.58 | 0.01 | 41950.46 | 5.4 | skipped_fast |
| FLUIDUSDT | IDLE | 0.23 | 1.44 | 0.24 | 0.01 | 18653.96 | 19.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
