# Hulk DIGEST — 2026-09-12T18:37:03Z

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
| ETHUSDT | IDLE | 0.54 | 0.94 | 0.87 | -0.01 | 253115450.78 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.43 | 0.76 | 0.69 | 0.0 | 19688277.18 | 2.2 | n/a |
| BTCUSDT | IDLE | 0.27 | 0.48 | 0.44 | -0.0 | 355225876.91 | 0.0 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 64.93 | 12.02 | 0.52 | 122742.67 | 133.55 | no_map |
| ZBCNUSDT | IDLE | 2.58 | 6.2 | 4.26 | -0.03 | 208616.16 | 15.1 | n/a |
| EDELUSDT | IDLE | 2.9 | 5.85 | 0.84 | 0.07 | 172633.83 | 25.37 | no_map |
| PYTHUSDT | IDLE | 1.76 | 4.42 | 0.69 | 0.07 | 348086.46 | 5.46 | tvl≈119,422,512 |
| CHIPUSDT | IDLE | 2.74 | 6.86 | 4.07 | 0.03 | 73271.92 | 12.26 | no_map |
| RWAINCUSDT | IDLE | 2.74 | 5.05 | 4.81 | -0.03 | 10578.64 | 33.22 | no_map |
| WUSDT | IDLE | 1.62 | 3.23 | 0.13 | 0.02 | 118029.42 | 11.98 | tvl≈1,482,563,750 |
| CCUSDT | IDLE | 0.93 | 1.66 | 1.34 | -0.0 | 243957.88 | 8.2 | no_map |
| REDUSDT | IDLE | 1.21 | 2.4 | 0.1 | 0.03 | 61101.99 | 17.59 | tvl≈2,346,858 |
| KITEUSDT | IDLE | 0.79 | 1.47 | 0.69 | -0.02 | 58911.38 | 12.2 | no_map |
| BIOUSDT | IDLE | 0.66 | 1.17 | 1.04 | 0.02 | 70889.0 | 7.82 | n/a |
| TELUSDT | IDLE | 1.27 | 2.3 | 1.6 | -0.06 | 101672.03 | 42.18 | no_map |
| RWAUSDT | IDLE | 1.11 | 1.93 | 1.89 | 0.0 | 52894.63 | 7.42 | no_map |
| HBARUSDT | IDLE | 0.47 | 0.83 | 0.72 | 0.0 | 153314.16 | 1.34 | empty_tvl |
| QNTUSDT | IDLE | 0.55 | 1.05 | 0.37 | 0.01 | 42389.43 | 3.11 | n/a |
| FLUIDUSDT | IDLE | 0.27 | 0.54 | 0.0 | 0.02 | 1429.0 | 19.64 | tvl≈2,685,127,204 |
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
