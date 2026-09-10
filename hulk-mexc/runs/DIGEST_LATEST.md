# Hulk DIGEST — 2026-09-10T05:14:54Z

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
| XRPUSDT | IDLE | 0.74 | 1.43 | 0.37 | -0.03 | 42400387.38 | 1.44 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 1.01 | 0.0 | -0.01 | 372811606.41 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.72 | 0.13 | -0.01 | 520455199.46 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.64 | 1.84 | 0.0 | -0.03 | 1005035.29 | 1.9 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 2.71 | 1.59 | -0.05 | 627193.52 | 8.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.66 | 5.11 | 1.42 | 0.04 | 192250.96 | 22.97 | skipped_fast |
| EDELUSDT | IDLE | 1.85 | 7.18 | 1.89 | 0.08 | 240286.99 | 8.75 | skipped_fast |
| WUSDT | IDLE | 1.94 | 3.66 | 2.69 | -0.04 | 212626.99 | 15.33 | skipped_fast |
| REDUSDT | IDLE | 2.44 | 4.31 | 3.8 | -0.01 | 63195.47 | 17.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.14 | 6.45 | 4.74 | -0.09 | 125114.44 | 12.22 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 3.62 | 1.23 | -0.06 | 105081.42 | 3.89 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 2.57 | 1.67 | -0.01 | 57114.53 | 11.57 | skipped_fast |
| HBARUSDT | IDLE | 0.69 | 1.37 | 0.01 | -0.03 | 433513.83 | 1.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 1.71 | 1.23 | -0.01 | 5870.64 | 16.89 | skipped_fast |
| RIZEUSDT | IDLE | 0.57 | 6.81 | 1.35 | 0.05 | 60674.92 | 103.68 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 2.0 | 1.28 | -0.02 | 46962.22 | 7.46 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.63 | 0.55 | -0.01 | 89685.41 | 50.21 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.83 | 0.22 | -0.03 | 54803.0 | 7.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 1.0 | 0.12 | -0.02 | 27487.26 | 4.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.65 | 1.41 | 0.0 | -0.05 | 1443.01 | 11.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
