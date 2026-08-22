# Hulk DIGEST — 2026-08-22T12:17:35Z

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
| PYTHUSDT | IDLE | 1.68 | 7.83 | 3.15 | 0.04 | 51610047.83 | 4.01 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.64 | 0.11 | 215344166.24 | 0.66 | n/a |
| HBARUSDT | IDLE | 1.25 | 4.63 | 2.04 | 0.03 | 1259530.69 | 7.69 | empty_tvl |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.0 | 0.13 | 774288.32 | 6.78 | no_map |
| WUSDT | IDLE | 1.53 | 6.27 | 3.01 | 0.02 | 577485.05 | 13.66 | tvl≈1,560,017,487 |
| ZBCNUSDT | IDLE | 2.22 | 5.77 | 3.95 | -0.03 | 371548.27 | 18.5 | n/a |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 0.92 | -0.1 | 612189.03 | 3.33 | no_map |
| KITEUSDT | IDLE | 2.59 | 6.24 | 0.13 | 0.04 | 83259.46 | 10.57 | no_map |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.2 | -0.03 | 78047.7 | 22.75 | no_map |
| BIOUSDT | IDLE | 0.76 | 5.65 | 0.22 | -0.01 | 240751.68 | 6.31 | n/a |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | no_map |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.43 | 0.03 | 153481.58 | 12.37 | tvl≈2,031,082 |
| TELUSDT | IDLE | 2.18 | 5.61 | 4.14 | -0.03 | 164226.43 | 53.25 | no_map |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | no_map |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.34 | -0.05 | 48112.58 | 22.24 | no_map |
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
