# Hulk DIGEST — 2026-10-10T07:44:11Z

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
| WUSDT | IDLE | 1.76 | 4.55 | 2.87 | -0.03 | 1826844.98 | 6.45 | skipped_fast |
| PYTHUSDT | IDLE | 1.87 | 4.6 | 4.05 | -0.07 | 1403870.05 | 3.8 | skipped_fast |
| XRPUSDT | IDLE | 0.48 | 0.89 | 0.52 | 0.0 | 24319052.02 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.2 | 0.37 | 0.21 | -0.0 | 132369494.04 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.13 | 0.0 | 245447677.5 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.21 | 1.64 | 0.01 | 1157974.75 | 6.1 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.9 | 1.74 | 0.02 | 575623.22 | 6.63 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 2.62 | 0.35 | -0.07 | 264012.11 | 16.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.22 | 4.04 | 2.27 | 0.07 | 99099.33 | 9.48 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 5.68 | 4.88 | 0.05 | 65874.52 | 15.92 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 2.32 | 1.72 | 0.13 | 208009.29 | 17.52 | skipped_fast |
| REDUSDT | IDLE | 1.27 | 2.22 | 2.18 | 0.01 | 57372.36 | 7.41 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.88 | 1.61 | 0.01 | 70629.63 | 3.47 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.21 | 0.43 | -0.02 | 75456.3 | 12.23 | skipped_fast |
| HBARUSDT | IDLE | 1.03 | 1.9 | 1.02 | 0.0 | 296924.06 | 3.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.29 | 1.81 | 0.01 | 9358.51 | 87.0 | skipped_fast |
| RWAUSDT | IDLE | 1.65 | 2.92 | 2.53 | -0.01 | 52771.36 | 23.61 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 2.67 | 1.22 | -0.01 | 114892.84 | 32.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.42 | 0.5 | 0.01 | 41505.34 | 29.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.3 | 1.99 | 0.0 | 0.01 | 17205.48 | 21.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
