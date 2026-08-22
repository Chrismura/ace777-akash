# Hulk DIGEST — 2026-08-22T15:05:49Z

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
| PYTHUSDT | IDLE | 1.6 | 7.62 | 1.95 | 0.04 | 51470031.95 | 11.91 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.31 | 0.03 | 214024982.63 | 1.38 | n/a |
| CCUSDT | IDLE | 1.3 | 5.65 | 2.35 | 0.11 | 800889.32 | 10.26 | no_map |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.36 | -0.01 | 1172766.01 | 6.55 | empty_tvl |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.62 | -0.11 | 614573.97 | 3.41 | no_map |
| WUSDT | IDLE | 0.79 | 3.17 | 1.94 | -0.02 | 563006.35 | 13.91 | tvl≈1,572,799,710 |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.67 | 0.04 | 83611.5 | 10.72 | no_map |
| ZBCNUSDT | IDLE | 1.27 | 3.49 | 1.03 | -0.06 | 323369.91 | 36.23 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.98 | -0.06 | 225236.6 | 3.32 | n/a |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.04 | 79005.46 | 34.15 | no_map |
| REDUSDT | IDLE | 0.48 | 5.1 | 4.6 | -0.03 | 150787.03 | 12.84 | tvl≈2,031,082 |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.42 | 0.04 | 46489.09 | 43.92 | no_map |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.07 | -0.01 | 188414.04 | 7.87 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9946.26 | 69.84 | no_map |
| TELUSDT | IDLE | 1.07 | 2.75 | 0.89 | 0.01 | 140947.17 | 53.08 | no_map |
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
