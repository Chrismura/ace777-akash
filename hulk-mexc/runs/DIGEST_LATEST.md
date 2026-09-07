# Hulk DIGEST — 2026-09-07T08:34:50Z

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
| XRPUSDT | IDLE | 1.03 | 1.95 | 0.79 | -0.01 | 31773272.52 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.64 | 0.91 | -0.0 | 306245200.31 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.67 | 1.24 | 0.62 | -0.0 | 417855532.84 | 0.06 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.49 | 7.96 | 6.83 | -0.03 | 65480.54 | 38.65 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.54 | 8.07 | 6.41 | -0.08 | 402996.36 | 12.85 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 3.55 | 1.79 | 0.0 | 597453.71 | 3.61 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.73 | 1.49 | 0.03 | 447651.12 | 14.44 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 1.91 | 1.23 | -0.0 | 416864.15 | 9.14 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 2.81 | 2.71 | -0.03 | 56368.58 | 22.65 | skipped_fast |
| RIZEUSDT | IDLE | 1.36 | 9.5 | 0.93 | -0.14 | 72212.33 | 56.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.04 | 1.89 | 1.23 | -0.03 | 160063.89 | 14.54 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.39 | 0.87 | -0.01 | 74185.52 | 3.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 5.5 | 4.51 | 0.07 | 6648.9 | 88.37 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.81 | 0.87 | -0.0 | 370796.46 | 1.24 | skipped_fast |
| REDUSDT | IDLE | 1.04 | 2.09 | 0.0 | 0.01 | 63125.9 | 9.31 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 2.46 | 1.6 | 0.01 | 100001.84 | 52.37 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 1.88 | 1.39 | 0.01 | 36508.47 | 6.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.81 | 1.58 | 0.25 | -0.01 | 1152.45 | 22.03 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.65 | 0.58 | -0.01 | 53863.78 | 7.23 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.23 | 0.11 | 0.0 | 39046.39 | 4.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
