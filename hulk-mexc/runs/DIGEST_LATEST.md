# Hulk DIGEST — 2026-09-17T16:16:52Z

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
| XRPUSDT | IDLE | 1.22 | 2.29 | 0.97 | 0.03 | 56922843.72 | 1.53 | n/a |
| ETHUSDT | IDLE | 1.16 | 2.25 | 0.49 | 0.03 | 402474485.49 | 0.2 | no_map |
| BTCUSDT | IDLE | 0.78 | 1.48 | 0.53 | 0.01 | 496451455.6 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.85 | 4.41 | 0.5 | 0.07 | 591252.87 | 3.58 | tvl≈120,961,665 |
| CCUSDT | IDLE | 1.19 | 4.1 | 1.54 | 0.12 | 617188.51 | 8.86 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 20.66 | 6.31 | -0.12 | 45871.27 | 110.02 | no_map |
| EDELUSDT | IDLE | 2.44 | 7.19 | 2.18 | -0.05 | 182886.03 | 31.83 | no_map |
| CHIPUSDT | IDLE | 2.17 | 7.14 | 3.35 | 0.06 | 140195.06 | 10.36 | no_map |
| REDUSDT | IDLE | 2.66 | 5.24 | 3.31 | 0.04 | 66452.51 | 18.26 | tvl≈2,343,689 |
| ZBCNUSDT | IDLE | 2.4 | 4.55 | 1.72 | 0.03 | 185441.75 | 39.52 | n/a |
| HBARUSDT | IDLE | 1.76 | 3.5 | 0.14 | 0.05 | 566744.98 | 1.31 | empty_tvl |
| WUSDT | IDLE | 1.64 | 4.63 | 0.45 | 0.09 | 228099.7 | 15.63 | tvl≈1,474,696,500 |
| RWAINCUSDT | IDLE | 1.93 | 3.46 | 2.71 | 0.0 | 21415.1 | 23.7 | no_map |
| KITEUSDT | IDLE | 1.1 | 2.49 | 0.6 | 0.03 | 69006.6 | 15.29 | no_map |
| BIOUSDT | IDLE | 1.05 | 2.09 | 0.04 | 0.04 | 64511.57 | 11.8 | n/a |
| TELUSDT | IDLE | 1.95 | 3.84 | 0.34 | 0.05 | 90346.7 | 60.71 | no_map |
| QNTUSDT | IDLE | 1.1 | 2.09 | 0.77 | 0.03 | 36543.16 | 6.5 | n/a |
| MNSRYUSDT | IDLE | 0.89 | 1.7 | 0.56 | 0.01 | 40890.6 | 6.98 | no_map |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.22 | 0.01 | 57850.87 | 37.38 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 143.49 | 21.7 | tvl≈2,614,801,587 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
