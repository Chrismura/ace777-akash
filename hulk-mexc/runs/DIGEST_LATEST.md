# Hulk DIGEST — 2026-09-20T11:02:26Z

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
| XRPUSDT | IDLE | 0.66 | 1.18 | 0.99 | -0.03 | 52434337.22 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 0.38 | 0.66 | 0.6 | -0.03 | 242830770.26 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.29 | 0.53 | 0.34 | -0.01 | 476120331.21 | 0.0 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 6.61 | 5.32 | -0.01 | 493381.9 | 6.5 | skipped_fast |
| PYTHUSDT | IDLE | 1.28 | 2.35 | 1.91 | -0.04 | 670603.85 | 5.2 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.05 | 2.76 | -0.0 | 785495.11 | 1.25 | skipped_fast |
| REDUSDT | IDLE | 2.77 | 5.03 | 3.44 | -0.0 | 75929.45 | 10.76 | skipped_fast |
| EDELUSDT | IDLE | 2.49 | 7.77 | 3.41 | -0.03 | 65867.01 | 10.08 | skipped_fast |
| CCUSDT | IDLE | 1.07 | 2.53 | 1.79 | -0.06 | 360300.97 | 4.83 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 3.21 | 2.86 | 0.03 | 231084.44 | 31.79 | skipped_fast |
| BIOUSDT | IDLE | 1.31 | 2.33 | 1.91 | -0.02 | 91718.47 | 3.75 | skipped_fast |
| CHIPUSDT | IDLE | 1.07 | 2.26 | 1.97 | -0.08 | 101487.73 | 12.11 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.17 | 1.48 | -0.03 | 72374.47 | 11.51 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 2.1 | 1.58 | -0.04 | 9979.06 | 5.95 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 2.7 | 2.23 | -0.07 | 37356.45 | 50.87 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.0 | 1.01 | -0.05 | 100046.61 | 47.83 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 1.58 | 1.15 | -0.02 | 55772.78 | 9.43 | skipped_fast |
| FLUIDUSDT | IDLE | 0.81 | 1.42 | 1.4 | -0.04 | 2429.86 | 23.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.87 | 0.83 | -0.02 | 33756.61 | 18.67 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.75 | 0.74 | -0.01 | 51653.7 | 22.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
