# Hulk DIGEST — 2026-09-28T07:17:48Z

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
| WUSDT | IDLE | 2.09 | 6.69 | 5.92 | -0.03 | 4769378.05 | 8.41 | skipped_fast |
| PYTHUSDT | IDLE | 2.47 | 6.54 | 2.99 | -0.05 | 1885105.3 | 3.65 | skipped_fast |
| XRPUSDT | IDLE | 1.71 | 3.07 | 2.34 | -0.03 | 51610978.22 | 2.03 | skipped_fast |
| QNTUSDT | IDLE | 0.53 | 17.68 | 3.54 | 0.58 | 16755433.45 | 13.96 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.33 | 0.78 | -0.02 | 575298086.1 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.53 | 0.99 | 0.49 | -0.02 | 281874667.56 | 0.04 | skipped_fast |
| CCUSDT | IDLE | 3.86 | 9.05 | 4.57 | 0.04 | 876951.84 | 7.2 | skipped_fast |
| HBARUSDT | IDLE | 2.84 | 5.6 | 0.5 | 0.05 | 1373930.34 | 2.02 | skipped_fast |
| BIOUSDT | IDLE | 2.71 | 5.02 | 4.62 | -0.06 | 99623.55 | 6.67 | skipped_fast |
| KITEUSDT | IDLE | 2.0 | 4.28 | 3.78 | -0.08 | 106726.48 | 9.14 | skipped_fast |
| EDELUSDT | IDLE | 1.25 | 6.77 | 3.4 | -0.13 | 187491.46 | 15.99 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 4.11 | 3.95 | -0.06 | 65231.83 | 14.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.56 | 9.18 | 6.17 | -0.14 | 59203.64 | 54.55 | skipped_fast |
| CHIPUSDT | IDLE | 1.23 | 3.38 | 2.68 | -0.08 | 87093.43 | 20.18 | skipped_fast |
| ZBCNUSDT | IDLE | 0.64 | 1.11 | 1.09 | -0.03 | 245034.31 | 21.24 | skipped_fast |
| FLUIDUSDT | IDLE | 2.73 | 4.78 | 4.57 | -0.03 | 3554.0 | 21.27 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 3.16 | 2.31 | 0.04 | 172333.74 | 27.45 | skipped_fast |
| RWAINCUSDT | IDLE | 0.6 | 5.57 | 5.27 | 0.17 | 31979.38 | 57.17 | skipped_fast |
| MNSRYUSDT | IDLE | 1.05 | 1.88 | 1.43 | -0.0 | 38226.9 | 37.17 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.22 | 0.85 | -0.01 | 59511.71 | 21.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
