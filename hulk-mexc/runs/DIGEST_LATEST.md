# Hulk DIGEST — 2026-10-26T10:19:29Z

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
| XRPUSDT | IDLE | 0.84 | 1.63 | 0.36 | -0.0 | 19847542.48 | 0.78 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.45 | 0.33 | 0.0 | 110724480.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.11 | 0.17 | 0.0 | 226664462.27 | 0.25 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.55 | 10.87 | 0.12 | 0.17 | 1048781.19 | 5.21 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 3.91 | 0.46 | 0.06 | 845385.57 | 3.99 | skipped_fast |
| ZBCNUSDT | IDLE | 2.8 | 6.09 | 4.97 | -0.02 | 204398.92 | 25.97 | skipped_fast |
| WUSDT | IDLE | 1.65 | 3.06 | 1.55 | -0.02 | 482154.57 | 16.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 6.29 | 0.97 | 0.06 | 111099.61 | 14.84 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 3.68 | 0.39 | 0.02 | 60649.45 | 14.98 | skipped_fast |
| RWAINCUSDT | IDLE | 1.55 | 2.95 | 1.89 | -0.06 | 67788.24 | 17.49 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.77 | 1.03 | 0.01 | 166166.45 | 7.91 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.61 | 1.58 | 0.01 | 54002.39 | 12.48 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 2.33 | 0.94 | -0.0 | 59418.56 | 9.03 | skipped_fast |
| LAUSDT | IDLE | 2.42 | 4.96 | 2.08 | 0.01 | 64824.64 | 18.82 | skipped_fast |
| EDELUSDT | IDLE | 0.97 | 2.57 | 0.74 | 0.08 | 140008.86 | 40.63 | skipped_fast |
| MNSRYUSDT | IDLE | 2.41 | 4.38 | 2.91 | -0.01 | 41338.49 | 76.46 | skipped_fast |
| WAXLUSDT | IDLE | 2.08 | 3.86 | 2.06 | -0.01 | 52110.28 | 52.53 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.78 | 0.48 | 0.01 | 174395.88 | 7.76 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 0.93 | 0.34 | 0.0 | 33113.36 | 48.38 | skipped_fast |
| IOTAUSDT | IDLE | 1.09 | 2.1 | 0.59 | -0.01 | 63545.61 | 23.56 | skipped_fast |
| RWAUSDT | IDLE | 0.14 | 0.24 | 0.24 | -0.01 | 53486.85 | 23.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.19 | 0.86 | 0.86 | -0.01 | 19108.66 | 22.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
