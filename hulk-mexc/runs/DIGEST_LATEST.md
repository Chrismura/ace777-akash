# Hulk DIGEST — 2026-08-22T15:32:22Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.42 | 0.04 | 51501092.66 | 1.97 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.34 | 0.03 | 214888623.89 | 1.38 | n/a |
| CCUSDT | IDLE | 1.35 | 5.65 | 3.6 | 0.08 | 796269.95 | 8.66 | no_map |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.52 | -0.02 | 1159566.57 | 5.24 | empty_tvl |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.36 | -0.09 | 604374.42 | 3.4 | no_map |
| WUSDT | IDLE | 0.79 | 3.17 | 1.85 | -0.02 | 556396.38 | 13.91 | tvl≈1,556,368,553 |
| KITEUSDT | IDLE | 2.75 | 6.37 | 1.98 | 0.03 | 85172.76 | 11.63 | no_map |
| ZBCNUSDT | IDLE | 1.33 | 3.49 | 2.2 | -0.05 | 320886.25 | 23.73 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.98 | -0.07 | 221287.75 | 3.31 | n/a |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.16 | -0.07 | 147989.31 | 11.98 | tvl≈2,005,037 |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.44 | 0.03 | 56469.44 | 23.62 | no_map |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.01 | 140522.28 | 48.04 | no_map |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
