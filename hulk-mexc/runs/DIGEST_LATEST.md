# Hulk DIGEST — 2026-09-14T20:43:59Z

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
| XRPUSDT | IDLE | 2.47 | 7.14 | 0.91 | 0.09 | 68830203.29 | 2.71 | skipped_fast |
| ETHUSDT | IDLE | 2.39 | 4.66 | 0.86 | 0.03 | 423120871.6 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.84 | 1.64 | 0.25 | 0.03 | 552535246.15 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 11.88 | 4.02 | 0.16 | 274298.8 | 13.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.96 | 3.8 | 0.83 | -0.01 | 438115.92 | 1.77 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 4.45 | 0.19 | 0.03 | 315310.2 | 8.05 | skipped_fast |
| ZBCNUSDT | IDLE | 2.36 | 4.6 | 0.74 | 0.02 | 198376.24 | 8.12 | skipped_fast |
| WUSDT | IDLE | 2.28 | 4.55 | 0.01 | 0.01 | 205947.67 | 10.74 | skipped_fast |
| BIOUSDT | IDLE | 2.03 | 4.06 | 0.0 | 0.03 | 92130.9 | 7.59 | skipped_fast |
| TELUSDT | IDLE | 3.15 | 8.53 | 2.02 | 0.07 | 103040.19 | 29.51 | skipped_fast |
| HBARUSDT | IDLE | 1.97 | 3.92 | 0.1 | 0.04 | 350765.01 | 1.26 | skipped_fast |
| KITEUSDT | IDLE | 1.98 | 3.94 | 0.11 | 0.01 | 65138.79 | 13.81 | skipped_fast |
| REDUSDT | IDLE | 1.24 | 4.71 | 0.29 | 0.08 | 187907.98 | 16.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 3.17 | 1.76 | -0.03 | 90325.66 | 19.12 | skipped_fast |
| RWAINCUSDT | IDLE | 1.57 | 2.84 | 2.06 | -0.0 | 5063.33 | 27.62 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 8.63 | 6.49 | -0.01 | 56179.78 | 54.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.47 | 2.94 | 0.0 | 0.03 | 1274.35 | 22.18 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 1.97 | 0.76 | -0.0 | 43504.93 | 6.22 | skipped_fast |
| MNSRYUSDT | IDLE | 1.12 | 2.17 | 0.49 | 0.01 | 31098.62 | 47.97 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.74 | 0.67 | -0.0 | 56324.59 | 52.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
