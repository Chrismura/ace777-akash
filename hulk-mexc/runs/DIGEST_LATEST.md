# Hulk DIGEST — 2026-10-12T02:31:04Z

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
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 24.62 | 0.64 | 0.4 | 5557043.38 | 19.58 | skipped_fast |
| ETHUSDT | IDLE | 0.98 | 1.89 | 0.44 | 0.02 | 202857742.47 | 0.2 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.07 | 0.41 | 0.0 | 17684616.57 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.89 | 0.17 | 0.01 | 165487261.04 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.5 | 2.98 | 0.1 | 0.01 | 888431.86 | 7.57 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 6.65 | 4.22 | -0.03 | 241535.1 | 14.95 | skipped_fast |
| QNTUSDT | IDLE | 1.24 | 2.28 | 1.29 | 0.01 | 707996.3 | 0.84 | skipped_fast |
| CCUSDT | IDLE | 1.25 | 2.67 | 0.35 | 0.06 | 384937.07 | 14.24 | skipped_fast |
| EDELUSDT | IDLE | 1.59 | 3.14 | 0.29 | -0.01 | 338015.74 | 28.9 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 3.14 | 0.0 | 0.03 | 227270.17 | 0.43 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.76 | 0.63 | 0.02 | 98187.86 | 6.69 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.26 | 0.63 | 0.0 | 62808.97 | 18.69 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 1.99 | 0.93 | 0.0 | 54873.75 | 10.62 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.78 | 0.92 | 0.02 | 300632.61 | 6.4 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 3.69 | 3.17 | 0.06 | 39167.69 | 32.14 | skipped_fast |
| RWAINCUSDT | IDLE | 0.61 | 1.6 | 1.43 | -0.01 | 25075.53 | 34.9 | skipped_fast |
| TELUSDT | IDLE | 1.26 | 2.48 | 0.23 | -0.01 | 170739.01 | 40.4 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 3.75 | 3.54 | 0.03 | 67177.03 | 21.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.78 | 0.18 | 0.0 | 34600.78 | 6.82 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.54 | 0.23 | 0.02 | 52804.81 | 7.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
