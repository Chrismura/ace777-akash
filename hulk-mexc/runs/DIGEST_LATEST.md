# Hulk DIGEST — 2026-09-12T09:22:01Z

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
| ETHUSDT | IDLE | 0.48 | 1.11 | 0.1 | 0.02 | 611680335.91 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.29 | 0.63 | 0.12 | 0.01 | 51152568.21 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.26 | 0.02 | 0.0 | 557726606.28 | 0.0 | skipped_fast |
| RWAINCUSDT | IDLE | 3.2 | 6.82 | 0.0 | 0.06 | 16132.02 | 10.45 | skipped_fast |
| PYTHUSDT | IDLE | 1.08 | 2.21 | 0.26 | 0.03 | 412490.28 | 1.89 | skipped_fast |
| CCUSDT | IDLE | 0.55 | 1.06 | 0.32 | 0.0 | 383481.04 | 8.08 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 2.88 | 1.95 | -0.03 | 60200.5 | 10.37 | skipped_fast |
| ZBCNUSDT | IDLE | 0.76 | 1.5 | 0.18 | 0.0 | 214963.07 | 8.3 | skipped_fast |
| WUSDT | IDLE | 0.69 | 1.31 | 1.08 | 0.02 | 199939.2 | 13.33 | skipped_fast |
| EDELUSDT | IDLE | 0.91 | 2.5 | 1.4 | 0.06 | 169866.95 | 35.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.08 | 3.08 | 1.2 | 0.05 | 89361.48 | 18.8 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 2.4 | 1.55 | 0.05 | 65247.55 | 18.84 | skipped_fast |
| RIZEUSDT | IDLE | 0.14 | 9.79 | 1.36 | 1.02 | 188635.94 | 71.98 | skipped_fast |
| BIOUSDT | IDLE | 0.61 | 1.15 | 0.51 | 0.02 | 82235.9 | 7.87 | skipped_fast |
| HBARUSDT | IDLE | 0.42 | 0.78 | 0.39 | 0.0 | 248310.41 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.73 | 0.94 | -0.02 | 100250.53 | 23.65 | skipped_fast |
| QNTUSDT | IDLE | 0.53 | 1.02 | 0.29 | -0.01 | 48555.93 | 4.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.58 | 1.1 | 0.36 | -0.0 | 27075.86 | 13.95 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.59 | 0.07 | 0.03 | 53270.14 | 14.79 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.03 | 1625.5 | 22.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
