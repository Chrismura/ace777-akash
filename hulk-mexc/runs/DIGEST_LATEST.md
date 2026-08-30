# Hulk DIGEST — 2026-08-30T22:15:08Z

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
| XRPUSDT | IDLE | 1.98 | 3.55 | 2.69 | 0.0 | 25233181.68 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 1.54 | 2.75 | 2.14 | 0.01 | 249002736.19 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.41 | 0.97 | 0.01 | 295577000.41 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.98 | 4.52 | 3.65 | -0.03 | 558608.32 | 2.57 | skipped_fast |
| PYTHUSDT | IDLE | 2.59 | 4.7 | 3.22 | 0.01 | 411231.36 | 2.05 | skipped_fast |
| WUSDT | IDLE | 2.14 | 3.92 | 2.38 | 0.03 | 232310.97 | 13.87 | skipped_fast |
| KITEUSDT | IDLE | 2.54 | 4.54 | 3.66 | -0.05 | 62331.47 | 11.31 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 4.1 | 2.42 | -0.05 | 208611.61 | 9.87 | skipped_fast |
| BIOUSDT | IDLE | 2.01 | 3.66 | 2.41 | -0.01 | 85949.31 | 3.69 | skipped_fast |
| REDUSDT | IDLE | 1.8 | 3.26 | 2.25 | -0.01 | 63112.1 | 10.14 | skipped_fast |
| EDELUSDT | IDLE | 1.87 | 5.38 | 0.4 | 0.09 | 74584.76 | 48.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.05 | 2.96 | -0.01 | 1528.3 | 5.64 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 1.52 | 0.22 | 0.01 | 230877.43 | 9.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 3.74 | 0.43 | -0.02 | 41344.4 | 61.18 | skipped_fast |
| TELUSDT | IDLE | 1.92 | 3.39 | 3.05 | 0.0 | 89247.19 | 29.11 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 1.87 | 1.75 | -0.01 | 169850.47 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.29 | 2.27 | 2.09 | -0.01 | 36959.15 | 3.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.07 | 2.0 | 0.9 | 0.02 | 3287.15 | 21.68 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.81 | 0.16 | 0.02 | 52075.11 | 16.1 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.89 | 0.47 | 0.0 | 31482.25 | 14.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
