# Hulk DIGEST — 2026-10-17T05:55:09Z

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
| PYTHUSDT | IDLE | 1.05 | 3.41 | 2.81 | -0.11 | 1735212.64 | 2.36 | skipped_fast |
| XRPUSDT | IDLE | 0.37 | 0.71 | 0.19 | -0.02 | 25208917.73 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.56 | 0.11 | -0.01 | 193589559.95 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.17 | 0.33 | 0.11 | -0.01 | 302110273.84 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.41 | 3.67 | 1.34 | -0.05 | 1245260.46 | 6.25 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.32 | 0.49 | -0.01 | 686256.95 | 1.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.85 | 3.37 | 2.2 | -0.03 | 202268.05 | 19.23 | skipped_fast |
| RIZEUSDT | IDLE | 2.76 | 6.07 | 3.46 | -0.04 | 50811.94 | 61.89 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 2.1 | 0.11 | -0.01 | 355528.7 | 8.59 | skipped_fast |
| REDUSDT | IDLE | 1.98 | 3.73 | 3.14 | -0.04 | 73286.01 | 14.7 | skipped_fast |
| EDELUSDT | IDLE | 1.11 | 1.95 | 1.75 | 0.0 | 192056.14 | 40.93 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.76 | 0.19 | 0.01 | 56953.87 | 10.51 | skipped_fast |
| RWAINCUSDT | IDLE | 1.06 | 5.19 | 2.09 | -0.09 | 24167.29 | 10.96 | skipped_fast |
| CHIPUSDT | IDLE | 0.77 | 2.42 | 1.28 | -0.07 | 108797.08 | 12.98 | skipped_fast |
| BIOUSDT | IDLE | 0.73 | 1.32 | 0.87 | -0.03 | 65163.0 | 3.99 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.45 | 0.69 | -0.02 | 311980.88 | 4.77 | skipped_fast |
| TELUSDT | IDLE | 0.89 | 1.58 | 1.27 | -0.04 | 89464.87 | 40.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.85 | 1.61 | 0.56 | 0.01 | 4738.51 | 21.41 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.71 | -0.01 | 52481.0 | 40.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.4 | 0.24 | -0.0 | 31941.22 | 12.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
