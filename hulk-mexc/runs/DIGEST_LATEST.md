# Hulk DIGEST — 2026-09-09T17:13:30Z

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
| XRPUSDT | IDLE | 1.29 | 2.41 | 1.15 | -0.01 | 42936689.95 | 1.41 | skipped_fast |
| BTCUSDT | IDLE | 1.09 | 2.04 | 0.98 | 0.0 | 526484743.6 | 0.04 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 2.0 | 0.93 | 0.0 | 340023291.4 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 7.67 | 5.27 | -0.03 | 190146.34 | 19.46 | skipped_fast |
| PYTHUSDT | IDLE | 2.14 | 4.14 | 0.93 | 0.04 | 561342.15 | 1.78 | skipped_fast |
| CCUSDT | IDLE | 1.84 | 3.37 | 2.06 | -0.03 | 525600.26 | 6.7 | skipped_fast |
| ZBCNUSDT | IDLE | 3.28 | 6.15 | 3.13 | 0.02 | 197616.51 | 16.31 | skipped_fast |
| RIZEUSDT | IDLE | 2.15 | 22.92 | 17.83 | -0.01 | 63747.92 | 186.92 | skipped_fast |
| CHIPUSDT | IDLE | 1.81 | 7.04 | 2.96 | 0.08 | 107075.92 | 8.63 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.69 | 0.06 | 0.01 | 168071.73 | 18.48 | skipped_fast |
| BIOUSDT | IDLE | 1.71 | 3.2 | 1.5 | -0.04 | 99048.43 | 3.71 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 3.52 | 1.19 | 0.02 | 61134.21 | 17.39 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.7 | 1.34 | 0.01 | 65046.25 | 12.22 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 2.03 | 0.87 | -0.02 | 415627.94 | 1.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.85 | 3.5 | 1.31 | 0.01 | 7522.82 | 44.08 | skipped_fast |
| TELUSDT | IDLE | 2.64 | 4.82 | 3.05 | 0.03 | 101566.6 | 43.96 | skipped_fast |
| FLUIDUSDT | IDLE | 2.03 | 3.56 | 3.29 | -0.04 | 507.42 | 21.84 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.48 | 1.18 | -0.01 | 47535.83 | 4.46 | skipped_fast |
| RWAUSDT | IDLE | 1.41 | 2.56 | 1.71 | -0.0 | 54677.92 | 28.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.57 | 0.41 | 0.0 | 22753.34 | 46.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
