# Hulk DIGEST — 2026-09-23T11:07:38Z

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
| XRPUSDT | IDLE | 1.97 | 3.74 | 2.61 | 0.04 | 121894779.82 | 1.25 | skipped_fast |
| PYTHUSDT | IDLE | 0.95 | 4.33 | 0.95 | 0.1 | 1888372.76 | 2.95 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.29 | 0.98 | -0.0 | 403676620.78 | 0.04 | skipped_fast |
| HBARUSDT | IDLE | 2.14 | 3.93 | 3.32 | 0.04 | 1639416.6 | 1.03 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.09 | 0.88 | -0.0 | 848414816.15 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.32 | 4.15 | 3.22 | -0.04 | 424694.02 | 8.88 | skipped_fast |
| WUSDT | IDLE | 1.59 | 2.97 | 1.41 | 0.04 | 399906.9 | 8.17 | skipped_fast |
| CHIPUSDT | IDLE | 2.46 | 4.57 | 2.36 | -0.0 | 194677.17 | 19.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 4.09 | 3.19 | 0.04 | 216972.63 | 0.48 | skipped_fast |
| KITEUSDT | IDLE | 1.77 | 3.47 | 0.51 | 0.05 | 137798.21 | 10.87 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.2 | 1.6 | 0.06 | 116419.43 | 9.95 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.5 | 1.84 | 0.04 | 58958.12 | 8.71 | skipped_fast |
| EDELUSDT | IDLE | 0.52 | 2.43 | 1.62 | -0.07 | 242639.32 | 26.46 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 2.23 | 1.44 | 0.03 | 20368.18 | 5.38 | skipped_fast |
| QNTUSDT | IDLE | 1.29 | 2.55 | 1.11 | 0.08 | 238902.71 | 13.33 | skipped_fast |
| RIZEUSDT | IDLE | 0.58 | 12.5 | 1.56 | 0.5 | 63763.64 | 92.08 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 5.65 | 5.19 | 0.11 | 152382.32 | 89.89 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.94 | 0.58 | 0.01 | 54529.52 | 14.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.68 | 0.42 | 0.01 | 40454.58 | 21.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.84 | 0.26 | 0.01 | 5019.56 | 21.0 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
