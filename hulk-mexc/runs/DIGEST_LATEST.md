# Hulk DIGEST — 2026-08-22T15:25:46Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.67 | 0.04 | 51499111.39 | 3.96 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.34 | 7.49 | 5.3 | 0.02 | 214761354.35 | 1.38 | n/a |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.89 | 0.1 | 798012.87 | 4.3 | no_map |
| HBARUSDT | IDLE | 0.87 | 3.03 | 2.73 | -0.02 | 1170878.6 | 1.31 | empty_tvl |
| WUSDT | IDLE | 0.79 | 3.17 | 2.02 | -0.03 | 555243.82 | 11.8 | tvl≈1,556,368,553 |
| KITEUSDT | IDLE | 2.81 | 6.37 | 2.84 | 0.02 | 85178.37 | 9.94 | no_map |
| ZBCNUSDT | IDLE | 1.35 | 3.49 | 2.48 | -0.07 | 324782.47 | 14.48 | n/a |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.88 | -0.06 | 221653.48 | 3.32 | n/a |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.03 | -0.05 | 150084.44 | 9.22 | tvl≈2,005,037 |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.42 | 0.03 | 56023.23 | 21.94 | no_map |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.63 | -0.01 | 140345.55 | 42.71 | no_map |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
