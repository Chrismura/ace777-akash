# Hulk DIGEST — 2026-08-15T15:28:50Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.24 | 0.44 | 0.24 | -0.0 | 11402581.7 | 2.0 | n/a |
| CHIPUSDT | IDLE | 2.12 | 6.95 | 0.51 | 0.13 | 102179.81 | 7.91 | no_map |
| REDUSDT | IDLE | 2.19 | 4.39 | 0.0 | 0.06 | 61537.38 | 14.42 | tvl≈1,581,849 |
| CCUSDT | IDLE | 1.25 | 2.48 | 0.14 | -0.0 | 203107.81 | 6.19 | no_map |
| ZBCNUSDT | IDLE | 0.91 | 1.66 | 1.05 | -0.01 | 209681.97 | 10.77 | n/a |
| PYTHUSDT | IDLE | 0.87 | 1.54 | 1.39 | 0.02 | 172891.3 | 2.52 | tvl≈89,744,698 |
| WUSDT | IDLE | 0.7 | 1.37 | 0.24 | 0.04 | 143343.64 | 16.62 | tvl≈1,355,711,707 |
| BIOUSDT | IDLE | 0.84 | 1.66 | 0.08 | 0.04 | 67151.62 | 3.99 | n/a |
| EDELUSDT | IDLE | 0.83 | 5.26 | 0.64 | -0.15 | 97887.07 | 51.41 | no_map |
| KITEUSDT | IDLE | 0.9 | 1.73 | 0.46 | 0.04 | 57498.24 | 12.35 | no_map |
| QAITUSDT | IDLE | 0.92 | 1.77 | 0.52 | -0.01 | 2924.73 | 49.32 | no_map |
| RIZEUSDT | IDLE | 0.68 | 2.96 | 0.52 | -0.1 | 41320.09 | 59.59 | no_map |
| TELUSDT | IDLE | 1.58 | 3.01 | 1.06 | 0.01 | 91551.93 | 40.24 | no_map |
| RWAINCUSDT | IDLE | 0.71 | 1.23 | 1.21 | -0.06 | 15991.76 | 79.34 | no_map |
| HBARUSDT | IDLE | 0.22 | 0.41 | 0.17 | -0.0 | 63367.42 | 1.52 | empty_tvl |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
