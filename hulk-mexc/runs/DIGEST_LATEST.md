# Hulk DIGEST — 2026-10-17T09:16:24Z

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
| WUSDT | IDLE | 3.31 | 6.58 | 0.3 | 0.01 | 1286904.07 | 15.31 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.5 | 0.11 | -0.01 | 164199843.92 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.25 | 0.44 | 0.42 | -0.03 | 23434262.82 | 1.53 | skipped_fast |
| PYTHUSDT | IDLE | 0.63 | 1.86 | 0.75 | -0.09 | 1587771.4 | 1.18 | skipped_fast |
| BTCUSDT | IDLE | 0.15 | 0.29 | 0.04 | -0.01 | 296764030.41 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.1 | 5.29 | 1.31 | -0.04 | 209243.39 | 2.32 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.1 | 0.94 | -0.01 | 660414.56 | 1.47 | skipped_fast |
| KITEUSDT | IDLE | 2.23 | 4.07 | 2.64 | -0.0 | 56642.53 | 9.75 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.82 | 1.61 | -0.02 | 326916.78 | 6.78 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.49 | 2.23 | -0.04 | 163422.65 | 10.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 6.18 | 0.84 | -0.06 | 23601.09 | 31.76 | skipped_fast |
| CHIPUSDT | IDLE | 0.99 | 2.43 | 1.73 | -0.08 | 107513.52 | 10.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.48 | 3.14 | 1.69 | -0.04 | 50924.36 | 61.51 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 1.78 | 1.34 | -0.03 | 74163.91 | 7.02 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.49 | 1.27 | -0.04 | 64893.63 | 4.02 | skipped_fast |
| HBARUSDT | IDLE | 0.46 | 0.84 | 0.51 | -0.03 | 275574.68 | 3.58 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.66 | 1.28 | -0.05 | 86396.32 | 17.68 | skipped_fast |
| FLUIDUSDT | IDLE | 1.13 | 2.2 | 0.41 | 0.03 | 4186.57 | 21.17 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.12 | 0.16 | -0.01 | 51769.63 | 15.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.28 | 0.23 | -0.0 | 29244.28 | 14.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
