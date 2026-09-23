# Hulk DIGEST — 2026-09-23T09:18:18Z

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
| XRPUSDT | IDLE | 2.25 | 4.59 | 3.42 | 0.05 | 119388237.25 | 1.25 | skipped_fast |
| PYTHUSDT | IDLE | 0.68 | 3.18 | 1.57 | 0.07 | 1817899.65 | 4.5 | skipped_fast |
| ETHUSDT | IDLE | 1.24 | 2.22 | 1.7 | 0.0 | 403034239.22 | 0.22 | skipped_fast |
| BTCUSDT | IDLE | 1.03 | 1.84 | 1.5 | 0.0 | 853607912.36 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.02 | 4.03 | 3.38 | 0.01 | 1685536.97 | 2.05 | skipped_fast |
| CCUSDT | IDLE | 2.48 | 4.52 | 2.97 | -0.03 | 407674.33 | 6.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.77 | 5.08 | 3.03 | -0.03 | 201706.14 | 17.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.04 | 4.8 | 3.39 | 0.04 | 217034.08 | 19.8 | skipped_fast |
| WUSDT | IDLE | 1.17 | 2.32 | 0.09 | 0.05 | 323352.83 | 10.46 | skipped_fast |
| BIOUSDT | IDLE | 1.76 | 3.2 | 2.12 | 0.04 | 116694.43 | 16.69 | skipped_fast |
| KITEUSDT | IDLE | 1.52 | 2.95 | 2.06 | 0.05 | 133888.61 | 8.16 | skipped_fast |
| EDELUSDT | IDLE | 0.65 | 3.1 | 1.49 | -0.05 | 255114.96 | 3.28 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.76 | 0.13 | 0.04 | 60399.09 | 21.39 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 12.5 | 2.91 | 0.5 | 63849.64 | 96.59 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 2.01 | 1.91 | 0.03 | 21566.13 | 27.09 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 2.57 | 0.49 | 0.12 | 241875.57 | 6.62 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 5.65 | 3.17 | 0.14 | 124619.92 | 54.59 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 1.95 | 1.91 | 0.0 | 2562.84 | 22.42 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.02 | 0.79 | 0.01 | 53835.82 | 21.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.55 | 0.33 | 0.01 | 40274.77 | 14.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
