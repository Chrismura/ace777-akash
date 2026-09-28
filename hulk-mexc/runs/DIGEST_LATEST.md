# Hulk DIGEST — 2026-09-28T14:40:45Z

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
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 14.75 | 9.55 | -0.0 | 1318465.29 | 4.51 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 30.69 | 8.66 | 0.39 | 20662222.16 | 12.04 | skipped_fast |
| WUSDT | IDLE | 1.48 | 6.03 | 4.56 | -0.03 | 3146436.28 | 9.37 | skipped_fast |
| HBARUSDT | IDLE | 1.99 | 16.48 | 4.26 | 0.28 | 7435514.4 | 13.36 | skipped_fast |
| XRPUSDT | IDLE | 2.26 | 4.22 | 2.02 | -0.01 | 60753665.4 | 3.33 | skipped_fast |
| ETHUSDT | IDLE | 1.2 | 2.3 | 0.63 | -0.0 | 338921409.56 | 0.97 | skipped_fast |
| PYTHUSDT | IDLE | 2.11 | 4.59 | 3.91 | -0.05 | 1465684.77 | 13.87 | skipped_fast |
| BTCUSDT | IDLE | 0.76 | 1.45 | 0.48 | -0.02 | 732430890.72 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.54 | 23.45 | 4.41 | 0.04 | 194967.52 | 6.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.57 | 5.22 | 3.94 | -0.07 | 81618.21 | 22.62 | skipped_fast |
| REDUSDT | IDLE | 1.79 | 3.58 | 2.73 | -0.05 | 62158.2 | 7.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.31 | 1.67 | -0.05 | 230625.8 | 30.93 | skipped_fast |
| TELUSDT | IDLE | 2.86 | 5.63 | 0.65 | -0.0 | 159716.01 | 37.91 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 3.54 | 2.39 | -0.07 | 96566.97 | 3.4 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 3.84 | 2.86 | -0.07 | 100933.33 | 8.04 | skipped_fast |
| RWAINCUSDT | IDLE | 0.56 | 5.69 | 1.76 | 0.05 | 30679.11 | 51.54 | skipped_fast |
| FLUIDUSDT | IDLE | 1.33 | 2.99 | 1.76 | -0.06 | 3159.4 | 19.94 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 2.89 | 0.48 | -0.14 | 60019.82 | 108.6 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.94 | 0.29 | -0.02 | 60522.54 | 7.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 0.96 | 0.7 | -0.02 | 34604.06 | 55.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
