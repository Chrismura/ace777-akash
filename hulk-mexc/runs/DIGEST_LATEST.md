# Hulk DIGEST — 2026-09-19T07:57:19Z

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
| XRPUSDT | IDLE | 1.06 | 2.18 | 1.82 | 0.06 | 69814770.24 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.49 | 0.93 | 0.29 | 0.06 | 596703421.21 | 0.23 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.63 | 0.3 | 0.04 | 672869839.91 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.54 | 4.45 | 3.02 | 0.06 | 968439.8 | 8.32 | skipped_fast |
| PYTHUSDT | IDLE | 2.69 | 4.8 | 3.81 | -0.01 | 699133.25 | 5.03 | skipped_fast |
| CCUSDT | IDLE | 2.2 | 3.87 | 3.47 | -0.0 | 458112.37 | 9.11 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 7.21 | 5.17 | 0.05 | 150189.92 | 17.73 | skipped_fast |
| EDELUSDT | IDLE | 1.73 | 7.59 | 5.73 | -0.07 | 189187.44 | 46.95 | skipped_fast |
| RIZEUSDT | IDLE | 2.02 | 16.62 | 10.23 | -0.07 | 41795.25 | 101.01 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.82 | 1.67 | 0.03 | 625570.46 | 1.27 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 2.73 | 2.15 | 0.01 | 82405.95 | 11.15 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 3.22 | 0.28 | 0.07 | 69631.93 | 11.23 | skipped_fast |
| ZBCNUSDT | IDLE | 0.98 | 1.95 | 0.02 | 0.02 | 190749.24 | 16.38 | skipped_fast |
| REDUSDT | IDLE | 0.96 | 5.3 | 2.49 | 0.07 | 117513.38 | 19.67 | skipped_fast |
| RWAINCUSDT | IDLE | 0.63 | 1.21 | 0.28 | 0.04 | 5338.86 | 56.85 | skipped_fast |
| TELUSDT | IDLE | 0.78 | 3.29 | 2.31 | 0.09 | 131995.82 | 31.94 | skipped_fast |
| QNTUSDT | IDLE | 0.74 | 1.38 | 0.61 | 0.01 | 74520.48 | 6.31 | skipped_fast |
| RWAUSDT | IDLE | 0.92 | 1.71 | 0.81 | 0.0 | 56061.31 | 44.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.62 | 2.59 | 1.86 | 0.16 | 5401.67 | 21.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.55 | 0.24 | 0.04 | 40686.44 | 22.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
