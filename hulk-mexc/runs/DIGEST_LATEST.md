# Hulk DIGEST — 2026-10-16T04:07:02Z

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
| WUSDT | IDLE | 2.9 | 7.08 | 1.7 | 0.02 | 2358105.71 | 13.86 | skipped_fast |
| PYTHUSDT | IDLE | 0.55 | 3.35 | 0.54 | 0.14 | 4262426.15 | 4.22 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.29 | 0.75 | 0.03 | 253512245.62 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.31 | 0.69 | 0.02 | 40657195.26 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 1.01 | 0.59 | 0.01 | 451123074.08 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 3.35 | 1.56 | 0.06 | 1184042.05 | 1.45 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 3.28 | 1.57 | -0.02 | 437638.51 | 9.38 | skipped_fast |
| CHIPUSDT | IDLE | 1.97 | 10.67 | 3.58 | 0.08 | 173652.77 | 13.93 | skipped_fast |
| REDUSDT | IDLE | 2.23 | 6.55 | 5.5 | -0.07 | 94057.64 | 8.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.67 | 3.2 | 1.94 | 0.05 | 185906.67 | 17.09 | skipped_fast |
| KITEUSDT | IDLE | 1.94 | 3.44 | 2.87 | 0.01 | 68366.98 | 9.07 | skipped_fast |
| EDELUSDT | IDLE | 0.85 | 2.46 | 1.35 | -0.1 | 217711.75 | 13.71 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 2.08 | 1.0 | 0.03 | 74552.59 | 7.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.43 | 2.17 | 0.0 | 28863.05 | 35.33 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 2.26 | 1.8 | 0.04 | 217273.05 | 3.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.68 | 1.73 | 1.7 | 0.04 | 73064.78 | 26.65 | skipped_fast |
| TELUSDT | IDLE | 0.82 | 1.53 | 0.78 | 0.04 | 84586.25 | 28.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.74 | 0.69 | -0.01 | 9529.57 | 21.58 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.48 | 0.16 | 0.02 | 52665.9 | 7.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.37 | 0.31 | 0.0 | 38056.55 | 23.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
