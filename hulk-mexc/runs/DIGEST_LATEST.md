# Hulk DIGEST — 2026-10-18T23:10:24Z

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
| XRPUSDT | IDLE | 1.91 | 3.76 | 0.44 | 0.01 | 27748859.4 | 0.77 | n/a |
| ETHUSDT | IDLE | 1.49 | 2.94 | 0.28 | 0.0 | 121657721.0 | 0.13 | no_map |
| BTCUSDT | IDLE | 0.7 | 1.39 | 0.12 | 0.0 | 239356180.86 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.84 | 5.31 | 1.34 | -0.06 | 1289974.8 | 2.7 | tvl≈166,595,289 |
| WUSDT | IDLE | 1.4 | 3.71 | 0.68 | -0.06 | 895144.92 | 17.0 | tvl≈1,524,792,025 |
| HBARUSDT | IDLE | 2.09 | 5.25 | 0.26 | 0.02 | 813129.89 | 2.34 | empty_tvl |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 9.75 | 8.29 | -0.01 | 60981.69 | 10.82 | no_map |
| CCUSDT | IDLE | 2.35 | 4.67 | 0.16 | -0.02 | 274714.33 | 8.9 | no_map |
| QNTUSDT | IDLE | 2.0 | 4.8 | 0.74 | -0.03 | 576113.57 | 3.17 | n/a |
| ZBCNUSDT | IDLE | 2.06 | 5.27 | 0.76 | -0.04 | 237982.71 | 5.38 | n/a |
| EDELUSDT | IDLE | 1.8 | 4.42 | 1.31 | -0.06 | 252554.14 | 7.6 | no_map |
| REDUSDT | IDLE | 2.17 | 4.32 | 0.15 | -0.01 | 94897.8 | 10.91 | tvl≈3,355,171 |
| BIOUSDT | IDLE | 1.97 | 4.03 | 0.21 | -0.03 | 82392.26 | 4.27 | n/a |
| CHIPUSDT | IDLE | 1.68 | 5.38 | 0.22 | -0.05 | 76083.96 | 9.8 | no_map |
| KITEUSDT | IDLE | 1.53 | 3.04 | 0.14 | -0.01 | 67171.73 | 9.64 | no_map |
| RIZEUSDT | IDLE | 0.77 | 3.9 | 3.07 | -0.04 | 58308.86 | 39.58 | no_map |
| FLUIDUSDT | IDLE | 1.88 | 3.56 | 2.55 | -0.06 | 4305.44 | 21.88 | tvl≈2,201,048,789 |
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
