# Hulk DIGEST — 2026-09-27T13:08:58Z

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
| WUSDT | IDLE | 2.03 | 11.95 | 9.81 | 0.13 | 3420469.43 | 11.15 | tvl≈1,907,411,414 |
| PYTHUSDT | IDLE | 1.57 | 6.09 | 3.2 | 0.1 | 2128867.82 | 8.16 | tvl≈192,558,911 |
| QNTUSDT | IDLE | 0.83 | 15.63 | 11.94 | 0.55 | 5671486.85 | 5.6 | n/a |
| XRPUSDT | IDLE | 0.86 | 1.54 | 1.15 | -0.01 | 42054972.45 | 1.31 | n/a |
| ETHUSDT | IDLE | 0.58 | 1.04 | 0.82 | 0.01 | 163565340.91 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.32 | 0.59 | 0.35 | 0.01 | 439347723.61 | 0.0 | no_map |
| CCUSDT | IDLE | 1.22 | 2.2 | 1.54 | -0.01 | 606040.12 | 7.32 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 5.8 | 5.21 | 0.0 | 65086.08 | 14.22 | tvl≈3,108,999 |
| HBARUSDT | IDLE | 1.71 | 3.06 | 2.45 | -0.0 | 672584.55 | 1.07 | empty_tvl |
| EDELUSDT | IDLE | 2.41 | 5.84 | 4.11 | -0.06 | 147943.13 | 24.37 | no_map |
| CHIPUSDT | IDLE | 2.18 | 4.95 | 4.45 | -0.02 | 120052.58 | 16.81 | no_map |
| KITEUSDT | IDLE | 1.37 | 5.5 | 4.0 | 0.1 | 172538.78 | 14.06 | no_map |
| ZBCNUSDT | IDLE | 1.03 | 1.81 | 1.61 | -0.02 | 229029.38 | 21.81 | n/a |
| BIOUSDT | IDLE | 1.3 | 2.32 | 1.86 | -0.03 | 98492.87 | 12.63 | n/a |
| RWAINCUSDT | IDLE | 1.06 | 5.06 | 0.81 | 0.1 | 6477.26 | 104.05 | no_map |
| TELUSDT | IDLE | 1.1 | 3.98 | 0.11 | 0.13 | 139468.73 | 33.31 | no_map |
| RIZEUSDT | IDLE | 0.3 | 1.11 | 0.59 | -0.03 | 46198.04 | 54.12 | no_map |
| RWAUSDT | IDLE | 0.91 | 1.71 | 0.77 | 0.03 | 56450.82 | 7.05 | no_map |
| FLUIDUSDT | IDLE | 1.05 | 1.9 | 1.29 | 0.01 | 1374.49 | 20.3 | tvl≈2,593,519,463 |
| MNSRYUSDT | IDLE | 0.38 | 0.71 | 0.28 | 0.01 | 39387.38 | 7.57 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
