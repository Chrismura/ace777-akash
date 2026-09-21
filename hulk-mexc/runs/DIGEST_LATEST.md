# Hulk DIGEST — 2026-09-21T19:07:07Z

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
| XRPUSDT | IDLE | 1.27 | 2.68 | 0.81 | 0.07 | 86853523.53 | 2.66 | skipped_fast |
| ETHUSDT | IDLE | 1.05 | 2.05 | 0.39 | 0.05 | 679266771.79 | 0.65 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.54 | 0.39 | 0.06 | 951925174.86 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.95 | 2.87 | 0.05 | 1152084.39 | 1.1 | skipped_fast |
| PYTHUSDT | IDLE | 2.38 | 5.49 | 4.66 | 0.04 | 676794.96 | 6.31 | skipped_fast |
| WUSDT | IDLE | 2.01 | 4.29 | 3.77 | 0.02 | 606787.47 | 7.75 | skipped_fast |
| CCUSDT | IDLE | 1.24 | 3.06 | 2.58 | 0.07 | 572533.52 | 6.1 | skipped_fast |
| ZBCNUSDT | IDLE | 2.15 | 6.77 | 1.53 | 0.1 | 239077.76 | 49.38 | skipped_fast |
| EDELUSDT | IDLE | 1.01 | 7.18 | 1.08 | 0.3 | 250751.07 | 9.66 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 5.87 | 4.16 | 0.08 | 140374.69 | 19.7 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.87 | 2.04 | -0.0 | 104244.67 | 14.58 | skipped_fast |
| BIOUSDT | IDLE | 1.57 | 2.88 | 1.67 | 0.04 | 101324.0 | 10.43 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 2.49 | 2.18 | 0.03 | 76520.74 | 9.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 1.56 | 1.2 | 0.04 | 11767.05 | 5.78 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 5.31 | 1.2 | 0.08 | 100915.2 | 42.51 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 2.68 | 1.93 | 0.03 | 112180.33 | 4.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 5.02 | 0.24 | -0.1 | 49278.54 | 51.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.81 | 1.28 | 0.06 | 9946.59 | 21.63 | skipped_fast |
| RWAUSDT | IDLE | 0.74 | 1.39 | 0.65 | 0.02 | 56219.77 | 21.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.55 | 1.01 | 0.58 | 0.03 | 42721.82 | 15.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
