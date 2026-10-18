# Hulk DIGEST — 2026-10-18T06:28:48Z

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
| ETHUSDT | IDLE | 0.57 | 1.03 | 0.76 | -0.01 | 94026021.39 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.58 | 1.06 | 0.67 | -0.01 | 18522988.2 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.65 | 0.44 | 0.0 | 186374198.83 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.3 | 3.26 | 2.8 | -0.09 | 1276199.03 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.26 | 4.03 | 2.88 | -0.09 | 1225209.26 | 13.36 | skipped_fast |
| QNTUSDT | IDLE | 1.9 | 3.47 | 2.19 | -0.05 | 592655.43 | 1.03 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 2.9 | 1.87 | -0.02 | 245214.37 | 10.79 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 4.47 | 2.19 | -0.08 | 183174.46 | 7.47 | skipped_fast |
| REDUSDT | IDLE | 1.84 | 3.33 | 2.28 | -0.04 | 61299.54 | 10.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.42 | 2.18 | -0.04 | 175755.73 | 15.88 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.69 | 2.25 | -0.05 | 70681.67 | 4.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.15 | 1.82 | -0.06 | 75017.9 | 11.61 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 2.35 | 2.11 | -0.09 | 70591.81 | 11.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.26 | 2.2 | 2.07 | -0.0 | 45501.48 | 40.51 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 2.45 | 0.51 | 0.03 | 279264.82 | 5.78 | skipped_fast |
| LAUSDT | IDLE | 1.96 | 3.46 | 3.0 | -0.06 | 54960.37 | 25.81 | skipped_fast |
| IOTAUSDT | IDLE | 1.8 | 3.22 | 2.54 | -0.04 | 64883.6 | 24.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.35 | 1.06 | 0.42 | 0.04 | 17421.97 | 5.26 | skipped_fast |
| WAXLUSDT | IDLE | 0.82 | 2.88 | 1.62 | 0.02 | 64369.15 | 51.29 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.8 | 0.16 | 0.0 | 51088.97 | 15.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.43 | 0.85 | 0.13 | -0.01 | 1735.18 | 21.14 | skipped_fast |
| MNSRYUSDT | IDLE | 0.61 | 1.09 | 0.88 | -0.01 | 29462.01 | 59.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
