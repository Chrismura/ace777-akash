# Hulk DIGEST — 2026-10-17T17:20:22Z

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
| ETHUSDT | IDLE | 0.85 | 1.51 | 1.31 | 0.0 | 95776974.79 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.85 | 1.53 | 1.17 | -0.0 | 18983654.14 | 1.55 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 7.35 | 5.7 | -0.03 | 1225134.7 | 16.04 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.95 | 7.06 | 5.36 | -0.03 | 1114362.48 | 3.71 | skipped_fast |
| BTCUSDT | IDLE | 0.29 | 0.51 | 0.46 | 0.0 | 198912582.33 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 4.6 | 3.32 | -0.01 | 619822.55 | 3.03 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 12.81 | 6.05 | 0.02 | 25290.73 | 5.24 | skipped_fast |
| CHIPUSDT | IDLE | 2.94 | 5.19 | 4.63 | -0.03 | 88193.54 | 15.99 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.56 | 1.78 | 0.01 | 272054.05 | 7.71 | skipped_fast |
| KITEUSDT | IDLE | 2.17 | 3.96 | 3.5 | -0.02 | 64072.93 | 11.1 | skipped_fast |
| BIOUSDT | IDLE | 2.05 | 3.62 | 3.18 | -0.03 | 69407.31 | 4.15 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.34 | 1.55 | -0.02 | 207101.03 | 8.01 | skipped_fast |
| EDELUSDT | IDLE | 1.02 | 1.78 | 1.68 | -0.05 | 149697.76 | 13.96 | skipped_fast |
| FLUIDUSDT | IDLE | 2.76 | 4.89 | 4.17 | 0.04 | 3697.15 | 21.6 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 1.92 | 1.51 | -0.03 | 60701.47 | 7.9 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 1.8 | 0.8 | -0.04 | 62074.82 | 31.77 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 1.97 | 1.6 | -0.0 | 137731.82 | 9.71 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.11 | 1.95 | -0.06 | 85638.8 | 18.06 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.28 | 0.87 | -0.01 | 51968.55 | 31.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.78 | 0.01 | 0.01 | 28841.63 | 9.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
