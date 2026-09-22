# Hulk DIGEST — 2026-09-22T10:09:30Z

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
| XRPUSDT | IDLE | 2.15 | 4.09 | 1.37 | 0.04 | 113446243.12 | 1.3 | skipped_fast |
| BTCUSDT | IDLE | 0.76 | 1.47 | 0.27 | 0.02 | 1080291506.3 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.44 | 0.25 | 0.01 | 606262723.85 | 0.04 | skipped_fast |
| HBARUSDT | IDLE | 3.2 | 6.9 | 3.28 | 0.07 | 1263581.33 | 1.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 3.39 | 2.73 | -0.01 | 777849.95 | 1.6 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.65 | 1.69 | 0.01 | 658684.42 | 3.39 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 8.33 | 0.0 | 0.1 | 102515.87 | 11.45 | skipped_fast |
| WUSDT | IDLE | 1.53 | 2.97 | 0.54 | -0.0 | 400028.74 | 7.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.98 | 5.29 | 4.36 | -0.0 | 177706.3 | 17.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.7 | 3.17 | 1.58 | 0.01 | 272181.43 | 31.53 | skipped_fast |
| REDUSDT | IDLE | 2.21 | 4.04 | 2.51 | 0.02 | 93420.62 | 14.76 | skipped_fast |
| EDELUSDT | IDLE | 0.99 | 4.97 | 1.62 | 0.13 | 232591.34 | 49.6 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.04 | 1.0 | 0.01 | 129274.04 | 6.95 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 2.02 | 0.33 | 0.06 | 25940.72 | 44.03 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 3.02 | 0.0 | 0.02 | 113866.08 | 30.61 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 2.1 | 0.4 | 0.02 | 119530.16 | 7.38 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 4.48 | 2.69 | -0.17 | 50115.3 | 125.79 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.81 | 0.51 | 0.01 | 55542.1 | 21.87 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.27 | 0.0 | 0.03 | 10520.37 | 23.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.37 | 0.12 | 0.01 | 40342.28 | 11.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
