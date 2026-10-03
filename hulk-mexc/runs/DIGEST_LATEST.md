# Hulk DIGEST — 2026-10-03T12:48:46Z

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
| QNTUSDT | IDLE | 1.44 | 6.44 | 5.51 | 0.03 | 3878626.02 | 9.04 | skipped_fast |
| XRPUSDT | IDLE | 0.36 | 0.67 | 0.33 | -0.04 | 44619083.1 | 2.02 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.42 | 0.09 | -0.02 | 595910598.63 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.19 | 0.35 | 0.21 | -0.02 | 342617890.3 | 0.04 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 7.77 | 0.98 | 0.25 | 716934.94 | 23.99 | skipped_fast |
| PYTHUSDT | IDLE | 1.23 | 2.72 | 2.26 | -0.01 | 630023.78 | 5.11 | skipped_fast |
| WUSDT | IDLE | 1.58 | 4.06 | 1.76 | -0.02 | 458383.08 | 9.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.37 | 4.59 | 1.53 | -0.04 | 237630.79 | 10.23 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 2.97 | 1.1 | -0.03 | 428851.84 | 4.93 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 2.0 | 0.76 | -0.05 | 822758.18 | 3.95 | skipped_fast |
| REDUSDT | IDLE | 2.11 | 5.51 | 1.14 | -0.04 | 97425.11 | 12.84 | skipped_fast |
| KITEUSDT | IDLE | 2.05 | 3.86 | 1.55 | 0.01 | 83494.32 | 10.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 2.59 | 1.62 | -0.04 | 81388.16 | 16.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.67 | 4.2 | 1.13 | 0.03 | 5452.15 | 20.4 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 2.45 | 2.29 | -0.03 | 82459.92 | 9.77 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.75 | 2.02 | -0.09 | 143160.47 | 41.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.37 | 2.56 | 1.19 | 0.02 | 3724.28 | 21.9 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 3.22 | 1.09 | 0.07 | 43980.58 | 131.4 | skipped_fast |
| RWAUSDT | IDLE | 0.23 | 0.44 | 0.07 | -0.01 | 54647.85 | 7.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.44 | 0.26 | -0.01 | 32777.46 | 14.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
