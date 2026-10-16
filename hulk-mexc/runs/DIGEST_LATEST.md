# Hulk DIGEST — 2026-10-16T01:20:59Z

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
| WUSDT | IDLE | 1.43 | 3.95 | 0.02 | -0.04 | 2801474.46 | 10.02 | skipped_fast |
| PYTHUSDT | IDLE | 0.71 | 3.98 | 3.3 | 0.11 | 4479002.84 | 5.37 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.19 | 1.13 | 0.01 | 299880357.92 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.02 | 0.74 | 0.01 | 47383523.16 | 2.25 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.79 | 0.29 | 0.01 | 502725825.31 | 0.6 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 2.98 | 0.71 | 0.02 | 1335925.69 | 2.41 | skipped_fast |
| CCUSDT | IDLE | 1.57 | 3.28 | 0.34 | -0.05 | 476343.32 | 7.41 | skipped_fast |
| ZBCNUSDT | IDLE | 1.63 | 3.29 | 2.05 | 0.04 | 216189.61 | 18.85 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 4.37 | 2.33 | -0.1 | 231368.94 | 30.57 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 5.78 | 0.58 | -0.03 | 145606.98 | 12.4 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 3.64 | 3.52 | -0.03 | 74287.84 | 8.5 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.27 | 1.42 | -0.01 | 69525.53 | 10.52 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.89 | 0.32 | 0.02 | 302018.74 | 8.16 | skipped_fast |
| BIOUSDT | IDLE | 0.56 | 1.05 | 0.5 | -0.01 | 83050.6 | 3.87 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 2.9 | 2.08 | 0.06 | 77562.25 | 51.19 | skipped_fast |
| RWAINCUSDT | IDLE | 0.71 | 1.55 | 0.54 | 0.02 | 29638.28 | 24.83 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 2.11 | 0.61 | 0.02 | 92271.85 | 22.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.27 | 0.84 | -0.04 | 10195.01 | 21.23 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.72 | 0.55 | 0.01 | 54010.94 | 15.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.25 | -0.0 | 36552.76 | 26.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
