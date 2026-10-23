# Hulk DIGEST — 2026-10-23T08:42:49Z

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
| XRPUSDT | IDLE | 0.56 | 1.06 | 0.34 | -0.0 | 26211719.17 | 0.75 | n/a |
| ETHUSDT | IDLE | 0.53 | 1.03 | 0.26 | 0.0 | 232094796.02 | 0.75 | no_map |
| BTCUSDT | IDLE | 0.31 | 0.6 | 0.18 | -0.0 | 355320196.2 | 0.0 | no_map |
| WUSDT | IDLE | 2.05 | 3.77 | 2.25 | 0.0 | 698842.09 | 8.81 | tvl≈1,558,230,904 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 14.95 | 6.94 | -0.08 | 45179.49 | 61.96 | no_map |
| PYTHUSDT | IDLE | 1.09 | 2.03 | 1.06 | -0.02 | 590605.97 | 5.49 | tvl≈162,477,830 |
| ZBCNUSDT | IDLE | 2.36 | 4.78 | 2.74 | 0.01 | 164101.98 | 18.22 | n/a |
| EDELUSDT | IDLE | 1.1 | 2.21 | 1.36 | -0.06 | 418316.46 | 18.79 | no_map |
| CHIPUSDT | IDLE | 2.24 | 4.48 | 1.77 | 0.04 | 132154.1 | 15.35 | no_map |
| QNTUSDT | IDLE | 1.26 | 2.23 | 1.9 | -0.04 | 456484.83 | 2.66 | n/a |
| RWAINCUSDT | IDLE | 1.43 | 2.7 | 1.1 | 0.01 | 50277.9 | 5.56 | no_map |
| CCUSDT | IDLE | 0.6 | 1.07 | 0.84 | -0.01 | 212942.0 | 8.74 | no_map |
| HBARUSDT | IDLE | 1.35 | 2.39 | 2.01 | -0.01 | 302028.01 | 6.24 | empty_tvl |
| REDUSDT | IDLE | 0.88 | 1.55 | 1.46 | -0.01 | 82755.23 | 10.66 | tvl≈3,537,570 |
| BIOUSDT | IDLE | 0.59 | 1.09 | 0.62 | 0.01 | 60061.28 | 8.35 | n/a |
| KITEUSDT | IDLE | 0.56 | 1.08 | 0.3 | 0.01 | 57591.63 | 10.82 | no_map |
| LAUSDT | IDLE | 1.12 | 2.1 | 0.93 | 0.01 | 53681.93 | 19.91 | no_map |
| WAXLUSDT | IDLE | 1.25 | 2.24 | 1.7 | -0.01 | 56675.27 | 66.67 | no_map |
| RWAUSDT | IDLE | 0.81 | 1.51 | 0.7 | -0.0 | 52572.76 | 15.76 | no_map |
| IOTAUSDT | IDLE | 0.71 | 1.3 | 0.86 | -0.0 | 64747.56 | 20.06 | no_map |
| FLUIDUSDT | IDLE | 0.42 | 0.89 | 0.32 | -0.04 | 9649.59 | 21.71 | tvl≈2,210,038,611 |
| MNSRYUSDT | IDLE | 0.34 | 0.63 | 0.33 | -0.0 | 38270.12 | 65.78 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
