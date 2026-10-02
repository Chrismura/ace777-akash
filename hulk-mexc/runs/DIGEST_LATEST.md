# Hulk DIGEST — 2026-10-02T03:21:09Z

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
| QNTUSDT | IDLE | 1.27 | 7.79 | 4.14 | -0.15 | 6611729.71 | 10.36 | skipped_fast |
| XRPUSDT | IDLE | 0.77 | 1.48 | 0.38 | 0.01 | 40081551.55 | 2.0 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.27 | 0.45 | 0.01 | 371574008.86 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.15 | 0.31 | 0.02 | 684858829.64 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.25 | 1.15 | -0.03 | 387797.16 | 3.98 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 1.63 | 1.54 | -0.06 | 545045.42 | 5.0 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.67 | 0.74 | -0.01 | 676802.81 | 3.86 | skipped_fast |
| RIZEUSDT | IDLE | 2.41 | 10.54 | 6.36 | -0.0 | 42929.5 | 41.35 | skipped_fast |
| WUSDT | IDLE | 1.04 | 2.02 | 0.43 | -0.01 | 430360.15 | 15.69 | skipped_fast |
| ZBCNUSDT | IDLE | 0.91 | 2.73 | 1.06 | -0.07 | 337798.89 | 20.06 | skipped_fast |
| EDELUSDT | IDLE | 0.94 | 6.44 | 3.51 | 0.15 | 165678.36 | 19.02 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 2.83 | 2.26 | 0.03 | 107367.31 | 10.08 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 2.5 | 0.55 | -0.01 | 89335.12 | 9.27 | skipped_fast |
| BIOUSDT | IDLE | 0.82 | 1.57 | 0.53 | -0.03 | 78421.46 | 6.61 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 1.55 | 1.25 | -0.02 | 66402.51 | 13.68 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 1.79 | 1.02 | 0.04 | 25132.22 | 37.26 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 2.52 | 1.76 | -0.08 | 142980.84 | 28.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.24 | 2.48 | 0.0 | 0.03 | 4372.17 | 21.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.71 | 0.57 | 0.0 | 36457.91 | 22.17 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.51 | 0.29 | 0.01 | 54466.21 | 43.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
