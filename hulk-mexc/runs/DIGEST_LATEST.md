# Hulk DIGEST — 2026-10-14T08:19:18Z

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
| PYTHUSDT | IDLE | 2.66 | 5.96 | 1.75 | -0.03 | 1818777.96 | 2.42 | skipped_fast |
| WUSDT | IDLE | 0.78 | 5.16 | 0.75 | -0.15 | 3753349.14 | 7.83 | skipped_fast |
| XRPUSDT | IDLE | 0.9 | 1.73 | 0.43 | 0.0 | 30321538.37 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 0.61 | 1.16 | 0.39 | -0.0 | 133890669.89 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.94 | 0.34 | -0.0 | 330713308.61 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.0 | 2.86 | 1.53 | -0.05 | 1676064.03 | 2.8 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.55 | 2.26 | -0.01 | 582041.66 | 5.71 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 9.52 | 1.39 | 0.1 | 73103.17 | 9.99 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.16 | 2.77 | -0.04 | 80776.32 | 10.47 | skipped_fast |
| EDELUSDT | IDLE | 1.19 | 2.31 | 0.46 | 0.04 | 216483.56 | 14.52 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 6.35 | 1.71 | 0.04 | 53001.38 | 59.36 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 2.74 | 1.16 | -0.0 | 84547.25 | 10.11 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 2.05 | 0.79 | -0.01 | 68938.23 | 3.61 | skipped_fast |
| ZBCNUSDT | IDLE | 0.6 | 1.1 | 0.62 | -0.03 | 200779.69 | 21.08 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 2.01 | 1.32 | -0.07 | 32546.66 | 20.55 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.61 | 0.32 | -0.01 | 289088.6 | 8.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.89 | 5.85 | 1.8 | 0.06 | 21308.25 | 21.51 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.91 | 0.83 | 0.02 | 116959.8 | 33.39 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.86 | 0.31 | -0.01 | 55661.97 | 15.55 | skipped_fast |
| MNSRYUSDT | IDLE | 0.02 | 0.03 | 0.01 | -0.01 | 37544.81 | 5.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
