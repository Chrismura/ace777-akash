# Hulk DIGEST — 2026-09-18T13:27:47Z

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
| XRPUSDT | IDLE | 1.0 | 1.81 | 1.23 | 0.02 | 40937949.56 | 2.27 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.41 | 0.69 | 0.02 | 374007670.22 | 0.72 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.04 | 0.5 | 0.02 | 555383547.8 | 0.38 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 6.0 | 3.59 | 0.08 | 651391.06 | 9.21 | skipped_fast |
| PYTHUSDT | IDLE | 1.74 | 4.64 | 3.41 | 0.08 | 666934.31 | 1.7 | skipped_fast |
| WUSDT | IDLE | 1.01 | 2.78 | 1.28 | 0.1 | 430986.69 | 13.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 7.51 | 2.55 | 0.15 | 167671.57 | 18.31 | skipped_fast |
| BIOUSDT | IDLE | 1.86 | 4.65 | 3.68 | 0.06 | 87864.4 | 3.75 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 2.34 | 1.22 | 0.03 | 503366.6 | 1.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.04 | 1.92 | 1.05 | 0.04 | 269684.02 | 31.02 | skipped_fast |
| EDELUSDT | IDLE | 0.48 | 4.61 | 3.45 | -0.07 | 255752.26 | 21.52 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 3.78 | 0.77 | 0.08 | 64494.55 | 19.86 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 2.93 | 1.18 | 0.06 | 76870.47 | 11.76 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 5.92 | 0.66 | 0.04 | 88375.78 | 53.05 | skipped_fast |
| FLUIDUSDT | IDLE | 2.42 | 4.83 | 0.07 | 0.07 | 763.27 | 15.45 | skipped_fast |
| RWAINCUSDT | IDLE | 0.84 | 1.49 | 1.29 | -0.02 | 11788.16 | 17.92 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.29 | 0.22 | 0.03 | 44279.14 | 11.04 | skipped_fast |
| RIZEUSDT | IDLE | 0.2 | 2.49 | 1.73 | 0.18 | 51896.24 | 81.74 | skipped_fast |
| RWAUSDT | IDLE | 1.38 | 2.46 | 2.04 | 0.0 | 58772.46 | 66.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.25 | 0.05 | 0.03 | 42435.91 | 2.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
