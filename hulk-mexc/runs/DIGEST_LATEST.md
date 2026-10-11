# Hulk DIGEST — 2026-10-11T02:08:01Z

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
| XRPUSDT | IDLE | 0.51 | 0.93 | 0.57 | -0.0 | 12150776.19 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.17 | 0.34 | 0.04 | 0.01 | 132204491.68 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.1 | 0.19 | 0.08 | 0.0 | 144179232.66 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.23 | 4.02 | 1.87 | 0.03 | 1237603.39 | 6.77 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 1.87 | 1.6 | -0.04 | 1292731.6 | 2.53 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 2.9 | 0.97 | -0.04 | 756341.5 | 2.54 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 4.54 | 3.41 | -0.05 | 273538.69 | 20.89 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 6.26 | 5.55 | -0.11 | 33468.04 | 46.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.14 | 10.76 | 3.79 | 0.31 | 276074.43 | 7.23 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 2.91 | 1.95 | 0.01 | 88645.32 | 6.86 | skipped_fast |
| TELUSDT | IDLE | 2.5 | 4.84 | 4.13 | -0.07 | 144345.51 | 40.2 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 1.73 | 1.22 | 0.02 | 172145.54 | 24.02 | skipped_fast |
| CCUSDT | IDLE | 0.55 | 1.09 | 0.05 | -0.02 | 238092.48 | 8.37 | skipped_fast |
| KITEUSDT | IDLE | 0.78 | 1.69 | 0.65 | 0.05 | 75237.14 | 17.23 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 1.21 | 0.87 | 0.0 | 56957.56 | 8.67 | skipped_fast |
| RWAINCUSDT | IDLE | 0.74 | 1.29 | 1.22 | -0.02 | 12381.42 | 19.69 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.1 | 0.5 | -0.0 | 308879.14 | 5.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.86 | 1.64 | 0.54 | -0.01 | 36766.13 | 68.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.52 | 0.91 | 0.9 | 0.01 | 7810.5 | 21.51 | skipped_fast |
| RWAUSDT | IDLE | 0.09 | 0.16 | 0.08 | -0.0 | 53606.51 | 15.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
