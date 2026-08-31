# Hulk DIGEST — 2026-08-31T16:17:59Z

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
| XRPUSDT | IDLE | 0.96 | 1.79 | 0.86 | -0.03 | 41776452.91 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 0.88 | 1.68 | 0.57 | -0.02 | 459839166.32 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.43 | 0.24 | -0.01 | 593562082.61 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 6.8 | 6.27 | -0.02 | 505637.47 | 2.56 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 3.05 | 1.78 | -0.05 | 433299.77 | 2.14 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 3.38 | 2.56 | -0.01 | 253399.67 | 6.82 | skipped_fast |
| WUSDT | IDLE | 1.8 | 3.23 | 2.93 | -0.05 | 211849.77 | 15.44 | skipped_fast |
| REDUSDT | IDLE | 1.83 | 3.21 | 2.94 | -0.05 | 69397.42 | 10.37 | skipped_fast |
| RIZEUSDT | IDLE | 2.01 | 3.6 | 2.77 | -0.04 | 40860.41 | 23.41 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 2.17 | 0.68 | -0.06 | 221956.79 | 9.42 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 3.18 | 3.08 | -0.08 | 98479.0 | 11.04 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.96 | 0.94 | -0.05 | 82388.7 | 3.8 | skipped_fast |
| EDELUSDT | IDLE | 0.84 | 5.1 | 3.58 | 0.01 | 127041.41 | 49.71 | skipped_fast |
| RWAUSDT | IDLE | 2.36 | 4.67 | 0.38 | 0.07 | 56747.72 | 22.81 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 1.97 | 1.7 | -0.03 | 287600.88 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 2.01 | 3.58 | 2.99 | -0.02 | 88496.4 | 29.68 | skipped_fast |
| QNTUSDT | IDLE | 1.98 | 3.67 | 2.0 | -0.02 | 51959.3 | 4.9 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 1.68 | 1.37 | -0.04 | 2298.59 | 17.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.76 | 0.7 | -0.0 | 2465.4 | 16.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.63 | 0.05 | -0.01 | 25851.13 | 18.95 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
