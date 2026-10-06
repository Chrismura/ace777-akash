# Hulk DIGEST — 2026-10-06T20:39:18Z

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
| QNTUSDT | IDLE | 2.5 | 4.77 | 1.52 | 0.04 | 2559466.95 | 2.28 | n/a |
| XRPUSDT | IDLE | 1.02 | 1.85 | 1.33 | -0.0 | 27372703.48 | 2.0 | n/a |
| BTCUSDT | IDLE | 0.82 | 1.45 | 1.21 | -0.0 | 554446830.21 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.82 | 1.48 | 1.01 | -0.01 | 314294479.81 | 0.07 | no_map |
| PYTHUSDT | IDLE | 2.68 | 4.78 | 3.9 | -0.01 | 608350.0 | 2.6 | tvl≈173,807,960 |
| EDELUSDT | IDLE | 1.94 | 6.25 | 3.06 | -0.05 | 412095.87 | 37.57 | no_map |
| WUSDT | IDLE | 1.65 | 3.08 | 1.43 | -0.0 | 413863.28 | 14.41 | tvl≈1,961,932,261 |
| RWAINCUSDT | IDLE | 3.34 | 6.07 | 4.12 | -0.04 | 19578.51 | 30.01 | no_map |
| CCUSDT | IDLE | 1.12 | 2.02 | 1.52 | 0.01 | 416987.56 | 7.04 | no_map |
| RIZEUSDT | IDLE | 1.24 | 13.66 | 4.23 | 0.28 | 113686.9 | 47.65 | no_map |
| CHIPUSDT | IDLE | 1.48 | 3.43 | 0.49 | 0.03 | 188253.4 | 15.18 | no_map |
| ZBCNUSDT | IDLE | 1.16 | 2.3 | 0.17 | 0.02 | 242034.77 | 11.96 | n/a |
| BIOUSDT | IDLE | 1.57 | 2.81 | 2.15 | -0.04 | 100954.06 | 6.29 | n/a |
| REDUSDT | IDLE | 1.37 | 2.43 | 2.11 | -0.05 | 60093.23 | 9.86 | tvl≈4,048,414 |
| TELUSDT | IDLE | 2.67 | 4.82 | 3.47 | -0.02 | 125570.91 | 47.71 | no_map |
| HBARUSDT | IDLE | 0.81 | 1.48 | 0.87 | -0.02 | 478206.41 | 5.98 | empty_tvl |
| KITEUSDT | IDLE | 1.31 | 2.41 | 1.37 | 0.0 | 59240.55 | 8.48 | no_map |
| FLUIDUSDT | IDLE | 1.45 | 6.67 | 3.73 | -0.1 | 83545.05 | 21.27 | tvl≈2,516,381,125 |
| RWAUSDT | IDLE | 0.58 | 1.03 | 0.87 | 0.0 | 51535.73 | 14.65 | no_map |
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
