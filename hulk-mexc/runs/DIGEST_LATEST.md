# Hulk DIGEST — 2026-09-15T00:35:20Z

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
| ETHUSDT | IDLE | 2.41 | 4.25 | 3.83 | 0.01 | 441714819.94 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.11 | 5.34 | 4.79 | 0.05 | 74848575.1 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 1.16 | 2.03 | 1.96 | 0.02 | 558784620.08 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.73 | 30.63 | 6.59 | 0.31 | 368327.83 | 44.99 | skipped_fast |
| CCUSDT | IDLE | 2.16 | 3.77 | 3.61 | 0.01 | 314080.28 | 6.25 | skipped_fast |
| PYTHUSDT | IDLE | 0.92 | 1.69 | 0.94 | -0.0 | 392420.15 | 1.78 | skipped_fast |
| WUSDT | IDLE | 1.6 | 2.92 | 1.9 | 0.02 | 208545.74 | 9.95 | skipped_fast |
| KITEUSDT | IDLE | 2.21 | 4.01 | 2.74 | -0.01 | 65515.0 | 12.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.83 | 3.42 | 1.55 | 0.04 | 199690.95 | 42.62 | skipped_fast |
| BIOUSDT | IDLE | 1.47 | 2.6 | 2.31 | 0.02 | 97787.75 | 3.88 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 3.09 | 2.03 | 0.08 | 189393.55 | 18.56 | skipped_fast |
| HBARUSDT | IDLE | 1.34 | 2.48 | 1.37 | 0.04 | 362649.74 | 1.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.15 | 2.25 | 0.97 | 0.01 | 75625.28 | 16.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.73 | 1.44 | 0.11 | 0.0 | 5557.17 | 5.48 | skipped_fast |
| TELUSDT | IDLE | 2.23 | 5.57 | 3.36 | 0.06 | 104995.89 | 109.02 | skipped_fast |
| RIZEUSDT | IDLE | 0.41 | 4.73 | 2.2 | 0.02 | 56100.79 | 104.28 | skipped_fast |
| FLUIDUSDT | IDLE | 1.36 | 2.37 | 2.31 | 0.02 | 1523.93 | 21.07 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 1.54 | 0.63 | 0.03 | 43600.73 | 6.22 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.05 | 0.74 | -0.0 | 55104.56 | 22.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.34 | 1.11 | 0.01 | 31525.78 | 44.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
