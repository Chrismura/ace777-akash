# Hulk DIGEST — 2026-09-18T22:59:32Z

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
| XRPUSDT | IDLE | 1.3 | 2.92 | 1.03 | 0.08 | 64405726.77 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 1.16 | 2.33 | 0.96 | 0.07 | 630276375.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 1.0 | 0.35 | 0.06 | 755785373.08 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.24 | 4.34 | 1.96 | 0.1 | 890361.09 | 11.88 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 12.26 | 10.72 | 0.02 | 176712.21 | 31.22 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.89 | 1.56 | 0.08 | 759741.52 | 1.67 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 3.08 | 0.08 | 0.11 | 666822.06 | 8.94 | skipped_fast |
| HBARUSDT | IDLE | 1.29 | 2.46 | 0.78 | 0.07 | 617059.36 | 2.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 8.61 | 3.66 | 0.2 | 190355.26 | 22.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 2.33 | 1.4 | 0.04 | 224500.89 | 9.37 | skipped_fast |
| TELUSDT | IDLE | 2.33 | 11.9 | 4.17 | 0.15 | 119713.0 | 67.55 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 2.7 | 0.57 | 0.04 | 7342.35 | 5.75 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 2.16 | 0.27 | 0.05 | 77486.7 | 11.66 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 2.19 | 1.09 | 0.09 | 88048.38 | 7.33 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 1.7 | 0.46 | 0.12 | 63285.26 | 15.77 | skipped_fast |
| FLUIDUSDT | IDLE | 1.62 | 6.66 | 1.51 | 0.15 | 2477.57 | 21.07 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.28 | 1.03 | 0.04 | 72850.62 | 3.16 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.47 | 0.16 | 0.07 | 43148.94 | 2.62 | skipped_fast |
| RIZEUSDT | IDLE | 0.15 | 2.53 | 0.7 | -0.1 | 57834.86 | 117.17 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.41 | 1.25 | 0.01 | 58398.88 | 44.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
