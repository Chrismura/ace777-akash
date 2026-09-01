# Hulk DIGEST — 2026-09-01T11:24:20Z

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
| XRPUSDT | IDLE | 1.31 | 2.45 | 1.15 | -0.0 | 29182175.67 | 0.73 | n/a |
| BTCUSDT | IDLE | 1.02 | 1.81 | 1.58 | -0.01 | 563878801.37 | 0.0 | no_map |
| ETHUSDT | IDLE | 1.01 | 1.83 | 1.21 | 0.0 | 293125574.58 | 0.04 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 27.51 | 21.09 | -0.05 | 178872.14 | 69.87 | no_map |
| PYTHUSDT | IDLE | 2.13 | 5.52 | 1.06 | 0.06 | 585793.3 | 1.98 | tvl≈112,010,422 |
| CHIPUSDT | IDLE | 2.61 | 4.67 | 3.62 | -0.04 | 340880.38 | 5.12 | no_map |
| CCUSDT | IDLE | 2.13 | 3.79 | 3.17 | -0.0 | 389762.85 | 5.02 | no_map |
| REDUSDT | IDLE | 3.21 | 6.02 | 2.63 | 0.0 | 61104.87 | 11.87 | tvl≈2,024,405 |
| WUSDT | IDLE | 1.63 | 3.09 | 1.1 | 0.03 | 235594.86 | 10.43 | tvl≈1,535,211,989 |
| ZBCNUSDT | IDLE | 1.57 | 2.97 | 1.18 | 0.03 | 181240.64 | 19.24 | n/a |
| BIOUSDT | IDLE | 1.72 | 3.13 | 2.03 | -0.01 | 62162.92 | 3.83 | n/a |
| KITEUSDT | IDLE | 1.41 | 2.66 | 1.03 | -0.02 | 62016.64 | 10.95 | no_map |
| RIZEUSDT | IDLE | 1.53 | 5.19 | 1.77 | -0.07 | 37556.09 | 46.82 | no_map |
| RWAINCUSDT | IDLE | 1.34 | 2.62 | 0.41 | -0.02 | 4544.94 | 29.06 | no_map |
| HBARUSDT | IDLE | 0.91 | 1.73 | 0.63 | 0.0 | 243693.16 | 1.34 | empty_tvl |
| TELUSDT | IDLE | 1.28 | 2.35 | 1.43 | -0.0 | 84020.79 | 5.82 | no_map |
| QNTUSDT | IDLE | 0.87 | 1.69 | 0.27 | 0.0 | 48964.95 | 3.24 | n/a |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1143.37 | 20.41 | tvl≈2,598,859,066 |
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
