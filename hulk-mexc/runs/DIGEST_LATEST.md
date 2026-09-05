# Hulk DIGEST — 2026-09-05T13:26:18Z

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
| XRPUSDT | IDLE | 0.67 | 1.32 | 0.13 | 0.0 | 27791184.92 | 2.12 | n/a |
| ETHUSDT | IDLE | 0.19 | 0.37 | 0.03 | 0.0 | 231671551.6 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.14 | 0.27 | 0.01 | 0.0 | 433305320.99 | 0.0 | no_map |
| CHIPUSDT | IDLE | 1.88 | 6.78 | 5.25 | 0.03 | 443675.87 | 1.79 | no_map |
| PYTHUSDT | IDLE | 2.04 | 3.95 | 0.92 | 0.03 | 370813.05 | 3.63 | tvl≈120,618,249 |
| KITEUSDT | IDLE | 2.39 | 4.51 | 4.26 | -0.05 | 64841.54 | 10.24 | no_map |
| ZBCNUSDT | IDLE | 1.42 | 2.66 | 1.16 | -0.02 | 193551.68 | 10.01 | n/a |
| CCUSDT | IDLE | 0.92 | 1.82 | 0.18 | -0.0 | 281710.53 | 10.04 | no_map |
| REDUSDT | IDLE | 1.57 | 2.75 | 2.55 | 0.03 | 65477.01 | 9.59 | tvl≈2,335,697 |
| RIZEUSDT | IDLE | 1.2 | 11.89 | 1.79 | -0.06 | 159947.26 | 125.23 | no_map |
| BIOUSDT | IDLE | 0.97 | 1.94 | 0.0 | 0.03 | 81246.47 | 7.2 | n/a |
| WUSDT | IDLE | 0.55 | 1.03 | 0.52 | 0.05 | 177052.58 | 14.08 | tvl≈1,554,945,456 |
| HBARUSDT | IDLE | 1.33 | 2.66 | 0.05 | 0.05 | 273608.65 | 1.23 | empty_tvl |
| EDELUSDT | IDLE | 0.13 | 2.29 | 0.75 | -0.03 | 200629.95 | 18.81 | no_map |
| RWAINCUSDT | IDLE | 0.82 | 1.52 | 0.75 | 0.0 | 7089.23 | 69.61 | no_map |
| TELUSDT | IDLE | 0.85 | 1.6 | 0.64 | -0.0 | 75039.67 | 23.53 | no_map |
| QNTUSDT | IDLE | 0.58 | 1.11 | 0.36 | -0.02 | 40857.86 | 3.12 | n/a |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
