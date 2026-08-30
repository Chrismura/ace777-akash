# Hulk DIGEST — 2026-08-30T18:14:25Z

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
| ETHUSDT | IDLE | 1.58 | 2.95 | 1.38 | 0.02 | 220783702.59 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 2.19 | 0.79 | 0.02 | 21318302.24 | 1.41 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.04 | 0.7 | 0.01 | 282540783.7 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.68 | 6.87 | 5.98 | -0.03 | 513103.68 | 2.51 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.07 | 8.55 | 5.92 | -0.05 | 200613.34 | 11.93 | skipped_fast |
| PYTHUSDT | IDLE | 2.57 | 4.73 | 2.67 | 0.02 | 390785.08 | 2.04 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 5.99 | 3.23 | 0.08 | 73746.56 | 24.99 | skipped_fast |
| KITEUSDT | IDLE | 2.06 | 3.6 | 3.43 | -0.03 | 59997.15 | 10.39 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.39 | 2.0 | 0.03 | 224444.75 | 12.74 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.72 | 1.2 | 0.01 | 254293.11 | 6.76 | skipped_fast |
| RIZEUSDT | IDLE | 1.94 | 5.3 | 4.42 | -0.06 | 36323.92 | 62.7 | skipped_fast |
| REDUSDT | IDLE | 1.24 | 2.18 | 1.99 | 0.02 | 62777.82 | 21.9 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.65 | 0.72 | 0.0 | 79704.67 | 3.64 | skipped_fast |
| TELUSDT | IDLE | 2.35 | 4.54 | 1.03 | 0.01 | 85127.04 | 34.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.63 | 0.0 | 0.02 | 1921.2 | 120.81 | skipped_fast |
| HBARUSDT | IDLE | 0.64 | 1.21 | 0.41 | 0.0 | 144011.46 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 0.65 | 1.14 | 1.13 | 0.01 | 37968.97 | 3.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 17.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.18 | 0.62 | 0.01 | 32551.29 | 9.33 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.22 | 0.32 | 0.02 | 52858.49 | 32.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
