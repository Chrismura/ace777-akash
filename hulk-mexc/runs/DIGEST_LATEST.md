# Hulk DIGEST — 2026-09-08T07:39:05Z

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
| XRPUSDT | IDLE | 1.0 | 1.83 | 1.07 | -0.01 | 32409806.83 | 1.44 | skipped_fast |
| ETHUSDT | IDLE | 0.96 | 1.77 | 1.04 | -0.0 | 295867325.64 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.52 | 1.16 | -0.01 | 550448855.21 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 7.31 | 6.03 | -0.07 | 126239.04 | 13.7 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 2.92 | 2.41 | -0.04 | 451048.22 | 1.9 | skipped_fast |
| HBARUSDT | IDLE | 1.97 | 3.51 | 2.81 | 0.0 | 546712.0 | 1.24 | skipped_fast |
| PYTHUSDT | IDLE | 1.08 | 2.06 | 0.73 | -0.01 | 401516.68 | 1.85 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 7.42 | 5.46 | -0.05 | 50353.52 | 56.28 | skipped_fast |
| WUSDT | IDLE | 1.67 | 3.1 | 1.58 | 0.01 | 208698.68 | 13.52 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 5.13 | 2.2 | -0.03 | 89527.0 | 58.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.19 | 3.17 | 1.91 | -0.05 | 227004.81 | 9.07 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 3.32 | 2.97 | -0.06 | 64796.56 | 10.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.92 | 7.39 | 4.76 | -0.09 | 3147.3 | 81.37 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 2.0 | 0.51 | 0.01 | 66458.94 | 7.31 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.94 | 0.39 | 0.04 | 57693.31 | 11.41 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 1.94 | 1.14 | 0.0 | 60037.85 | 9.08 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 1.84 | 1.11 | -0.01 | 78965.73 | 29.49 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.53 | 0.57 | 0.01 | 53731.18 | 14.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.18 | -0.01 | 36071.31 | 38.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.17 | 0.3 | 0.29 | 0.02 | 762.92 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
