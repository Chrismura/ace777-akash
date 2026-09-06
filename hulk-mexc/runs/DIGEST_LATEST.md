# Hulk DIGEST — 2026-09-06T02:29:24Z

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
| XRPUSDT | IDLE | 0.74 | 1.41 | 0.46 | 0.01 | 23936418.26 | 2.82 | n/a |
| ETHUSDT | IDLE | 0.69 | 1.33 | 0.29 | 0.02 | 194348888.47 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.23 | 0.43 | 0.16 | 0.0 | 372392064.96 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.1 | 3.73 | 3.17 | 0.02 | 408489.82 | 10.97 | tvl≈123,271,808 |
| CHIPUSDT | IDLE | 1.66 | 4.43 | 2.59 | 0.05 | 424176.56 | 3.38 | no_map |
| RWAINCUSDT | IDLE | 2.89 | 5.2 | 3.9 | -0.0 | 8413.26 | 27.05 | no_map |
| WUSDT | IDLE | 1.92 | 3.59 | 1.6 | 0.04 | 171925.11 | 11.87 | tvl≈1,660,209,857 |
| CCUSDT | IDLE | 1.32 | 2.52 | 0.85 | 0.03 | 290438.12 | 9.96 | no_map |
| ZBCNUSDT | IDLE | 1.41 | 2.5 | 2.19 | -0.01 | 224698.15 | 17.42 | n/a |
| RIZEUSDT | IDLE | 1.41 | 9.29 | 2.64 | -0.06 | 125171.0 | 60.59 | no_map |
| REDUSDT | IDLE | 1.3 | 2.28 | 2.2 | 0.0 | 59531.33 | 8.73 | tvl≈2,331,573 |
| HBARUSDT | IDLE | 1.01 | 1.98 | 0.21 | 0.03 | 377848.12 | 1.23 | empty_tvl |
| KITEUSDT | IDLE | 1.07 | 2.27 | 0.38 | -0.06 | 64661.86 | 12.47 | no_map |
| BIOUSDT | IDLE | 0.64 | 1.22 | 0.46 | 0.02 | 96051.32 | 3.57 | n/a |
| RWAUSDT | IDLE | 2.22 | 3.91 | 3.49 | 0.04 | 53538.98 | 28.37 | no_map |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.94 | 0.02 | 116217.44 | 18.83 | no_map |
| TELUSDT | IDLE | 1.73 | 3.28 | 1.21 | 0.0 | 72976.58 | 29.2 | no_map |
| QNTUSDT | IDLE | 1.37 | 2.62 | 0.74 | 0.03 | 36818.54 | 9.11 | n/a |
| FLUIDUSDT | IDLE | 1.05 | 2.11 | 0.0 | 0.03 | 390.92 | 21.24 | tvl≈2,658,707,096 |
| MNSRYUSDT | IDLE | 0.5 | 0.94 | 0.42 | 0.0 | 38960.47 | 44.77 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
