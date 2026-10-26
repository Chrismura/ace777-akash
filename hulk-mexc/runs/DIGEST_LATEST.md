# Hulk DIGEST — 2026-10-26T20:28:49Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.86 | 1.53 | 1.31 | -0.02 | 146326179.63 | 0.22 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.57 | 0.96 | -0.0 | 24604763.92 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.3 | 1.17 | -0.01 | 358719031.96 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 6.16 | 5.6 | 0.04 | 1441407.18 | 1.48 | skipped_fast |
| PYTHUSDT | IDLE | 2.49 | 4.35 | 4.17 | -0.02 | 865324.78 | 2.71 | skipped_fast |
| WUSDT | IDLE | 1.94 | 3.87 | 1.81 | 0.03 | 665419.57 | 40.4 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 13.24 | 8.24 | -0.12 | 56994.23 | 6.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.67 | 12.74 | 8.93 | 0.15 | 323375.56 | 9.64 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 4.11 | 3.43 | 0.02 | 92779.96 | 28.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 3.08 | 2.84 | -0.06 | 215066.52 | 30.05 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.4 | 2.25 | -0.03 | 206566.81 | 5.04 | skipped_fast |
| RIZEUSDT | IDLE | 2.32 | 4.4 | 1.55 | 0.0 | 45495.68 | 64.9 | skipped_fast |
| BIOUSDT | IDLE | 1.63 | 2.86 | 2.65 | -0.01 | 59036.89 | 4.53 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.86 | 2.53 | -0.0 | 63274.38 | 16.51 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.17 | 0.9 | 0.01 | 53578.48 | 11.41 | skipped_fast |
| FLUIDUSDT | IDLE | 2.65 | 5.19 | 0.74 | -0.01 | 1850.79 | 21.44 | skipped_fast |
| WAXLUSDT | IDLE | 2.59 | 4.54 | 4.24 | -0.04 | 53625.89 | 69.83 | skipped_fast |
| HBARUSDT | IDLE | 1.15 | 2.07 | 1.51 | -0.01 | 256991.73 | 14.32 | skipped_fast |
| IOTAUSDT | IDLE | 1.59 | 2.83 | 2.31 | -0.02 | 84962.99 | 21.34 | skipped_fast |
| LAUSDT | IDLE | 1.41 | 2.76 | 2.1 | 0.01 | 64644.39 | 24.08 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.88 | 0.4 | -0.0 | 54006.78 | 15.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.67 | -0.0 | 41788.42 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
