# Hulk DIGEST — 2026-08-31T06:15:53Z

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
| XRPUSDT | IDLE | 1.09 | 2.14 | 0.26 | -0.02 | 36720972.27 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.7 | 0.18 | -0.01 | 399808290.72 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.96 | 0.12 | -0.0 | 425770842.24 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.1 | 26.28 | 19.19 | 0.02 | 120973.7 | 25.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.48 | 3.7 | 0.63 | -0.01 | 555607.3 | 2.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.43 | 4.75 | 0.25 | -0.02 | 484415.88 | 2.52 | skipped_fast |
| WUSDT | IDLE | 2.44 | 4.75 | 1.48 | 0.02 | 230139.87 | 10.71 | skipped_fast |
| ZBCNUSDT | IDLE | 1.71 | 5.3 | 2.89 | -0.07 | 228474.2 | 10.11 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 3.35 | 0.45 | -0.0 | 206009.37 | 5.9 | skipped_fast |
| REDUSDT | IDLE | 1.84 | 3.6 | 0.53 | 0.02 | 69254.14 | 11.67 | skipped_fast |
| KITEUSDT | IDLE | 1.52 | 4.19 | 0.93 | -0.05 | 90825.41 | 10.63 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.57 | 0.15 | -0.03 | 87251.16 | 3.74 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.97 | 2.89 | -0.02 | 2199.72 | 96.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.01 | 1.15 | -0.03 | 37510.04 | 62.7 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.67 | 0.08 | -0.01 | 214186.14 | 1.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.74 | 0.0 | 0.01 | 3851.4 | 21.25 | skipped_fast |
| QNTUSDT | IDLE | 0.92 | 1.84 | 0.02 | -0.01 | 41328.06 | 1.64 | skipped_fast |
| TELUSDT | IDLE | 0.54 | 1.02 | 0.35 | -0.0 | 83405.57 | 11.87 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.65 | 0.16 | 0.01 | 52907.02 | 16.22 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.68 | 0.53 | -0.01 | 29956.14 | 12.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
