# Hulk DIGEST — 2026-10-25T22:41:15Z

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
| XRPUSDT | IDLE | 0.83 | 1.53 | 0.82 | 0.01 | 14298775.05 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.82 | 1.52 | 0.81 | 0.0 | 81679782.0 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.5 | 0.92 | 0.52 | -0.0 | 144018930.2 | 0.08 | no_map |
| PYTHUSDT | IDLE | 2.3 | 5.34 | 0.5 | 0.08 | 625707.39 | 6.61 | tvl≈163,033,460 |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.27 | 8.58 | 0.84 | 0.06 | 331124.75 | 25.08 | no_map |
| WUSDT | IDLE | 2.08 | 3.7 | 3.04 | -0.03 | 603187.86 | 17.71 | tvl≈1,514,944,648 |
| CHIPUSDT | IDLE | 2.92 | 5.26 | 3.87 | -0.01 | 92045.63 | 15.76 | no_map |
| RIZEUSDT | IDLE | 3.33 | 6.05 | 4.12 | -0.0 | 33463.28 | 62.78 | no_map |
| ZBCNUSDT | IDLE | 2.08 | 3.82 | 2.73 | 0.04 | 183701.3 | 3.12 | n/a |
| CCUSDT | IDLE | 0.91 | 1.59 | 1.56 | 0.0 | 202037.67 | 10.84 | no_map |
| RWAINCUSDT | IDLE | 1.48 | 2.59 | 2.53 | -0.03 | 63169.57 | 16.96 | no_map |
| BIOUSDT | IDLE | 1.29 | 2.39 | 1.32 | -0.02 | 59773.14 | 4.47 | n/a |
| REDUSDT | IDLE | 1.08 | 1.97 | 1.22 | -0.03 | 58433.32 | 15.14 | tvl≈3,657,507 |
| KITEUSDT | IDLE | 0.82 | 1.47 | 1.14 | -0.02 | 53279.31 | 12.48 | no_map |
| HBARUSDT | IDLE | 0.94 | 1.82 | 0.44 | 0.0 | 154803.0 | 5.14 | empty_tvl |
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
