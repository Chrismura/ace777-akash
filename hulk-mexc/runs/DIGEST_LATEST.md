# Hulk DIGEST — 2026-09-19T04:57:06Z

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
| XRPUSDT | IDLE | 1.22 | 2.45 | 0.88 | 0.07 | 69357499.38 | 2.12 | n/a |
| BTCUSDT | IDLE | 0.61 | 1.09 | 0.88 | 0.05 | 744065069.99 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.6 | 1.12 | 0.52 | 0.06 | 628278931.98 | 0.04 | no_map |
| WUSDT | IDLE | 1.21 | 3.75 | 2.8 | 0.08 | 962227.87 | 4.61 | tvl≈1,615,074,693 |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 19.02 | 14.51 | 0.06 | 99039.63 | 15.18 | tvl≈2,634,218 |
| PYTHUSDT | IDLE | 2.07 | 3.89 | 1.68 | 0.0 | 699992.36 | 16.41 | tvl≈135,102,918 |
| CCUSDT | IDLE | 1.63 | 2.99 | 1.86 | 0.03 | 564924.48 | 6.27 | no_map |
| CHIPUSDT | IDLE | 2.29 | 7.81 | 3.78 | 0.08 | 148464.11 | 19.66 | no_map |
| HBARUSDT | IDLE | 1.02 | 1.89 | 1.05 | 0.02 | 681810.87 | 1.27 | empty_tvl |
| EDELUSDT | IDLE | 1.8 | 8.37 | 2.87 | -0.04 | 174432.49 | 36.4 | no_map |
| KITEUSDT | IDLE | 1.66 | 3.11 | 1.4 | 0.04 | 73462.54 | 11.51 | no_map |
| ZBCNUSDT | IDLE | 0.79 | 1.47 | 0.78 | 0.01 | 210841.31 | 26.56 | n/a |
| BIOUSDT | IDLE | 1.04 | 1.85 | 1.49 | 0.02 | 84438.28 | 14.75 | n/a |
| RWAINCUSDT | IDLE | 0.69 | 1.21 | 1.19 | 0.05 | 6539.34 | 5.72 | no_map |
| TELUSDT | IDLE | 1.06 | 4.44 | 3.89 | 0.1 | 126860.39 | 50.66 | no_map |
| RIZEUSDT | IDLE | 0.52 | 4.1 | 1.71 | -0.1 | 38710.66 | 115.12 | no_map |
| QNTUSDT | IDLE | 0.61 | 1.14 | 0.56 | 0.01 | 73479.48 | 9.45 | n/a |
| FLUIDUSDT | IDLE | 0.74 | 3.4 | 0.0 | 0.18 | 5299.2 | 21.7 | tvl≈2,629,915,263 |
| RWAUSDT | IDLE | 0.48 | 0.89 | 0.44 | 0.0 | 55011.91 | 29.67 | no_map |
| MNSRYUSDT | IDLE | 0.01 | 0.01 | 0.01 | 0.05 | 40667.26 | 2.62 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
