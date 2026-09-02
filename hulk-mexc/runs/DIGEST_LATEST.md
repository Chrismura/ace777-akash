# Hulk DIGEST — 2026-09-02T02:24:58Z

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
| XRPUSDT | IDLE | 1.16 | 2.16 | 1.03 | -0.02 | 36935342.65 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.78 | 0.81 | -0.02 | 357847088.74 | 0.17 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.16 | 0.5 | -0.01 | 529990563.02 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.81 | 8.04 | 3.59 | 0.05 | 666894.38 | 1.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 7.22 | 4.79 | 0.12 | 807302.2 | 4.59 | skipped_fast |
| WUSDT | IDLE | 2.94 | 5.36 | 3.42 | 0.03 | 417686.93 | 14.58 | skipped_fast |
| ZBCNUSDT | IDLE | 2.31 | 4.69 | 3.52 | -0.04 | 197599.47 | 18.29 | skipped_fast |
| RIZEUSDT | IDLE | 2.5 | 7.4 | 4.53 | -0.05 | 42559.68 | 77.43 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 3.8 | 3.02 | 0.06 | 143685.38 | 13.31 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 9.32 | 2.09 | -0.01 | 170444.61 | 35.49 | skipped_fast |
| CCUSDT | IDLE | 0.48 | 1.17 | 0.21 | -0.08 | 312162.72 | 10.54 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.37 | 0.76 | 0.05 | 68805.02 | 11.31 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.99 | 0.82 | -0.04 | 70395.39 | 3.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.48 | 1.21 | 0.01 | 5760.07 | 40.69 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 1.94 | 1.34 | -0.0 | 254068.96 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.8 | 0.61 | 0.04 | 46940.38 | 3.12 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.04 | 2.0 | -0.06 | 328.66 | 22.78 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.01 | 0.96 | -0.03 | 89953.43 | 66.45 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 1.01 | 0.61 | -0.03 | 58057.02 | 15.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.42 | -0.02 | 35770.44 | 23.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
