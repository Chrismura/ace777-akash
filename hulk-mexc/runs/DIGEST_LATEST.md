# Hulk DIGEST — 2026-09-23T16:22:09Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 13.83 | 9.52 | -0.07 | 1413825.74 | 6.46 | tvl≈150,045,080 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 7.61 | 5.62 | -0.03 | 122113503.42 | 1.33 | n/a |
| ETHUSDT | IDLE | 2.18 | 3.93 | 2.8 | -0.02 | 513244958.17 | 0.98 | no_map |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 9.35 | 6.77 | -0.06 | 1615725.18 | 1.1 | empty_tvl |
| BTCUSDT | IDLE | 1.6 | 2.91 | 1.94 | -0.02 | 888616308.43 | 0.0 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 10.1 | 6.96 | -0.03 | 405802.51 | 7.86 | tvl≈1,725,923,572 |
| CCUSDT | IDLE | 3.04 | 6.94 | 4.6 | -0.04 | 483294.9 | 2.77 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 10.94 | 7.41 | -0.07 | 220947.0 | 18.69 | no_map |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.95 | 10.05 | 6.56 | -0.02 | 126758.49 | 10.6 | n/a |
| REDUSDT | IDLE | 3.74 | 6.92 | 4.43 | -0.01 | 60171.8 | 16.15 | tvl≈2,847,874 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 11.06 | 7.19 | -0.09 | 212539.2 | 56.56 | no_map |
| KITEUSDT | IDLE | 3.13 | 5.94 | 2.51 | -0.02 | 165155.96 | 10.37 | no_map |
| ZBCNUSDT | IDLE | 2.4 | 5.58 | 4.43 | -0.02 | 256932.23 | 28.39 | n/a |
| QNTUSDT | IDLE | 3.67 | 8.72 | 4.34 | -0.01 | 199892.86 | 8.33 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.94 | 8.0 | 7.41 | -0.05 | 4112.19 | 20.72 | tvl≈2,614,218,940 |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 7.45 | 6.71 | -0.02 | 156359.28 | 52.62 | no_map |
| RIZEUSDT | IDLE | 1.14 | 15.55 | 12.16 | 0.4 | 68427.15 | 104.75 | no_map |
| RWAINCUSDT | IDLE | 0.78 | 1.69 | 0.43 | 0.02 | 20755.48 | 5.43 | no_map |
| RWAUSDT | IDLE | 1.82 | 3.2 | 2.89 | -0.02 | 55322.67 | 22.26 | no_map |
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
