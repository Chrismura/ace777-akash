# Hulk DIGEST — 2026-09-10T14:15:01Z

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
| ETHUSDT | IDLE | 1.64 | 3.01 | 1.78 | -0.03 | 423375695.48 | 0.58 | skipped_fast |
| XRPUSDT | IDLE | 1.44 | 2.65 | 1.47 | -0.04 | 46073605.33 | 2.2 | skipped_fast |
| BTCUSDT | IDLE | 1.08 | 1.96 | 1.38 | -0.02 | 558661119.57 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 68.27 | 18.01 | -0.52 | 121899.31 | 123.2 | skipped_fast |
| PYTHUSDT | IDLE | 0.93 | 2.72 | 0.86 | -0.06 | 1007863.81 | 1.93 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 4.04 | 2.61 | -0.04 | 680221.1 | 9.88 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 4.54 | 2.83 | 0.02 | 182675.46 | 23.31 | skipped_fast |
| KITEUSDT | IDLE | 2.73 | 5.92 | 3.26 | -0.05 | 55995.52 | 11.04 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 5.8 | 1.91 | 0.06 | 229590.86 | 8.86 | skipped_fast |
| WUSDT | IDLE | 1.02 | 2.78 | 1.35 | -0.06 | 249129.11 | 15.71 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 2.96 | 2.22 | -0.07 | 80525.07 | 7.95 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.27 | 0.84 | -0.03 | 337881.68 | 1.32 | skipped_fast |
| CHIPUSDT | IDLE | 0.68 | 3.59 | 3.05 | -0.18 | 92096.42 | 12.7 | skipped_fast |
| RWAINCUSDT | IDLE | 1.34 | 2.33 | 2.27 | -0.03 | 5084.63 | 22.62 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 2.57 | 1.16 | -0.07 | 66941.99 | 19.64 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 3.88 | 3.02 | -0.03 | 82238.96 | 33.98 | skipped_fast |
| QNTUSDT | IDLE | 1.57 | 2.84 | 1.99 | -0.03 | 39546.24 | 3.06 | skipped_fast |
| FLUIDUSDT | IDLE | 1.68 | 3.96 | 3.81 | -0.09 | 2281.11 | 20.86 | skipped_fast |
| RWAUSDT | IDLE | 1.34 | 2.37 | 2.01 | -0.05 | 54481.43 | 22.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.98 | 1.77 | 1.26 | -0.03 | 25949.93 | 55.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
