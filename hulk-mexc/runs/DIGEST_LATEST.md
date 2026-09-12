# Hulk DIGEST — 2026-09-12T07:21:56Z

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
| ETHUSDT | IDLE | 0.28 | 0.64 | 0.09 | 0.02 | 622187280.11 | 0.08 | skipped_fast |
| XRPUSDT | IDLE | 0.22 | 0.48 | 0.0 | 0.01 | 51349140.81 | 1.46 | skipped_fast |
| BTCUSDT | IDLE | 0.11 | 0.22 | 0.03 | 0.0 | 567508966.25 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.69 | 0.02 | 0.02 | 424579.59 | 1.9 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.79 | 1.2 | 0.0 | 419891.73 | 9.11 | skipped_fast |
| REDUSDT | IDLE | 1.68 | 4.21 | 3.38 | 0.05 | 65528.51 | 17.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.93 | 3.83 | 1.84 | 0.01 | 15621.36 | 27.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 2.05 | 0.02 | -0.0 | 185796.29 | 8.85 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.5 | 2.32 | -0.01 | 57684.52 | 12.23 | skipped_fast |
| EDELUSDT | IDLE | 0.93 | 2.6 | 1.22 | 0.07 | 166527.91 | 17.64 | skipped_fast |
| WUSDT | IDLE | 0.75 | 1.55 | 0.29 | 0.02 | 200612.26 | 12.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.08 | 3.08 | 1.22 | 0.05 | 91047.02 | 27.13 | skipped_fast |
| RIZEUSDT | IDLE | 0.12 | 7.74 | 4.47 | 0.8 | 185712.42 | 53.59 | skipped_fast |
| BIOUSDT | IDLE | 0.64 | 1.23 | 0.39 | 0.02 | 80540.65 | 7.85 | skipped_fast |
| HBARUSDT | IDLE | 0.44 | 0.82 | 0.35 | -0.01 | 265032.08 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 0.7 | 1.73 | 0.88 | -0.03 | 96138.2 | 41.41 | skipped_fast |
| QNTUSDT | IDLE | 0.56 | 1.03 | 0.62 | -0.01 | 44702.71 | 4.69 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.74 | 0.07 | 0.03 | 53350.75 | 7.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.67 | 0.39 | 0.0 | 27300.54 | 13.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 1925.04 | 19.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
