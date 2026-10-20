# Hulk DIGEST — 2026-10-20T21:24:58Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 0.8 | 1.58 | 0.18 | 0.02 | 24194227.74 | 0.75 | n/a |
| ETHUSDT | IDLE | 0.65 | 1.28 | 0.1 | 0.02 | 154438975.54 | 0.08 | no_map |
| BTCUSDT | IDLE | 0.4 | 0.78 | 0.07 | 0.01 | 323333340.25 | 0.09 | no_map |
| PYTHUSDT | IDLE | 2.18 | 6.24 | 0.67 | 0.1 | 1169113.76 | 1.26 | tvl≈175,627,523 |
| WUSDT | IDLE | 2.09 | 4.08 | 0.72 | 0.03 | 675929.77 | 15.6 | tvl≈1,600,835,314 |
| ZBCNUSDT | IDLE | 1.95 | 3.67 | 1.48 | 0.03 | 190948.26 | 16.79 | n/a |
| RIZEUSDT | IDLE | 2.33 | 9.41 | 5.31 | 0.05 | 75095.97 | 59.43 | no_map |
| CCUSDT | IDLE | 1.03 | 1.86 | 1.3 | 0.01 | 383363.6 | 7.6 | no_map |
| REDUSDT | IDLE | 1.43 | 2.68 | 1.15 | 0.03 | 59819.22 | 15.64 | tvl≈3,476,342 |
| BIOUSDT | IDLE | 1.23 | 2.38 | 0.48 | 0.06 | 62659.35 | 8.05 | n/a |
| HBARUSDT | IDLE | 0.92 | 1.8 | 0.24 | 0.02 | 369371.9 | 4.75 | empty_tvl |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
