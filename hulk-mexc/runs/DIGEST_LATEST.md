# Hulk DIGEST — 2026-09-25T21:47:27Z

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
| XRPUSDT | IDLE | 1.26 | 2.22 | 1.94 | 0.01 | 116766581.59 | 1.93 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.81 | 0.65 | -0.0 | 333403259.07 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.65 | 0.44 | -0.01 | 694016455.44 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 4.42 | 1.02 | 0.08 | 1223378.2 | 6.81 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 7.48 | 3.75 | 0.13 | 829054.63 | 7.82 | skipped_fast |
| HBARUSDT | IDLE | 1.88 | 3.46 | 2.06 | 0.0 | 925581.01 | 8.51 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.47 | 1.67 | 0.03 | 405097.7 | 13.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 21.14 | 15.7 | -0.05 | 113045.82 | 34.25 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 4.68 | 3.82 | 0.02 | 183151.18 | 6.79 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.9 | 3.49 | 0.05 | 255458.52 | 29.21 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 4.28 | 2.4 | 0.09 | 572181.38 | 3.1 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 4.27 | 1.83 | -0.02 | 159025.31 | 20.53 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 3.49 | 1.05 | 0.0 | 81339.51 | 12.1 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 3.67 | 2.55 | 0.05 | 111533.06 | 9.23 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 2.35 | 1.45 | 0.08 | 136825.39 | 13.86 | skipped_fast |
| RWAINCUSDT | IDLE | 0.72 | 2.63 | 0.7 | -0.11 | 15350.84 | 60.42 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.02 | 1.32 | -0.0 | 119055.14 | 24.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.27 | 2.46 | 0.52 | 0.02 | 3356.58 | 21.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.37 | 0.82 | 0.02 | 40884.86 | 7.63 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.26 | 0.8 | -0.01 | 54766.3 | 44.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
