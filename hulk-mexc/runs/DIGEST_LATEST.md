# Hulk DIGEST — 2026-10-12T23:52:14Z

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
| WUSDT | IDLE | 1.05 | 16.34 | 12.77 | -0.13 | 15237211.2 | 7.36 | tvl≈1,725,744,511 |
| PYTHUSDT | IDLE | 1.57 | 5.95 | 4.6 | 0.03 | 3477860.88 | 4.91 | tvl≈184,442,013 |
| ETHUSDT | IDLE | 1.95 | 3.43 | 3.18 | -0.04 | 241302868.45 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.42 | 2.5 | 2.28 | -0.05 | 31426427.06 | 2.24 | n/a |
| BTCUSDT | IDLE | 0.94 | 1.65 | 1.57 | -0.02 | 315829564.09 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.85 | 3.59 | 2.52 | -0.05 | 790946.43 | 5.3 | n/a |
| CCUSDT | IDLE | 1.63 | 2.92 | 2.33 | -0.05 | 402741.43 | 9.18 | no_map |
| HBARUSDT | IDLE | 1.83 | 3.98 | 3.53 | -0.08 | 611841.16 | 9.2 | empty_tvl |
| KITEUSDT | IDLE | 2.54 | 4.5 | 3.82 | -0.04 | 65833.2 | 10.47 | no_map |
| RIZEUSDT | IDLE | 2.22 | 14.0 | 8.5 | -0.06 | 73405.4 | 88.7 | no_map |
| BIOUSDT | IDLE | 2.03 | 4.82 | 4.21 | -0.09 | 75325.08 | 3.67 | n/a |
| EDELUSDT | IDLE | 0.89 | 3.69 | 3.13 | -0.1 | 291819.19 | 11.96 | no_map |
| ZBCNUSDT | IDLE | 1.23 | 2.23 | 1.5 | 0.01 | 264395.51 | 15.21 | n/a |
| REDUSDT | IDLE | 0.67 | 4.24 | 2.98 | 0.02 | 272832.3 | 9.03 | tvl≈3,971,098 |
| CHIPUSDT | IDLE | 0.86 | 4.12 | 2.79 | -0.15 | 160698.52 | 13.76 | no_map |
| RWAINCUSDT | IDLE | 1.01 | 2.85 | 0.44 | 0.02 | 33626.16 | 4.88 | no_map |
| TELUSDT | IDLE | 2.09 | 3.69 | 3.28 | 0.0 | 116609.56 | 46.84 | no_map |
| FLUIDUSDT | IDLE | 2.11 | 3.83 | 2.57 | -0.02 | 15637.17 | 21.03 | tvl≈2,378,791,210 |
| RWAUSDT | IDLE | 0.43 | 0.78 | 0.54 | -0.0 | 52892.22 | 23.25 | no_map |
| MNSRYUSDT | IDLE | 0.6 | 1.06 | 0.88 | -0.01 | 41229.56 | 64.79 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
