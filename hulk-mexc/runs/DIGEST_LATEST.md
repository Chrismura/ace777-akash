# Hulk DIGEST — 2026-09-17T12:03:34Z

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
| XRPUSDT | IDLE | 0.71 | 1.33 | 0.6 | 0.01 | 56394371.82 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.05 | 0.47 | 0.01 | 362053564.93 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.76 | 0.3 | 0.0 | 476594791.56 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.11 | 3.96 | 2.77 | 0.1 | 643968.12 | 9.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.7 | 8.24 | 4.01 | 0.0 | 139346.89 | 15.75 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 1.64 | 0.97 | 0.03 | 542058.13 | 5.56 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 6.56 | 4.12 | -0.12 | 204953.89 | 36.74 | skipped_fast |
| REDUSDT | IDLE | 2.06 | 4.14 | 2.13 | 0.01 | 64014.89 | 18.8 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 2.23 | 1.42 | 0.0 | 171475.7 | 10.99 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 4.7 | 4.27 | 0.05 | 67536.64 | 14.33 | skipped_fast |
| RWAINCUSDT | IDLE | 1.67 | 2.93 | 2.73 | -0.0 | 17659.06 | 29.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.13 | 14.49 | 10.95 | -0.3 | 53510.13 | 121.48 | skipped_fast |
| HBARUSDT | IDLE | 0.67 | 1.31 | 0.25 | 0.0 | 495506.82 | 1.34 | skipped_fast |
| WUSDT | IDLE | 0.52 | 1.04 | 0.01 | 0.04 | 220742.23 | 13.97 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.85 | 1.3 | 0.0 | 68764.72 | 15.97 | skipped_fast |
| RWAUSDT | IDLE | 1.7 | 3.31 | 0.6 | 0.01 | 58957.28 | 37.5 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.2 | 0.78 | 0.02 | 35273.75 | 4.88 | skipped_fast |
| TELUSDT | IDLE | 1.14 | 2.17 | 0.75 | -0.01 | 106956.67 | 41.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.63 | 0.46 | 0.01 | 38558.16 | 8.44 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.66 | 0.36 | 0.0 | 1261.39 | 52.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
