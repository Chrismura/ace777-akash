# Hulk DIGEST — 2026-10-20T15:18:45Z

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
| XRPUSDT | IDLE | 2.28 | 4.28 | 1.87 | 0.01 | 22182057.7 | 2.27 | n/a |
| ETHUSDT | IDLE | 2.12 | 4.03 | 1.34 | 0.01 | 143417079.64 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.35 | 2.55 | 0.97 | 0.0 | 327753617.44 | 0.0 | no_map |
| PYTHUSDT | IDLE | 4.0 | 9.08 | 3.26 | 0.03 | 963477.89 | 6.57 | tvl≈162,629,459 |
| WUSDT | IDLE | 3.31 | 6.16 | 3.11 | 0.02 | 743588.32 | 16.04 | tvl≈1,561,006,722 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.49 | 12.27 | 10.07 | -0.02 | 77598.42 | 10.57 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.26 | 10.64 | 0.0 | 72563.37 | 59.09 | no_map |
| QNTUSDT | IDLE | 3.23 | 6.0 | 3.11 | -0.0 | 653689.21 | 3.55 | n/a |
| ZBCNUSDT | IDLE | 4.08 | 7.67 | 3.23 | 0.01 | 192044.81 | 30.31 | n/a |
| CCUSDT | IDLE | 1.95 | 3.65 | 1.62 | 0.01 | 421876.32 | 9.53 | no_map |
| CHIPUSDT | IDLE | 2.69 | 10.03 | 4.49 | 0.11 | 110677.25 | 11.03 | no_map |
| BIOUSDT | IDLE | 3.2 | 6.1 | 1.97 | 0.04 | 63636.37 | 8.19 | n/a |
| EDELUSDT | IDLE | 1.46 | 12.37 | 0.4 | 0.3 | 318903.41 | 25.66 | no_map |
| HBARUSDT | IDLE | 2.5 | 4.66 | 2.31 | 0.02 | 388647.17 | 10.74 | empty_tvl |
| REDUSDT | IDLE | 2.68 | 5.05 | 2.09 | 0.01 | 58647.82 | 17.34 | tvl≈3,400,565 |
| KITEUSDT | IDLE | 2.42 | 4.65 | 1.32 | 0.01 | 90231.21 | 8.95 | no_map |
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
