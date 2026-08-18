# Hulk DIGEST — 2026-08-18T04:21:37Z

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
| XRPUSDT | IDLE | 0.88 | 1.58 | 1.21 | -0.01 | 12626507.4 | 1.01 | n/a |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 28.73 | 19.42 | -0.03 | 8243.15 | 9.78 | no_map |
| REDUSDT | IDLE | 2.39 | 6.18 | 1.43 | 0.06 | 59223.2 | 15.58 | tvl≈1,616,182 |
| CHIPUSDT | IDLE | 0.92 | 4.4 | 2.49 | -0.03 | 333000.14 | 3.6 | no_map |
| CCUSDT | IDLE | 1.39 | 2.69 | 0.54 | -0.04 | 291873.53 | 9.85 | no_map |
| PYTHUSDT | IDLE | 1.56 | 2.76 | 2.38 | -0.03 | 178321.28 | 2.65 | tvl≈86,707,897 |
| WUSDT | IDLE | 1.54 | 2.7 | 2.5 | -0.05 | 131664.12 | 9.89 | tvl≈1,364,327,123 |
| BIOUSDT | IDLE | 1.68 | 3.04 | 2.19 | -0.01 | 82152.64 | 4.14 | n/a |
| ZBCNUSDT | IDLE | 1.12 | 2.0 | 1.61 | -0.0 | 204174.35 | 5.76 | n/a |
| KITEUSDT | IDLE | 1.37 | 2.7 | 0.21 | -0.01 | 60207.55 | 12.85 | no_map |
| EDELUSDT | IDLE | 1.53 | 2.78 | 1.93 | -0.02 | 66592.98 | 52.63 | no_map |
| RIZEUSDT | IDLE | 0.65 | 4.62 | 3.48 | 0.02 | 81871.82 | 45.62 | no_map |
| RWAINCUSDT | IDLE | 0.78 | 1.36 | 1.34 | -0.05 | 1114.7 | 53.18 | no_map |
| TELUSDT | IDLE | 0.88 | 1.88 | 0.71 | -0.05 | 135503.23 | 14.31 | no_map |
| HBARUSDT | IDLE | 0.74 | 1.35 | 0.91 | 0.01 | 142457.29 | 4.58 | empty_tvl |
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
