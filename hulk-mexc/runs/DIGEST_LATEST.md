# Hulk DIGEST — 2026-09-28T02:14:34Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 90.56 | 28.08 | 0.48 | 14877179.08 | 10.06 | n/a |
| WUSDT | IDLE | 2.18 | 9.22 | 7.38 | 0.1 | 5280989.99 | 10.09 | tvl≈1,909,008,188 |
| PYTHUSDT | IDLE | 1.48 | 3.33 | 1.74 | -0.01 | 2018702.15 | 2.4 | tvl≈189,639,965 |
| XRPUSDT | IDLE | 1.41 | 2.64 | 1.23 | -0.01 | 46629248.4 | 2.64 | n/a |
| ETHUSDT | IDLE | 1.1 | 1.96 | 1.54 | -0.02 | 240423207.89 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.0 | 1.78 | 1.44 | -0.01 | 462658674.48 | 0.0 | no_map |
| CCUSDT | IDLE | 2.49 | 4.83 | 0.95 | 0.02 | 679302.35 | 7.85 | no_map |
| HBARUSDT | IDLE | 2.23 | 4.38 | 0.57 | 0.04 | 905643.99 | 2.06 | empty_tvl |
| KITEUSDT | IDLE | 2.83 | 4.97 | 4.58 | -0.03 | 101069.4 | 8.14 | no_map |
| ZBCNUSDT | IDLE | 2.16 | 3.83 | 3.23 | -0.03 | 242549.58 | 17.65 | n/a |
| BIOUSDT | IDLE | 2.6 | 4.72 | 3.15 | -0.02 | 86272.01 | 9.56 | n/a |
| EDELUSDT | IDLE | 1.86 | 8.75 | 7.04 | -0.13 | 150671.28 | 20.05 | no_map |
| CHIPUSDT | IDLE | 1.83 | 4.01 | 2.94 | -0.06 | 95865.05 | 15.24 | no_map |
| REDUSDT | IDLE | 1.38 | 2.49 | 1.76 | -0.0 | 66956.64 | 13.66 | tvl≈3,086,203 |
| RIZEUSDT | IDLE | 0.99 | 9.55 | 4.62 | -0.22 | 61612.14 | 74.21 | no_map |
| TELUSDT | IDLE | 1.18 | 2.8 | 0.91 | 0.06 | 176532.94 | 16.16 | no_map |
| RWAINCUSDT | IDLE | 0.67 | 6.69 | 2.31 | 0.25 | 30896.14 | 82.99 | no_map |
| FLUIDUSDT | IDLE | 1.87 | 3.39 | 2.31 | 0.03 | 3556.81 | 18.89 | tvl≈2,591,382,455 |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
