# Hulk DIGEST — 2026-08-17T16:08:07Z

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
| XRPUSDT | IDLE | 0.59 | 1.13 | 0.29 | 0.0 | 12823265.3 | 1.99 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.74 | 26.76 | 14.27 | 0.22 | 71060.81 | 43.33 | no_map |
| CHIPUSDT | IDLE | 2.05 | 8.9 | 7.57 | 0.0 | 334895.92 | 3.43 | no_map |
| CCUSDT | IDLE | 2.04 | 3.57 | 3.39 | -0.04 | 251718.54 | 6.53 | no_map |
| EDELUSDT | IDLE | 2.86 | 5.45 | 3.69 | 0.03 | 65080.98 | 12.78 | no_map |
| ZBCNUSDT | IDLE | 2.05 | 3.95 | 0.95 | 0.0 | 172429.32 | 11.42 | n/a |
| REDUSDT | IDLE | 2.05 | 3.97 | 0.87 | -0.03 | 56944.0 | 17.64 | tvl≈1,540,264 |
| TELUSDT | IDLE | 2.77 | 4.86 | 4.5 | -0.03 | 105262.71 | 35.65 | no_map |
| PYTHUSDT | IDLE | 0.62 | 1.16 | 0.59 | -0.01 | 145343.44 | 2.56 | tvl≈88,233,824 |
| WUSDT | IDLE | 0.63 | 1.21 | 0.32 | -0.03 | 156127.71 | 14.3 | tvl≈1,350,775,771 |
| KITEUSDT | IDLE | 0.82 | 1.47 | 1.18 | -0.02 | 59036.85 | 11.9 | no_map |
| BIOUSDT | IDLE | 0.63 | 1.22 | 0.28 | -0.0 | 72914.11 | 4.05 | n/a |
| QNTUSDT | IDLE | 1.97 | 3.77 | 1.14 | -0.0 | 36984.18 | 5.26 | n/a |
| RWAINCUSDT | IDLE | 1.1 | 1.92 | 1.88 | -0.0 | 1860.75 | 81.35 | no_map |
| QAITUSDT | IDLE | 0.78 | 1.39 | 1.18 | -0.01 | 737.18 | 61.3 | no_map |
| HBARUSDT | IDLE | 0.76 | 1.48 | 0.3 | 0.01 | 125977.32 | 1.51 | empty_tvl |
| FLUIDUSDT | IDLE | 1.11 | 2.23 | 0.0 | 0.01 | 857.46 | 3.45 | tvl≈2,314,168,395 |
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
