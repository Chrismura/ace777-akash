# Hulk DIGEST — 2026-09-25T23:49:11Z

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
| XRPUSDT | IDLE | 1.02 | 1.94 | 0.66 | 0.02 | 115644194.17 | 1.91 | skipped_fast |
| ETHUSDT | IDLE | 0.43 | 0.81 | 0.28 | 0.0 | 321050848.66 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.65 | 0.13 | -0.0 | 689518790.79 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.09 | 5.67 | 1.42 | 0.09 | 1245355.7 | 5.39 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 4.89 | 1.88 | 0.15 | 861761.72 | 10.75 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.33 | 0.77 | 0.03 | 936904.83 | 1.05 | skipped_fast |
| WUSDT | IDLE | 2.0 | 3.88 | 0.75 | 0.05 | 434476.57 | 6.47 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 4.72 | 3.66 | 0.0 | 183063.78 | 13.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.98 | 4.39 | 3.93 | 0.05 | 244686.41 | 20.97 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 18.48 | 12.56 | 0.06 | 109035.18 | 64.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.07 | 5.74 | 0.12 | 0.06 | 162070.56 | 17.77 | skipped_fast |
| QNTUSDT | IDLE | 0.74 | 3.19 | 1.06 | 0.1 | 570164.38 | 3.04 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 3.35 | 0.84 | 0.07 | 115199.51 | 6.05 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.87 | 1.11 | 0.08 | 136920.96 | 13.81 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.85 | 0.01 | 0.02 | 80075.29 | 9.74 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 2.15 | 0.75 | -0.08 | 13525.58 | 15.09 | skipped_fast |
| TELUSDT | IDLE | 1.21 | 2.15 | 1.8 | -0.0 | 115595.23 | 55.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.25 | 0.82 | 0.02 | 41230.53 | 5.09 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.04 | 0.88 | -0.01 | 54400.94 | 29.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 0.68 | 0.52 | 0.03 | 3316.59 | 22.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
