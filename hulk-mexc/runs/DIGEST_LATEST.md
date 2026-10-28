# Hulk DIGEST — 2026-10-28T06:26:17Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.8 | 1.42 | 1.18 | 0.02 | 19518323.8 | 2.26 | n/a |
| ETHUSDT | IDLE | 0.65 | 1.21 | 0.61 | 0.02 | 245496762.96 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.39 | 0.74 | 0.3 | 0.02 | 304087493.52 | 0.0 | no_map |
| WUSDT | IDLE | 0.92 | 1.86 | 0.95 | 0.04 | 636222.47 | 22.63 | tvl≈1,522,776,135 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.71 | 5.68 | 5.24 | -0.08 | 58995.13 | 6.84 | no_map |
| PYTHUSDT | IDLE | 1.37 | 2.41 | 2.18 | -0.01 | 363954.41 | 2.76 | tvl≈162,833,822 |
| ZBCNUSDT | IDLE | 1.9 | 3.66 | 2.56 | -0.04 | 203748.16 | 22.52 | n/a |
| RIZEUSDT | IDLE | 2.43 | 4.52 | 2.31 | 0.03 | 36255.88 | 59.1 | no_map |
| CCUSDT | IDLE | 0.91 | 1.6 | 1.5 | 0.01 | 235858.58 | 9.11 | no_map |
| CHIPUSDT | IDLE | 1.23 | 3.01 | 2.83 | 0.04 | 121682.68 | 16.67 | no_map |
| HBARUSDT | IDLE | 1.04 | 1.9 | 1.23 | -0.0 | 351758.01 | 3.93 | empty_tvl |
| BIOUSDT | IDLE | 0.99 | 1.82 | 1.05 | 0.02 | 68435.45 | 8.81 | n/a |
| REDUSDT | IDLE | 0.63 | 1.33 | 0.55 | 0.06 | 57807.48 | 14.94 | tvl≈3,858,198 |
| KITEUSDT | IDLE | 0.48 | 0.86 | 0.63 | 0.05 | 60018.66 | 11.04 | no_map |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
