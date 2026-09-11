# Hulk DIGEST — 2026-09-11T11:20:46Z

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
| XRPUSDT | IDLE | 1.68 | 2.98 | 2.53 | -0.04 | 39693040.56 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.32 | 1.12 | -0.0 | 463750155.46 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.94 | 0.87 | -0.01 | 522115021.17 | 0.12 | skipped_fast |
| CCUSDT | IDLE | 2.86 | 5.15 | 3.83 | -0.06 | 437107.36 | 3.13 | skipped_fast |
| PYTHUSDT | IDLE | 2.26 | 4.04 | 3.25 | -0.03 | 360651.91 | 1.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 26.96 | 14.97 | -0.16 | 134852.47 | 64.24 | skipped_fast |
| WUSDT | IDLE | 2.07 | 3.67 | 3.1 | -0.02 | 133726.79 | 11.73 | skipped_fast |
| REDUSDT | IDLE | 2.08 | 3.68 | 3.17 | -0.03 | 59127.22 | 21.01 | skipped_fast |
| BIOUSDT | IDLE | 1.78 | 3.16 | 2.67 | -0.04 | 79647.73 | 8.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 3.62 | 1.86 | -0.06 | 127125.58 | 2.21 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 2.46 | 2.4 | -0.02 | 57714.76 | 10.29 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 2.87 | 2.6 | -0.07 | 197905.78 | 19.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.57 | 3.14 | 0.0 | 0.04 | 3892.07 | 5.48 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.38 | 1.01 | -0.03 | 200521.93 | 18.27 | skipped_fast |
| HBARUSDT | IDLE | 1.69 | 2.97 | 2.75 | -0.04 | 194449.24 | 1.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.8 | 3.15 | 3.05 | -0.03 | 2404.99 | 22.19 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 1.63 | 1.43 | -0.04 | 99420.3 | 23.27 | skipped_fast |
| QNTUSDT | IDLE | 0.99 | 1.73 | 1.7 | -0.03 | 37054.63 | 1.56 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.6 | 0.43 | -0.01 | 37405.47 | 9.79 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.46 | 0.3 | -0.02 | 49422.47 | 22.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
