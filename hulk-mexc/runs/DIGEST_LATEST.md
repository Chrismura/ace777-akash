# Hulk DIGEST — 2026-10-10T22:43:08Z

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
| ETHUSDT | IDLE | 0.32 | 0.58 | 0.43 | 0.01 | 112500431.98 | 0.64 | skipped_fast |
| XRPUSDT | IDLE | 0.27 | 0.48 | 0.36 | 0.01 | 12989059.38 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.11 | 0.2 | 0.1 | 0.01 | 168855190.45 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.07 | 3.34 | 2.54 | 0.03 | 1268791.05 | 13.05 | skipped_fast |
| CHIPUSDT | IDLE | 3.4 | 28.8 | 3.12 | 0.3 | 234531.75 | 14.89 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.17 | 1.88 | -0.04 | 1234638.91 | 2.09 | skipped_fast |
| PYTHUSDT | IDLE | 0.87 | 1.64 | 0.65 | -0.02 | 768015.42 | 3.8 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 4.71 | 3.21 | -0.05 | 247017.66 | 26.14 | skipped_fast |
| RWAINCUSDT | IDLE | 2.21 | 4.24 | 1.16 | -0.02 | 9523.81 | 29.51 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 3.01 | 1.55 | 0.04 | 87259.23 | 3.41 | skipped_fast |
| CCUSDT | IDLE | 0.68 | 1.3 | 0.41 | -0.03 | 288849.57 | 9.24 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.31 | 0.18 | 0.03 | 203837.09 | 12.98 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 2.37 | 2.2 | 0.07 | 61431.5 | 10.18 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 3.46 | 2.63 | -0.03 | 136651.76 | 28.18 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 1.05 | 0.61 | 0.03 | 55590.88 | 8.62 | skipped_fast |
| RIZEUSDT | IDLE | 0.99 | 1.82 | 1.01 | -0.04 | 33137.3 | 48.16 | skipped_fast |
| HBARUSDT | IDLE | 0.43 | 0.79 | 0.5 | 0.01 | 310852.64 | 3.25 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.45 | 0.87 | 0.0 | 8504.7 | 21.33 | skipped_fast |
| MNSRYUSDT | IDLE | 1.01 | 1.8 | 1.51 | -0.01 | 36737.04 | 52.18 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.79 | 0.7 | 0.0 | 53352.83 | 7.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
