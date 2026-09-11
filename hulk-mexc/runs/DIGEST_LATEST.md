# Hulk DIGEST — 2026-09-11T06:16:37Z

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
| ETHUSDT | IDLE | 0.63 | 1.24 | 0.07 | -0.0 | 452734932.02 | 0.36 | no_map |
| XRPUSDT | IDLE | 0.61 | 1.2 | 0.07 | -0.02 | 40599709.0 | 2.22 | n/a |
| BTCUSDT | IDLE | 0.49 | 0.97 | 0.05 | -0.01 | 550666671.81 | 0.0 | no_map |
| RIZEUSDT | IDLE | 1.68 | 47.43 | 27.0 | -0.52 | 165995.93 | 129.15 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 5.89 | 5.29 | -0.06 | 101773.16 | 15.29 | no_map |
| CCUSDT | IDLE | 0.87 | 1.79 | 0.17 | -0.05 | 462292.2 | 6.07 | no_map |
| PYTHUSDT | IDLE | 1.1 | 2.15 | 0.29 | -0.02 | 356635.95 | 1.94 | tvl≈116,258,822 |
| WUSDT | IDLE | 1.44 | 2.76 | 0.86 | -0.01 | 159228.97 | 12.41 | tvl≈1,485,387,395 |
| ZBCNUSDT | IDLE | 1.21 | 2.41 | 0.0 | -0.02 | 203750.24 | 17.57 | n/a |
| REDUSDT | IDLE | 1.11 | 2.19 | 0.24 | -0.01 | 60231.08 | 10.61 | tvl≈2,206,857 |
| BIOUSDT | IDLE | 0.89 | 1.7 | 0.48 | -0.01 | 73929.77 | 3.99 | n/a |
| KITEUSDT | IDLE | 0.81 | 1.47 | 1.04 | -0.03 | 57683.39 | 12.02 | no_map |
| RWAINCUSDT | IDLE | 1.03 | 1.85 | 1.43 | 0.0 | 3644.13 | 33.58 | no_map |
| TELUSDT | IDLE | 1.49 | 2.73 | 1.64 | -0.03 | 96410.79 | 45.95 | no_map |
| HBARUSDT | IDLE | 0.6 | 1.14 | 0.4 | -0.02 | 177575.22 | 2.66 | empty_tvl |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
