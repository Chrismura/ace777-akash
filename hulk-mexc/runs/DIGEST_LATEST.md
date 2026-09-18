# Hulk DIGEST — 2026-09-18T23:55:19Z

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
| XRPUSDT | IDLE | 0.97 | 2.11 | 1.29 | 0.08 | 64932784.05 | 1.43 | n/a |
| ETHUSDT | IDLE | 0.89 | 1.71 | 1.26 | 0.07 | 638979175.35 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.4 | 0.71 | 0.59 | 0.06 | 765454389.87 | 0.01 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.5 | 14.89 | 12.4 | -0.03 | 183311.29 | 45.77 | no_map |
| WUSDT | IDLE | 0.92 | 3.32 | 0.76 | 0.11 | 904994.72 | 9.03 | tvl≈1,601,519,029 |
| PYTHUSDT | IDLE | 1.42 | 2.89 | 1.21 | 0.07 | 771313.54 | 4.98 | tvl≈134,365,419 |
| CCUSDT | IDLE | 0.93 | 2.46 | 0.61 | 0.09 | 667368.68 | 8.99 | no_map |
| CHIPUSDT | IDLE | 1.47 | 8.16 | 4.01 | 0.19 | 158602.37 | 13.4 | no_map |
| HBARUSDT | IDLE | 1.0 | 1.86 | 0.93 | 0.06 | 639546.52 | 1.26 | empty_tvl |
| ZBCNUSDT | IDLE | 1.29 | 2.33 | 1.61 | 0.03 | 226351.83 | 20.41 | n/a |
| TELUSDT | IDLE | 2.35 | 11.9 | 4.88 | 0.14 | 119456.93 | 43.25 | no_map |
| KITEUSDT | IDLE | 1.0 | 1.94 | 0.44 | 0.05 | 78255.3 | 11.67 | no_map |
| RWAINCUSDT | IDLE | 1.27 | 2.46 | 0.57 | 0.04 | 7347.35 | 11.49 | no_map |
| BIOUSDT | IDLE | 0.79 | 1.92 | 0.62 | 0.09 | 87214.11 | 10.94 | n/a |
| REDUSDT | IDLE | 0.52 | 1.36 | 0.25 | 0.11 | 61777.84 | 16.41 | tvl≈2,644,380 |
| RIZEUSDT | IDLE | 0.15 | 2.53 | 0.67 | -0.09 | 57349.81 | 17.76 | no_map |
| FLUIDUSDT | IDLE | 1.23 | 5.48 | 0.0 | 0.18 | 2786.42 | 21.66 | tvl≈2,633,807,760 |
| QNTUSDT | IDLE | 0.72 | 1.27 | 1.11 | 0.04 | 72417.62 | 6.32 | n/a |
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
