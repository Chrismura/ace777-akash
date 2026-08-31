# Hulk DIGEST — 2026-08-31T05:16:06Z

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
| XRPUSDT | IDLE | 1.25 | 2.34 | 1.09 | -0.03 | 35517512.09 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.6 | 0.7 | -0.01 | 387475369.5 | 0.45 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 1.01 | 0.54 | -0.0 | 407934593.27 | 0.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.78 | 4.25 | 2.21 | -0.02 | 555382.84 | 2.15 | skipped_fast |
| WUSDT | IDLE | 2.69 | 5.42 | 0.39 | 0.02 | 224690.24 | 12.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.01 | 3.27 | 0.74 | -0.04 | 492112.92 | 5.15 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 5.3 | 3.91 | -0.08 | 228715.65 | 10.78 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 3.45 | 0.58 | -0.01 | 204570.86 | 9.29 | skipped_fast |
| KITEUSDT | IDLE | 1.99 | 5.91 | 0.18 | -0.04 | 90564.91 | 8.95 | skipped_fast |
| EDELUSDT | IDLE | 2.2 | 4.27 | 2.46 | 0.04 | 90256.37 | 42.0 | skipped_fast |
| REDUSDT | IDLE | 1.74 | 3.32 | 1.03 | -0.02 | 67812.42 | 10.94 | skipped_fast |
| BIOUSDT | IDLE | 1.1 | 2.15 | 0.34 | -0.04 | 87081.01 | 3.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.97 | 2.89 | -0.01 | 2255.56 | 96.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.14 | 2.01 | 1.81 | -0.04 | 37422.06 | 60.75 | skipped_fast |
| HBARUSDT | IDLE | 0.72 | 1.41 | 0.24 | -0.01 | 211420.18 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.24 | 0.17 | -0.02 | 40607.56 | 6.62 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.81 | 0.32 | 0.02 | 52869.38 | 16.22 | skipped_fast |
| TELUSDT | IDLE | 0.55 | 1.02 | 0.53 | -0.0 | 83167.93 | 59.49 | skipped_fast |
| FLUIDUSDT | IDLE | 0.46 | 0.91 | 0.0 | -0.02 | 3849.88 | 22.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.68 | 0.58 | -0.01 | 29989.62 | 47.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
