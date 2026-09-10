# Hulk DIGEST — 2026-09-10T13:15:21Z

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
| ETHUSDT | IDLE | 1.71 | 3.01 | 2.74 | -0.04 | 371934809.19 | 0.71 | skipped_fast |
| XRPUSDT | IDLE | 1.49 | 2.65 | 2.23 | -0.06 | 45566636.9 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 1.11 | 1.96 | 1.8 | -0.03 | 545676876.25 | 0.08 | skipped_fast |
| RIZEUSDT | IDLE | 1.25 | 68.27 | 22.39 | -0.55 | 114227.24 | 108.93 | skipped_fast |
| CCUSDT | IDLE | 2.64 | 4.72 | 3.69 | -0.05 | 674995.24 | 6.95 | skipped_fast |
| PYTHUSDT | IDLE | 0.96 | 2.72 | 1.59 | -0.08 | 1019497.46 | 1.95 | skipped_fast |
| KITEUSDT | IDLE | 3.1 | 6.55 | 4.96 | -0.06 | 55852.79 | 12.09 | skipped_fast |
| ZBCNUSDT | IDLE | 2.73 | 4.79 | 4.49 | -0.02 | 179327.51 | 25.29 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 6.26 | 3.2 | 0.05 | 229486.59 | 26.77 | skipped_fast |
| WUSDT | IDLE | 1.11 | 2.96 | 1.88 | -0.07 | 251451.7 | 18.91 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 2.96 | 2.6 | -0.08 | 82613.05 | 7.97 | skipped_fast |
| HBARUSDT | IDLE | 1.35 | 2.4 | 1.97 | -0.05 | 341238.07 | 2.67 | skipped_fast |
| REDUSDT | IDLE | 1.04 | 2.57 | 1.44 | -0.09 | 66242.78 | 10.64 | skipped_fast |
| CHIPUSDT | IDLE | 0.65 | 3.34 | 3.19 | -0.19 | 93492.16 | 14.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.27 | 1.89 | -0.01 | 5981.8 | 22.59 | skipped_fast |
| TELUSDT | IDLE | 2.22 | 3.88 | 3.73 | -0.03 | 90690.88 | 34.07 | skipped_fast |
| QNTUSDT | IDLE | 1.67 | 2.95 | 2.64 | -0.04 | 39241.34 | 4.62 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 3.96 | 3.81 | -0.1 | 2472.1 | 21.86 | skipped_fast |
| RWAUSDT | IDLE | 1.35 | 2.37 | 2.16 | -0.05 | 54092.11 | 15.27 | skipped_fast |
| MNSRYUSDT | IDLE | 0.91 | 1.64 | 1.2 | -0.03 | 25199.95 | 65.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
