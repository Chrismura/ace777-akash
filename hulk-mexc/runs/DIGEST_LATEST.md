# Hulk DIGEST — 2026-09-17T03:15:34Z

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
| XRPUSDT | IDLE | 1.23 | 2.36 | 0.66 | 0.01 | 56767102.44 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 1.21 | 2.35 | 0.47 | 0.01 | 381397616.15 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.49 | 0.42 | 0.01 | 515796951.87 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.16 | 7.73 | 5.21 | 0.07 | 563041.59 | 8.21 | skipped_fast |
| PYTHUSDT | IDLE | 2.86 | 5.71 | 0.07 | 0.03 | 427485.47 | 3.67 | skipped_fast |
| WUSDT | IDLE | 2.75 | 5.27 | 1.72 | 0.01 | 225661.26 | 13.05 | skipped_fast |
| CHIPUSDT | IDLE | 3.15 | 7.1 | 3.54 | -0.04 | 81819.83 | 19.32 | skipped_fast |
| RWAINCUSDT | IDLE | 3.15 | 5.77 | 3.54 | -0.02 | 20720.82 | 5.83 | skipped_fast |
| REDUSDT | IDLE | 2.15 | 4.49 | 1.09 | 0.01 | 64026.34 | 16.68 | skipped_fast |
| BIOUSDT | IDLE | 1.92 | 3.74 | 0.71 | 0.02 | 77845.58 | 7.9 | skipped_fast |
| EDELUSDT | IDLE | 0.89 | 3.78 | 3.09 | 0.03 | 267332.75 | 19.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.59 | 0.0 | 0.03 | 162699.11 | 5.11 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 4.0 | 2.62 | 0.05 | 66876.8 | 9.5 | skipped_fast |
| RIZEUSDT | IDLE | 0.81 | 10.2 | 7.6 | 0.21 | 62866.69 | 66.45 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.27 | 0.43 | -0.01 | 301790.07 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.88 | 1.16 | -0.02 | 115387.45 | 34.66 | skipped_fast |
| QNTUSDT | IDLE | 0.74 | 1.32 | 1.09 | -0.0 | 37462.54 | 4.95 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 0.98 | 0.75 | 0.01 | 55230.05 | 15.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.52 | 0.97 | 0.42 | 0.0 | 33735.36 | 29.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1573.23 | 21.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
