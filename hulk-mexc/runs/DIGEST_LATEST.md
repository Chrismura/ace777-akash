# Hulk DIGEST — 2026-08-21T03:29:23Z

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
| PYTHUSDT | IDLE | 2.28 | 5.01 | 1.15 | 0.07 | 1845828.96 | 2.2 | tvl≈101,647,402 |
| XRPUSDT | IDLE | 0.72 | 4.12 | 0.22 | 0.2 | 110253024.53 | 0.77 | n/a |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 12.03 | 0.12 | 0.19 | 418590.23 | 14.54 | no_map |
| CCUSDT | IDLE | 1.81 | 3.47 | 0.94 | 0.0 | 474523.18 | 15.91 | no_map |
| ZBCNUSDT | IDLE | 2.04 | 6.14 | 2.51 | 0.06 | 301365.85 | 18.73 | n/a |
| EDELUSDT | IDLE | 2.82 | 5.22 | 2.85 | 0.02 | 92074.1 | 21.72 | no_map |
| BIOUSDT | IDLE | 1.07 | 4.71 | 2.39 | 0.08 | 227328.52 | 3.22 | n/a |
| HBARUSDT | IDLE | 1.5 | 2.91 | 0.61 | 0.06 | 455142.31 | 1.34 | empty_tvl |
| WUSDT | IDLE | 1.05 | 1.93 | 1.13 | 0.06 | 263384.09 | 15.49 | tvl≈1,529,129,765 |
| REDUSDT | IDLE | 0.88 | 4.77 | 2.57 | 0.06 | 181367.09 | 23.77 | tvl≈1,905,423 |
| RWAINCUSDT | IDLE | 1.89 | 3.77 | 0.05 | 0.04 | 8551.33 | 27.33 | no_map |
| KITEUSDT | IDLE | 1.23 | 2.43 | 0.22 | 0.03 | 61876.39 | 16.02 | no_map |
| RIZEUSDT | IDLE | 1.19 | 6.49 | 2.46 | -0.06 | 41184.32 | 48.63 | no_map |
| QAITUSDT | IDLE | 1.12 | 2.55 | 2.49 | -0.03 | 6326.77 | 51.76 | no_map |
| TELUSDT | IDLE | 1.0 | 4.98 | 3.8 | 0.14 | 200673.47 | 43.86 | no_map |
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
