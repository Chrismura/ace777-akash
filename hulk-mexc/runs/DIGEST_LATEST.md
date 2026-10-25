# Hulk DIGEST — 2026-10-25T16:40:00Z

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
| ETHUSDT | IDLE | 0.55 | 1.05 | 0.33 | 0.02 | 91287537.16 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.44 | 0.82 | 0.34 | 0.02 | 15026948.41 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.67 | 0.31 | 0.01 | 149445931.21 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.53 | 2.98 | 0.59 | -0.0 | 639222.87 | 15.76 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 21.0 | 6.26 | 0.04 | 18803.67 | 21.45 | skipped_fast |
| EDELUSDT | IDLE | 2.09 | 3.98 | 1.39 | 0.0 | 416809.61 | 33.44 | skipped_fast |
| PYTHUSDT | IDLE | 1.68 | 3.13 | 1.55 | 0.05 | 421959.56 | 1.4 | skipped_fast |
| KITEUSDT | IDLE | 2.8 | 5.12 | 3.23 | 0.0 | 54318.57 | 21.39 | skipped_fast |
| ZBCNUSDT | IDLE | 2.71 | 5.33 | 0.62 | 0.07 | 203496.69 | 76.64 | skipped_fast |
| QNTUSDT | IDLE | 2.27 | 4.52 | 0.13 | 0.07 | 453483.82 | 1.59 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 4.83 | 3.1 | 0.07 | 98982.61 | 18.03 | skipped_fast |
| CCUSDT | IDLE | 1.82 | 3.52 | 0.86 | 0.03 | 180763.84 | 8.8 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.22 | 0.88 | 0.01 | 60390.2 | 4.47 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.0 | 1.2 | -0.0 | 58173.51 | 5.51 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.94 | 0.22 | -0.01 | 66424.03 | 9.06 | skipped_fast |
| WAXLUSDT | IDLE | 2.53 | 4.9 | 1.1 | 0.03 | 53856.64 | 52.44 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 2.61 | 1.62 | -0.03 | 45756.58 | 62.78 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.36 | 0.25 | 0.02 | 138841.71 | 11.64 | skipped_fast |
| LAUSDT | IDLE | 0.9 | 3.73 | 1.12 | -0.07 | 70369.07 | 24.36 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.36 | 0.4 | 0.01 | 50827.55 | 7.95 | skipped_fast |
| IOTAUSDT | IDLE | 0.8 | 1.48 | 0.76 | 0.01 | 61801.33 | 25.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.59 | -0.01 | 36522.66 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
